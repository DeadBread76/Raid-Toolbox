import discord
import asyncio
import random
import time
import sys
import os
import random
import aiohttp

useproxies = sys.argv[6]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

token = sys.argv[1]
tokenno = sys.argv[2]
textchan = sys.argv[3]
allchan = sys.argv[4]
SERVER = sys.argv[5]
#fuck i'm stupid
#i had asc = "" up here instead of in the loop
@client.event
async def on_ready():
    txtchan = client.get_channel(textchan)
    if allchan == 'true': #wew no sleep
        while not client.is_closed:
            for c in client.get_server(SERVER).channels:
                if c.type != discord.ChannelType.text:
                    continue
                myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                asc = ''
                for x in range(1999):
                    num = random.randrange(13000)
                    asc = asc + chr(num)
                try:
                    await client.send_message(c, asc)
                except Exception:
                    return ''
                    
    else:
        while not client.is_closed:
            asc = ''
            for x in range(1999):
                num = random.randrange(13000)
                asc = asc + chr(num)
            try:
                await client.send_message(txtchan, asc)
            except Exception:
                    return ''
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
