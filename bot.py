import discord
from discord.ext import commands

from config.bot_setup import bot
from config.constants import BASE_VOICE_CHANNEL_ID, GUILD_ID
import voice_handler


@bot.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def invite(ctx, *, message: str = "Join us in voice chat!"):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel
        invite = await voice_channel.create_invite(max_age=1800, max_uses=0)
        await ctx.send(f"**Voice Channel Invite:** {invite.url}\n{message}")
    else:
        await ctx.send("❌ You are not in a voice channel!")

@invite.error
async def invite_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"⏳ Please wait {error.retry_after:.1f} seconds before using `!invite` again.")


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
    from config.settings import TOKEN

    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: Discord token is missing! Check your .env file.")