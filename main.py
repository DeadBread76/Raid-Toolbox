import os
import re
import sys
import time
import discord
import asyncio
import requests
import youtube_dl
import subprocess
from colorama import init
from termcolor import colored

ydl_opts = {
    'outtmpl': '.\\spammer\\file.mp3',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
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
    print (colored("|           Welcome to DeadBread's Raid Toolbox         |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|           There are "+str(tcounter)+" tokens available.              |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|           1. Joiner                                   |","red"))
    print (colored("|           2. Leaver                                   |","red"))
    print (colored("|           3. Token Checker                            |","red"))
    print (colored("|           4. Message spammer                          |","red"))
    print (colored("|           5. Ascii spammer (Buggy)                    |","red"))
    print (colored("|           6. Mass mention spammer                     |","red"))
    print (colored("|           7. Voice Chat Spammer                       |","red"))
    print (colored("|                                                       |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    print (colored("|        Please enter the number of your choice.        |","red"))
    print (colored("+-------------------------------------------------------+","red"))
    choice = input()
    if int(choice) == 1:
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
    else:
        clear()
        print (colored('Invalid Option.',"yellow"))
        time.sleep(2)
        main()




def joiner():
    clear()
    link = input('Discord Invite Link: ')
    if len(link) > 7:
        link = link[19:]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\joiner.py',token,link],shell=True)
    main()

def leaver():
    clear()
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
    SERVER = input ("Server ID: ")
    chan = input ("Channel to spam in: ")
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\messagespam.py',token,SERVER,number,msgtxt,chan],shell=True)
        time.sleep(0.1)
    p.wait()

def asciispam():
    clear()
    print (colored("This works, although due to the high ammount of ascii characters the http requests usually becomes malformed.","blue"))
    input ("Press enter to continue...")
    clear()
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
    ytlink = input ('YouTube Link to play: ')
    SERVER = input('Server ID: ')
    chanid = input ('Voice channel ID: ')
    if os.path.isfile('.\\spammer\\file.mp3'):
        os.remove('.\\spammer\\file.mp3')
        print ("Removed old mp3.")
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

      
def friender(): #i will be adding this in the future, i just need to figure out how to get it working
    clear()
    userid = input('Users ID: ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\friender.py',token,userid],shell=True)
    p.wait()
    main()



main()

