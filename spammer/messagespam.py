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
allchan = sys.argv[6]

@client.event
async def on_ready():
    print ("Token " + str(tokenno) + " logged in!")
    txtchan = client.get_channel(textchan)
    if allchan == 'true':
        while not client.is_closed:
           for c in client.get_server(SERVER).channels:
                if c.type != discord.ChannelType.text:
                   continue
                myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
                if not myperms.send_messages:
                    continue
                try:
                    await client.send_message(c, msgtxt)
                except:
                    print("Token " + str(tokenno) + ': Error sending message.')
    else:
        while True:
            await client.send_message(txtchan, msgtxt)

client.run(token, bot=False)

