import discord
import asyncio
import time
import sys
import os

client = discord.Client()
token = sys.argv[1]
tokenno = sys.argv[2]
msgtxt = sys.argv[3]
userid = sys.argv[4]

@client.event
async def on_ready():
    print ("Token " + str(tokenno) + " logged in!")
    user = await client.get_user_info(userid)
    while True:
        await client.send_message(user, msgtxt)

client.run(token, bot=False)
