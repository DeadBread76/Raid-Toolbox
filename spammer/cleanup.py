import discord
import asyncio
import time
import sys
import os

client = discord.Client()
token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]

@client.event
async def on_ready():
    #print ("Token " + str(tokenno) + " logged in!")
    for channel in client.get_server(SERVER).channels:
        if channel.type != discord.ChannelType.text:
            continue
        myperms = channel.permissions_for(client.get_server(SERVER).get_member(client.user.id))
        if not myperms.send_messages:
            continue
        for x in range(3):
            async for x in client.logs_from(channel):
                channame = channel.name
                if x.author.id == str(client.user.id):
                    await client.delete_message(x)
                    #print ("Token " + str(tokenno) + ": Cleaned " + channame)
    client.close()


client.run(token, bot=False)

