import discord
import asyncio
import sys
import random
import aiohttp

token = sys.argv[1]
tokenno = sys.argv[2]
SERVER = sys.argv[3]
useproxies = sys.argv[4]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()



@client.event
async def on_ready():
    CHANNELS = []
    server = client.get_guild(int(SERVER))
    for channel in server.voice_channels:
        myperms = channel.permissions_for(server.get_member(client.user.id))
        if not myperms.connect:
            continue
        CHANNELS.append(channel)
    while not client.is_closed():
        try:
            voicechannel = random.choice(CHANNELS)
            vc = await voicechannel.connect()
            await asyncio.sleep(0.1)
            await vc.disconnect(force=True)
        except Exception as e:
            print (e)
            pass
try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
