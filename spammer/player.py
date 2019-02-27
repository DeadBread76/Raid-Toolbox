#moved the code into here to give it some value lmao
#you can also change the songs or add some if you want
import os
import random
import winsound
import youtube_dl
from colorama import init
from termcolor import colored
init()
clear = lambda: os.system('cls')

ydl_opts = {
    'outtmpl': '.\\spammer\\song.webm',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
clear()
print (colored(";)","red"))
if os.path.isfile('.\\spammer\\song.wav'):
    os.remove('.\\spammer\\song.wav')
music = ['https://www.youtube.com/watch?v=t7WAPIR67xc',
         'https://www.youtube.com/watch?v=F2BpaeIcVHo',
         'https://www.youtube.com/watch?v=-cCPZQ3mvck',
         'https://www.youtube.com/watch?v=bQ_z8MNApz4',
         'https://www.youtube.com/watch?v=rPhte_IRb2o',
         'https://www.youtube.com/watch?v=IWEpkRoxK0o',
         'https://www.youtube.com/watch?v=CFbpQ14xkt4',
         'https://www.youtube.com/watch?v=UiVb7KrSQ2c',
         'https://www.youtube.com/watch?v=KoVG-F8mekE',
         'https://www.youtube.com/watch?v=68wk6m05ojw',
         'https://www.youtube.com/watch?v=LcpQkOV-kKc']
file = (random.choice(music))
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([file])
clear()
print ("Playing " + str(file))
winsound.PlaySound('.\\spammer\\song.wav', winsound.SND_FILENAME) 
