"""Import required modules."""
from itertools import cycle
import discord
from discord.ext import commands, tasks


class StartupCommands(commands.Cog):
    """Startup commands class."""

    def __init__(self, client):
        """Initialize command."""
        self.client = client
        self.status = cycle(["Never", "gonna", "give", "you", "up"])

    # on startup
    @commands.Cog.listener()
    async def on_ready(self):
        """On ready command."""
        self.change_status.start()  # pylint: disable=E1101
        print("The Bot is ready to take over the wor- serve you!!!")

    # latency check
    @commands.command()
    async def ping(self, ctx):
        """Ppppiiinnnggg."""
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}")

    # on member join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        """To run when members join."""
        channel = self.client.get_channel(805726305031028737)
        if channel is not None:
            await channel.send(f"Welcome to ACTUAL HELL, {member.mention}")

    # background tasks
    @tasks.loop(seconds=4)
    async def change_status(self):
        """Change activites regularly."""
        await self.client.change_presence(activity=discord.Game(
            next(self.status)
        ))

    # error thing
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Post this bullshit when there is an error."""
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please send required arguments')


def setup(client):
    """Set up all the cogs."""
    client.add_cog(StartupCommands(client))
