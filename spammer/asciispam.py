import discord
import asyncio
import random
import time
import sys
import os

client = discord.Client()
token = sys.argv[1]
tokenno = sys.argv[2]
textchan = sys.argv[3]
#fuck i'm stupid
#i had asc = "" up here instead of in the loop
@client.event
async def on_ready():
    print ("Token " + str(tokenno) + " logged in!")
    txtchan = client.get_channel(textchan)
    while True:
        try:
            asc = ""
            for x in range(1995):
                num = random.randrange(13000)
                asc = asc + chr(num)
            await client.send_message(txtchan, asc)
        except Exception:
            return ''

client.run(token, bot=False)
