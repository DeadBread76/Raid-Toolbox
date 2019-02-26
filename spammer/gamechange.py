import discord
import asyncio
import sys

token = sys.argv[1]
game = sys.argv[2]

client = discord.Client()

@client.event
async def on_ready():
    try:
        await client.change_presence(game=discord.Game(name=game))
    except Exception:
        return ''
client.run(token, bot=False)
