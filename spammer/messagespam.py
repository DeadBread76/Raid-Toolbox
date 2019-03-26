import discord
import sys
import random
import aiohttp
import logging

token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]
msgtxt = sys.argv[4]
textchan = sys.argv[5]
allchan = sys.argv[6]
useproxies = sys.argv[7]

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
    server = client.get_guild(int(SERVER))
    if allchan == 'true':
        while not client.is_closed():
            for channel in server.channels:
                if not isinstance(channel, discord.TextChannel):
                    continue
                myperms = channel.permissions_for(server.get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                try:
                    await channel.send(msgtxt)
                except Exception:
                    pass
    else:
        txtchan = client.get_channel(int(textchan))
        while not client.is_closed():
            await txtchan.send(msgtxt)

try:
    client.run(token, bot=False)
except Exception as c:
    logging.critical('Token {} Unable to login: {}'.format(str(tokenno),str(c)))
    print (c)
