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
    async def clear(self, ctx, amount: int):
        """Clear Messages."""
        await ctx.channel.purge(limit=amount+1)

    # command for sending personal dms
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def _dm(self, ctx, user_id=None, *, args=None):
        """Dm's a specific user."""
        if user_id and args:
            target = await self.client.fetch_user(user_id)
            await target.send(args)
            await ctx.channel.send(args +
                                   "has been sent to: " +
                                   target.name)
        else:
            await ctx.channel.send(
                    "A user_id and/or arguments were not included.")

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
