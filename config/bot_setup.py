import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def send_long_message(ctx, message):
    MAX_MESSAGE_LENGTH = 2000
    for i in range(0, len(message), MAX_MESSAGE_LENGTH):
        await ctx.send(message[i : i + MAX_MESSAGE_LENGTH])