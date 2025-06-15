import discord
import os
import google.generativeai as genai
import asyncio

# Configure Gemini API
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    print("Gemini API configured successfully")
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

token = os.getenv("SECRET_SAYANDIPGPT_KEY")

# Split long messages into 2000-char chunks
def split_message(message, limit=2000):
    return [message[i:i+limit] for i in range(0, len(message), limit)]

# Detect simple greetings or common phrases
def detect_basic_response(user_input):
    user_input = user_input.lower()
    greetings = ['hi', 'hello', 'hey', 'namaste', 'hola']
    thanks = ['thank you', 'thanks', 'thx', 'dhanyavad']
    how_are_you = ['how are you', 'how r u', 'kya haal hai']

    if any(word in user_input for word in greetings):
        return "Hey there! 😊 How can I help you today?"

    elif any(word in user_input for word in thanks):
        return "You're very welcome! 🙌 Let me know if you need anything else."

    elif any(phrase in user_input for phrase in how_are_you):
        return "I'm doing great! Thanks for asking. How about you? 😄"

    return None

# Build a personality-enhanced prompt
def build_prompt(user_input):
    base_personality = (
        "You are a friendly, humorous, emotionally intelligent AI chatbot assistant. "
        "Talk like a human friend. Respond in the same language the user uses. "
        "Be supportive, clear, and fun when appropriate.\n\n"
    )

    return base_personality + f"User says: {user_input}\nAI:"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user in message.mentions:
            channel = message.channel
            user_input = message.content.replace(f"<@{self.user.id}>", "").strip()
            print(f'Message from {message.author}: {user_input}')

            # Step 1: Check if it's a basic known input
            basic_reply = detect_basic_response(user_input)
            if basic_reply:
                await channel.send(basic_reply)
                return

            # Step 2: Send to Gemini with personality
            try:
                async with channel.typing():
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = build_prompt(user_input)
                    response = model.generate_content(prompt)
                    response.resolve()
                    reply = response.text or "Sorry, I couldn't think of a good answer."

                    for part in split_message(reply):
                        await channel.send(part)

            except Exception as e:
                print(f"Error with Gemini: {e}")
                await channel.send("Oops! Something went wrong while processing that.")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
