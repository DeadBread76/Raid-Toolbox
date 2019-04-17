# This is an example plugin, made to assist people in making their own.
import subprocess
import time
import sys
import os

pythonprefix = sys.argv[1]
text = 'What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit.'
#these are the inputs, for the user to enter information.
chan = input ("Channel to spam in: ")
#tokenlist is needed to use the tokens from RTB
tokenlist = open("tokens.txt").read().splitlines()
tcounter = 0
for token in tokenlist:
    tcounter += 1
    number = str(tcounter) #For numbering the tokens
    p = subprocess.Popen([pythonprefix,'plugins/Copypasta Spammer (Example Plugin)/copypastaspam.py',token,number,text,chan],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(0.1) #sleeping so the load isnt so much.
    with open ('pluginpids','a+') as handle:
        handle.write(str(p.pid)+'\n')
input("Press enter to return to raid toolbox.") #this will confirm retruning to raid toolbox once done
