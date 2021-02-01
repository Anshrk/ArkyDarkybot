"""Import modules."""
import discord
from discord.ext import commands


class ModerationCommands(commands.Cog):
    """Moderation commands to... moderate."""

    def __init__(self, client):
        """Initialize the class."""
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=10):
        """Clear Messages."""
        await ctx.channel.purge(limit=amount+1)

    # command for ban
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban members."""
        await member.ban(reason=reason)
        await ctx.send(f'Banned <@!{member.id}>')

    # kick command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick members."""
        await member.kick(reason=reason)
        await ctx.send(f'Kicked <@!{member.id}>')


def setup(client):
    """Set up all the cogs."""
    client.add_cog(ModerationCommands(client))
