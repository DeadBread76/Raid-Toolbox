try:
    import os
    import re
    import sys
    import time
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading...")
    import random
    import datetime
    import discord
    import asyncio
    import requests
    import youtube_dl
    import subprocess
    from colorama import init
    from termcolor import colored
    from proxyscrape import create_collector
    from config import*
except Exception as i:
    print ("Module error: " + str(i))
    print ("Please check that the module is installed.")
    input ()
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
tcounter = 0
clear = lambda: os.system('cls')
collector = create_collector('my-collector', 'https')

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
    now = datetime.datetime.now()
    clear()
    if useproxies == 'True':
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Proxies Enabled")
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox")
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                               Welcome to DeadBread's Raid Toolbox                              ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                                 There are "+str(tcounter)+" tokens available.              "+now.strftime("%Y-%m-%d %H:%M:%S")+"██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██         0. Exit                               ██         11. Image Spammer                     ██",menucolour))
    print (colored("██         1. Joiner                             ██         12. Playing game changer              ██",menucolour))
    print (colored("██         2. Leaver                             ██         13. Ascii Nickname (Spams Audit log)  ██",menucolour))
    print (colored("██         3. Group DM leaver                    ██         14. Embed Spammer                     ██",menucolour))
    print (colored("██         4. Token Checker                      ██         15. TrafficLight status effect        ██",menucolour))
    print (colored("██         5. Message spammer                    ██         16. Role Mass Mentioner               ██",menucolour))
    print (colored("██         6. Ascii spammer                      ██         17. Channel Message Cleaner           ██",menucolour))
    print (colored("██         7. Mass mention spammer               ██         18. Server Smasher (Single bot token) ██",menucolour))
    print (colored("██         8. Voice Chat Spammer                 ██         19. Proxy Scraper                     ██",menucolour))
    print (colored("██         9. User DM Spammer                    ██                                               ██",menucolour))
    print (colored("██         10. Friend Request Spammer            ██                                               ██",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("██                                               ██                                               ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("██                            Please enter the number of your choice.                             ██",menucolour))
    print (colored("██                                                                                                ██",menucolour))
    print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
    choice = input()
    try:
        if int(choice) == 0:
            os.system("taskkill /f /im python.exe")
        elif int(choice) == 1:
            joiner() 
        elif int(choice) == 2:
            leaver()
        elif int(choice) == 3:
            groupleaver()
        elif int(choice) == 4:
            tokencheck()
        elif int(choice) == 5:
            messagespam()
        elif int(choice) == 6:
            asciispam()
        elif int(choice) == 7:
            massmentioner()
        elif int(choice) == 8:
            vcspam()
        elif int(choice) == 9:
            dmspam()
        elif int(choice) == 10:
            friender()
        elif int(choice) == 11:
            imagespam()
        elif int(choice) == 12:
            gamechange()
        elif int(choice) == 13:
            asciinick()
        elif int(choice) == 14:
            embedspam()
        elif int(choice) == 15:
            trafficlight()
        elif int(choice) == 16:
            rolemassmention()
        elif int(choice) == 17:
            cleanup()
        elif int(choice) == 18:
            serversmasher()
        elif int(choice) == 19:
            proxyscrape(useproxies)
        elif int(choice) == 986:
            wew()
        #wew i actually had what was left of a multi page menu i was working on left here lmao       
        else:
            clear()
            print (colored('Invalid Option.',"yellow"))
            input()
            main()
    except Exception as i:
        clear()
        print (colored('Invalid Input.',"yellow"))
        print (colored(i,"yellow"))
        input()
        main()

def joiner():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Invite Joiner")
    print (colored("Discord invite joiner.",menucolour))
    link = input('Discord Invite Link: ')
    if len(link) > 7:
        link = link[19:]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\joiner.py',token,link,useproxies],shell=True)
    time.sleep(3)
    main()

def leaver():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Leaver")
    print (colored("Discord server leaver.",menucolour))
    ID = input ('ID of the server to leave: ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\leaver.py',token,ID,useproxies],shell=True)
    time.sleep(3)
    main()

def groupleaver():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Leaver")
    print (colored("Discord group DM leaver.",menucolour))
    ID = input ('ID of the group DM to leave: ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\groupleaver.py',token,ID,useproxies],shell=True)
    time.sleep(3)
    main()

def tokencheck(): #not even going to add proxy support for this because of how fucking slow this shit goes with proxies
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Checker")
    vcounter = 0
    icounter = 0
    if os.path.isdir('.\\tokens\\') == False:
        os.mkdir('.\\tokens\\') 
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
                    with open('.\\tokens\\valid.txt','a') as handle:
                        handle.write(token + '\n')
                else:
                    print(colored(token + ' Invalid.',"red"))
                    icounter +=1
                    with open('.\\tokens\\invalid.txt','a') as handle:
                        handle.write(token + '\n')
            except Exception:
                print("Yeah we can't contact discordapp.com")
        print ("---------------------------------------")
        print (colored("Number of valid tokens: " + str(vcounter),"green"))
        print (colored("Number of invalid tokens: " + str(icounter),"red"))
        print (colored("tokens.txt has been sorted.","green"))
        print (colored("Check the tokens directory for results.","green"))
        print ("---------------------------------------")
        input("Press enter to return to menu.")
        main()

def messagespam():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Spammer")
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
        p = subprocess.Popen(['python','.\\spammer\\messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],shell=True)
        time.sleep(0.1)
    p.wait()

def asciispam(): #no longer bugged
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Spammer")
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
        p = subprocess.Popen(['python','.\\spammer\\asciispam.py',token,number,chan,allchan,SERVER,useproxies],shell=True)
        time.sleep(0.1)
    p.wait()
      
def massmentioner():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Mass Mentioner")
    print (colored("Discord server mass mentioner.",menucolour))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\massmention.py',token,SERVER,number,useproxies],shell=True)
        time.sleep(0.1)
    p.wait()

def vcspam():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice Chat Spammer")
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
        p = subprocess.Popen(['python','.\\spammer\\vcspam.py',token,number,chanid,useproxies],shell=True)
        if number == str(tokencount):
            break
        time.sleep(0.1)
    p.wait()

def dmspam():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | DM Spammer")
    print (colored("Discord user DM spammer.",menucolour))
    user = input ("User's ID: ")
    msgtxt = input ("Text to spam: ")
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\dmspammer.py',token,number,msgtxt,user,useproxies],shell=True)
    p.wait()

def friender(): #finally it works
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Friend Request Spammer")
    print (colored("Discord user mass friender.",menucolour))
    userid = input("User's ID: ")
    tokenlist = open("tokens.txt").read().splitlines()
    tcounter = 0
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\friender.py',token,userid,useproxies],shell=True)
    p.wait()
    main()

def imagespam():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Image Spammer")
    print (colored("Discord server image spammer.",menucolour))
    SERVER = input ("Server ID: ")
    chan = input ("Channel to spam in: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\imagespam.py',token,SERVER,number,chan,useproxies],shell=True)
        time.sleep(0.1)
    p.wait()

def gamechange():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing Status Changer")
    print (colored("Discord game playing status changer.",menucolour))
    print (colored("This will probably slow down some attacks.","blue"))
    print ('Name of game to play: ')
    game = input ('Playing ')
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\gamechange.py',token,game,useproxies],shell=True)
    time.sleep(5)
    main()

def asciinick():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Nickname Changer")
    print (colored("Discord random ascii nickname.",menucolour))
    print (colored("This will probably slow down some attacks, and it seems to get tokens banned quickly.","blue"))
    SERVER = input ("Server ID: ")
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\nickname.py',token,SERVER,useproxies],shell=True)
    time.sleep(5)
    main()

def embedspam():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Embed Spammer")
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
        p = subprocess.Popen(['python','.\\spammer\\embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies],shell=True)
    p.wait()

def trafficlight():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | TrafficLight Status Effect")
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen(['python','.\\spammer\\trafficlight.py',token,useproxies],shell=True)
    time.sleep(3)
    print (colored("Started traffic Light effect.","green"))
    time.sleep(0.5)
    clear()
    print (colored("Started traffic Light effect.","yellow"))
    time.sleep(0.5)
    clear()
    print (colored("Started traffic Light effect.","red"))
    time.sleep(0.5)
    main()
    
def rolemassmention():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Role Mass Mentioner")
    print (colored("Discord role mass mentioner.",menucolour))
    print (colored("This will spam mention all roles that are mentionable.",menucolour))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\rolemention.py',token,SERVER,number,useproxies],shell=True)
        time.sleep(0.1)
    p.wait()

def cleanup():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Cleaner")
    print (colored("Clean up messages sent by a token",menucolour))
    print (colored("This will delete all the messages sent by the token.",menucolour))
    SERVER = input('Server ID: ')
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\cleanup.py',token,SERVER,number,useproxies],shell=True)
        time.sleep(0.1)
    time.sleep(5)
    main()

def serversmasher():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | SERVER SMASHER")
    print ("The config file for this option is located: \spammer\smconfig.py")
    p = subprocess.Popen(['python','.\\spammer\\serversmasher.py'],shell=True)
    p.wait()

def proxyscrape(useproxies):
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Proxy Scraper")
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
    print (colored(str(amm) + "proxies have been scraped.",menucolour))
    input ()
    main()
'''
def vcjoinspammer(): #another failed attempt
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice Chat Join Spammer")
    tcounter = 0
    print (colored("Discord VC join spammer. Joins a channel then leaves.",menucolour))
    chanid = input ('Voice channel ID: ')
    tcounter = 0
    tokenlist = open("./tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\vcjoinspam.py',token,number,chanid,useproxies],shell=True)
        time.sleep(0.1)
    p.wait()

def emoji(): #IM WORKING ON IT FUCK
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Emoji Reactor")
    print (colored("Reacts to a message with an emoji",menucolour))
    messageid = input ("Message ID: ")
    emojiname = input ("Emoji name(Eg. thinking): ")
    emojiname = emojiname.lower()
    tcounter = 0
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        tcounter += 1
        number = str(tcounter)
        p = subprocess.Popen(['python','.\\spammer\\emojireact.py',token,messageid,emojiname,number,useproxies],shell=True)
    time.sleep(5)
'''    
def wew():
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | ¯\_(ツ)_/¯")
    p = subprocess.Popen(['python','.\\spammer\\player.py'],shell=True)
    main()

main()

