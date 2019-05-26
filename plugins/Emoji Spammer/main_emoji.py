# Plugin Author: DeadBread76
# Plugin Name: tourettes
# Date: 29/03/2019

import subprocess
import time
import sys
import os

pyprefix = sys.argv[1]
print("Edit Emoticon at emojispammer.py")
chan = input("Channel ID: ")
tokenlist = open("tokens.txt").read().splitlines()
tcounter = 0

for token in tokenlist:
    tcounter += 1
    number = str(tcounter)
    p = subprocess.Popen([pyprefix,'plugins/emojispammer/emojispammer.py',token,chan],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(0.1)
    with open('pluginpids', 'a+') as handle:
        handle.write(str(p.pid)+'\n')
input("Press enter to return to raid toolbox.")
