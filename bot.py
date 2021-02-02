"""Import all modules."""
import os
import json
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


def get_prefix(message):
    """Get the prefixes as the name suggests."""
    with open('prefixes.json', 'r') as _f:
        prefixes = json.load(_f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix, intents=intents)


@client.event
async def on_guild_join(guild):
    """When joining the a new server, set prefix."""
    with open('prefixes.json', 'r') as _f:
        prefixes = json.load(_f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as _f:
        json.dump(prefixes, _f)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv('BOT_TOKEN'))
