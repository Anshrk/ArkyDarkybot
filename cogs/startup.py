import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

pictures = ["https://bit.ly/2MLMWjG", "https://bit.ly/3pAZd9u", "https://bit.ly/2Yv0web"]
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

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}, to hell, heres a random cat picture to look at')
            await channel.send(f'{random.choice(pictures)}')
            


def setup(client):
    client.add_cog(StartupCommands(client))
