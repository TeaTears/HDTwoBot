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

firstname = load_words("config/firstname.txt")
secondname = load_words("config/secondname.txt")

team_counters = {}

@bot.event
async def on_voice_state_update(member, before, after):
    guild = bot.get_guild(GUILD_ID)

    if after.channel and after.channel.id == BASE_VOICE_CHANNEL_ID:
        category = after.channel.category
        if after.channel and after.channel.id == BASE_VOICE_CHANNEL_ID:
            category = after.channel.category
            if not category:
                print("⚠ Base voice channel is not inside a category! Cannot create team channels.")
                return
        next_team_number = team_counters.get(guild.id, 1)
        team_counters[guild.id] = next_team_number + 1

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
        if before.channel.id != BASE_VOICE_CHANNEL_ID and len(before.channel.members) == 0:
            await before.channel.delete()