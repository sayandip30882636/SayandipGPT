# SayandipGPT 🤖💬

**SayandipGPT** is an AI-powered chatbot for Discord, built using Google's **Gemini 1.5 Flash** model. It enables real-time, intelligent conversations within any Discord server. Developed and deployed on **Replit**, this bot is fast, easy to maintain, and cloud-hosted.

---

## 📽️ Demo Video

Watch SayandipGPT in action!  
Check out the full demonstration video showing how the bot works inside Discord.

🔗 [Watch Demo on Google Drive](https://drive.google.com/file/d/16mBLyDUGXzxY5ndhVyGaynynP7wyg7Ik/view?usp=sharing)

> 🎥 The video includes:
> - Real-time bot responses using Gemini 1.5 Flash
> - Integration process on Discord
> - Live testing on a sample Discord server



## 🚀 Key Features

- 💡 Chatbot powered by Gemini 1.5 Flash (Google Generative AI)
- 🌐 Fully developed and deployed on Replit (no local setup needed)
- 💬 Seamlessly interacts in Discord servers using Discord Bot API
- 🔐 Secure API key and token management via Replit Secrets
- ⚡ Lightweight and responsive

---

## 🧰 Tech Stack

| Component                | Description                             |
|--------------------------|-----------------------------------------|
| **Replit**               | Cloud IDE and runtime environment       |
| **Python**               | Primary programming language            |
| **discord.py**           | Python wrapper for Discord API          |
| **Google Generative AI** | Backend AI model (Gemini 1.5 Flash)     |
| **asyncio**              | Asynchronous processing in Python       |
| **Environment Secrets**  | For secure API key and token handling   |

---

## 🧠 How It Works

1. User sends a message in a Discord server.
2. SayandipGPT listens for the message and processes it.
3. The message is sent to Gemini 1.5 Flash via Google’s Generative AI API(Gemini API).
4. The bot receives a response and sends it back to the channel.

---
## 🧠 Backdrops
1. It gives you two responses in one time
2. It is a text based bot , can't give you image and stuffs
3. It is in learning stage
4. Best if you use paid APIs like OPENAI-API

## ⚙️ Setup (Replit Instructions)

1. **create a new Python Replit** and **Create own bot in discord developers**
2. **Paste your code** into `main.py`.
3. **Add Secrets** in Replit:
   - `GOOGLE_API_KEY` → Your Gemini API key
   - `OPENAI_API_KEY` → Your OPENAI API key (optional if you are using OPENAI)
   - Step-by-Step guide for OPENAPI → https://youtu.be/BP-w99ZINTc?si=BGlBsUaEziRshcME
   - `SECRET_SAYANDIPGPT_KEY` → Your Discord Bot Token
4. Click **"Run"** on Replit to start your bot.
5. Invite the bot to your Discord server using your bot's OAuth2 URL from the [Discord Developer Portal](https://discord.com/developers/applications).

---

## 📄 Example Message

**User**: `@SayandipGPT What is Schrödinger’s cat?`  
**Bot**: `Schrödinger’s cat is a thought experiment in quantum mechanics where...`

---

## 🙋 About Me

**Sayandip Ghosh**  
🎓 Aspiring Data Scientist & Researcher  
💻 Passionate about intelligent systems and real-world applications

---

## 📌 Notes

- **No local environment required** — everything runs on Replit/Railway.
- All sensitive information (API keys, tokens) are handled via Replit Secrets for security.
- Make sure your Discord bot has the right permissions (`MESSAGE CONTENT INTENT`, `SEND_MESSAGES`, etc.)

---

## 📜 License

This bot is developed for educational and personal use. Please do not publicly share your API keys or Discord token.

---

## 🌟 Like the Project?

Then take it as reference and create your own !! For feedback or suggestions, feel free to reach out.
