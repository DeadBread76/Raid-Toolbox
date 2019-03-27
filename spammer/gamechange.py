import discord
import sys
import random
import aiohttp

token = sys.argv[1]
game = sys.argv[2]
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
    try:
        await client.change_presence(activity=discord.Game(name=game))
    except Exception:
        pass
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
