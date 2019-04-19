#!/usr/bin/env python3
# coding: utf-8
# Raid Toolbox
# Author: DeadBread76 - https://github.com/DeadBread76/
# Febuary 23rd, 2019

rtbversion = "0.3.6r1"
smversion = "0.1.6r3"

from config import*

if verbose == 1:
    try:
        with open ("load.log", "w+") as handle:
            print ("Loading system modules...")
            import os
            print ("Loaded os")
            handle.write("Loaded os\n")
            import sys
            print ("Loaded sys")
            handle.write("Loaded sys\n")
            import time
            print ("Loaded time")
            handle.write("Loaded time\n")
            import json
            print ("Loaded json")
            handle.write("Loaded json\n")
            import ctypes
            print ("Loaded ctypes")
            handle.write("Loaded ctypes\n")
            if sys.platform.startswith('win32'):
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading... | Verbose Mode")
                handle.write("Set Title, Windows, ctypes\n")
                if runasadmin == 1:
                    def is_admin():
                        try:
                            return ctypes.windll.shell32.IsUserAnAdmin()
                        except:
                            return False
                    if is_admin():
                        pass
                    else:
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                        sys.exit()
            elif sys.platform.startswith('linux'):
                sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading... | Verbose Mode\x07")
                handle.write("Set Title, Linux, sys\n")
            import random
            print ("Loaded random")
            handle.write("Loaded random\n")
            import datetime
            print ("Loaded datetime")
            handle.write("Loaded datetime\n")
            import platform
            print ("Loaded platform")
            handle.write("Loaded platform\n")
            import shutil
            print ("Loaded shutil")
            handle.write("Loaded shutil\n")
            import subprocess
            print ("Loaded subprocess")
            handle.write("Loaded subprocess\n")
            import signal
            print ("Loaded signal")
            handle.write("Loaded signal\n")
            from distutils.dir_util import copy_tree
            print ("Loaded copy_tree")
            handle.write("Loaded copy_tree\n")
            if sys.platform.startswith('win32'):
                from subprocess import CREATE_NEW_CONSOLE
                print ("Loaded CREATE_NEW_CONSOLE")
                handle.write("Loaded CREATE_NEW_CONSOLE\n")
            from tkinter import *
            print ("Loaded tkinter")
            handle.write("Loaded tkinter\n")
            from tkinter.filedialog import *
            print ("Loaded tkinter.filedialog")
            handle.write("Loaded tkinter.filedialog\n")
    except Exception as i:
        print ("Error loading system module, Exception: "+str(i))
        with open ("load.log", "a") as handle:
            handle.write(str(i)+"\n")
    with open ("load.log", "a") as handle:
        try:
            print ("Loading discord.py...")
            import discord
            print ("Loaded discord.py")
            handle.write("Loaded discord.py\n")
        except Exception as i:
            print ("Error Loading discord.py")
            handle.write("Error Loading discord.py\n")
        try:
            print ("Loading requests...")
            import requests
            print ("Loaded requests")
            handle.write("Loaded requests\n")
        except Exception as i:
            print ("Error Loading requests")
            handle.write("Error Loading requests\n")
        try:
            print ("Loading youtube-dl...")
            import youtube_dl
            print ("Loaded youtube-dl")
            handle.write("Loaded youtube-dl\n")
        except Exception as i:
            print ("Error Loading youtube-dl")
            handle.write("Error Loading youtube-dl\n")
        try:
            print ("Loading colorama...")
            from colorama import init
            print ("Loaded colorama")
            handle.write("Loaded colorama\n")
        except Exception as i:
            print ("Error Loading colorama")
            handle.write("Error Loading colorama\n")
        try:
            print ("Loading termcolor...")
            from termcolor import colored
            print ("Loaded termcolor")
            handle.write("Loaded termcolor\n")
        except Exception as i:
            print ("Error Loading termcolor")
            handle.write("Error Loading termcolor\n")
        try:
            print ("Loading proxyscrape...")
            from proxyscrape import create_collector
            print ("Loaded proxyscrape")
            handle.write("Loaded proxyscrape\n")
        except Exception as i:
            print ("Error Loading proxyscrape")
            handle.write("Error Loading proxyscrape\n")
    print ("Starting...")

else:
    try:
        import os
        import sys
        import time
        import json
        import ctypes
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading...")
            if runasadmin == 1:
                def is_admin():
                    try:
                        return ctypes.windll.shell32.IsUserAnAdmin()
                    except:
                        return False
                if is_admin():
                    pass
                else:
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
                    sys.exit()
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading...\x07")
        else:
            print ("Unsupported OS.")
            input()
            sys.exit()
        import random
        import datetime
        import platform
        import shutil
        import subprocess
        import signal
        import discord
        import requests
        import youtube_dl
        from colorama import init
        from termcolor import colored
        from proxyscrape import create_collector
        from distutils.dir_util import copy_tree
        if sys.platform.startswith('win32'):
            from subprocess import CREATE_NEW_CONSOLE
        from tkinter import *
        from tkinter.filedialog import *
    except Exception as i:
        print ("Module error: " + str(i))
        print ("Please check that the module is installed.")
        install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
        if install.lower() == 'y':
            if sys.platform.startswith('win32'):
                installation = subprocess.Popen([winpip,'install','-r','requirements.txt','--user'])
            elif sys.platform.startswith('linux'):
                installation = subprocess.Popen([linuxpip,'install','-r','requirements.txt'])
            installation.wait()
            print("Please Restart Raid Toolbox.")
            input()
            sys.exit()
        else:
            sys.exit()
if sys.platform.startswith('win32'):
    ydl_opts = {
        'outtmpl': '.\\spammer\\file.webm',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
elif sys.platform.startswith('linux'):
    ydl_opts = {
        'outtmpl': 'spammer/file.webm',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

init()
if menucolour.lower() == 'random':
    colours=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    menucolour = random.choice(colours)
tcounter = 0
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')

if os.path.isfile("pluginpids"):
    os.remove("pluginpids")
if os.path.isfile("ffmpeg.zip"):
    try:
        shutil.unpack_archive("ffmpeg.zip")
        shutil.unpack_archive("ffplay.zip")
        shutil.unpack_archive("ffprobe.zip")
        os.remove("ffmpeg.zip")
        os.remove("ffplay.zip")
        os.remove("ffprobe.zip")
    except Exception:
        pass
collector = create_collector('my-collector', 'https')

if os.path.exists('tokens.txt'):
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        for x in line:
            tcounter += 1
else:
    with open('tokens.txt','w+') as handle:
        print ("Created Tokens.txt")

currentattacks = []
spawnedpids = []

def main(currentattacks,spawnedpids):
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    elif sys.platform.startswith('linux'):
        os.system("printf '\033[8;30;100t'")
    tcounter = 0
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        for x in line:
            tcounter += 1
    now = datetime.datetime.now()
    clear()
    if useproxies == 'True':
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Proxies Enabled")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Proxies Enabled\x07")
    else:
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{}".format(rtbversion))
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox vL{}\x07".format(rtbversion))
    if len(str(tcounter)) == 1:
        menublank = "    "
    if len(str(tcounter)) == 2:
        menublank = "   "
    if len(str(tcounter)) == 3:
        menublank = "  "
    if len(str(tcounter)) == 4:
        menublank = " "
        print (colored("Um, thats too many tokens. Remove some to use Raid ToolBox.\n Type 'continue' to continue anyway despite, the warning.","red"))
        lem = input ()
        if lem == 'continue':
            clear()
        else:
            sys.exit()
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                               Welcome to DeadBread's Raid Toolbox                              ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    if tcounter == 0:
        print (colored("██                                      No tokens available.              "+menublank+now.strftime("%d/%m/%Y %H:%M:%S")+" ██",menucolour))
    elif tcounter == 1:
        print (colored("██                                  There is "+str(tcounter)+" token available.           "+menublank+now.strftime("%d/%m/%Y %H:%M:%S")+" ██",menucolour))
    else:
        print (colored("██                                  There are "+str(tcounter)+" tokens available.         "+menublank+now.strftime("%d/%m/%Y %H:%M:%S")+" ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("██         0.  Exit                              ██         13. Playing game changer              ██",menucolour))
    print (colored("██         1.  Joiner                            ██         14. Ascii Nickname (Spams Audit log)  ██",menucolour))
    print (colored("██         2.  Leaver                            ██         15. Embed Spammer                     ██",menucolour))
    print (colored("██         3.  Group DM leaver                   ██         16. TrafficLight status effect        ██",menucolour))
    print (colored("██         4.  Token Checker                     ██         17. Role Mass Mentioner               ██",menucolour))
    print (colored("██         5.  Message spammer                   ██         18. Channel Message Cleaner           ██",menucolour))
    print (colored("██         6.  Ascii spammer                     ██         19. Server Smasher (Single bot token) ██",menucolour))
    print (colored("██         7.  Mass mention spammer              ██         20. Proxy Scraper                     ██",menucolour))
    print (colored("██         8.  Voice Chat Spammer                ██         21. Voice chat join spammer           ██",menucolour))
    print (colored("██         9.  User DM Spammer                   ██         22. View Running Attacks              ██",menucolour))
    print (colored("██         10. Friend Request Spammer            ██         23. Custom attack plugins             ██",menucolour))
    print (colored("██         11. Group DM spammer                  ██         24. More Options                      ██",menucolour))
    print (colored("██         12. Image Spammer                     ██                                               ██",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("██     Please enter the number of your choice.   ██    Type 'info' for Information and Updates    ██",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    choice = input()
    try:
        if choice.lower() == 'info':
            info(currentattacks,spawnedpids)
        if int(choice) == 0:
            for pid in spawnedpids:
                if sys.platform.startswith('win32'):
                    try:
                        os.kill(int(pid), 9)
                    except Exception:
                        pass
                elif sys.platform.startswith('linux'):
                    try:
                        os.kill(int(pid), signal.SIGKILL)
                    except Exception:
                        pass
            sys.exit()
        elif int(choice) == 1:
            joiner(currentattacks,spawnedpids)
        elif int(choice) == 2:
            leaver(currentattacks,spawnedpids)
        elif int(choice) == 3:
            groupleaver(currentattacks,spawnedpids)
        elif int(choice) == 4:
            tokencheck(currentattacks,spawnedpids)
        elif int(choice) == 5:
            messagespam(currentattacks,spawnedpids)
        elif int(choice) == 6:
            asciispam(currentattacks,spawnedpids)
        elif int(choice) == 7:
            massmentioner(currentattacks,spawnedpids)
        elif int(choice) == 8:
            vcspam(currentattacks,spawnedpids)
        elif int(choice) == 9:
            dmspam(currentattacks,spawnedpids)
        elif int(choice) == 10:
            friender(currentattacks,spawnedpids)
        elif int(choice) == 11:
            groupdmspam(currentattacks,spawnedpids)
        elif int(choice) == 12:
            imagespam(currentattacks,spawnedpids)
        elif int(choice) == 13:
            gamechange(currentattacks,spawnedpids)
        elif int(choice) == 14:
            asciinick(currentattacks,spawnedpids)
        elif int(choice) == 15:
            embedspam(currentattacks,spawnedpids)
        elif int(choice) == 16:
            trafficlight(currentattacks,spawnedpids)
        elif int(choice) == 17:
            rolemassmention(currentattacks,spawnedpids)
        elif int(choice) == 18:
            cleanup(currentattacks,spawnedpids)
        elif int(choice) == 19:
            serversmasher(currentattacks,spawnedpids)
        elif int(choice) == 20:
            proxyscrape(currentattacks,spawnedpids)
        elif int(choice) == 21:
            vcjoinspammer(currentattacks,spawnedpids)
        elif int(choice) == 22:
            viewcurrentat(currentattacks,spawnedpids)
        elif int(choice) == 23:
            customplugins(currentattacks,spawnedpids)
        elif int(choice) == 24:
            tools(currentattacks,spawnedpids)
        elif int(choice) == 986:
            wew(currentattacks,spawnedpids)
        else:
            clear()
            print (colored('Invalid Option.',"yellow"))
            input()
            main(currentattacks,spawnedpids)
    except Exception as i:
        clear()
        if 'invalid literal for int()' in str(i):
            print (colored('Invalid Option.',"yellow"))
        else:
            print (colored(i,"yellow"))
        input()
        main(currentattacks,spawnedpids)

def joiner(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Invite Joiner")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Invite Joiner\x07")
    print (colored("Discord invite joiner.",menucolour))
    print (colored("0: Back",menucolour))
    link = input('Discord Invite Link: ')
    if link == '0':
        main(currentattacks,spawnedpids)
    if len(link) > 7:
        link = link[19:]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\joiner.py',token,link,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/joiner.py',token,link,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(3)
    main(currentattacks,spawnedpids)

def leaver(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Leaver")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Leaver\x07")
    print (colored("Discord server leaver.",menucolour))
    print (colored("0: Back",menucolour))
    ID = input ('ID of the server to leave: ')
    if str(ID) == '0':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\leaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/leaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(3)
    main(currentattacks,spawnedpids)

def groupleaver(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Leaver")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Leaver\x07")
    print (colored("Discord group DM leaver.",menucolour))
    print (colored("0: Back",menucolour))
    ID = input ('ID of the group DM to leave: ')
    if str(ID) == '0':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\groupleaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/groupleaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(3)
    main(currentattacks,spawnedpids)

def tokencheck(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Checker")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Token Checker\x07")
    vcounter = 0
    ucounter = 0
    icounter = 0
    validtokens = []
    unverified = []
    with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        if len(tokens) > 50:
            print("I'd Recommend using the quick checker for {} tokens.".format(len(tokens)))
            tok = input("Press enter to continue anyway, or type 0 to return to menu.\n")
            if tok == '0':
                main(currentattacks, spawnedpids)
        print (colored("Checking tokens...",menucolour))
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.post('https://discordapp.com/api/v6/invite/RTBCHECKER', headers=headers)
            try:
                if "You need to verify your account in order to perform this action." in str(src.content):
                    print (colored(token + ' Unverified.',"yellow"))
                    ucounter +=1
                    unverified.append(token)
                elif "401: Unauthorized" in str(src.content):
                    print (colored(token + ' Invalid.',"red"))
                    icounter +=1
                else:
                    print (colored(token + ' Valid.',"green"))
                    vcounter +=1
                    if token in validtokens:
                        continue
                    validtokens.append(token)
            except Exception as exc:
                print (exc)
        with open('tokens.txt','w') as handle:
            for token in validtokens:
                handle.write(token+'\n')
        with open('unverified_tokens.txt','a') as handle:
            for token in unverified:
                handle.write(token+'\n')
        print ("---------------------------------------")
        print (colored("Number of valid tokens: " + str(vcounter),"green"))
        print (colored("Number of unverified tokens: " + str(ucounter),"yellow"))
        print (colored("Number of invalid tokens: " + str(icounter),"red"))
        print ("---------------------------------------")
        input("Press enter to return to menu.")
        main(currentattacks,spawnedpids)

def messagespam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Spammer\x07")
    print (colored("Discord Server message spammer.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
        allchan = 'true'
    else:
        allchan = 'false'
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Message Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def asciispam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Spammer\x07")
    print (colored("Discord server ascii spammer.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
        allchan = 'true'
    else:
        allchan = 'false'
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\asciispam.py',token,number,chan,allchan,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/asciispam.py',token,number,chan,allchan,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Ascii Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def massmentioner(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Mass Mentioner")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Mass Mentioner\x07")
    print (colored("Discord server mass mentioner.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\massmention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/massmention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Mass Mention Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def vcspam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice Chat Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice Chat Spammer\x07")
    tcounter = 0
    print (colored("Discord VC joiner/spammer.",menucolour))
    print (colored("0: Back",menucolour))
    ytlink = input ('YouTube Link to play: ')
    if ytlink == '0':
        main(currentattacks,spawnedpids)
    chanid = input ('Voice channel ID: ')
    tokencount = input ('Number of tokens to use: ')
    if sys.platform.startswith('win32'):
        if os.path.isfile('.\\spammer\\file.wav'):
            os.remove('.\\spammer\\file.wav')
    elif sys.platform.startswith('linux'):
        if os.path.isfile('spammer/file.wav'):
            os.remove('spammer/file.wav')
        print ("Removed old .wav.")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([ytlink])
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\vcspam.py',token,number,chanid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/vcspam.py',token,number,chanid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        if number == str(tokencount):
            break
        time.sleep(0.1)
    currentattacks.append("Voice Chat Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def dmspam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | DM Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | DM Spammer\x07")
    print (colored("Discord user DM spammer.",menucolour))
    print (colored("0: Back",menucolour))
    user = input ("User's ID: ")
    if str(user) == '0':
        main(currentattacks,spawnedpids)
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\dmspammer.py',token,number,msgtxt,user,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/dmspammer.py',token,number,msgtxt,user,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
    currentattacks.append("DM Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def friender(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Friend Request Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Friend Request Spammer\x07")
    print (colored("Discord user mass friender.",menucolour))
    print (colored("0: Back",menucolour))
    userid = input("User's ID: ")
    if str(userid) == '0':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    tcounter = 0
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\friender.py',token,userid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/friender.py',token,userid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    p.wait()
    main(currentattacks,spawnedpids)

def imagespam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Image Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Image Spammer\x07")
    print (colored("Discord server image spammer.",menucolour))
    print (colored("0: Back",menucolour))
    chan = input ("Channel to spam in: ")
    if str(chan) == '0':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\imagespam.py',token,number,chan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'/spammer/imagespamlinux.py',token,number,chan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Image Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def gamechange(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing Status Changer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Playing Status Changer\x07")
    print (colored("Discord game playing status changer.",menucolour))
    print (colored("This will probably slow down some attacks.","blue"))
    print (colored("0: Back",menucolour))
    print ('Name of game to play: ')
    game = input ('Playing ')
    if game == '0':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\gamechange.py',token,game,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/gamechange.py',token,game,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
    currentattacks.append("Playing status change with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def asciinick(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Nickname Changer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Nickname Changer\x07")
    print (colored("Discord random ascii nickname.",menucolour))
    print (colored("This will probably slow down some attacks.","blue"))
    print (colored("0: Back",menucolour))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\nickname.py',token,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/nickname.py',token,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
    currentattacks.append("Ascii Nickname Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def embedspam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Embed Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Embed Spammer\x07")
    print (colored("Discord embed spammer.",menucolour))
    print (colored("Will probably bypass some bots that have word and image restrictions.",menucolour))
    print (colored("0: Back",menucolour))
    title = input ("Embed Title: ")
    if title == '0':
        main(currentattacks,spawnedpids)
    author = input ("Embed Author: ")
    iconurl = input ("Author Icon URL: ")
    thumburl = input ("Thumbnail image URL: ")
    footer = input ("Embed Footer Text: ")
    textchan = input ("Text Channel to spam in: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
    currentattacks.append("Embed Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def trafficlight(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | TrafficLight Status Effect")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | TrafficLight Status Effect\x07")
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\trafficlight.py',token,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/trafficlight.py',token,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
    currentattacks.append("TrafficLight effect with "+ str(tcounter) + " tokens.")
    time.sleep(3)
    print (colored("Started traffic Light effect.","green"))
    time.sleep(0.5)
    clear()
    print (colored("Started traffic Light effect.","yellow"))
    time.sleep(0.5)
    clear()
    print (colored("Started traffic Light effect.","red"))
    time.sleep(0.5)
    main(currentattacks,spawnedpids)

def rolemassmention(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Role Mass Mentioner")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Role Mass Mentioner\x07")
    print (colored("Discord role mass mentioner.",menucolour))
    print (colored("This will spam mention all roles that are mentionable.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\rolemention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/rolemention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Role Mass Mention with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def cleanup(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Cleaner")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Cleaner\x07")
    print (colored("Clean up messages sent by a token",menucolour))
    print (colored("This will delete all the messages sent by the token.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\cleanup.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/cleanup.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    time.sleep(5)
    main(currentattacks,spawnedpids)

def serversmasher(currentattacks,spawnedpids):
    clear()
    print ("The config file for the Server Smasher is in spammer/smconfig.py, please add token before starting.")
    if sys.platform.startswith('win32'):
        p = subprocess.Popen([winpy,'.\\spammer\\serversmasher.py',smversion,menucolour],creationflags=CREATE_NEW_CONSOLE)
    elif sys.platform.startswith('linux'):
        subprocess.call(['gnome-terminal', '-x', linuxpy,'spammer/serversmasher.py',smversion,menucolour])
    time.sleep(3)
    main(currentattacks,spawnedpids)

def proxyscrape(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Proxy Scraper")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Proxy Scraper\x07")
    print (colored("RTB Proxy Scraper.",menucolour))
    print (colored("I recommend that you get enough proxies for the ammount of tokens you have.",menucolour))
    print (colored("0: Back",menucolour))
    amm = input ("Ammount of proxies to scrape: ")
    if str(amm) == '0':
        main(currentattacks,spawnedpids)
    for x in range(int(amm)):
        proxy = collector.get_proxy()
        port = proxy[1]
        proxy = proxy[0]
        proxy = proxy + ":" + port
        print (proxy)
        with open ('proxies.txt','a+') as handle:
            handle.write(proxy+'\n')
    print (colored(str(amm) + " proxies have been scraped.",menucolour))
    input ()
    main(currentattacks,spawnedpids)

def vcjoinspammer(currentattacks,spawnedpids): #wew its here
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice chat join spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice chat join spammer\x07")
    print (colored("Discord Voice chat join spammer. Joins random voice channels in a server.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input ('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\vcjoinspam.py',token,number,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/vcjoinspam.py',token,number,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Voice chat join and spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def groupdmspam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Spammer\x07")
    print (colored("Discord Group DM message spammer.",menucolour))
    print (colored("0: Back",menucolour))
    group = input ("Group ID: ")
    if str(group) == '0':
        main(currentattacks,spawnedpids)
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen([winpy,'.\\spammer\\groupdmspam.py',token,group,number,msgtxt,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen([linuxpy,'spammer/groupdmspam.py',token,group,number,msgtxt,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Group DM spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def viewcurrentat(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Current Attacks")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Current Attacks\x07")
    print (colored("Current Attacks:",menucolour))
    print (colored("---------------------",menucolour))
    for attack in currentattacks:
        print (colored(attack,"green"))
    if currentattacks == []:
        print (colored('None',"green"))
    print (colored("---------------------\nType 'killall' to end all current attacks.",menucolour))
    attackkill = input ()
    if attackkill.lower() == 'killall':
        for pid in spawnedpids:
            if sys.platform.startswith('win32'):
                try:
                    os.kill(int(pid), 9)
                except Exception:
                    pass
            elif sys.platform.startswith('linux'):
                try:
                    os.kill(int(pid), signal.SIGKILL)
                except Exception:
                    pass
        currentattacks = []
        spawnedpids = []
    main(currentattacks,spawnedpids)

def customplugins(currentattacks,spawnedpids):
    clear()
    pluginlist = {}
    pluginfile = []
    pluginfolder = []
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Custom Plugins")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Custom Plugins\x07")
    pluginno = -1
    print (colored("Installed Plugins:",menucolour))
    print (colored("----------------------",menucolour))
    for root, dirs, files in os.walk("plugins/", topdown=False):
        for folder in dirs:
            try:
                plugdir = os.listdir('plugins/{}/'.format(folder))
            except Exception:
                continue
            for file in plugdir:
                if str(file).startswith("main_"):
                    pluginlist[folder] = file
    for plugin in pluginlist:
        pluginno += 1
        pluginfolder.append(plugin)
        print (str(pluginno) +". "+ plugin)
    for plugin in pluginlist.items():
        pluginfile.append(plugin[1])
    print (colored("----------------------\nb: Back",menucolour))
    print (colored("e: Kill all plugins\nd: Download plugins from Repo",menucolour))
    plug = input ("Choice of plugin: ")
    if plug == 'b':
        main(currentattacks,spawnedpids)
    if plug == 'e':
        pluginpids = open("pluginpids").readlines()
        for pid in pluginpids:
            if sys.platform.startswith('win32'):
                try:
                    os.kill(int(pid), 9)
                except Exception:
                    pass
            elif sys.platform.startswith('linux'):
                try:
                    os.kill(int(pid), signal.SIGKILL)
                except Exception:
                    pass
        os.remove('pluginpids')
        customplugins(currentattacks,spawnedpids)
    if plug == 'd':
        clear()
        down = requests.get("https://github.com/DeadBread76/Raid-Toolbox-Plugins/archive/master.zip")
        with open("plugins/package.zip", "wb") as handle:
            handle.write(down.content)
        shutil.unpack_archive("plugins/package.zip","plugins/")
        os.remove("plugins/package.zip")
        for root, dirs, files in os.walk("plugins/Raid-Toolbox-Plugins-master/", topdown=False):
            for folder in dirs:
                copy_tree("plugins/Raid-Toolbox-Plugins-master/{}/".format(folder), "plugins/{}/".format(folder+"/"))
        shutil.rmtree("plugins/Raid-Toolbox-Plugins-master/")
        print("Downloaded plugins from Repo.")
        input("Press enter to reload plugins")
        customplugins(currentattacks,spawnedpids)
    plugchoice = "{}/{}".format(pluginfolder[int(plug)],pluginfile[int(plug)])
    clear()
    if sys.platform.startswith('win32'):
        p = subprocess.Popen([winpy,'plugins/'+plugchoice,winpy,menucolour])
    elif sys.platform.startswith('linux'):
        p = subprocess.Popen([linuxpy,'plugins/'+plugchoice,linuxpy,menucolour])
    p.wait()
    customplugins(currentattacks,spawnedpids)

def info(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Info")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Info\x07")
    print (colored("  _____       _     _   _______          _ ____            ",menucolour))
    print (colored(" |  __ \     (_)   | | |__   __|        | |  _ \           ",menucolour))
    print (colored(" | |__) |__ _ _  __| |    | | ___   ___ | | |_) | _____  __",menucolour))
    print (colored(" |  _  // _` | |/ _` |    | |/ _ \ / _ \| |  _ < / _ \ \/ /",menucolour))
    print (colored(" | | \ \ (_| | | (_| |    | | (_) | (_) | | |_) | (_) >  < ",menucolour))
    print (colored(" |_|  \_\__,_|_|\__,_|    |_|\___/ \___/|_|____/ \___/_/\_\ ",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    print (colored("                                                            ",menucolour))
    print (colored("https://github.com/DeadBread76/Raid-Toolbox",menucolour))
    print (colored("                                                            ",menucolour))
    if sys.platform.startswith('win32'):
        print (colored("Raid ToolBox version: "+rtbversion,menucolour))
    elif sys.platform.startswith('linux'):
        print (colored("Raid ToolBox version: "+'L'+rtbversion,menucolour))
    print (colored("Server Smasher version: "+smversion,menucolour))
    print (colored("Discord.py version: "+ discord.__version__,menucolour))
    print (colored("                                                            ",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    print (colored("Type 'update' to update Raid ToolBox to the latest version.",menucolour))
    print (colored("Type 'reinstall' to reinstall requirements",menucolour))
    print (colored("Type 'diag' for diagnostics log.",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    inf = input("")
    if inf == "d":
        print('7RtuZEe')
        input()
        info(currentattacks,spawnedpids)
    elif inf.lower() == 'reinstall':
        if sys.platform.startswith('win32'):
            installation = subprocess.Popen([winpip,'install','-r','requirements.txt','--user'])
        elif sys.platform.startswith('linux'):
            installation = subprocess.Popen([linuxpip,'install','-r','requirements.txt'])
        installation.wait()
        input("Installation Complete.")
        info(currentattacks,spawnedpids)
    elif inf.lower() == 'diag':
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Diagnostics")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Diagnostics\x07")
        try:
            import speedtest
        except Exception:
            if sys.platform.startswith('win32'):
                installation = subprocess.Popen([winpip,'install','speedtest-cli','--user'])
            elif sys.platform.startswith('linux'):
                installation = subprocess.Popen([linuxpip,'install','speedtest-cli'])
            installation.wait()
            import speedtest
        clear()
        with open('tokens.txt','r') as handle:
            lines = handle.readlines()
        tcounter = len(lines)
        print ("Running Speedtest...")
        servers = []
        s = speedtest.Speedtest()
        s.get_servers(servers)
        print ("Testing Ping...")
        s.get_best_server()
        print ("Testing Download Speed...")
        s.download()
        print ("Testing Upload Speed...")
        s.upload()
        s.results.share()
        results_dict = s.results.dict()
        d = results_dict["download"]
        u = results_dict["upload"]
        p = results_dict["ping"]
        print('Download Speed: {:.2f} Kb/s'.format(d / 1024))
        print('Upload Speed: {:.2f} Kb/s'.format(u / 1024))
        print('Ping: {}'.format(p))
        now = datetime.datetime.now()
        with open ("Diagnostics" + str(now.strftime("%d%m%Y%H%M%S"))+".txt", 'w+') as handle:
            handle.write("Raid Toolbox Diagnostics "+str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
            handle.write("=====================================================\n")
            handle.write("RTB VERSION: " + rtbversion + "\n")
            handle.write("SM VERSION: " + smversion + "\n")
            handle.write("AMMOUNT OF TOKENS LOADED: " + str(tcounter) + "\n")
            handle.write("---------------\n")
            handle.write("Python Info:\n\n")
            handle.write("Python Version: " + sys.version+"\n")
            handle.write("Discord.py version: " + discord.__version__ + "\n")
            handle.write("---------------\n")
            handle.write("OS info:\n\n")
            handle.write("Platform: " + platform.platform()+"\n")
            handle.write("Processor: " + platform.processor()+"\n")
            handle.write("---------------\n")
            handle.write("SpeedTest Results: \n\n")
            handle.write('Download Speed: {:.2f} Kb/s\n'.format(d / 1024))
            handle.write('Upload Speed: {:.2f} Kb/s\n'.format(u / 1024))
            handle.write('Ping: {}\n'.format(p))
            handle.write("---------------\n")
            handle.write("RTB Dump:\n\n")
            handle.write(menucolour+"\n")
            handle.write(useproxies+"\n")
            if sys.platform.startswith('win32'):
                plugindir = os.listdir('.\\plugins\\')
            elif sys.platform.startswith('linux'):
                plugindir = os.listdir('plugins/')
            for plugin in plugindir:
                handle.write(plugin+"\n")
            for attack in currentattacks:
                handle.write(attack+"\n")
            for pid in spawnedpids:
                handle.write(str(pid)+"\n")
            handle.write("---------------\n")
        print ("Diagnostics Written to file.")
        input()
    elif inf.lower() == 'update':
        clear()
        u = input("Are you sure you want to update?(Y/N)\nBe Sure to backup your configs.\n")
        if u.lower() == 'y':
            clear()
            print ("Downloading latest version from GitHub...")
            update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
            with open("update.zip", "wb") as handle:
                handle.write(update.content)
            shutil.unpack_archive("update.zip")
            if sys.platform.startswith('win32'):
                copy_tree(".\\Raid-Toolbox-master\\", ".\\")
                os.remove(".\\update.zip")
                shutil.rmtree(".\\Raid-Toolbox-master\\")
                shutil.unpack_archive("ffmpeg.zip")
                shutil.unpack_archive("ffplay.zip")
                shutil.unpack_archive("ffprobe.zip")
                os.remove("ffmpeg.zip")
                os.remove("ffplay.zip")
                os.remove("ffprobe.zip")
                print ("Update complete, exiting.")
                time.sleep(5)
                sys.exit()
            elif sys.platform.startswith('linux'):
                copy_tree("Raid-Toolbox-master/", ".")
                os.remove("update.zip")
                shutil.rmtree("Raid-Toolbox-master/")
                os.remove("ffmpeg.zip")
                os.remove("ffplay.zip")
                os.remove("ffprobe.zip")
                print ("Update complete, exiting.")
                time.sleep(5)
                sys.exit()
        else:
            info(currentattacks,spawnedpids)
    main(currentattacks,spawnedpids)

def tools(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | More Options")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Tools\x07")
    print (colored("Raid Toolbox Tools",menucolour))
    print (colored("-------------------",menucolour))
    print (colored("0.  Return to menu",menucolour))
    print (colored("1.  HypeSquad House Changer",menucolour))
    print (colored("2.  Avatar Changer",menucolour))
    print (colored("3.  Token Cleaner",menucolour))
    print (colored("4.  Quick Checker",menucolour))
    print (colored("5.  Nickname Changer",menucolour))
    print (colored("6.  Widget Joiner",menucolour))
    choice = input('Selection: ')
    if int(choice) == 0:
        main(currentattacks,spawnedpids)
    elif int(choice) == 1:
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | HypeSquad Changer")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | HypeSquad Changer\x07")
        print (colored("1. Bravery",menucolour))
        print (colored("2. Brilliance",menucolour))
        print (colored("3. Ballance",menucolour))
        choice = input('Selection: ')
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            if sys.platform.startswith('win32'):
                p = subprocess.Popen([winpy,'.\\tools\\hypesquad.py',token,choice],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
            elif sys.platform.startswith('linux'):
                p = subprocess.Popen([linuxpy,'tools/hypesquad.py',token,choice],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        p.wait()
        tools(currentattacks,spawnedpids)
    elif int(choice) == 2:
        Tk().withdraw()
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Avatar Changer")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Avatar Changer\x07")
        avatar = askopenfilename(initialdir = os.getcwd(),title = "Select avatar to change")
        if avatar == "":
            tools(currentattacks,spawnedpids)
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            if sys.platform.startswith('win32'):
                p = subprocess.Popen([winpy,'.\\tools\\avatarchange.py',token,avatar],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
            elif sys.platform.startswith('linux'):
                p = subprocess.Popen([linuxpy,'tools/avatarchange.py',token,avatar],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        time.sleep(5)
        tools(currentattacks,spawnedpids)
    elif int(choice) == 3:
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Cleaner")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Token Cleaner\x07")
        print (colored("Token Cleaner: Leaves every server that the token is on, making it faster to login to.",menucolour))
        choice = input("Clean Tokens?(Y/N): ")
        if choice.lower() == 'y':
            tokenlist = open("tokens.txt").read().splitlines()
            for token in tokenlist:
                if sys.platform.startswith('win32'):
                    p = subprocess.Popen([winpy,'.\\tools\\cleaner.py',token,choice],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
                elif sys.platform.startswith('linux'):
                    p = subprocess.Popen([linuxpy,'tools/cleaner.py',token,choice],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
            time.sleep(3)
            tools(currentattacks,spawnedpids)
        else:
            tools(currentattacks,spawnedpids)
    elif int(choice) == 4:
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Quick Checker")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Quick Checker\x07")
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            if sys.platform.startswith('win32'):
                p = subprocess.Popen([winpy,'.\\tools\\quickchecker.py',token])
                time.sleep(0.07)
            elif sys.platform.startswith('linux'):
                p = subprocess.Popen([linuxpy,'tools/quickchecker.py',token])
                time.sleep(0.07)
        p.wait()
        input("Checking complete.")
        tools(currentattacks,spawnedpids)
    elif int(choice) == 5:
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Nickname Changer")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Nickname Changer\x07")
        print (colored("Server Nickname Changer",menucolour))
        print (colored("0: Back",menucolour))
        SERVER = input("Server ID: ")
        if SERVER == "0":
            tools(currentattacks,spawnedpids)
        nick = input("New Nickname: ")
        tokenlist = open("tokens.txt").read().splitlines()
        for token in tokenlist:
            if sys.platform.startswith('win32'):
                p = subprocess.Popen([winpy,'.\\tools\\changenickname.py',token,SERVER,nick],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
            elif sys.platform.startswith('linux'):
                p = subprocess.Popen([linuxpy,'tools/changenickname.py',token,SERVER,nick],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        time.sleep(5)
        tools(currentattacks,spawnedpids)
    elif int(choice) == 6:
        clear()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Widget Joiner")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Widget Joiner\x07")
        print (colored("Server Widget Joiner (Only Works on servers that have widget enabled.)",menucolour))
        print (colored("0: Back",menucolour))
        SERVER = input("Server ID: ")
        if SERVER == "0":
            tools(currentattacks,spawnedpids)
        src = requests.get("https://discordapp.com/api/guilds/{}/widget.json".format(SERVER)).text
        if "is not snowflake." in str(src):
            print("{} is not a server ID.".format(SERVER))
            input()
            tools(currentattacks, spawnedpids)
        elif "Widget Disabled" in str(src):
            print("Widget is disabled in this server.")
            input()
            tools(currentattacks, spawnedpids)
        else:
            split = src.split('"') # ghetto way to do it but fuck it i don't care
            for string in split:
                if "https://discordapp.com/invite/" in string:
                    print("Invite: {}".format(string))
                    invite = string[30:]
                    break
            tokenlist = open("tokens.txt").read().splitlines()
            for token in tokenlist:
                if sys.platform.startswith('win32'):
                    p = subprocess.Popen([winpy,'.\\spammer\\joiner.py',token,invite,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
                elif sys.platform.startswith('linux'):
                    p = subprocess.Popen([linuxpy,'spammer/joiner.py',token,invite,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
            time.sleep(1)
            tools(currentattacks, spawnedpids)

def wew(currentattacks,spawnedpids):
    if sys.platform.startswith('win32'):
        clear()
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | ¯\_(ツ)_/¯")
    else:
        main(currentattacks,spawnedpids)
    p = subprocess.Popen([winpy,'.\\spammer\\player.py',winpy],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    currentattacks.append("Music!")
    spawnedpids.append(p.pid)
    main(currentattacks,spawnedpids)

main(currentattacks,spawnedpids)
