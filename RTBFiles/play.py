import os
import sys
import winsound
import threading
import time
import psutil


def parent_check():
    while True:
        if psutil.pid_exists(int(sys.argv[2])):
            pass
        else:
            os.system("taskkill /F /pid "+str(os.getpid()))
        time.sleep(1)


t = threading.Thread(name='parent_check', target=parent_check)
t.start()
winsound.PlaySound(sys.argv[1], winsound.SND_FILENAME)
os.system("taskkill /F /pid "+str(os.getpid()))
