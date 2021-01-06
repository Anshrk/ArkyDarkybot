import os
import discord
from discord.ext import commands
import re
import requests
import random

bot = commands.Bot(command_prefix='>')

# Opening message
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('programming my self, use ">help" to summon"'))
    print("Bot is connecting...\n")
    print("Bot is live!")


# alert new joiners
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to Programmer's Cafe :>")


# command to post a youtubevideo
@bot.command(aliases=["yt"])
async def youtube(ctx, *, arg):
    """Search YouTube"""
    query = str(arg)
    # print("query: ", query)
    url = "https://www.youtube.com/results?search_query="
    with requests.get(url + query) as response:
        # regex = '/watch\?v\=[a-zA-z0-9/_/-/*]+'
        regex = '/watch\?v\=(.*?)\"'
        # regex = r'/watch\?v=[a-zA-Z0-9]+'
        match = re.findall(regex, response.text)[0]
        payload = "https://www.youtube.com/watch?v=" + match
        # print(payload)
        await ctx.send(f"> Here is your result for: {query}\n{payload}")


# Command to display the latency of the bot.
@bot.command()
async def ping(ctx):
    """Display the latency, with a pong ofcource."""
    await ctx.send(f"Pong! {round(bot.latency * 1000)}")

# Clear Messages from the bot.
@bot.command()
async def clear(ctx, amount=10):
    """Clear Messages."""
    await ctx.channel.purge(limit=amount+1)


# command to Kick and Ban.
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


# @bot.command()
# async def poll(ctx, *, message):
#     """Creates a Poll."""
#     embd = discord.Embded(title=f"Poll created by {ctx.author}", discription=f"{message}")
#     msg = await ctx.channel.send(embded=embd)
#     await msg.add_reaction(":thumbsup:")
#     await msg.add_reaction(":down:")



token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)
