import discord
import asyncio
import youtube_dl
import time
import sys
import os


client = discord.Client()

token = sys.argv[1]
SERVER = sys.argv[2]
tokenno = sys.argv[3]
voice_id = sys.argv[4]


@client.event
async def on_ready():
    print('Token ' + str(tokenno) + ' Logged in!')
    await client.loop.create_task(main())

async def main():
    time.sleep(8)
    voice_channel1 = client.get_channel(voice_id)
    vc = await client.join_voice_channel(voice_channel1)
    player = vc.create_ffmpeg_player('.\\spammer\\file.mp3')
    player.start()

client.run(token, bot=False)
