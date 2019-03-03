import discord
import asyncio
import youtube_dl
import sys
import os
import random
import aiohttp

useproxies = sys.argv[4] 
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()
token = sys.argv[1]
tokenno = sys.argv[2]
voice_id = sys.argv[3]

@client.event
async def on_ready():
    voice_channel = client.get_channel(voice_id)
    while not client.is_closed:
        await client.join_voice_channel(voice_channel)
        await asyncio.sleep(1)
        await client.join_voice_channel(voice_channel).disconnect()
        await asyncio.sleep(3)

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)

