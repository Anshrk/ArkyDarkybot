"""Import all the modules."""
import re
import random
import requests
import discord
from discord.ext import commands
from udpy import UrbanClient


class FunCommands(commands.Cog):
    """Funcommands to play with :D."""

    def __init__(self, client):
        """Initialize the class."""
        self.client = client

    @commands.command(aliases=["yt"])
    async def youtube(self, ctx, *, arg):
        """Search YouTube."""
        query = str(arg)
        # print("query: ", query)
        url = "https://www.youtube.com/results?search_query="
        with requests.get(url + query) as response:
            # regex = '/watch\?v\=[a-zA-z0-9/_/-/*]+'
            regex = r'/watch\?v\=(.*?)\"'
            # regex = r'/watch\?v=[a-zA-Z0-9]+'
            match = re.findall(regex, response.text)[0]
            payload = "https://www.youtube.com/watch?v=" + match
            # print(payload)
            await ctx.send(f"> Here is your result for: {query}\n{payload}")

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, member: commands.MemberConverter = None):
        """What's your profile pic?."""
        member = member or ctx.author
        embed = discord.Embed()
        embed.set_author(name=f"{ctx.author}", icon_url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.display_name}")
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["ub"])
    async def urban_dictionary(self, ctx, function: str, *words):
        """options: -sr, -rm, -st (kinda broken)."""
        async def get_r_meaning(ctx=ctx, words=words):
            print(" ".join(words))
            client = UrbanClient()
            defs = client.get_definition(str(" ".join(words)))
            random_def = random.choice(defs)
            send_back = f"Meaning of {random_def.word}\n\n\n"
            send_back += f"""{random_def.definition}


            **EXAMPLES**
            {random_def.example}"""
            await ctx.send(send_back)

        async def get_t_meaning(ctx=ctx, words=words):
            print(" ".join(words))
            client = UrbanClient()
            defs = client.get_definition(str(' '.join(words)))
            _def = defs[0]
            send_back = f"Meaning of {_def.word}\n\n\n"
            send_back += f"""{_def.definition}

            **EXAMPLES**
            {_def.example}"""
            await ctx.send(send_back)

        async def get_r(ctx=ctx, words=words):
            print(" ".join(words))
            client = UrbanClient()
            defs = client.get_random_definition()
            random_def = random.choice(defs)
            send_back = f"Meaning of {random_def.word}\n\n\n"
            send_back += f"""{random_def.definition}

            **EXAMPLES**
            {random_def.example}"""
            await ctx.send(send_back)

        async def not_found():
            await ctx.send("option {function} not found :(")

        do_stuff = {
                "-sr": get_r_meaning,
                "-st": get_t_meaning,
                "-r": get_r
                }
        await do_stuff.get(function, not_found)()


def setup(client):
    """Set up all the cogs."""
    client.add_cog(FunCommands(client))
