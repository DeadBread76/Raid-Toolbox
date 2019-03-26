import discord
import asyncio
import sys
import random
import aiohttp


token = sys.argv[1]
tokenno = sys.argv[2]
voice_id = sys.argv[3]
volume = sys.argv[1]
useproxies = sys.argv[4]  # proxies for voice chats smh

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

@client.event
async def on_ready():
    await asyncio.sleep(1)
    voice_channel = client.get_channel(int(voice_id))
    while not client.is_closed():
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('.\\spammer\\file.wav'))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 10.0
        while vc.is_playing():
            await asyncio.sleep(3)
        await vc.disconnect(force=True)

try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
