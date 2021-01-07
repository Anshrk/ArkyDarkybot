import discord
import os
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    # on ready function
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # latency check
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}")




def setup(client):
    client.add_cog(Example(client))
