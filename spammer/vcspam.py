import discord
import asyncio
import youtube_dl
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
    await asyncio.sleep(6)
    voice_channel = client.get_channel(voice_id)
    try:
        vc = await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('.\\spammer\\file.wav')
        player.start()
    except Exception:
        print('Failed to join voice channel')

client.run(token, bot=False)
