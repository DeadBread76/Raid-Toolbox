try:
    import os
    import re
    import sys
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading...\x07")
    import time
    import pgrep
    import signal
    import random
    import datetime
    import subprocess
    import asyncio
    import discord
    import requests
    import youtube_dl
    from colorama import init
    from termcolor import colored
    from proxyscrape import create_collector
    from config import*
    from rtbplugins import*
except Exception as i:
    print ("Module error: " + str(i))
    print ("Please check that the module is installed.")
    install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
    if install.lower() == 'y':
        installation = subprocess.Popen(['pip3', 'install', '-r', 'requirements.txt'],shell=False)
        installation.wait()
    else:
        sys.exit()
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
clear = lambda: os.system('clear')
collector = create_collector('my-collector', 'https')
rtbversion = "L 0.2.2"

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

currentattacks = []

def main(currentattacks):
    tcounter = 0
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        for x in line:
            tcounter += 1
    now = datetime.datetime.now()
    if useproxies == 'True':
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Proxies Enabled\x07")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox\x07")
    clear()
    if len(str(tcounter)) == 1:
        menublank = "   "
    if len(str(tcounter)) == 2:
        menublank = "  "
    if len(str(tcounter)) == 3:
        menublank = " "
    if len(str(tcounter)) == 4:
        menublank = ""
        print (colored("Um, thats too many tokens. Remove some to use Raid ToolBox.","red"))
        lem = input ()
        if lem == 'lemme in':
            print (colored("This will probably kill your PC, but whatever ¯\_(ツ)_/¯","red"))
            input()
            clear()
        else:
            sys.exit()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox\x07")
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                               Welcome to DeadBread's Raid Toolbox                              ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                                 There are "+str(tcounter)+" tokens available.           "+menublank+now.strftime("%d/%m/%Y %H:%M:%S")+" ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██         0. Exit                               ██         12. Image Spammer                     ██",menucolour))
    print (colored("██         1. Joiner                             ██         13. Playing game changer              ██",menucolour))
    print (colored("██         2. Leaver                             ██         14. Ascii Nickname (Spams Audit log)  ██",menucolour))
    print (colored("██         3. Group DM leaver                    ██         15. Embed Spammer                     ██",menucolour))
    print (colored("██         4. Token Checker                      ██         16. TrafficLight status effect        ██",menucolour))
    print (colored("██         5. Message spammer                    ██         17. Role Mass Mentioner               ██",menucolour))
    print (colored("██         6. Ascii spammer                      ██         18. Channel Message Cleaner           ██",menucolour))
    print (colored("██         7. Mass mention spammer               ██         19. Server Smasher (Single bot token) ██",menucolour))
    print (colored("██         8. Voice Chat Spammer                 ██         20. Proxy Scraper                     ██",menucolour))
    print (colored("██         9. User DM Spammer                    ██         21. Voice chat join and spam          ██",menucolour))
    print (colored("██         10. Friend Request Spammer            ██         22. View Running Attacks              ██",menucolour))
    print (colored("██         11. Group DM spammer                  ██         23. Custom attack plugins             ██",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                            Please enter the number of your choice.                             ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    choice = input()
    try:
        if choice.lower() == 'info':
            info(currentattacks)
        if int(choice) == 0:
            sys.exit()
        elif int(choice) == 1:
            joiner(currentattacks) 
        elif int(choice) == 2:
            leaver(currentattacks)
        elif int(choice) == 3:
            groupleaver(currentattacks)
        elif int(choice) == 4:
            tokencheck(currentattacks)
        elif int(choice) == 5:
            messagespam(currentattacks)
        elif int(choice) == 6:
            asciispam(currentattacks)
        elif int(choice) == 7:
            massmentioner(currentattacks)
        elif int(choice) == 8:
            vcspam(currentattacks)
        elif int(choice) == 9:
            dmspam(currentattacks)
        elif int(choice) == 10:
            friender(currentattacks)
        elif int(choice) == 11:
            groupdmspam(currentattacks)  
        elif int(choice) == 12:
            imagespam(currentattacks)
        elif int(choice) == 13:
            gamechange(currentattacks)
        elif int(choice) == 14:
            asciinick(currentattacks)
        elif int(choice) == 15:
            embedspam(currentattacks)
        elif int(choice) == 16:
            trafficlight(currentattacks)
        elif int(choice) == 17:
            rolemassmention(currentattacks)
        elif int(choice) == 18:
            cleanup(currentattacks)
        elif int(choice) == 19:
            serversmasher(currentattacks)
        elif int(choice) == 20:
            proxyscrape(useproxies)
        elif int(choice) == 21:
            vcjoinspammer(currentattacks)
        elif int(choice) == 22:
            viewcurrentat(currentattacks)
        elif int(choice) == 23:
            customplugins(currentattacks,pluginlist)
        elif int(choice) == 986:
            wew(currentattacks)
        else:
            clear()
            print (colored('Invalid Option.',"yellow"))
            input()
            main(currentattacks)
        #I actually had what was left of a multi page menu i was working on left here lmao       
    except Exception as i:
        clear()
        print (colored('Invalid Input.',"yellow"))
        print (colored(i,"yellow"))
        input()
        main(currentattacks)

def joiner(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Invite Joiner\x07")
    print (colored("Discord invite joiner.",menucolour))
    link = input('Discord Invite Link: ')
    if len(link) > 7:
        link = link[19:]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python3','spammer/joiner.py',token,link,useproxies],shell=False)
    time.sleep(3)
    main(currentattacks)

def leaver(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Leaver\x07")
    print (colored("Discord server leaver.",menucolour))
    ID = input ('ID of the server to leave: ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python3','spammer/leaver.py',token,ID,useproxies],shell=False)
    time.sleep(3)
    main(currentattacks)

def groupleaver(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Leaver\x07")
    print (colored("Discord group DM leaver.",menucolour))
    ID = input ('ID of the group DM to leave: ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python3','spammer/groupleaver.py',token,ID,useproxies],shell=False)
    time.sleep(3)
    main(currentattacks)

def tokencheck(currentattacks): #not even going to add proxy support for this because of how fucking slow this shit goes with proxies
    clear()
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
        main(currentattacks)

def messagespam(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Spammer\x07")
    print (colored("Discord Server message spammer.",menucolour))
    SERVER = input ("Server ID: ")
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
        p = subprocess.Popen(['python3','spammer/messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Message Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def asciispam(currentattacks): #no longer bugged
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Spammer\x07")
    print (colored("Discord server ascii spammer.",menucolour))
    SERVER = input('Server ID: ')
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
        p = subprocess.Popen(['python3','spammer/asciispam.py',token,number,chan,allchan,SERVER,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Ascii Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)
      
def massmentioner(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Mass Mentioner\x07")
    print (colored("Discord server mass mentioner.",menucolour))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/massmention.py',token,SERVER,number,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Mass Mention Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def vcspam(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice Chat Spammer\x07")
    tcounter = 0
    print (colored("Discord VC joiner/spammer.",menucolour))
    ytlink = input ('YouTube Link to play: ')
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
        p = subprocess.Popen(['python3','spammer/vcspamlinux.py',token,number,chanid,useproxies],shell=False)
        if number == str(tokencount):
            break
        time.sleep(0.1)
    p.wait()

def dmspam(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | DM Spammer\x07")
    print (colored("Discord user DM spammer.",menucolour))
    user = input ("User's ID: ")
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/dmspammer.py',token,number,msgtxt,user,useproxies],shell=False)
    currentattacks.append("DM Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def friender(currentattacks): #finally it works
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Friend Request Spammer\x07")
    print (colored("Discord user mass friender.",menucolour))
    userid = input("User's ID: ")
    tokenlist = open("tokens.txt").read().splitlines()
    tcounter = 0
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/friender.py',token,userid,useproxies],shell=False)
    p.wait()
    main(currentattacks)

def imagespam(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Image Spammer\x07")
    print (colored("Discord server image spammer.",menucolour))
    SERVER = input ("Server ID: ")
    chan = input ("Channel to spam in: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','/spammer/imagespamlinux.py',token,SERVER,number,chan,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Image Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def gamechange(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Playing Status Changer\x07")
    print (colored("Discord game playing status changer.",menucolour))
    print (colored("This will probably slow down some attacks.","blue"))
    print ('Name of game to play: ')
    game = input ('Playing ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python3','spammer/gamechange.py',token,game,useproxies],shell=False)
    currentattacks.append("Playing status change with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def asciinick(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Nickname Changer\x07")
    print (colored("Discord random ascii nickname.",menucolour))
    print (colored("This will probably slow down some attacks.","blue"))
    SERVER = input ("Server ID: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/nickname.py',token,SERVER,useproxies],shell=False)
    currentattacks.append("Ascii Nickname Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def embedspam(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Embed Spammer\x07")
    print (colored("Discord embed spammer.",menucolour))
    print (colored("Will probably bypass some bots that have word and image restrictions.",menucolour))
    title = input ("Embed Title: ")
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
        p = subprocess.Popen(['python3','spammer/embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies],shell=False)
    currentattacks.append("Embed Spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def trafficlight(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | TrafficLight Status Effect\x07")
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python3','spammer/trafficlight.py',token,useproxies],shell=False)
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
    main(currentattacks)
    
def rolemassmention(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Role Mass Mentioner\x07")
    print (colored("Discord role mass mentioner.",menucolour))
    print (colored("This will spam mention all roles that are mentionable.",menucolour))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/rolemention.py',token,SERVER,number,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Role Mass Mention with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def cleanup(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Cleaner\x07")
    print (colored("Clean up messages sent by a token",menucolour))
    print (colored("This will delete all the messages sent by the token.",menucolour))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/cleanup.py',token,SERVER,number,useproxies],shell=False)
        time.sleep(0.1)
    time.sleep(5)
    main(currentattacks)

def serversmasher(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | SERVER SMASHER\x07")
    print ("The config file for this option is located: \spammer\smconfig.py")
    p = subprocess.Popen(['python3','spammer/serversmasherlinux.py'],shell=False)
    p.wait()
    main(currentattacks)

def proxyscrape(useproxies):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Proxy Scraper\x07")
    print (colored("RTB Proxy Scraper.",menucolour))
    print (colored("I recommend that you get enough proxies for the ammount of tokens you have.",menucolour))
    amm = input ("Ammount of proxies to scrape: ")
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
    main(currentattacks)

def vcjoinspammer(currentattacks): #wew its here
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice chat join and spam\x07")
    print (colored("Discord Voice chat join and spam . Joins all the channels in a server, and can spam messages.",menucolour))
    SERVER = input ('Server ID: ')
    spammsg = input ("Spam Messages?(Y/N)")
    if spammsg.lower() == "y":
        chan = input ("Channel to spam in (type 'all' for all channels): ")
        if chan.lower() == "all":
            print (colored("Spamming all channels","blue"))
            allchan = 'true'
        else:
            allchan = 'false'
        msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    if spammsg.lower() == "y":
        for token in tokenlist:
            tcounter += 1
            number = str(tcounter)
            p = subprocess.Popen(['python3','spammer/messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],shell=False)
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/vcjoinspam.py',token,number,SERVER,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Voice chat join and spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def groupdmspam(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Spammer\x07")
    print (colored("Discord Group DM message spammer.",menucolour))
    group = input ("Group ID: ")
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python3','spammer/groupdmspam.py',token,group,number,msgtxt,useproxies],shell=False)
        time.sleep(0.1)
    currentattacks.append("Group DM spam with "+ str(tcounter) + " tokens.")
    time.sleep(5)
    main(currentattacks)

def viewcurrentat(currentattacks):
    clear()
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Current Attacks\x07")
    print (colored("Current Attacks:",menucolour))
    print (colored("---------------------",menucolour))
    for attack in currentattacks:
        print (colored(attack,"green"))
    print (colored("Type 'killall' to end all current attacks.",menucolour))
    attackkill = input ()
    if attackkill.lower() == 'killall':
        thisinst = os.getpid()
        pyproc = pgrep.pgrep('python')
        for process in pyproc:
            if process == thisinst:
                continue
            os.kill(int(process), signal.SIGKILL)
    main(currentattacks)

def customplugins(currentattacks,pluginlist):
    clear()
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
    p = subprocess.Popen(['python3','plugins/'+plugchoice],shell=False)
    p.wait()
    main(currentattacks)
    
def info(currentattacks):
    clear()
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
    print (colored("Raid ToolBox version: "+rtbversion,menucolour))
    print (colored("Discord.py version: "+ discord.__version__,menucolour))
    print (colored("                                                            ",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    ack = input("Press enter to return to menu.")
    if ack == "d":
        print('7RtuZEe')
        input()
        info(currentattacks)
    main(currentattacks)

def wew(currentattacks):
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | ¯\_(ツ)_/¯\x07")
    p = subprocess.Popen(['python3','spammer/player.py'],shell=False)
    main(currentattacks)

main(currentattacks)




