import os
import discord
from dotenv import load_dotenv
from bee_movie import BEE_MOVIE_SCRIPT

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_member_join(self,member):
    ment = member.mention
    await self.client.get_channel(107812793603891200).send(f"{ment} has joined the server.")
    print(f"{member} has joined the server.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "bee":
        await message.channel.send(BEE_MOVIE_SCRIPT)

client.run(TOKEN)
