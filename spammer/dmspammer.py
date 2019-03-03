import discord
import asyncio
import time
import sys
import os
import random
import aiohttp

useproxies = sys.argv[5]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()
token = sys.argv[1]
tokenno = sys.argv[2]
msgtxt = sys.argv[3]
userid = sys.argv[4]

@client.event
async def on_ready():
    print ("Token " + str(tokenno) + " logged in!")
    user = await client.get_user_info(userid)
    while not client.is_closed:
        try:
            await client.send_message(user, msgtxt)
        except Exception as e:
            print (str(tokenno) + "error: " + e)
            

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
