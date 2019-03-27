import discord
import sys
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
    server = client.get_guild(int(SERVER))
    mention = ''
    try:
        for role in server.roles:
            if role.mentionable:
                mention += role.mention + ' '
            else:
                continue
        while not client.is_closed():
            for channel in server.text_channels:
                myperms = channel.permissions_for(server.get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                for m in [mention[i:i+1999] for i in range(0, len(mention), 1999)]:
                    try:
                        await channel.send(m)
                    except Exception:
                        pass
    except Exception as e:
        print (e)
        pass
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
