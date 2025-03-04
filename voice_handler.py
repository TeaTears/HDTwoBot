import os
import random
from config.bot_setup import bot
from config.constants import GUILD_ID, BASE_VOICE_CHANNEL_ID

def load_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"❌ File {filename} not found! Using fallback value.")
        return ["Default"]

script_dir = os.path.dirname(os.path.abspath(__file__))
firstname = load_words(os.path.join(script_dir, "config", "firstname.txt"))
secondname = load_words(os.path.join(script_dir, "config", "secondname.txt"))

team_counters = {}

@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(GUILD_ID)

    base_channel = guild.get_channel(BASE_VOICE_CHANNEL_ID)
    if not base_channel or not base_channel.category:
        print("⚠ Base voice channel or category not found. Skipping channel creation.")
        return

    category = base_channel.category

    if after.channel and after.channel.id == BASE_VOICE_CHANNEL_ID:
        first_part = random.choice(firstname)
        second_part = random.choice(secondname)
        channel_name = f"💀 {first_part} {second_part}"

        new_channel = await guild.create_voice_channel(
            name=channel_name,
            category=category,
            user_limit=4
        )

        await member.move_to(new_channel)

    if before.channel and before.channel != after.channel:
        if (
            before.channel.id != BASE_VOICE_CHANNEL_ID
            and before.channel.category == category
            and len(before.channel.members) == 0
        ):
            await before.channel.delete()