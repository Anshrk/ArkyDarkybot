"""Import all modules."""
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix='.', intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv('BOT_TOKEN'))
