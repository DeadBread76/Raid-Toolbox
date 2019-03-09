import discord
import asyncio
import time
import sys
import os
import random

token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]
text = sys.argv[4]
textchan = sys.argv[5]
client = discord.Client()
@client.event
async def on_ready():
    txtchan = client.get_channel(textchan)
    server = client.get_server(SERVER)
    while not client.is_closed:
        for word in text:
            await client.send_message(txtchan, word)

try:
    client.run(token, bot=False)
except Exception as c:
    print (c)

