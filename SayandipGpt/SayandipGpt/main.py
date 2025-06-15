# app id: 1383711185387524217
# public key: 8030265019948605746487968737497903954563688544

import discord
import os
import google.generativeai as genai

# Configure API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
token = os.getenv("SECRET_SAYANDIPGPT_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # Don't respond to the bot's own messages
        if message.author == self.user:
            return
            
        print(f'Message from {message.author}: {message.content}')
        
        if self.user in message.mentions:
            channel = message.channel
            try:
                # Use Google Gemini - updated model name
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(message.content)
                messageToSend = response.text
                await channel.send(messageToSend)
            except Exception as e:
                print(f"Error with Gemini: {e}")
                await channel.send('Sorry, I encountered an error processing your request.')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
