import discord
from discord.ext import commands
from config.settings import PREFIX

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)