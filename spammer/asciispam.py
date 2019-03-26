import discord
import random
import sys
import aiohttp
import logging

token = sys.argv[1]
tokenno = sys.argv[2]
textchan = sys.argv[3]
allchan = sys.argv[4]
SERVER = sys.argv[5]
useproxies = sys.argv[6]

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
            for channel in server.text_channels::
                myperms = channel.permissions_for(server.get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                asc = ''
                for x in range(1999):
                    num = random.randrange(13000)
                    asc = asc + chr(num)
                try:
                    await channel.send(asc)
                except Exception:
                    pass
    else:
        txtchan = client.get_channel(int(textchan))
        while not client.is_closed():
            asc = ''
            for x in range(1999):
                num = random.randrange(13000)
                asc = asc + chr(num)
            try:
                await txtchan.send(asc)
            except Exception:
                    pass
try:
    client.run(token, bot=False)
except Exception as c:
    logging.critical('Token {} Unable to login: {}'.format(str(tokenno),str(c)))
    print (c)
