import discord
import sys
import random
import aiohttp

token = sys.argv[1]
tokenno = sys.argv[2]
msgtxt = sys.argv[3]
userid = sys.argv[4]
useproxies = sys.argv[5]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()


@client.event
async def on_ready():
    user = await client.fetch_user(int(userid))
    while not client.is_closed():
        try:
            await user.send(msgtxt)
        except Exception:
            pass

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
