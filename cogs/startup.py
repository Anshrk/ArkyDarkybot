import discord
import os
from discord.ext import commands

class StartupCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    # on startup
    @commands.Cog.listener()
    async def on_ready(self):
        print("The Bot is ready to take over the wor- serve you!!!")


    # latency check
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}")


def setup(client):
    client.add_cog(StartupCommands(client))
