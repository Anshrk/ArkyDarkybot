import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

status = ["AttributeError", "EOFError", "IOError",
        "IndexError", "KeyError", "KeyboardInterrupt",
        "NameError", "StopIteration", "TypeError",
        "ValueError", "ZeroDivisionError"]

class StartupCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # on startup
    @commands.Cog.listener()
    async def on_ready(self):
#         self.change_status.start()
        print("The Bot is ready to take over the wor- serve you!!!")


    # latency check
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}")

#     @tasks.loop(seconds=10)
#     async def change_status(self):
#         await commands.bot.changepresence(
#                 activity=discord.Game(next(status)))

def setup(client):
    client.add_cog(StartupCommands(client))
