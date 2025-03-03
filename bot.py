import discord
from discord.ext import commands
from cachetools import TTLCache

from config.bot_setup import bot
from config.constants import BASE_VOICE_CHANNEL_ID, GUILD_ID, ALLOWED_CHANNEL_ID
import voice_handler
import time

last_used_cache = TTLCache(maxsize=50, ttl=15)

@bot.command()
async def invite(ctx, *, message: str = "Join us in voice chat!"):
    if ctx.channel.id != ALLOWED_CHANNEL_ID:
        return

    user_id = ctx.author.id
    current_time = time.time()

    if user_id in last_used_cache:
        await ctx.send(f"⏳ {ctx.author.mention}, you can only use this command once every 15 seconds.")
        return

    last_used_cache[user_id] = current_time

    MAX_MESSAGE_LENGTH = 100

    if len(message) > MAX_MESSAGE_LENGTH:
        await ctx.message.delete()
        await ctx.send(f"⚠ {ctx.author.mention}, your message was too long and has been deleted! Maximum {MAX_MESSAGE_LENGTH} characters allowed.")
        return

    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        invite = await voice_channel.create_invite(max_age=1800, max_uses=0)
        await ctx.send(f"**Voice Channel Invite:** {invite.url}\n{message}")
    else:
        await ctx.send(f":pleading_face: {ctx.author.mention}, you are not in a voice channel!")

@bot.event
async def on_ready():
    guild = bot.get_guild(GUILD_ID)

    if not guild:
        print("❌ Guild not found! Bot is running without cleanup.")
        return

    base_channel = guild.get_channel(BASE_VOICE_CHANNEL_ID)

    if not base_channel or not base_channel.category:
        print("⚠ Base voice channel or category not found. Skipping cleanup.")
    else:
        category = base_channel.category
        for channel in category.voice_channels:
            if channel.id == BASE_VOICE_CHANNEL_ID:
                continue

            if len(channel.members) == 0:
                await channel.delete()

    print(f"✅ {bot.user} is ready!")


if __name__ == "__main__":
    from config.settings import TOKEN, PREFIX

    if not TOKEN or not PREFIX:
        print("❌ ERROR: Token or prefix is missing! Check your .env file.")
        exit(1)
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"❌ ERROR: Failed to run the bot. {str(e)}")
        exit(1)