import os
import sys
import threading
import json
import time
import psutil
from playsound import playsound


def parent_check():
    while True:
        if psutil.pid_exists(int(parentpid)):
            pass
        else:
            os.kill(os.getpid(), 15)
        time.sleep(1)


def config_check():
    while True:
        with open('config.json', 'r') as handle:
            config = json.load(handle)
            skin = config['skin']
        if not skin == my_theme:
            os.kill(os.getpid(), 15)
        time.sleep(0.5)


mode = sys.argv[1]
if mode == "Theme":
    mp3 = sys.argv[2]
    my_theme = sys.argv[3]
    parentpid = sys.argv[4]
    t = threading.Thread(name='config_check', target=config_check)
    p = threading.Thread(name='parent_check', target=parent_check)
    p.start()
    t.start()
    while True:
        playsound(sys.argv[2])
else:
    parentpid = sys.argv[3]
    t = threading.Thread(name='parent_check', target=parent_check)
    t.start()
    playsound(sys.argv[2])
    os.kill(os.getpid(), 15)
