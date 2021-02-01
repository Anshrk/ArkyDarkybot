"""Import required modules."""
import random
from discord.ext import commands

pictures = [
    "https://bit.ly/2MLMWjG",
    "https://bit.ly/3pAZd9u",
    "https://bit.ly/2Yv0web",
]


class StartupCommands(commands.Cog):
    """Startup commands class."""

    def __init__(self, client):
        """Initialize command."""
        self.client = client

    # on startup
    @commands.Cog.listener()
    async def on_ready(self):
        """On ready command."""
#         self.change_status.start()
        print("The Bot is ready to take over the wor- serve you!!!")

    # latency check
    @commands.command()
    async def ping(self, ctx):
        """Ping yourself or something i dunno."""
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """To run when members join."""
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"""Welcome {member.mention}, to hell,
                    heres a random cat picture to look at""")
            await channel.send(f'{random.choice(pictures)}')


def setup(client):
    """Set up all the cogs."""
    client.add_cog(StartupCommands(client))
