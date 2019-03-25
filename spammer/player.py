import os
import time
import ctypes
import random
import subprocess
import youtube_dl

ydl_opts = {
    'outtmpl': '.\\spammer\\song.webm',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

if os.path.isfile('.\\spammer\\song.wav'):
    os.remove('.\\spammer\\song.wav')
music = []
with open (".\\spammer\\YtLinks","r") as handle:
    lines = handle.readlines()
    for line in lines:
        music.append(line.rstrip())

played = []

while True:
    try:
        os.remove('.\\spammer\\song.wav')
    except Exception:
        pass
    song = random.choice(music)
    selectedsong = song
    while selectedsong in played:
        song = random.choice(music)
        selectedsong = song
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(selectedsong, download=True)
        video_title = info_dict.get('title', None)
    p = subprocess.Popen(['python','.\\spammer\\play.py'])
    while p.poll() == None:
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing: {}".format(video_title))
        time.sleep(5)
    played.append(selectedsong)
    if len(played) == len(music):
        break
