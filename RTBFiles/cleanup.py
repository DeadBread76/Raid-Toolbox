import discord
import sys
import random
import aiohttp

token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]

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
    server = client.get_guild(int(SERVER))
    for channel in server.text_channels:
        myperms = channel.permissions_for(server.get_member(client.user.id))
        if not myperms.send_messages:
            continue
        async for message in channel.history(limit=9999):
            if message.author == client.user:
                await message.delete()
    await client.close()

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
