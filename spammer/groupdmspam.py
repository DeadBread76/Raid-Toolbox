import discord
import sys
import random
import aiohttp
import logging

token = sys.argv[1]
group = sys.argv[2]
tokenno = sys.argv[3]
msgtxt = sys.argv[4]
useproxies = sys.argv[5]

logging.basicConfig(filename='RTB.log', filemode='w', format='Token {}'.format(str(tokenno))+' - %(levelname)s - %(message)s',level=logging.CRITICAL)
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
    logging.critical('Token {} Unable to login: {}'.format(str(tokenno),str(c)))
    print (c)
