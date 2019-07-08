import os
import winsound

winsound.PlaySound('RTBFiles/song.wav', winsound.SND_FILENAME)
os.system("taskkill /F /pid "+str(os.getpid()))
