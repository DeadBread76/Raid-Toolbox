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
#sends images but will probably send any file you put in the images folder ¯\_(ツ)_/¯ 
counter = 1
@client.event
async def on_ready():
    counter = 1
    print ("Token " + str(tokenno) + " logged in and starting to spam images.")
    txtchan = client.get_channel(textchan)
    while not client.is_closed:
        try:
            img = random.choice(os.listdir('.\\spammer\\images'))
            imgdir = '.\\spammer\\images\\' + img
            await client.send_file(txtchan, imgdir)
            await asyncio.sleep(int(counter))
        except Exception:
            print ("Error sending file, slowing down.")
            counter += 5

client.run(token, bot=False)
