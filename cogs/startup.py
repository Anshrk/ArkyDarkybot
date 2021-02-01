"""Import required modules."""
from discord.ext import commands


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
        channel = self.client.get_channel(805726305031028737)
        if channel is not None:
            await channel.send(f"Welcome to ACTUAL HELL, {member.mention}")


def setup(client):
    """Set up all the cogs."""
    client.add_cog(StartupCommands(client))
