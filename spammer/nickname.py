import discord
import asyncio
import random
import sys

token = sys.argv[1]
SERVER = sys.argv[2]
client = discord.Client()

@client.event
async def on_ready():
    server = client.get_server(SERVER)
    while not client.is_closed:
        try:
            asc = ''
            for x in range(32):
                num = random.randrange(13000)
                asc = asc + chr(num)
            await client.change_nickname(server.me, asc)
            await asyncio.sleep(1)
        except Exception:
            continue
client.run(token, bot=False)
