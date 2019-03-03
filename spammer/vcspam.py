import discord
import asyncio
import youtube_dl
import sys
import os
import random
import aiohttp

useproxies = sys.argv[4] #proxies for voice chats smh
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

token = sys.argv[1]
tokenno = sys.argv[2]
voice_id = sys.argv[3]


@client.event
async def on_ready():
    print('Token ' + str(tokenno) + ' Logged in!')
    await asyncio.sleep(1)
    await voice()

async def voice():
    voice_channel = client.get_channel(voice_id)
    while not client.is_closed:
        try:
            vc = await client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('.\\spammer\\file.wav')
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            await vc.disconnect()
        except Exception as exception:
            print('Failed to join voice channel')
            print(exception)
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
