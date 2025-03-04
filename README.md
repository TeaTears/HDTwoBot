# 💀 Helldivers 2 Voice Bot

A **Discord bot** that dynamically creates and manages voice channels for a **Helldivers 2** community. The bot automatically generates **temporary voice channels** when users join a base voice channel and removes empty ones for better organization.  

It also provides an `!invite` command to share an invite link to your voice channel.  

---

## 🚀 Features
- ✅ **Dynamic Voice Channel Creation** – Automatically creates a new voice channel when a user joins the base channel.
- 🗑 **Automatic Cleanup** – Deletes empty temporary channels to keep things tidy.
- 🎲 **Custom Naming System** – Generates random channel names using two separate word lists (`firstname.txt` & `secondname.txt`).
- 🔗 **`!invite` Command** – Creates an **invite link** to your current voice channel.

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/TeaTears/HDTwoBot.git
cd HelldiversTwoBot
```

### 2️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

---
### 🔗 Adding the Bot to Your Server
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Select the **Bot** tab, scroll down to **Privileged Gateway Intents**, and **enable all options**.
3. Go to **OAuth2 > URL Generator**.
4. Under **Scopes**, select **bot**.
5. Under **Bot Permissions**, select **Administrator** (or choose specific permissions as needed).
6. Copy the generated URL and paste it into your browser.
7. Select your server and **authorize the bot**.
---

### 3️⃣ Configure the Bot

• Create `.env` and paste your token with prefix:
```
TOKEN=your_discord_bot_token
PREFIX=any_symbol_as_prefix
```
• Set your server ID, base voice channel ID and allowed text channel ID in config/constants.py:

```
GUILD_ID = 123  # Your Discord server ID
BASE_VOICE_CHANNEL_ID = 321  # Base voice channel ID
ALLOWED_CHANNEL_ID = 333 # Allowed text channel for invite command
```
---
# 🎛 Running the Bot
```sh
python bot.py
```
---
# 🎤 Commands

Invite:
```sh
!invite [optional message]
```

Example:
```sh
!invite Diff 10, bugs.
```

Output:
**Voice Channel Invite:** `https://discord.gg/xyz123`
Diff 10, bugs.

---

# 🎛 Updating the Project
Run this command inside the project folder:
```sh
git pull origin main
```
This will fetch the latest updates from the repository.

---
# 🐞 Troubleshooting
**Bot does not work?**

	• Check if the bot is online.
	• Verify your TOKEN in .env.
	• Ensure the bot has permissions to create and delete channels.
	• Confirm that BASE_VOICE_CHANNEL_ID is correctly set in config/constants.py.