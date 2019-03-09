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
group = sys.argv[2]
tokenno = sys.argv[3]
msgtxt = sys.argv[4]

@client.event
async def on_ready():
    groupdm = client.get_channel(group)
    while not client.is_closed:
        try:
            await client.send_message(groupdm, msgtxt)
        except Exception:
            return ''

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)


