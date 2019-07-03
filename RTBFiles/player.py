import os
import sys
import time
import ctypes
import random
import requests
import subprocess
import youtube_dl

ydl_opts = {
    'outtmpl': 'RTBFIles/song.webm',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
winpy = sys.argv[1]
music = []
played = []
if os.path.isfile('RTBFIles/song.wav'):
    os.remove('RTBFIles/song.wav')
if os.path.isfile("RTBFIles/YtLinks"):
    with open ("RTBFIles/YtLinks", "r") as handle:
        lines = handle.readlines()
        for line in lines:
            music.append(line.rstrip())
else:
    songs = requests.get('https://pastebin.com/raw/1zwdz16u').text
    lines = songs.split('\n')
    for line in lines:
        music.append(line.rstrip())
while True:
    try:
        os.remove('RTBFIles/song.wav')
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
    p = subprocess.Popen([winpy,'RTBFIles/play.py'])
    while p.poll() == None:
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing: {}".format(video_title))
        time.sleep(5)
    played.append(selectedsong)
    if len(played) == len(music):
        break
