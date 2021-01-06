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
@bot.command(aliases=["yt", "youtube"])
async def _youtube(ctx, *, arg):
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
@bot.command(aliases=["ping"])
async def _ping(ctx):
    """Display the latency, with a pong ofcource."""
    await ctx.send(f"Pong! {round(bot.latency * 1000)}")


# Clear Messages from the bot.
@bot.command(aliases=["clear"])
async def _clear(ctx, amount=10):
    """Clear Messages."""
    await ctx.channel.purge(limit=amount+1)


# command to Kick.
@bot.command(aliases=["kick"])
@commands.has_permissions(administrator=True)
async def _kick(ctx, member : discord.Member, *, reason=None):
    """Kick members."""
    await member.kick(reason=reason)
    await ctx.send(f'banned {member}')

# command to Ban.
@bot.command(aliases=["ban"])
@commands.has_permissions(administrator=True)
async def _ban(ctx, member : discord.Member, *, reason=None):
    """Ban members."""
    await member.ban(reason=reason)
    await ctx.send(f'Banned <@!{member.id}>')

# @bot.command(aliases=['unban'])
# @commands.has_permissions(administrator=True)
# async def _unban(ctx, *, member):
#     member_name = bot.fetch_uer(member)
#     banned_users = await ctx.guild.bans()
#     member_name, member_discriminator = member_name.split('#')
# 
#     for ban_entry in banned_users:
#         user = ban_entry.user
# 
#         if (user.name, user.discriminator) == (member, member__discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}')
#     await ctx.guild.unban(bot.fetch_user(member))


# 8 ball command.
@bot.command(aliases=["8ball", "8b"])
async def _8ball(ctx, *, question):
    await ctx.send(random.choice(["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.",
             "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.",
             "Yes.", "Yes – definitely.", "You may rely on it."]))

# @bot.command()
# async def poll(ctx, *, message):
#     """Creates a Poll."""
#     embd = discord.Embded(title=f"Poll created by {ctx.author}", discription=f"{message}")
#     msg = await ctx.channel.send(embded=embd)
#     await msg.add_reaction(":thumbsup:")
#     await msg.add_reaction(":down:")



token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)
