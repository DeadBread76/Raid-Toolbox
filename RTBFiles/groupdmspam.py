import discord
import sys
import random
import aiohttp

token = sys.argv[1]
group = sys.argv[2]
tokenno = sys.argv[3]
msgtxt = sys.argv[4]
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
    groupdm = client.get_channel(int(group))
    while not client.is_closed():
        try:
            await groupdm.send(msgtxt)
        except Exception:
            pass
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
