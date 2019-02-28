import discord
import asyncio
import sys
import random
import aiohttp

useproxies = sys.argv[3]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

token = sys.argv[1]
game = sys.argv[2]

@client.event
async def on_ready():
    try:
        await client.change_presence(game=discord.Game(name=game))
    except Exception:
        return ''
client.run(token, bot=False)
