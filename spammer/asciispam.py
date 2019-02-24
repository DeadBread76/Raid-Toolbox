import discord
import asyncio
import random
import time
import sys
import os

client = discord.Client()
token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]
textchan = sys.argv[4]

@client.event
async def on_ready():
    asc = ""
    print ("Token " + str(tokenno) + " logged in!")
    txtchan = client.get_channel(textchan)
    #print ("Token " + str(tokenno) + " spamming ascii in: " + txtchan.name)
    while True:
        try:
            for x in range(1995):
                num = random.randrange(13000)
                asc = asc + chr(num)
            await client.send_message(txtchan, asc)
        except Exception:
            print("Error, probably overloading. Sleeping for 3 seconds.")
            time.sleep(3)

client.run(token, bot=False)
