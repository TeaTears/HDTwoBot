from config.bot_setup import bot
import datetime
import voice_handler


@bot.command()
async def invite(ctx, *, message: str = "Join us in voice chat!"):
    if ctx.author.voice and ctx.author.voice.channel:
        voice_channel = ctx.author.voice.channel

        invite = await voice_channel.create_invite(max_age=1800, max_uses=10)

        await ctx.send(f"🔗 **Voice Channel Invite:** {invite.url}\n📢 {message}")

    else:
        await ctx.send("❌ You are not in a voice channel!")

if __name__ == "__main__":
    from config.settings import TOKEN

    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ ERROR: Discord token is missing! Check your .env file.")