import discord
import asyncio
import time
import sys
import os

client = discord.Client()
token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]
msgtxt = sys.argv[4]
textchan = sys.argv[5]

@client.event
async def on_ready():
    print ("Token " + str(tokenno) + " logged in!")
    txtchan = client.get_channel(textchan)
    while True:
        await client.send_message(txtchan, msgtxt)

client.run(token, bot=False)

