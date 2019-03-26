import discord
import asyncio
import random
import sys
import aiohttp


token = sys.argv[1]
SERVER = sys.argv[2]
useproxies = sys.argv[3]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

@client.event
async def on_ready():
    server = client.get_guild(int(SERVER))
    while not client.is_closed():
        try:
            asc = ''
            for x in range(32):
                num = random.randrange(13000)
                asc = asc + chr(num)
            await server.me.edit(nick=asc)
            await asyncio.sleep(3)
        except Exception:
            pass
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
