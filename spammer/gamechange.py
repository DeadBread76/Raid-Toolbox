import discord
import asyncio
import sys

token = sys.argv[1]
game = sys.argv[2]

client = discord.Client()

@client.event
async def on_ready():
    try:
        while not client.is_closed:
            await client.change_presence(game=discord.Game(name=game))
            await asyncio.sleep(5)
    except Exception:
        continue
client.run(token, bot=False)
