import discord
import asyncio
import random
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
SERVER = sys.argv[2]

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
            await asyncio.sleep(5)
        except Exception:
            continue
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)

