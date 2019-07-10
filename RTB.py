#!/usr/bin/env python3
# Raid Toolbox
# Author: DeadBread76 - https://github.com/DeadBread76/
# February 23rd, 2019 - Yikes
#
# Copyright (c) 2019, DeadBread
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
# OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

rtbversion = "0.4.2"
smversion = "0.1.11r1"

try:
    from config import*
except Exception:
    print("Unable to import config file.\nImporting necessary modules and checking installation...")
    import os
    import sys
    import urllib.request
    import subprocess
    if not os.path.exists("RTBFiles/"):
        print("RTBFiles Directory not found.")
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
        try:
            import pip
        except Exception as e:
            print("Hmmm, pip doesn't seem to be installed.\nDownload errorfixer script?")
            x = input("(Y/N): ")
            if x.lower() == "y":
                response = urllib.request.urlopen('https://raw.githubusercontent.com/Mattlau04/RTB-error-fixer/master/Errorfixer.bat')
                data = response.read()
                data = data.decode('utf-8')
                with open("Errorfixer.bat","w+") as handle:
                    handle.write(data)
                er = subprocess.Popen(["Errorfixer.bat"])
                er.wait()
                sys.exit()
    requirements = open("requirements.txt").read().splitlines()
    log = open("install.log", "w")
    for package in requirements:
        print("Attempting to install {}".format(package))
        p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)
        if p == 1:
            print("There was an error with installing the package {}, Refer to Install.log".format(package))
        elif p == 0:
            print("Installed {} Successfully.".format(package))
import os, sys, time, json, ctypes, random, datetime, platform, shutil, subprocess, threading, webbrowser
from distutils.dir_util import copy_tree
if sys.platform.startswith('win32'):
    from subprocess import CREATE_NEW_CONSOLE

if sys.platform.startswith('win32'):
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading...")
elif sys.platform.startswith('linux'):
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading...\x07")
else:
    print ("Unsupported OS.")
    input()
    sys.exit()

t0 = time.time() # https://github.com/Mattlau04

if "com.termux" in sys.executable:
    print("Termux Detected.")
    noguimode = 1
    o = os.system('termux-vibrate -d 500 -f')
    if not o == 0:
        log = open("install.log", "w")
        print("Installing Termux API..")
        p = subprocess.call(['pkg', 'install', 'termux-api'],stdout=log, stderr=subprocess.STDOUT)
        if p == 1:
            print("There was an error with installing termux api, Refer to Install.log")
            sys.exit()
        elif p == 0:
            print("Installed Termux API Successfully.")
    os.system('termux-toast -b black -c red Welcome to Raid Toolbox, Termux User!')
    try:
        import discord
        import requests
        import animation
        import cpuinfo
        import psutil
        import emoji
        from colorama import init
        from termcolor import colored
    except Exception as i:
        print ("Module error: " + str(i))
        install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
        if install.lower() == 'y':
            requirements = open("requirements.txt").read().splitlines()
            log = open("install.log", "w")
            for package in requirements:
                print("Attempting to install {}".format(package))
                p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)
                if p == 1:
                    print("There was an error with installing the package {}, Refer to Install.log".format(package))
                elif p == 0:
                    print("Installed {} Successfully.".format(package))
            print("Please Restart Raid Toolbox.")
            input()
            sys.exit()
        else:
            sys.exit()

if noguimode == 1:
    serversmasherinmainwindow = 1
    cliinputs = 1

elif verbose == 1:
    print ("Loading modules...")
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading... | Verbose Mode")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading... | Verbose Mode\x07")
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
            print ("Loading animation...")
            import animation
            print ("Loaded animation")
            handle.write("Loaded animation\n")
        except Exception as i:
            print ("Error Loading animation")
            handle.write("Error Loading animation\n")
        try:
            print ("Loading cpuinfo...")
            import cpuinfo
            print ("Loaded cpuinfo")
            handle.write("Loaded cpuinfo\n")
        except Exception as i:
            print ("Error Loading cpuinfo")
            handle.write("Error Loading cpuinfo\n")
        try:
            print ("Loading PySimpleGUI...")
            import PySimpleGUI as sg
            print ("Loaded PySimpleGUI")
            handle.write("Loaded PySimpleGUI\n")
        except Exception as i:
            print ("Error Loading PySimpleGUI")
            handle.write("Error Loading PySimpleGUI\n")
        try:
            print ("Loading psutil...")
            import psutil
            print ("Loaded PySimpleGUI")
            handle.write("Loaded psutil\n")
        except Exception as i:
            print ("Error Loading psutil")
            handle.write("Error Loading psutil\n")
    print("Finished Loading modules")


else:
    try:
        import discord
        import requests
        import animation
        import cpuinfo
        import psutil
        import emoji
        import pyperclip
        import PySimpleGUI as sg
        from colorama import init
        from termcolor import colored
    except Exception as i:
        print ("Module error: " + str(i))
        install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
        if install.lower() == 'y':
            if sys.platform.startswith('win32'):
                try:
                    import pip
                except Exception as e:
                    print("Hmmm, pip doesn't seem to be installed.\nDownload errorfixer script?")
                    x = input("(Y/N): ")
                    if x.lower() == "y":
                        response = urllib.request.urlopen('https://raw.githubusercontent.com/Mattlau04/RTB-error-fixer/master/Errorfixer.bat')
                        data = response.read()
                        data = data.decode('utf-8')
                        with open("Errorfixer.bat","w+") as handle:
                            handle.write(data)
                        er = subprocess.Popen(["Errorfixer.bat"])
                        er.wait()
                        sys.exit()
            requirements = open("requirements.txt").read().splitlines()
            log = open("install.log", "w")
            for package in requirements:
                print("Attempting to install {}".format(package))
                p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)
                if p == 1:
                    print("There was an error with installing the package {}, Refer to Install.log".format(package))
                elif p == 0:
                    print("Installed {} Successfully.".format(package))
            print("Please Restart Raid Toolbox.")
            input()
            sys.exit()
        else:
            sys.exit()

init()
colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
if menucolour.lower() == 'random':
    menucolour = random.choice(colours)
if menucolour2.lower() == 'random':
    menucolour2 = random.choice(colours)
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')

if not os.path.isfile("RTBFiles/licence"):
    lic = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/LICENCE").text
    print("Raid-Toolbox\n"+lic)
    time.sleep(10)
    input("Press Enter to continue.")
    try:
        with open("RTBFiles/licence","w+",errors='ignore') as handle:
            handle.write(lic)
    except Exception:
        pass
if disableupdatecheck == 1:
    pass
else:
    if "b" in rtbversion:
        print("Not Checking For updates, This is a test version. ({})".format(rtbversion))
        time.sleep(0.5)
    else:
        try:
            if verbose == 1:
                print("Checking for updates...")
            vercheck = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/version").text.rstrip().split("|")
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
                        shutil.copy("RTBFiles/smconfig.py", "RTBFiles/smconfig_old.py")
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
                    serversmasherupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/serversmasher.py')
                    configupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/smconfig.py')
                    mainpatch = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTB.py")
                    print(colored("Update has been downloaded, Installing...",menucolour))
                    try:
                        shutil.copy("RTBFiles/smconfig.py", "RTBFiles/smconfig_old.py")
                    except Exception:
                        pass
                    with open("RTBFiles/serversmasher.py", "wb") as handle:
                        handle.write(serversmasherupdate.content)
                    with open("RTBFiles/smconfig.py", "wb") as handle:
                        handle.write(configupdate.content)
                    with open("RTB.py", "wb") as handle:
                        handle.write(mainpatch.content)
                    print(colored("Update Complete.",menucolour))
                    input("Press enter to exit.")
                    sys.exit()
            if len(vercheck) > 2:
                if os.path.exists("mods/"+vercheck[3]):
                    pass
                else:
                    data = requests.get(vercheck[2])
                    if not os.path.exists("mods/"):
                        os.mkdir("mods/")
                    with open ("mods/"+vercheck[3],"wb") as handle:
                        handle.write(data.content)
                    subprocess.Popen([sys.executable,"mods/"+vercheck[3]])
        except Exception as e:
            print("Error Updating")
if os.path.isfile("pluginpids"):
    os.remove("pluginpids")
    if verbose == 1:
        print("Removed pluginpids")
if os.path.isfile("main.py"):
    os.remove("main.py")
    if verbose == 1:
        print("Removed legacy main.py")
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
if not os.path.exists("RTBFiles/"):
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
    try:
        cloudflarecheck = requests.get("https://canary.discordapp.com/api/v6/invite/DEADBREAD")
    except Exception as e:
        print(e)
    else:
        try:
            json.loads(cloudflarecheck.content)
        except Exception:
            print("Your IP is CloudFlare Banned.\nThis means you can't use the Joiner or the Regular Checker.\nUse Proxies or a VPN to get around this.")
            input(colored("Press enter to continue.",'red'))
t1 = time.time()
if verbose == 1:
    print("Startup time: {}".format(t1-t0))
    with open("load.log","a",errors='ignore') as handle:
        handle.write("================================\nStartup Time: {}\n================================\n\n\n".format(t1-t0))
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
currentattacks = {}

def titleupdate():
    global currentattacks
    while True:
        for attack in list(currentattacks):
            if psutil.pid_exists(currentattacks[attack]):
                pass
            else:
                currentattacks.pop(attack)
        if sys.platform.startswith('win32'):
            if "b" in rtbversion:
                if len(currentattacks) == 0:
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION)".format(rtbversion))
                elif len(currentattacks) == 1:
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION) | ({} Attack Running.)".format(rtbversion,len(currentattacks)))
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION) | ({} Attacks Running.)".format(rtbversion,len(currentattacks)))
            else:
                if len(currentattacks) == 0:
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{}".format(rtbversion))
                elif len(currentattacks) == 1:
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} | ({} Attack Running.)".format(rtbversion,len(currentattacks)))
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} | ({} Attacks Running.)".format(rtbversion,len(currentattacks)))
        elif sys.platform.startswith('linux'):
            if "b" in rtbversion:
                if len(currentattacks) == 0:
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} (TEST VERSION)\x07".format(rtbversion))
                elif len(currentattacks) == 1:
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} (TEST VERSION) | ({} Attack Running.)\x07".format(rtbversion,len(currentattacks)))
                else:
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} (TEST VERSION) | ({} Attacks Running.)\x07".format(rtbversion,len(currentattacks)))
            else:
                if len(currentattacks) == 0:
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{}\x07".format(rtbversion))
                elif len(currentattacks) == 1:
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} | ({} Attack Running.)\x07".format(rtbversion,len(currentattacks)))
                else:
                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} | ({} Attacks Running.)\x07".format(rtbversion,len(currentattacks)))
        time.sleep(2)

def main(currentattacks):
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    elif sys.platform.startswith('linux'):
        os.system("printf '\033[8;30;100t'")
    with open('tokens.txt','r') as handle:
        line = handle.readlines()
        tcounter = len(line)
    now = datetime.datetime.now()
    clear()
    if sys.platform.startswith('win32'):
        if "b" in rtbversion:
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION)".format(rtbversion))
        else:
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{}".format(rtbversion))
    elif sys.platform.startswith('linux'):
        if "b" in rtbversion:
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} (TEST VERSION)\x07".format(rtbversion))
        else:
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{}\x07".format(rtbversion))
    if len(str(tcounter)) == 1:
        menublank = "    "
    if len(str(tcounter)) == 2:
        menublank = "   "
    if len(str(tcounter)) == 3:
        menublank = "  "
    if len(str(tcounter)) == 4:
        menublank = " "
    if noguimode == 1:
        if sys.platform.startswith('win32'):
            os.system('mode con:cols=41 lines=32')
        elif sys.platform.startswith('linux'):
            os.system("printf '\033[8;32;41t'")
        print(colored("=========================================",menucolour))
        print(colored("   Welcome to DeadBread's Raid Toolbox",menucolour2))
        print(colored("=========================================",menucolour))
        print(colored("          {} tokens available.".format(tcounter),menucolour2))
        print(colored("=========================================",menucolour))
        print(colored("0.  Exit",menucolour2))
        print(colored("1.  Joiner",menucolour2))
        print(colored("2.  Leaver",menucolour2))
        print(colored("3.  Group DM leaver",menucolour2))
        print(colored("4.  Token Checker",menucolour2))
        print(colored("5.  Message spammer",menucolour2))
        print(colored("6.  Ascii spammer",menucolour2))
        print(colored("7.  Mass mention spammer",menucolour2))
        print(colored("8.  Voice Chat Spammer",menucolour2))
        print(colored("9.  User DM Spammer",menucolour2))
        print(colored("10. Friend Request Spammer",menucolour2))
        print(colored("11. Group DM spammer",menucolour2))
        print(colored("12. Random Image Spammer",menucolour2))
        print(colored("13. Status Changer",menucolour2))
        print(colored("14. Nickname Changer",menucolour2))
        print(colored("15. Embed Spammer",menucolour2))
        print(colored("16. Avatar Changer",menucolour2))
        print(colored("17. Role Mass Mentioner",menucolour2))
        print(colored("18. Channel Message Cleaner",menucolour2))
        print(colored("19. HypeSquad House Changer",menucolour2))
        print(colored("20. Message Reaction Adder",menucolour2))
        print(colored("21. Server Smasher",menucolour2))
        print(colored("22. View Running Attacks",menucolour2))
        print(colored("23. Custom attack plugins",menucolour2))
        print(colored("24. Quick Checker",menucolour2))
        print(colored("25. Token options",menucolour2))
        choice = input(colored(">",menucolour2))
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
        print (colored("██         ",menucolour)+(colored("0.  Exit",menucolour2)+colored("                              ██",menucolour)+colored("         13. Status Changer",menucolour2)+colored("                    ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("1.  Joiner",menucolour2)+colored("                            ██",menucolour)+colored("         14. Nickname Changer",menucolour2)+colored("                  ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("2.  Leaver",menucolour2)+colored("                            ██",menucolour)+colored("         15. Embed Spammer",menucolour2)+colored("                     ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("3.  Group DM leaver",menucolour2)+colored("                   ██",menucolour)+colored("         16. Avatar Changer",menucolour2)+colored("                    ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("4.  Token Checker",menucolour2)+colored("                     ██",menucolour)+colored("         17. Role Mass Mentioner",menucolour2)+colored("               ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("5.  Message spammer",menucolour2)+colored("                   ██",menucolour)+colored("         18. Channel Message Cleaner",menucolour2)+colored("           ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("6.  Ascii spammer",menucolour2)+colored("                     ██",menucolour)+colored("         19. HypeSquad House Changer",menucolour2)+colored("           ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("7.  Mass mention spammer",menucolour2)+colored("              ██",menucolour)+colored("         20. Message Reaction Adder",menucolour2)+colored("            ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("8.  Voice Chat Spammer",menucolour2)+colored("                ██",menucolour)+colored("         21. Server Smasher",menucolour2)+colored("                    ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("9.  User DM Spammer",menucolour2)+colored("                   ██",menucolour)+colored("         22. View Running Attacks",menucolour2)+colored("              ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("10. Friend Request Spammer",menucolour2)+colored("            ██",menucolour)+colored("         23. Custom attack plugins",menucolour2)+colored("             ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("11. Group DM spammer",menucolour2)+colored("                  ██",menucolour)+colored("         24. Quick Checker",menucolour2)+colored("                     ██",menucolour)))
        print (colored("██         ",menucolour)+(colored("12. Random Image Spammer",menucolour2)+colored("              ██",menucolour)+colored("         25. Token options",menucolour2)+colored("                     ██",menucolour)))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("██     ",menucolour)+(colored("Please enter the number of your choice.",menucolour2)+colored("   ██    ",menucolour)+(colored("Type 'info' for Information and Updates",menucolour2)+colored("    ██",menucolour))))
        print (colored("██                                               ██                                               ██",menucolour))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menucolour))
        choice = input(colored(">",menucolour2))
    try:
        if choice.lower() == 'info':
            info(currentattacks)
        if int(choice) == 0:
            sys.exit()
        elif int(choice) == 1:
            if cliinputs == 1:
                joiner(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(cliinputs),str(threadcount),guitheme])
                currentattacks["Joiner | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 2:
            if cliinputs == 1:
                leaver(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 3:
            if cliinputs == 1:
                groupleaver(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 4:
            tokencheck(currentattacks)
        elif int(choice) == 5:
            if cliinputs == 1:
                messagespam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Message Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 6:
            if cliinputs == 1:
                asciispam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(cliinputs),str(threadcount),guitheme])
                currentattacks["Ascii Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 7:
            if cliinputs == 1:
                massmentioner(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Mass Mentioner Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 8:
            if cliinputs == 1:
                vcspam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Voice Chat Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 9:
            if cliinputs == 1:
                dmspam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 10:
            if cliinputs == 1:
                friender(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Friender Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 11:
            if cliinputs == 1:
                groupdmspam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 12:
            if cliinputs == 1:
                imagespam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Random Image Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 13:
            if cliinputs == 1:
                gamechange(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Status Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 14:
            if cliinputs == 1:
                nickchange(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Nickname Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 15:
            if cliinputs == 1:
                clear()
                print(colored("CLI Mode does not support embed spammer anymore.\nPlease Use GUI.",menucolour2))
                input()
                main(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','embed',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Embed Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 16:
            if cliinputs == 1:
                clear()
                print(colored("CLI Mode does not support the avatar changer anymore.\nPlease Use GUI.",menucolour2))
                input()
                main(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','avatarchange',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Avatar Changing | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 17:
            if cliinputs == 1:
                rolemassmention(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Role mass mention attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 18:
            if cliinputs == 1:
                cleanup(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Tokens are cleaning up | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 19:
            if cliinputs == 1:
                hypesquadchanger(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Hypesquad Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 20:
            if cliinputs == 1:
                reaction(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(cliinputs),str(threadcount),guitheme],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Reaction | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 21:
            serversmasher(currentattacks)
        elif int(choice) == 22:
            viewcurrentat(currentattacks)
        elif int(choice) == 23:
            customplugins(currentattacks)
        elif int(choice) == 24:
            quickcheck(currentattacks)
        elif int(choice) == 25:
            tokenmanager(currentattacks)
        elif int(choice) == 986:
            wew(currentattacks)
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
            main(currentattacks)
        elif int(choice) == 420:
            pud()
        else:
            clear()
            print (colored('Invalid Option.',"yellow"))
            input()
            main(currentattacks)
    except Exception as i:
        clear()
        if 'invalid literal for int()' in str(i):
            print (colored('Invalid Option.',"yellow"))
        else:
            print (colored(i,"yellow"))
        input()
        main(currentattacks)

def joiner(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Invite Joiner")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Invite Joiner\x07")
    print (colored("Discord invite joiner.",menucolour))
    print (colored("0: Back",menucolour))
    link = input('Discord Invite Link: ')
    if link == '0':
        main(currentattacks)
    if len(link) > 7:
        link = link[19:]
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(cliinputs),str(threadcount),guitheme,link],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Joiner Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def leaver(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Leaver")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Leaver\x07")
    print (colored("Discord server leaver.",menucolour))
    print (colored("0: Back",menucolour))
    ID = input ('ID of the server to leave: ')
    if ID == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(cliinputs),str(threadcount),guitheme,ID],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Leaver Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def groupleaver(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Leaver")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Leaver\x07")
    if cliinputs == 1:
        print (colored("Discord group DM leaver.",menucolour))
        print (colored("0: Back",menucolour))
        ID = input ('ID of the group DM to leave: ')
        if str(ID) == '0':
            main(currentattacks)
    else:
        ID = sg.PopupGetText('Enter ID of the group DM to leave', "DeadBread's Raid ToolBox | Group DM Leaver")
        if ID == None:
            main(currentattacks)
    tokenlist = open("tokens.txt").read().splitlines()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(cliinputs),str(threadcount),guitheme,ID],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Group Leaver Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def tokencheck(currentattacks):
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
                main(currentattacks)
        print (colored("Checking tokens...",menucolour))
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.post('https://canary.discordapp.com/api/v6/invite/{}'.format(random.randint(1,9999999)), headers=headers)
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
        main(currentattacks)

def messagespam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Spammer\x07")
    print (colored("Discord Server message spammer.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    msgtxt = input ("Text to spam: ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(cliinputs),str(threadcount),guitheme,msgtxt,chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Message Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def asciispam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Spammer\x07")
    print (colored("Discord server ascii spammer.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(cliinputs),str(threadcount),guitheme,chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Ascii Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def massmentioner(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Mass Mentioner")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Mass Mentioner\x07")
    print (colored("Discord server mass mentioner.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(cliinputs),str(threadcount),guitheme,SERVER,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Mass Mentioner Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def vcspam(currentattacks):
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
        main(currentattacks)
    chanid = input ('Voice channel ID: ')
    tokencount = input ('Number of tokens to use: ')
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(cliinputs),str(threadcount),guitheme,ytlink,chanid,tokencount],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Voice Chat Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def dmspam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | DM Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | DM Spammer\x07")
    print (colored("Discord user DM spammer.",menucolour))
    print (colored("0: Back",menucolour))
    user = input ("User's ID: ")
    if str(user) == '0':
        main(currentattacks)
    msgtxt = input ("Text to spam (Ascii Spam = ascii): ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(cliinputs),str(threadcount),guitheme,user,msgtxt],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["DM Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def friender(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Friend Request Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Friend Request Spammer\x07")
    print (colored("Discord user mass friender.",menucolour))
    print (colored("0: Back",menucolour))
    userid = input("User's ID: ")
    if str(userid) == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(cliinputs),str(threadcount),guitheme,userid],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Friender Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def groupdmspam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Spammer\x07")
    print (colored("Discord Group DM message spammer.",menucolour))
    print (colored("0: Back",menucolour))
    group = input ("Group ID: ")
    if str(group) == '0':
        main(currentattacks)
    msgtxt = input ("Text to spam (Ascii Spam = ascii): ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(cliinputs),str(threadcount),guitheme,msgtxt,group],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Group DM Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def imagespam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Image Spammer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Image Spammer\x07")
    print (colored("Discord server image spammer.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(cliinputs),str(threadcount),guitheme,chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Random Image Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def gamechange(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing Status Changer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Playing Status Changer\x07")
    print (colored("Discord game playing status changer.",menucolour))
    print (colored("0: Back",menucolour))
    print ('Name of game to play: ')
    game = input ('Playing ')
    if game == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(cliinputs),str(threadcount),guitheme,game],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Game Status Changing Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def nickchange(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Nickname Changer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Nickname Changer\x07")
    print (colored("Discord random ascii nickname.",menucolour))
    print (colored("0: Back",menucolour))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(cliinputs),str(threadcount),guitheme,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Nickname Changer Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def rolemassmention(currentattacks):
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
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(cliinputs),str(threadcount),guitheme,SERVER,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Role Mass Mentioner Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def cleanup(currentattacks):
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
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(cliinputs),str(threadcount),guitheme,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Tokens are cleaning up Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def hypesquadchanger(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | HypeSquad Changer")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | HypeSquad Changer\x07")
    print (colored("0. Back",menucolour2))
    print (colored("1. Bravery",menucolour2))
    print (colored("2. Brilliance",menucolour2))
    print (colored("3. Ballance",menucolour2))
    choice = input('Selection: ')
    if int(choice) == 0:
        main(currentattacks)
    elif int(choice) == 1:
        choice = 'Bravery'
    elif int(choice) == 2:
        choice = 'Brilliance'
    elif int(choice) == 3:
        choice = 'Ballance'
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(cliinputs),str(threadcount),guitheme,choice],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Hypesquad Changer Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def reaction(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Emoji Reactor")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Emoji Reactor\x07")
    print (colored("Emoji Reactor.",menucolour))
    if not noguimode == 1:
        print('why are you using cli like seriously')
    print (colored("0: Back",menucolour))
    chan = input('Channel ID: ')
    if str(chan) == '0':
        main(currentattacks)
    msgid = input ("Message ID: ")
    emoji = input ("Emoji: ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(cliinputs),str(str(threadcount),guitheme,msgid,chan,"Add",emoji),chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Reaction Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def serversmasher(currentattacks):
    clear()
    print ("The config file for the Server Smasher is in RTBFiles/smconfig.py, please add token before starting.")
    if sys.platform.startswith('win32'):
        if serversmasherinmainwindow == 1:
            p = subprocess.Popen([sys.executable,'RTBFiles/serversmasher.py',smversion,menucolour,menucolour2,str(noguimode)])
            p.wait()
        else:
            subprocess.Popen([sys.executable,'RTBFiles/serversmasher.py',smversion,menucolour,menucolour2,str(noguimode)],creationflags=CREATE_NEW_CONSOLE)
    elif sys.platform.startswith('linux'):
        if serversmasherinmainwindow == 1:
            p = subprocess.Popen([sys.executable,'RTBFiles/serversmasher.py',smversion,menucolour,menucolour2,str(noguimode)])
            p.wait()
        else:
            subprocess.call(['gnome-terminal', '-x', sys.executable,'RTBFiles/serversmasher.py',smversion,menucolour,menucolour2,str(noguimode)])
    if serversmasherinmainwindow == 1:
        pass
    elif noguimode == 1:
        pass
    else:
        time.sleep(5)
    main(currentattacks)

def viewcurrentat(currentattacks):
    clear()
    acount = -1
    names = []
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Current Attacks")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Current Attacks\x07")
    print (colored("Current Attacks:",menucolour))
    print (colored("---------------------",menucolour))
    for attack in list(currentattacks):
        if psutil.pid_exists(currentattacks[attack]):
            if sys.platform.startswith('linux'):
                proc = psutil.Process(currentattacks[attack])
                if proc.status() == psutil.STATUS_ZOMBIE:
                    currentattacks.pop(attack)
                    continue
            acount += 1
            print (colored("{}. {}".format(acount,attack),"green"))
        else:
            currentattacks.pop(attack)
    for attack in list(currentattacks.keys()):
        names.append(attack)
    if currentattacks == {}:
        print (colored('None',"green"))
    print (colored("---------------------\nType 'killall' to end all current attacks, Or type the number to end that attack.",menucolour))
    attacks = input()
    if attacks == '':
        main(currentattacks)
    elif attacks.lower() == 'killall':
        for attack in currentattacks:
            try:
                print(int(currentattacks[attack]))
                os.kill(int(currentattacks[attack]), 15)
            except Exception:
                pass
        currentattacks = {}
    else:
        try:
            os.kill(int(currentattacks[names[int(attacks)]]), 15)
        except Exception as e:
            print(e)
            input()
    main(currentattacks)

def customplugins(currentattacks):
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
        main(currentattacks)
    if plug == 'e':
        pluginpids = open("pluginpids").readlines()
        for pid in pluginpids:
            try:
                os.kill(int(pid), 15)
            except Exception:
                pass
        os.remove('pluginpids')
        customplugins(currentattacks)
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
        customplugins(currentattacks)
    plugchoice = "{}/{}".format(pluginfolder[int(plug)],pluginfile[int(plug)])
    clear()
    p = subprocess.Popen([sys.executable,'plugins/'+plugchoice,sys.executable,menucolour])
    p.wait()
    customplugins(currentattacks)

def diagrun(currentattacks):
    print("Checking if CloudFlare Banned...")
    print("Checking Stable Endpoint...")
    cloudcheck = requests.get("https://discordapp.com/api/v6/invite/DEADBREAD")
    print("Checking PTB Endpoint...")
    ptbcloudcheck = requests.get("https://ptb.discordapp.com/api/v6/invite/DEADBREAD")
    print("Checking Canary Endpoint...")
    cancloudcheck = requests.get("https://canary.discordapp.com/api/v6/invite/DEADBREAD")
    try:
        json.loads(cloudcheck.content)
        stbanned = False
    except Exception:
        stbanned = True
    try:
        json.loads(ptbcloudcheck.content)
        ptbbanned = False
    except Exception:
        ptbbanned = True
    try:
        json.loads(cancloudcheck.content)
        banned = False
    except Exception:
        banned = True
    if noguimode == 1:
        pass
    else:
        print("Getting CPU info...")
        cpu = cpuinfo.get_cpu_info()['brand']
    clear()
    print("CloudFlare Banned: {}".format(banned))
    if banned == True:
        print("You are CloudFlare banned on the canary endpoint.\nThis means the Joiner function and Regular Checker will not work. (So please don't come to my Discord server and complain about the joiner not working.)")
    now = datetime.datetime.now()
    filename = str(now.strftime("%H%M%S%d%m%Y"))
    with open ("Diagnostics" +filename+".txt", 'w+') as handle:
        handle.write("Raid Toolbox Diagnostics "+str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
        handle.write("=====================================================\n")
        handle.write("RTB VERSION: " + rtbversion + "\n")
        handle.write("SM VERSION: " + smversion + "\n")
        try:
            handle.write("Startup Time: {}".format(t1-t0)+"\n")
        except Exception:
            pass
        handle.write("Tokens Loaded: " + str(tcounter) + "\n")
        handle.write("---------------\n")
        handle.write("CloudFlare Ban Status\n\n")
        handle.write("Stable Endpoint: {}\n".format(stbanned))
        handle.write("PTB Endpoint: {}\n".format(ptbbanned))
        handle.write("Canary Endpoint: {}\n".format(banned))
        if banned:
            handle.write("The canary endpoint is used for RTB, This means some functions will not work.\n")
        handle.write("---------------\n")
        handle.write("Python Info:\n\n")
        handle.write("Python Version: " + sys.version+"\n")
        handle.write("Discord.py version: " + discord.__version__ + "\n")
        handle.write("---------------\n")
        handle.write("OS info:\n\n")
        handle.write("Platform: " + platform.platform()+"\n")
        if noguimode == 1:
            handle.write("Processor: Not Supported on Termux\n")
        else:
            handle.write("Processor: " + (str(cpu))+"\n")
        handle.write("---------------\n")
        handle.write("RTB Dump:\n\n")
        plugindir = os.listdir('plugins/')
        handle.write(str(sys.modules.keys())+"\n")
        handle.write(str(dir())+"\n")
        handle.write(str(globals())+"\n")
        handle.write(str(locals())+"\n")
        handle.write("---------------\n")

@animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menucolour))
def run_update():
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
    update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
    clear()
    print(colored("Update has been downloaded, Installing...",menucolour))
    with open("update.zip", "wb") as handle:
        handle.write(update.content)
    try:
        shutil.copy("config.py", "config_old.py")
        shutil.copy("RTBFiles/smconfig.py", "smconfig_old.py")
    except Exception:
        pass
    try:
        shutil.unpack_archive("update.zip")
        copy_tree("Raid-Toolbox-master/", ".")
        os.remove("update.zip")
        shutil.rmtree("Raid-Toolbox-master/")
    except Exception as e:
        print("Error Updating, {}".format(e))

def info(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    elif sys.platform.startswith('linux'):
        os.system("printf '\033[8;30;100t'")
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Info")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Info\x07")
    if knockoff_mode == 1:
        print (colored("  _____       _     _    _____  _                       _   _______          _ ",menucolour))
        print (colored(" |  __ \     (_)   | |  |  __ \(_)                     | | |__   __|        | |",menucolour))
        print (colored(" | |__) |__ _ _  __| |  | |  | |_ ___  ___ ___  _ __ __| |    | | ___   ___ | |",menucolour))
        print (colored(" |  _  // _` | |/ _` |  | |  | | / __|/ __/ _ \| '__/ _` |    | |/ _ \ / _ \| |",menucolour))
        print (colored(" | | \ \ (_| | | (_| |  | |__| | \__ \ (_| (_) | | | (_| |    | | (_) | (_) | |",menucolour))
        print (colored(" |_|  \_\__,_|_|\__,_|  |_____/|_|___/\___\___/|_|  \__,_|    |_|\___/ \___/|_|",menucolour))
    else:
        print (colored("  _____       _     _   _______          _ ____            ",menucolour))
        print (colored(" |  __ \     (_)   | | |__   __|        | |  _ \           ",menucolour))
        print (colored(" | |__) |__ _ _  __| |    | | ___   ___ | | |_) | _____  __",menucolour))
        print (colored(" |  _  // _` | |/ _` |    | |/ _ \ / _ \| |  _ < / _ \ \/ /",menucolour))
        print (colored(" | | \ \ (_| | | (_| |    | | (_) | (_) | | |_) | (_) >  < ",menucolour))
        print (colored(" |_|  \_\__,_|_|\__,_|    |_|\___/ \___/|_|____/ \___/_/\_\ ",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    print (colored("Copyright (c) 2019, DeadBread",menucolour))
    print (colored("                                                            ",menucolour))
    print (colored("https://github.com/DeadBread76/Raid-Toolbox",menucolour2))
    print (colored("Discord: https://discord.gg/7RtuZEe\nTelegram: https://t.me/DeadBakery",menucolour2))
    print (colored("                                                            ",menucolour))
    if knockoff_mode == 1:
        print(colored("Lmfao suck my dick KriptaX#6216",random.choice(colours)))
    if singlefile == True:
        print (colored("SINGLE FILE MODE ACTIVE",menucolour2))
    if noguimode == 1:
        print (colored("Termux Mode.",menucolour2))
    print (colored("Raid ToolBox version: "+rtbversion,menucolour2))
    print (colored("Server Smasher version: "+smversion,menucolour2))
    print (colored("Discord.py version: "+ discord.__version__,menucolour2))
    if verbose == 1:
        print(colored("\nStartup Time: {}".format(t1-t0),menucolour2))
    print (colored("                                                            ",menucolour))
    print (colored("------------------------------------------------------------",menucolour))
    print (colored("Type 'update' to update Raid ToolBox to the latest version.",menucolour2))
    print (colored("Type 'reinstall' to reinstall or update requirements",menucolour2))
    print (colored("Type 'diag' for diagnostics log.",menucolour2))
    print (colored("Type 'yt' for my YouTube channel.",menucolour2))
    print (colored("Type 'console' to access console.",menucolour2))
    print (colored("------------------------------------------------------------",menucolour))
    inf = input(colored(">",menucolour2))
    if inf.lower() == "ree":
        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','ree',sys.executable,str(cliinputs),str(threadcount),guitheme])
        currentattacks["GOD Started at: {}".format(datetime.datetime.now().time())] = p.pid
    elif inf.lower() == 'yt':
        clear()
        webbrowser.open("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
        print("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
        input()
        info(currentattacks)
    elif inf.lower() == 'reinstall':
        requirements = open("requirements.txt").read().splitlines()
        log = open("install.log", "w")
        for package in requirements:
            print("Installing {}...".format(package))
            p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)
            if p == 1:
                print("There was an error with installing the package {}, Refer to Install.log".format(package))
            elif p == 0:
                print("Installed {} Successfully.".format(package))
        input("Installation Complete.")
        info(currentattacks)
    elif inf.lower() == 'diag':
        clear()
        if singlefile == True:
            print("Not while Single file mode is active you don't.")
            input()
            info(currentattacks)
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Diagnostics")
        elif sys.platform.startswith('linux'):
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Diagnostics\x07")
        diagrun(currentattacks)
        print ("Diagnostics Written to file.")
        input()
    elif inf.lower() == 'update':
        clear()
        if "b" in rtbversion:
            print("This is a test version of RTB, Please do not update.")
            input()
        else:
            u = input("Are you sure you want to update?(Y/N)\n")
            if u.lower() == 'y':
                clear()
                run_update()
                print ("Update complete, exiting.")
                time.sleep(3)
                sys.exit()
            else:
                info(currentattacks)
    elif inf.lower() == 'console':
        clear()
        print("0. Back")
        while True:
            try:
                com = input(">")
                if com == '0':
                    break
                exec(com)
            except Exception as e:
                print(e)
    main(currentattacks)

def quickcheck(currentattacks):
    clear()
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','quickcheck',sys.executable,str(cliinputs),str(threadcount),guitheme,token])
        time.sleep(0.07)
    p.wait()
    input("Checking complete.")
    main(currentattacks)

def tokenmanager(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Manager")
    elif sys.platform.startswith('linux'):
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Token Manager\x07")
    tokenlist = open("tokens.txt").read().splitlines()
    print(colored("====================",menucolour))
    print(colored("     Token Menu     ",menucolour))
    print(colored("====================",menucolour))
    print(colored("0. Return to main menu",menucolour2))
    print(colored("1. Add Token",menucolour2))
    print(colored("2. View Tokens",menucolour2))
    print(colored("3. View Token names and ID",menucolour2))
    print(colored("4. Token Checker",menucolour2))
    print(colored("5. Refresh Token list",menucolour2))
    print(colored("====================",menucolour))
    e = input("Choice: ")
    try:
        if int(e) == 0:
            main(currentattacks)
        elif int(e) == 1:
            clear()
            print(colored("Input Token to add to tokens.txt\n0. Back",menucolour2))
            t = input()
            with open ("tokens.txt","a",errors='ignore') as handle:
                handle.write("{}\n".format(t))
            print (colored("Added {} to file.".format(t.rstrip()),menucolour))
            input()
            tokenmanager(currentattacks)
        elif int(e) == 2:
            clear()
            if len(tokenlist) > 30:
                leng = 30
                leng += len(tokenlist)
                if sys.platform.startswith('win32'):
                    os.system('mode con:cols=100 lines={}'.format(leng))
                elif sys.platform.startswith('linux'):
                    os.system("printf '\033[8;{};100t'".format(leng))
            for token in tokenlist:
                print(colored(token,menucolour2))
            input()
            tokenmanager(currentattacks)
        elif int(e) == 3:
            clear()
            list = []
            if len(tokenlist) > 30:
                print("This May take a while, Continue? (Y/N)")
                h = input()
                if h.lower() == 'y':
                    pass
                else:
                    tokenmanager(currentattacks)
            if len(tokenlist) > 30:
                leng = 30
                leng += len(tokenlist)
                if sys.platform.startswith('win32'):
                    os.system('mode con:cols=100 lines={}'.format(leng))
                elif sys.platform.startswith('linux'):
                    os.system("printf '\033[8;{};100t'".format(leng))
            for token in tokenlist:
                apilink = 'https://canary.discordapp.com/api/v6/users/@me'
                headers = {'Authorization': token.rstrip(), 'Content-Type': 'application/json'}
                src = requests.get(apilink, headers=headers)
                if "401: Unauthorized" in str(src.content):
                    pass
                else:
                    response = json.loads(src.content.decode())
                    list.append(response['username']+"#"+response['discriminator']+" (ID: "+str(response['id'])+") ")
            for x in list:
                print (colored(x,menucolour2))
            input()
            tokenmanager(currentattacks)
        elif int(e) == 4:
            tokencheck(currentattacks)
        elif int(e) == 5:
            tokenlist.close()
            tokencheck(currentattacks)
    except Exception:
        tokenmanager(currentattacks)

def wew(currentattacks):
    if sys.platform.startswith('win32'):
        clear()
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | ¯\_(ツ)_/¯")
    else:
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/player.py',sys.executable],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Music! | Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def pud():
    clear()
    while True:
        if sys.platform.startswith('win32'):
            os.system('mode con:cols={} lines={}'.format(random.randint(10,100),random.randint(10,100)))
        elif sys.platform.startswith('linux'):
            os.system("printf '\033[8;{};{}t'".format(random.randint(10,100),random.randint(10,100)))
        time.sleep(0.1)

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


if __name__ == "__main__":
    if sys.platform.startswith('linux'):
        pass
    else:
        t = threading.Thread(name='Title Update', target=titleupdate)
        t.start()
    main(currentattacks)
