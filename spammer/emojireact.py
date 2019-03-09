import discord
import asyncio
import time
import sys
import os
import random
import aiohttp

useproxies = sys.argv[6]
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
chanid = sys.argv[4]
tokenno = sys.argv[5]

@client.event
async def on_ready():
    channel = client.get_channel(chanid)
    message = await client.get_message(channel, messageid)
    await client.add_reaction(message, emojiname)
    await client.close()

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
