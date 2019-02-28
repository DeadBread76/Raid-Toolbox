import discord
import asyncio
import time
import sys
import os
import random
import aiohttp

useproxies = sys.argv[5]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()
token = sys.argv[1]
messageid = sys.argv[2]
emojiname = sys.argv[3]
tokenno = sys.argv[4]

@client.event
async def on_ready():
    emoji = ':' + emojiname + ':'
    await client.add_reaction(messageid, emoji)
    client.close()

client.run(token, bot=False)
