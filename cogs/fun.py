import discord
import os
from discord.ext import commands
import re
import requests

class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["yt"])
    async def youtube(self, ctx, *, arg):
        """Search YouTube"""
        query = str(arg)
        # print("query: ", query)
        url = "https://www.youtube.com/results?search_query="
        with requests.get(url + query) as response:
            # regex = '/watch\?v\=[a-zA-z0-9/_/-/*]+'
            regex = '/watch\?v\=(.*?)\"'
            # regex = r'/watch\?v=[a-zA-Z0-9]+'
            match = re.findall(regex, response.text)[0]
            payload = "https://www.youtube.com/watch?v=" + match
            # print(payload)
            embed = discord.Embed()
            embed.discription = f"> Here is your result for: {query}\n{payload}"
            await ctx.send(embed=embed)

    @commands.command(alias="pfp")
    async def profilepicture(self, ctx, user):
        pass



def setup(client):
    client.add_cog(FunCommands(client))
