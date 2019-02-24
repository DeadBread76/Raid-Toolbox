import sys
import youtube_dl

ydl_opts = {
    'outtmpl': '.\\spammer\\file.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
SERVER = sys.argv[1]
chanid = sys.argv[2]
ytlink = sys.argv[3]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([ytlink])

tcounter = 0
tokenlist = open("../tokens.txt").read().splitlines()
for token in tokenlist:
    tcounter += 1
    number = str(tcounter)
    p = subprocess.Popen(['python','.\\spammer\\vcspam.py',token,SERVER,number],shell=True)
    time.sleep(0.1)
p.wait()
