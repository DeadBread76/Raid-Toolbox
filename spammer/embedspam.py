import discord
import asyncio
import sys

token = sys.argv[1]
title = sys.argv[2]
author = sys.argv[3]
iconurl = sys.argv[4]
thumburl = sys.argv[5]
footer = sys.argv[6]
textchan = sys.argv[7]
client = discord.Client()

#set embed
embed=discord.Embed(title=title)
embed.set_author(name=author, icon_url=iconurl)
embed.set_thumbnail(url=thumburl)
embed.set_footer(text=footer)

@client.event
async def on_ready():
    try:
        txtchan = client.get_channel(textchan)
        while True:
            await client.send_message(txtchan, embed=embed)
    except Exception:
        return ''

client.run(token, bot=False)

