import os
import re
import sys
import time
import random
import discord
import asyncio
import requests
import winsound
import youtube_dl
import subprocess
from colorama import init
from termcolor import colored

ydl_opts = {
    'outtmpl': '.\\spammer\\file.webm',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

init()
tcounter = 0
clear = lambda: os.system('cls')

if os.path.exists('tokens.txt'):
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        for x in line:
            tcounter += 1
        
        if tcounter == 0:
            print ("Please add some tokens to the tokens.txt file.")
            time.sleep(5)
            sys.exit()
else:
    with open('tokens.txt','w+') as handle:
        print ("Please add some tokens to the tokens.txt file that was just created")
        time.sleep(5)
        sys.exit()

def main():
    clear()
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|         Welcome to DeadBread's Raid Toolbox           |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|           There are "+str(tcounter)+" tokens available.              |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|           0. Exit                                     |","red"))
    print (colored("|           1. Joiner                                   |","red"))
    print (colored("|           2. Leaver                                   |","red"))
    print (colored("|           3. Token Checker                            |","red"))
    print (colored("|           4. Message spammer                          |","red"))
    print (colored("|           5. Ascii spammer (Buggy)                    |","red"))
    print (colored("|           6. Mass mention spammer                     |","red"))
    print (colored("|           7. Voice Chat Spammer                       |","red"))
    print (colored("|           8. DM Spammer                               |","red"))
    print (colored("|           9. Friend Request Spammer                   |","red"))
    print (colored("|           10. Image Spammer                           |","red"))
    print (colored("|           11. Playing game changer                    |","red"))
    print (colored("|           12. Ascii Nickname (Spams Audit log)        |","red"))
    print (colored("|                                                       |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|        Please enter the number of your choice.        |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    choice = input()
    try:
        if int(choice) == 0:
            os.system("taskkill /f /im python.exe")
        elif int(choice) == 1:
            joiner() 
        elif int(choice) == 2:
            leaver()
        elif int(choice) == 3:
            tokencheck()
        elif int(choice) == 4:
            messagespam()
        elif int(choice) == 5:
            asciispam()
        elif int(choice) == 6:
            massmentioner()
        elif int(choice) == 7:
            vcspam()
        elif int(choice) == 8:
            dmspam()
        elif int(choice) == 9:
            friender()
        elif int(choice) == 10:
            imagespam()
        elif int(choice) == 11:
            gamechange()
        elif int(choice) == 12:
            asciinick()
        elif int(choice) == 986:
            wew()
        else:
            clear()
            print (colored('Invalid Option.',"yellow"))
            input()
            main()
    except Exception:
        clear()
        print (colored('Invalid Input.',"yellow"))
        input()
        main()

def joiner():
    clear()
    print (colored("Discord invite joiner.","red"))
    link = input('Discord Invite Link: ')
    if len(link) > 7:
        link = link[19:]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\joiner.py',token,link],shell=True)
    main()

def leaver():
    clear()
    print (colored("Discord server leaver.","red"))
    ID = input ('ID of the server to leave: ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\leaver.py',token,ID],shell=True)
    main()

def tokencheck():
    clear()
    vcounter = 0
    icounter = 0
    print ("Checking tokens...")
    with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
            try:
                if src.status_code == 200:
                    print (colored(token + ' Valid.',"green"))
                    vcounter +=1
                    with open('valid.txt','a') as handle:
                        handle.write(token + '\n')
                else:
                    print(colored(token + ' Invalid.',"red"))
                    icounter +=1
                    with open('invalid.txt','a') as handle:
                        handle.write(token + '\n')
            except Exception:
                print("Yeah we can't contact discordapp.com")
        print ("---------------------------------------")
        print (colored("Number of valid tokens: " + str(vcounter),"green"))
        print (colored("Number of invalid tokens: " + str(icounter),"red"))
        print (colored("tokens.txt has been sorted.","green"))
        print ("---------------------------------------")
        input("Press enter to return to menu.")
        main()

def messagespam():
    clear()
    print (colored("Discord Server message spammer.","red"))
    SERVER = input ("Server ID: ")
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
        allchan = 'true'
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if allchan == 'true':
            p = subprocess.Popen(['python','.\\spammer\\messagespam.py',token,SERVER,number,msgtxt,chan,allchan],shell=True)
        else:   
            p = subprocess.Popen(['python','.\\spammer\\messagespam.py',token,SERVER,number,msgtxt,chan],shell=True)
        time.sleep(0.1)
    p.wait()

def asciispam():
    clear()
    print (colored("This works, although due to the high ammount of ascii characters the http request usually becomes malformed.","blue"))
    input ("Press enter to continue...")
    clear()
    print (colored("Discord server ascii spammer.","red"))
    SERVER = input('Server ID: ')
    chan = input ("Channel to spam in: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\asciispam.py',token,SERVER,number,chan],shell=True)
        time.sleep(0.1)
    p.wait()
    
    
def massmentioner():
    clear()
    print (colored("Discord server mass mentioner.","red"))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\massmention.py',token,SERVER,number],shell=True)
        time.sleep(0.1)
    p.wait()

def vcspam():
    clear()
    tcounter = 0
    print (colored("Discord VC joiner/spammer.","red"))
    ytlink = input ('YouTube Link to play: ')
    SERVER = input('Server ID: ')
    chanid = input ('Voice channel ID: ')
    if os.path.isfile('.\\spammer\\file.wav'):
        os.remove('.\\spammer\\file.wav')
        print ("Removed old .wav.")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytlink])
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\vcspam.py',token,SERVER,number,chanid],shell=True)
        time.sleep(0.1)
    p.wait()

def dmspam():
    clear()
    print (colored("Discord user DM spammer.","red"))
    user = input ("User's ID: ")
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\dmspammer.py',token,number,msgtxt,user],shell=True)
    p.wait()


def friender(): #finally it works
    clear()
    print (colored("Discord user mass friender.","red"))
    userid = input("User's ID: ")
    tokenlist = open("tokens.txt").read().splitlines()
    tcounter = 0
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\friender.py',token,userid],shell=True)
    p.wait()
    main()

def imagespam():
    clear()
    print (colored("Discord server image spammer.","red"))
    SERVER = input ("Server ID: ")
    chan = input ("Channel to spam in: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\imagespam.py',token,SERVER,number,chan],shell=True)
        time.sleep(0.1)
    p.wait()

def gamechange():
    clear()
    print (colored("Discord game playing changer.","red"))
    print (colored("This will probably slow down some attacks.","blue"))
    print ('Name of game to play: ')
    game = input ('Playing ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\gamechange.py',token,game],shell=True)
    time.sleep(5)
    main()

def asciinick():
    clear()
    print (colored("Discord random ascii nickname.","red"))
    print (colored("This will probably slow down some attacks.","blue"))
    SERVER = input ("Server ID: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\nickname.py',token,SERVER],shell=True)
    time.sleep(5)
    main()

def wew():
    print (colored(";)","red"))
    if os.path.isfile('.\\spammer\\file.wav'):
        os.remove('.\\spammer\\file.wav')
    e = ['https://www.youtube.com/watch?v=-cCPZQ3mvck', 'https://www.youtube.com/watch?v=bQ_z8MNApz4', 'https://www.youtube.com/watch?v=rPhte_IRb2o', 'https://www.youtube.com/watch?v=dAtnNLyeP-8', 'https://www.youtube.com/watch?v=IWEpkRoxK0o']
    file = (random.choice(e))
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([file])
    p = subprocess.Popen(['python','.\\spammer\\player.py'],shell=True)
    main()

main()

