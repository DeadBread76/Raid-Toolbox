import discord
import asyncio
import time
import sys
import os
import random
import aiohttp

useproxies = sys.argv[4]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]

@client.event
async def on_ready():
    print ("Token " + str(tokenno) + " logged in!")
    try:
        msg = ' '
        for m in client.get_server(SERVER).members:
            msg += m.mention + ' '
        while not client.is_closed:
           for c in client.get_server(SERVER).channels:
                if c.type != discord.ChannelType.text:
                   continue
                myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                print('Token ' + str(tokenno) + ' mass mentioning in: '+c.name)
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    try:
                        await client.send_message(c, m)
                    except:
                        print("Token " + str(tokenno) + ': Error sending mass mention.')
    except Exception:
        time.sleep(1)
    
client.run(token, bot=False)

