import discord
from discord.ext import commands



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged an as {self.user}')

    async def on_message(self, message):
        print(f"message from {message.author}: {message.content}")

    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
                f"Hi {member.name}, welcome to Programmer's Cafe :>"
                )

client = MyClient('code.')
with open('token.txt','r') as my_token:
    token = my_token.read()
client.run(token)

