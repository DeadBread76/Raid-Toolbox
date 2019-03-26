try:
    import os
    import sys
    import time
    import ctypes
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading...")
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
    from config import*
    from rtbplugins import*
except Exception as i:
    print ("Module error: " + str(i))
    print ("Please check that the module is installed.")
    install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
    if install.lower() == 'y':
        if sys.platform.startswith('win32'):
            installation = subprocess.Popen(['pip','install','-r','requirements.txt','--user'])
        elif sys.platform.startswith('linux'):
            installation = subprocess.Popen(['pip3','install','-r','requirements.txt'])
        installation.wait()
        print("Please Restart Raid Toolbox.")
        input()
        sys.exit()
    else:
        sys.exit()

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
if menucolour.lower() == 'random':
    colours=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    menucolour = random.choice(colours)
tcounter = 0
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')


collector = create_collector('my-collector', 'https')
rtbversion = "0.3.0b"
smversion = "0.1.0"
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
        print (colored("Um, thats too many tokens. Remove some to use Raid ToolBox.","red"))
        lem = input ()
        if lem == 'lemme in':
            print (colored("This will probably kill your PC, but whatever ¯\_(ツ)_/¯","red"))
            input()
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
    print (colored("██         8.  Voice Chat Spammer                ██         21. Voice chat join and spam          ██",menucolour))
    print (colored("██         9.  User DM Spammer                   ██         22. View Running Attacks              ██",menucolour))
    print (colored("██         10. Friend Request Spammer            ██         23. Custom attack plugins             ██",menucolour))
    print (colored("██         11. Group DM spammer                  ██         24. Tools                             ██",menucolour))
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
                        os.system("taskkill /F /pid "+str(pid))
                elif sys.platform.startswith('linux'):
                        os.kill(int(pid), signal.SIGKILL)
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
            customplugins(currentattacks,pluginlist,spawnedpids)
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
        print (colored('Invalid Input.',"yellow"))
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
    link = input('Discord Invite Link: ')
    if link.lower() == 'b':
        main(currentattacks,spawnedpids)
    if len(link) > 7:
        link = link[19:]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\joiner.py',token,link,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/joiner.py',token,link,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(3)
    main(currentattacks,spawnedpids)

def leaver(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Leaver")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Leaver\x07")
    print (colored("Discord server leaver.",menucolour))
    ID = input ('ID of the server to leave: ')
    if str(ID).lower() == 'b':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\leaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/leaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    time.sleep(3)
    main(currentattacks,spawnedpids)

def groupleaver(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Leaver")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Leaver\x07")
    print (colored("Discord group DM leaver.",menucolour))
    ID = input ('ID of the group DM to leave: ')
    if str(ID).lower() == 'b':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\groupleaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/groupleaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    print (colored("Checking tokens...",menucolour))
    with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.post('https://discordapp.com/api/v6/invite/r3sSKJJ', headers=headers)
            try:
                if "You need to verify your account in order to perform this action." in str(src.content):
                    print (colored(token + ' Unverified.',"yellow"))
                    ucounter +=1
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
    SERVER = input ("Server ID: ")
    if str(SERVER).lower() == 'b':
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
            p = subprocess.Popen(['python','.\\spammer\\messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    currentattacks.append("Message Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def asciispam(currentattacks,spawnedpids): #no longer bugged
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Spammer\x07")
    print (colored("Discord server ascii spammer.",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER).lower() == 'b':
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
            p = subprocess.Popen(['python','.\\spammer\\asciispam.py',token,number,chan,allchan,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/asciispam.py',token,number,chan,allchan,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    SERVER = input('Server ID: ')
    if str(SERVER).lower() == 'b':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\massmention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/massmention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    ytlink = input ('YouTube Link to play: ')
    if ytlink.lower() == 'b':
        main(currentattacks,spawnedpids)
    chanid = input ('Voice channel ID: ')
    tokencount = input ('Number of tokens to use: ')
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
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\vcspam.py',token,number,chanid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/vcspam.py',token,number,chanid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    user = input ("User's ID: ")
    if str(user).lower() == 'b':
        main(currentattacks,spawnedpids)
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\dmspammer.py',token,number,msgtxt,user,useproxies])
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/dmspammer.py',token,number,msgtxt,user,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
    currentattacks.append("DM Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks,spawnedpids)

def friender(currentattacks,spawnedpids): #finally it works
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Friend Request Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Friend Request Spammer\x07")
    print (colored("Discord user mass friender.",menucolour))
    userid = input("User's ID: ")
    if str(userid).lower() == 'b':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    tcounter = 0
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\friender.py',token,userid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/friender.py',token,userid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    p.wait()
    main(currentattacks,spawnedpids)

def imagespam(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Image Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Image Spammer\x07")
    print (colored("Discord server image spammer.",menucolour))
    chan = input ("Channel to spam in: ")
    if str(chan).lower() == 'b':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\imagespam.py',token,number,chan,useproxies])
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','/spammer/imagespamlinux.py',token,number,chan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    print ('Name of game to play: ')
    game = input ('Playing ')
    if game.lower() == 'b':
        main(currentattacks,spawnedpids)
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\gamechange.py',token,game,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/gamechange.py',token,game,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    SERVER = input ("Server ID: ")
    if str(SERVER).lower() == 'b':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\nickname.py',token,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/nickname.py',token,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    title = input ("Embed Title: ")
    if title.lower() == 'b':
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
            p = subprocess.Popen(['python','.\\spammer\\embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies])
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen(['python','.\\spammer\\trafficlight.py',token,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/trafficlight.py',token,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    SERVER = input('Server ID: ')
    if str(SERVER).lower() == 'b':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\rolemention.py',token,SERVER,number,useproxies])
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/rolemention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    SERVER = input('Server ID: ')
    if str(SERVER).lower() == 'b':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\cleanup.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/cleanup.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        spawnedpids.append(p.pid)
        time.sleep(0.1)
    time.sleep(5)
    main(currentattacks,spawnedpids)

def serversmasher(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Smasher v{}".format(smversion))
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Smasher v{}\x07".format(smversion))
    print ("The config file for this option is located: \spammer\smconfig.py")
    if sys.platform.startswith('win32'):
        p = subprocess.Popen(['python','.\\spammer\\serversmasher.py'])
    elif sys.platform.startswith('linux'):
        p = subprocess.Popen(['python3','spammer/serversmasher.py'])
    p.wait()
    main(currentattacks,spawnedpids)

def proxyscrape(currentattacks,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Proxy Scraper")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Proxy Scraper\x07")
    print (colored("RTB Proxy Scraper.",menucolour))
    print (colored("I recommend that you get enough proxies for the ammount of tokens you have.",menucolour))
    amm = input ("Ammount of proxies to scrape: ")
    if str(amm).lower() == 'b':
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
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice chat join and spam")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice chat join and spam\x07")
    print (colored("Discord Voice chat join and spam. Joins all the channels in a server, and can spam messages.",menucolour))
    SERVER = input ('Server ID: ')
    if str(SERVER).lower() == 'b':
        main(currentattacks,spawnedpids)
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\vcjoinspam.py',token,number,SERVER,useproxies])
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/vcjoinspam.py',token,number,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    group = input ("Group ID: ")
    if str(group).lower() == 'b':
        main(currentattacks,spawnedpids)
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        if sys.platform.startswith('win32'):
            p = subprocess.Popen(['python','.\\spammer\\groupdmspam.py',token,group,number,msgtxt,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        elif sys.platform.startswith('linux'):
            p = subprocess.Popen(['python3','spammer/groupdmspam.py',token,group,number,msgtxt,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    print (colored("Type 'killall' to end all current attacks.",menucolour))
    attackkill = input ()
    if attackkill.lower() == 'killall':
        for pid in spawnedpids:
            if sys.platform.startswith('win32'):
                    os.system("taskkill /F /pid "+str(pid))
                    currentattacks = []
            elif sys.platform.startswith('linux'):
                    os.kill(int(pid), signal.SIGKILL)
            currentattacks = []
            spawnedpids = []
    main(currentattacks,spawnedpids)

def customplugins(currentattacks,pluginlist,spawnedpids):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Custom Plugins")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Custom Plugins\x07")
    pluginno = -1
    print (colored("Installed Plugins:",menucolour))
    for plugin in pluginlist:
        pluginno += 1
        print (str(pluginno) +". "+ plugin)
    plug = input ("Choice of plugin: ")
    if plug.lower() == 'back':
        main(currentattacks)
    plugchoice = pluginlist[int(plug)]
    clear()
    if sys.platform.startswith('win32'):
        p = subprocess.Popen(['python','.\\plugins\\'+plugchoice])
    elif sys.platform.startswith('linux'):
        p = subprocess.Popen(['python3','plugins/'+plugchoice])
    p.wait()
    main(currentattacks,spawnedpids)

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
            installation = subprocess.Popen(['pip','install','-r','requirements.txt','--user'])
        elif sys.platform.startswith('linux'):
            installation = subprocess.Popen(['pip3','install','-r','requirements.txt'])
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
                installation = subprocess.Popen(['pip','install','speedtest-cli','--user'])
            elif sys.platform.startswith('linux'):
                installation = subprocess.Popen(['pip3','install','speedtest-cli'])
            installation.wait()
            import speedtest
        clear()
        tcounter = 0
        with open('tokens.txt','r') as handle:
            line = handle.readlines()
        for x in line:
            tcounter += 1
        testtoken = line[0]
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
            handle.write("Raid Toolbox Diagnostics test "+str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
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
            for plugin in pluginlist:
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
    input("Soon")
    main(currentattacks,spawnedpids)

def wew(currentattacks,spawnedpids):
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | ¯\_(ツ)_/¯")
    else:
        main(currentattacks,spawnedpids)
    p = subprocess.Popen(['python','.\\spammer\\player.py'],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    currentattacks.append("Music!")
    spawnedpids.append(p.pid)
    main(currentattacks,spawnedpids)

main(currentattacks,spawnedpids)
