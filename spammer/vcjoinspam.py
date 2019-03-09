import discord
import asyncio
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
tokenno = sys.argv[2]
SERVER = sys.argv[3]
CHANNELS = []

@client.event
async def on_ready():
    server = client.get_server(SERVER)
    for chan in server.channels:
        if chan.type != discord.ChannelType.voice:
            continue
        myperms = chan.permissions_for(server.get_member(client.user.id))
        if not myperms.connect:
            continue
        CHANNELS.append(chan)
    while not client.is_closed:
        try:
            voicechannel = random.choice(CHANNELS)
            vc = await client.join_voice_channel(voicechannel)
            await asyncio.sleep(0.1)
            await vc.disconnect()
        except Exception:
            await on_ready()
try:
    client.run(token, bot=False)
except Exception as c:
    print ("Token " + str(tokenno)+ ": " +c)

