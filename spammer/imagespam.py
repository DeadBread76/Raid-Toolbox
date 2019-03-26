import discord
import asyncio
import random
import sys
import os
import aiohttp
import logging

token = sys.argv[1]
tokenno = sys.argv[2]
textchan = sys.argv[3]
useproxies = sys.argv[4]

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
    counter = 1
    txtchan = client.get_channel(int(textchan))
    while not client.is_closed():
        try:
            if sys.platform.startswith('win32'):
                img = random.choice(os.listdir('.\\spammer\\images'))
                imgdir = '.\\spammer\\images\\'+img
            elif sys.platform.startswith('linux'):
                img = random.choice(os.listdir('spammer/images/'))
                imgdir = 'spammer/images/'+img
            file = discord.File(imgdir)
            await txtchan.send(file=file)
            await asyncio.sleep(int(counter))
            if counter != 1:
                counter -= 1
            else:
                pass
        except Exception as e:
            counter += 5

try:
    client.run(token, bot=False)
except Exception as c:
    logging.critical('Token {} Unable to login: {}'.format(str(tokenno),str(c)))
    print (c)
