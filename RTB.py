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

rtbversion = "1.0.1r1"
smversion = "0.1.11r1"

try:
    import json
    with open('config.json', 'r') as handle:
        config = json.load(handle)
        skin = config['skin']
        threadcount = config['threadcount']
        verbose = config['verbose']
        cliinputs = config['cliinputs']
        noguimode = config['noguimode']
        disablecloudflarecheck = config['disablecloudflarecheck']
        disableupdatecheck = config['disableupdatecheck']
        combineuverifiedandverified = config['combineuverifiedandverified']
        tokenwarningthreshhold = config['tokenwarningthreshhold']
        serversmasherinmainwindow = config['serversmasherinmainwindow']
        ignoreffmpegmissing = config['ignoreffmpegmissing']
except Exception:
    print("Unable to read config file.\nImporting necessary modules and checking installation...")
    import os
    import sys
    import urllib.request
    import subprocess
    if not os.path.exists("RTBFiles/"):
        print("RTBFiles Directory not found.")
    if not os.path.exists("tools/"):
        print("Tools Directory not found.")
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/config.json')
    data = response.read()
    data = data.decode('utf-8')
    with open("config.json","w+") as handle:
        handle.write(data)
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/requirements.txt')
    data = response.read()
    data = data.decode('utf-8')
    with open("requirements.txt","w+") as handle:
        handle.write(data)
    try:
        with open('config.json', 'r') as handle:
            config = json.load(handle)
            skin = config['skin']
            threadcount = config['threadcount']
            verbose = config['verbose']
            cliinputs = config['cliinputs']
            noguimode = config['noguimode']
            disablecloudflarecheck = config['disablecloudflarecheck']
            disableupdatecheck = config['disableupdatecheck']
            combineuverifiedandverified = config['combineuverifiedandverified']
            tokenwarningthreshhold = config['tokenwarningthreshhold']
            serversmasherinmainwindow = config['serversmasherinmainwindow']
            ignoreffmpegmissing = config['ignoreffmpegmissing']
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
import os, sys, time, ctypes, random, datetime, platform, shutil, subprocess, threading, webbrowser, importlib
from distutils.dir_util import copy_tree
if sys.platform.startswith('win32'):
    from subprocess import CREATE_NEW_CONSOLE

mdl = importlib.import_module("themes.{}".format(skin))
if "__all__" in mdl.__dict__:
    names = mdl.__dict__["__all__"]
else:
    names = [x for x in mdl.__dict__ if not x.startswith("_")]
globals().update({k: getattr(mdl, k) for k in names})

menu1 = menu1
menu2 = menu2

if sys.platform.startswith('win32'):
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading...")
else:
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading...\x07")

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
            print("There was an error with installing termux API, Refer to Install.log")
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
            requirements = open("requirements_termux.txt").read().splitlines()
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

elif verbose == 1:
    print ("Loading modules...")
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading... | Verbose Mode")
    else:
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
            if sys.platform.startswith('darwin'):
                requirements = open("requirements_mac.txt").read().splitlines()
            else:
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

init()
colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
if menu1.lower() == 'random':
    menu1 = random.choice(colours)
if menu2.lower() == 'random':
    menu2 = random.choice(colours)
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
if not cliinputs == 1:
    sg.ChangeLookAndFeel(window_theme)
if not os.path.isfile("RTBFiles/licence"):
    lic = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/LICENCE").text
    if cliinputs == 1:
        print("Raid-Toolbox\n"+lic)
        time.sleep(10)
        input("Press Enter to continue.")
    else:
        sg.Popup(lic, button_type=None, no_titlebar=True, title="LICENCE", keep_on_top=True, grab_anywhere=True)
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
    else:
        try:
            if verbose == 1:
                print("Checking for updates...")
            vercheck = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/version").text.rstrip().split("|")
            if not vercheck[0] == rtbversion:
                if cliinputs == 1:
                    print(colored("There is an update for RTB, Download update?", menu1))
                    verchoice = input("(Y/N): ")
                    if verchoice.lower() == "y":
                        @animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menu1))
                        def run_update():
                            if sys.platform.startswith('win32'):
                                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
                            else:
                                sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
                            update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
                            clear()
                            print(colored("Update has been downloaded, Installing...",menu1))
                            return update
                        update = run_update()
                        with open("update.zip", "wb") as handle:
                            handle.write(update.content)
                        try:
                            shutil.copy("RTBFiles/smconfig.py", "RTBFiles/smconfig_old.py")
                        except Exception:
                            pass
                        try:
                            shutil.unpack_archive("update.zip")
                            copy_tree("Raid-Toolbox-master/", ".")
                            os.remove("update.zip")
                            shutil.rmtree("Raid-Toolbox-master/")
                            print ("Update complete, exiting.")
                            with open('config.json', 'r+') as handle:
                                edit = json.load(handle)
                                edit['skin'] = skin
                                edit['threadcount'] = threadcount
                                edit['cliinputs'] = cliinputs
                                handle.seek(0)
                                json.dump(edit, handle, indent=4)
                                handle.truncate()
                        except Exception as e:
                            print("Error Updating, {}".format(e))
                        time.sleep(3)
                        sys.exit()
                else:
                    verchoice = sg.PopupYesNo("There is an update for RTB, Download update?")
                    if verchoice == "Yes":
                        clear()
                        @animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menu1))
                        def run_update():
                            if sys.platform.startswith('win32'):
                                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
                            else:
                                sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
                            update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
                            clear()
                            print(colored("Update has been downloaded, Installing...",menu1))
                            return update
                        update = run_update()
                        with open("update.zip", "wb") as handle:
                            handle.write(update.content)
                        shutil.copy("RTBFiles/smconfig.py", "RTBFiles/smconfig_old.py")
                        shutil.unpack_archive("update.zip")
                        copy_tree("Raid-Toolbox-master/", ".")
                        os.remove("update.zip")
                        shutil.rmtree("Raid-Toolbox-master/")
                        with open('config.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['skin'] = skin
                            edit['threadcount'] = threadcount
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
                        print ("Update complete, exiting.")

            if not vercheck[1] == smversion:
                if cliinputs == 1:
                    print(colored("There is an update for Server Smasher, Download update?", menu1))
                    verchoice = input("(Y/N): ")
                    if verchoice.lower() == "y":
                        clear()
                        print(colored('Downloading update for Server Smasher, Please Wait...',menu1))
                        serversmasherupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/serversmasher.py')
                        configupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/smconfig.py')
                        mainpatch = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTB.py")
                        print(colored("Update has been downloaded, Installing...",menu1))
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
                        print(colored("Update Complete.",menu1))
                        input("Press enter to exit.")
                        sys.exit()
                else:
                    verchoice = sg.PopupYesNo("There is an update for Server Smasher, Download update?")
                    if verchoice == "Yes":
                        clear()
                        print(colored('Downloading update for Server Smasher, Please Wait...',menu1))
                        serversmasherupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/serversmasher.py')
                        configupdate = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/smconfig.py')
                        mainpatch = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTB.py")
                        print(colored("Update has been downloaded, Installing...",menu1))
                        shutil.copy("RTBFiles/smconfig.py", "RTBFiles/smconfig_old.py")
                        with open("RTBFiles/serversmasher.py", "wb") as handle:
                            handle.write(serversmasherupdate.content)
                        with open("RTBFiles/smconfig.py", "wb") as handle:
                            handle.write(configupdate.content)
                        with open("RTB.py", "wb") as handle:
                            handle.write(mainpatch.content)
                        sg.Popup("Update Complete, Press ok to close.")
                        sys.exit()
        except Exception as e:
            if cliinputs == 1:
                print("Error Updating: {}".format(e))
            else:
                sg.PopupError("Error Updating Raid Toolbox.\n ({})".format(e), title="Update Error")
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
    input(colored("Press enter to continue.",menu1))
else:
    singlefile = False
    if sys.platform.startswith('win32'):
        if ignoreffmpegmissing == 0:
            if not os.path.isfile("ffmpeg.exe"):
                if verbose == 1:
                    print("FFmpeg is missing")
                print(colored("Download FFMpeg? (Needed For Voice Chat Spammer)", menu1))
                fmpg = input("(Y/N):")
                if fmpg.lower() == "y":
                    clear()
                    @animation.wait(colored('Downloading FFMpeg, Please Wait ',menu1))
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
            if cliinputs == 1:
                print("Your IP is CloudFlare Banned.\nThis means you can't use the Joiner or the Regular Checker.\nUse a VPN to get around this.")
                input(colored("Press enter to continue.",'red'))
            else:
                sg.Popup("Your IP is CloudFlare Banned.\nThis means you can't use the Joiner or the Regular Checker.\nUse a VPN to get around this.")
t1 = time.time()
if verbose == 1:
    print("Startup time: {}".format(t1-t0))
    with open("load.log","a",errors='ignore') as handle:
        handle.write("================================\nStartup Time: {}\n================================\n\n\n".format(t1-t0))
    print("Starting...")

currentattacks = {}

def titleupdate():
    global currentattacks
    while True:
        for attack in list(currentattacks):
            if psutil.pid_exists(currentattacks[attack]):
                pass
            else:
                currentattacks.pop(attack)
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
        time.sleep(2)

def main(currentattacks):
    global skin
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    else:
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
    else:
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
        else:
            os.system("printf '\033[8;32;41t'")
        print(colored("=========================================",menu1))
        print(colored("   Welcome to DeadBread's Raid Toolbox",menu2))
        print(colored("=========================================",menu1))
        print(colored("          {} tokens available.".format(tcounter),menu2))
        print(colored("=========================================",menu1))
        print(colored("0.  Exit",menu2))
        print(colored("1.  Joiner",menu2))
        print(colored("2.  Leaver",menu2))
        print(colored("3.  Group DM leaver",menu2))
        print(colored("4.  Token Checker",menu2))
        print(colored("5.  Message spammer",menu2))
        print(colored("6.  Ascii spammer",menu2))
        print(colored("7.  Mass mention spammer",menu2))
        print(colored("8.  Voice Chat Spammer",menu2))
        print(colored("9.  User DM Spammer",menu2))
        print(colored("10. Friend Request Spammer",menu2))
        print(colored("11. Group DM spammer",menu2))
        print(colored("12. Random Image Spammer",menu2))
        print(colored("13. Status Changer",menu2))
        print(colored("14. Nickname Changer",menu2))
        print(colored("15. Embed Spammer",menu2))
        print(colored("16. Avatar Changer",menu2))
        print(colored("17. Role Mass Mentioner",menu2))
        print(colored("18. Channel Message Cleaner",menu2))
        print(colored("19. HypeSquad House Changer",menu2))
        print(colored("20. Message Reaction Adder",menu2))
        print(colored("21. Server Smasher",menu2))
        print(colored("22. View Running Attacks",menu2))
        print(colored("23. Custom attack plugins",menu2))
        print(colored("24. Quick Checker",menu2))
        print(colored("25. Token options",menu2))
        choice = input(colored(">",menu2))
    elif cliinputs == 0:
        pluginlist = {}
        pluginfolder = []
        pluginfile = []
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
            pluginfolder.append(plugin)
        for plugin in pluginlist.items():
            pluginfile.append(plugin[1])
        menu_def = [['RTB', ['Running Attacks', 'Info', 'Diagnostics', 'Skins']],
                    ['Tokens', ['View/Add Tokens']],
                    ['Help', ['Wiki', 'My YouTube', 'Discord Server', 'Telegram']],
                    ['Server Smasher', ['Launch']],
                    ['Plugins', ['Support Coming soon.']] #['Plugins', ['Download Plugins From Repo', 'Kill All Plugins', 'Load Plugin...', pluginfolder]]
                    ]
        layout =[
                [sg.Menu(menu_def)],
                [sg.Image(data=rtb_banner, size=banner_size, pad=banner_padding)],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_joiner, key="Joiner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_leaver, key="Leaver"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_group_leaver, key="Group Leaver")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_token_checker, key="Checker"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_checker_v2, key="Checker V2"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_message_spammer, key="Message Spammer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_ascii_spammer, key="Ascii Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_mass_mentioner, key="Mass Mentioner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_role_mass_mentioner, key="Role Mass Mentioner")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_vc_spammer, key="VC Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_dm_spammer, key="DM Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_friend_bomber, key="Friend Bomber")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_group_spammer, key="Group Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_image_spammer, key="Image Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_status_changer, key="Status Changer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_nickname_changer, key="Nickname Changer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_embed_spammer, key="Embed Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_avatar_changer, key="Avatar Changer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_server_cleaner, key="Server Cleaner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_hypesquad_changer, key="HypeSquad Changer"),  sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_reaction_adder, key="Reaction Adder")],
                ]
        tokenlist = open("tokens.txt").read().splitlines()
        window = sg.Window("DeadBread's Raid ToolBox v{} | ({} Tokens available.)".format(rtbversion,len(tokenlist)), icon=rtb_icon).Layout(layout)
        while True:
            event, values = window.Read()
            if event is None:
                sys.exit()
            elif event == "Running Attacks":
                while True:
                    window.Close()
                    acount = -1
                    attackbox = ''
                    names = []
                    for attack in list(currentattacks):
                        if psutil.pid_exists(currentattacks[attack]):
                            if not sys.platform.startswith('win32'):
                                proc = psutil.Process(currentattacks[attack])
                                if proc.status() == psutil.STATUS_ZOMBIE:
                                    currentattacks.pop(attack)
                                    continue
                            acount += 1
                            attackbox += ("{}. {}\n".format(acount,attack))
                        else:
                            currentattacks.pop(attack)
                    for attack in list(currentattacks.keys()):
                        names.append(attack)
                    if currentattacks == {}:
                        attackbox += "None\n"
                    layout = [
                             [sg.Text("Running Attacks: {}".format(len(currentattacks)))],
                             [sg.Multiline(attackbox,size=(50,20))],
                             [sg.Input(focus=True), sg.Button('Kill',size=(10,1)), sg.Button('Kill All',size=(10,1))]
                             ]
                    window = sg.Window("DeadBread's Raid ToolBox v{} | Running Attacks".format(rtbversion)).Layout(layout)
                    event, values = window.Read()
                    attacks = values[1]
                    if event is None:
                        window.Close()
                        main(currentattacks)
                    elif event == "Kill All":
                        for attack in currentattacks:
                            try:
                                print(int(currentattacks[attack]))
                                os.kill(int(currentattacks[attack]), 15)
                            except Exception:
                                pass
                        currentattacks = {}
                    elif event == "Kill":
                        try:
                            os.kill(int(currentattacks[names[int(attacks)]]), 15)
                        except Exception as e:
                            print(e)
            elif event == "Diagnostics":
                sg.PopupNoWait("Checking Endpoints...", title='Diagnostics', auto_close=True)
                cloudcheck = requests.get("https://discordapp.com/api/v6/invite/DEADBREAD")
                ptbcloudcheck = requests.get("https://ptb.discordapp.com/api/v6/invite/DEADBREAD")
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
                try:
                    cpu = cpuinfo.get_cpu_info()['brand']
                except Exception:
                    pass
                if banned == True:
                    sg.PopupNoWait("Diagnostics Written to file.\nCloudFlare Results:\nYou are CloudFlare banned on the canary endpoint.\nThis means the Joiner function and Regular Checker will not work.\n(So please don't come to my Discord server and complain about the joiner not working.)", title="CloudFlare Banned")
                else:
                    sg.PopupNoWait("Diagnostics Written to file.\nCloudFlare Results:\nYou are not CloudFlare Banned.\nCongrats.", title="Results")
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
                    try:
                        handle.write("Processor: " + (str(cpu))+"\n")
                    except Exception as e:
                        handle.write("Processor: " + (str(e))+"\n")
                    handle.write("---------------\n")
                    handle.write("RTB Dump:\n\n")
                    plugindir = os.listdir('plugins/')
                    handle.write(str(sys.modules.keys())+"\n")
                    handle.write(str(dir())+"\n")
                    handle.write(str(globals())+"\n")
                    handle.write(str(locals())+"\n")
                    handle.write("---------------\n")
            elif event == "Info":
                while True:
                    window.Close()
                    layout = [
                             [sg.Image(data=rtb_banner)],
                             [sg.Text("Version {}".format(rtbversion))],
                             [sg.Text("Copyright (c) 2019, DeadBread\n\n")],
                             [sg.Text("Credits/Special Thanks:\nMattlau04 - Writing the Docs and helping me out with general shit\nAliveChive - Bug Hunting\ndirt - Creating Skins and Testing\nNextro - Termux Testing\nColt. - Termux Testing\nLucas. - Creating Skins and Nitro Boosting DeadBakery\nTummy Licker - Gifting Nitro\n")],
                             ]
                    window = sg.Window("DeadBread's Raid ToolBox v{} | Info".format(rtbversion)).Layout(layout)
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main(currentattacks)
            elif event == "Skins":
                while True:
                    window.Close()
                    skinlist = []
                    for file in os.listdir('themes'):
                        if file.endswith(".py"):
                            skinlist.append(file.replace(".py",""))
                    layout = [
                             [sg.Text('Current Skin:',size=(13,1)),sg.Text("{} v{} by {}".format(theme_name,theme_version,theme_author))],
                             [sg.Text('Skin Bio:',size=(13,1)),sg.Text((theme_bio))],
                             [sg.Text('Change Theme:',size=(13,1)), sg.Combo(skinlist,default_value=skin,size=(20,1)), sg.Button('Change',size=(18,1))]
                             ]
                    window = sg.Window("DeadBread's Raid ToolBox v{} | Skins".format(rtbversion), size=(400,100)).Layout(layout)
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main(currentattacks)
                    elif event == "Change":
                        new_skin = values[0]
                        skin = new_skin
                        mdl = importlib.import_module("themes.{}".format(new_skin))
                        if "__all__" in mdl.__dict__:
                            names = mdl.__dict__["__all__"]
                        else:
                            names = [x for x in mdl.__dict__ if not x.startswith("_")]
                        globals().update({k: getattr(mdl, k) for k in names})
                        sg.ChangeLookAndFeel(window_theme)
                        with open('config.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['skin'] = new_skin
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
            elif event == "View/Add Tokens":
                while True:
                    window.Close()
                    textedit = ''
                    with open("tokens.txt","r") as handle:
                        data = handle.readlines()
                        for token in data:
                            textedit += token
                        menu_def = [['File', ['Save', 'Reset']]]
                        layout = [
                                 [sg.Menu(menu_def)],
                                 [sg.Multiline(default_text=textedit, size=(80, 20))]
                                 ]
                        window = sg.Window("DeadBread's Raid ToolBox v{} | tokens.txt".format(rtbversion)).Layout(layout)
                        event, values = window.Read()
                        if event is None:
                            window.Close()
                            main(currentattacks)
                        elif event == "Save":
                            text = values[1]
                            with open("tokens.txt", "w") as write:
                                write.write(text)
            elif event == "Launch":
                window.Close()
                serversmasher(currentattacks)
            elif event == "Wiki":
                webbrowser.open("https://github.com/DeadBread76/Raid-Toolbox/wiki")
            elif event == "My YouTube":
                webbrowser.open("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
            elif event == "Discord Server":
                webbrowser.open("discord.gg/JtvphCQ")
            elif event == "Telegram":
                webbrowser.open("https://t.me/DeadBakery")
            elif event == "Joiner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Joiner | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Leaver":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Group Leaver":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Checker":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','Checker',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Token Checker | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Checker V2":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','Checker V2',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Token Checker V2 | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Message Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Message Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Ascii Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Ascii Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Mass Mentioner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Mass Mentioner Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Role Mass Mentioner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Role mass mention attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "VC Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Voice Chat Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "DM Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Friend Bomber":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Friender Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Group Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Image Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Random Image Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Status Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Status Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Nickname Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Nickname Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Embed Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','embed',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Embed Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Avatar Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','avatarchange',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Avatar Changing | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Server Cleaner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Tokens are cleaning up | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "HypeSquad Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Hypesquad Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Reaction Adder":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Reaction | Started at: {}".format(datetime.datetime.now().time())] = p.pid
    else:
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                                                                                ██",menu1))
        if singlefile == True:
            print (colored("██                                   ",menu1)+(colored("SINGLE FILE MODE IS ACTIVE",menu2)+(colored("                                   ██",menu1))))
        else:
            print (colored("██                               ",menu1)+colored("Welcome to DeadBread's Raid Toolbox",menu2)+colored("                              ██",menu1))
        print (colored("██                                                                                                ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                                                                                ██",menu1))
        if tcounter == 0:
            print (colored("██                                      ",menu1)+(colored("No tokens available.",menu2)+(colored("              "+colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menu2)+(colored(" ██",menu1))))))
        elif tcounter == 1:
            print (colored("██                                  ",menu1)+(colored("There is "+str(tcounter),menu2)+(colored(" token available.           ",menu2)+(colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menu2)+(colored(" ██",menu1))))))
        else:
            print (colored("██                                  ",menu1)+(colored("There are "+str(tcounter),menu2)+(colored(" tokens available.         ",menu2)+(colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menu2)+(colored(" ██",menu1))))))
        print (colored("██                                                                                                ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("██         ",menu1)+(colored("0.  Exit",menu2)+colored("                              ██",menu1)+colored("         13. Status Changer",menu2)+colored("                    ██",menu1)))
        print (colored("██         ",menu1)+(colored("1.  Joiner",menu2)+colored("                            ██",menu1)+colored("         14. Nickname Changer",menu2)+colored("                  ██",menu1)))
        print (colored("██         ",menu1)+(colored("2.  Leaver",menu2)+colored("                            ██",menu1)+colored("         15. Embed Spammer",menu2)+colored("                     ██",menu1)))
        print (colored("██         ",menu1)+(colored("3.  Group DM leaver",menu2)+colored("                   ██",menu1)+colored("         16. Avatar Changer",menu2)+colored("                    ██",menu1)))
        print (colored("██         ",menu1)+(colored("4.  Token Checker",menu2)+colored("                     ██",menu1)+colored("         17. Role Mass Mentioner",menu2)+colored("               ██",menu1)))
        print (colored("██         ",menu1)+(colored("5.  Message spammer",menu2)+colored("                   ██",menu1)+colored("         18. Channel Message Cleaner",menu2)+colored("           ██",menu1)))
        print (colored("██         ",menu1)+(colored("6.  Ascii spammer",menu2)+colored("                     ██",menu1)+colored("         19. HypeSquad House Changer",menu2)+colored("           ██",menu1)))
        print (colored("██         ",menu1)+(colored("7.  Mass mention spammer",menu2)+colored("              ██",menu1)+colored("         20. Message Reaction Adder",menu2)+colored("            ██",menu1)))
        print (colored("██         ",menu1)+(colored("8.  Voice Chat Spammer",menu2)+colored("                ██",menu1)+colored("         21. Server Smasher",menu2)+colored("                    ██",menu1)))
        print (colored("██         ",menu1)+(colored("9.  User DM Spammer",menu2)+colored("                   ██",menu1)+colored("         22. View Running Attacks",menu2)+colored("              ██",menu1)))
        print (colored("██         ",menu1)+(colored("10. Friend Request Spammer",menu2)+colored("            ██",menu1)+colored("         23. Custom attack plugins",menu2)+colored("             ██",menu1)))
        print (colored("██         ",menu1)+(colored("11. Group DM spammer",menu2)+colored("                  ██",menu1)+colored("         24. Quick Checker",menu2)+colored("                     ██",menu1)))
        print (colored("██         ",menu1)+(colored("12. Random Image Spammer",menu2)+colored("              ██",menu1)+colored("         25. Token options",menu2)+colored("                     ██",menu1)))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("██     ",menu1)+(colored("Please enter the number of your choice.",menu2)+colored("   ██    ",menu1)+(colored("Type 'info' for Information and Updates",menu2)+colored("    ██",menu1))))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        choice = input(colored(">",menu2))
    try:
        if choice.lower() == 'info':
            info(currentattacks)
        if int(choice) == 0:
            sys.exit()
        elif int(choice) == 1:
            if cliinputs == 1:
                joiner(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Joiner | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 2:
            if cliinputs == 1:
                leaver(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 3:
            if cliinputs == 1:
                groupleaver(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 4:
            tokencheck(currentattacks)
        elif int(choice) == 5:
            if cliinputs == 1:
                messagespam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Message Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 6:
            if cliinputs == 1:
                asciispam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Ascii Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 7:
            if cliinputs == 1:
                massmentioner(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Mass Mentioner Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 8:
            if cliinputs == 1:
                vcspam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Voice Chat Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 9:
            if cliinputs == 1:
                dmspam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 10:
            if cliinputs == 1:
                friender(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Friender Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 11:
            if cliinputs == 1:
                groupdmspam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 12:
            if cliinputs == 1:
                imagespam(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Random Image Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 13:
            if cliinputs == 1:
                gamechange(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Status Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 14:
            if cliinputs == 1:
                nickchange(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Nickname Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 15:
            if cliinputs == 1:
                clear()
                print(colored("CLI Mode does not support embed spammer anymore.\nPlease Use GUI.",menu2))
                input()
                main(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','embed',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Embed Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 16:
            if cliinputs == 1:
                clear()
                print(colored("CLI Mode does not support the avatar changer anymore.\nPlease Use GUI.",menu2))
                input()
                main(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','avatarchange',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Avatar Changing | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 17:
            if cliinputs == 1:
                rolemassmention(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Role mass mention attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 18:
            if cliinputs == 1:
                cleanup(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Tokens are cleaning up | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 19:
            if cliinputs == 1:
                hypesquadchanger(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Hypesquad Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main(currentattacks)
        elif int(choice) == 20:
            if cliinputs == 1:
                reaction(currentattacks)
            else:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
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
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Invite Joiner\x07")
    print (colored("Discord invite joiner.",menu1))
    print (colored("0: Back",menu1))
    link = input('Discord Invite Link: ')
    if link == '0':
        main(currentattacks)
    if len(link) > 7:
        link = link[19:]
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),link],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Joiner Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def leaver(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Leaver")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Leaver\x07")
    print (colored("Discord server leaver.",menu1))
    print (colored("0: Back",menu1))
    ID = input ('ID of the server to leave: ')
    if ID == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),ID],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Leaver Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def groupleaver(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Leaver")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Leaver\x07")
    if cliinputs == 1:
        print (colored("Discord group DM leaver.",menu1))
        print (colored("0: Back",menu1))
        ID = input ('ID of the group DM to leave: ')
        if str(ID) == '0':
            main(currentattacks)
    else:
        ID = sg.PopupGetText('Enter ID of the group DM to leave', "DeadBread's Raid ToolBox | Group DM Leaver")
        if ID == None:
            main(currentattacks)
    tokenlist = open("tokens.txt").read().splitlines()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),ID],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Group Leaver Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def tokencheck(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Checker")
    else:
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
        print (colored("Checking tokens...",menu1))
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
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Spammer\x07")
    print (colored("Discord Server message spammer.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    msgtxt = input ("Text to spam: ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),msgtxt,chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Message Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def asciispam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Spammer\x07")
    print (colored("Discord server ascii spammer.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Ascii Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def massmentioner(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Mass Mentioner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Mass Mentioner\x07")
    print (colored("Discord server mass mentioner.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),SERVER,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Mass Mentioner Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def vcspam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice Chat Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice Chat Spammer\x07")
    tcounter = 0
    print (colored("Discord VC joiner/spammer.",menu1))
    print (colored("0: Back",menu1))
    ytlink = input ('YouTube Link to play: ')
    if ytlink == '0':
        main(currentattacks)
    chanid = input ('Voice channel ID: ')
    tokencount = input ('Number of tokens to use: ')
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),ytlink,chanid,tokencount],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Voice Chat Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def dmspam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | DM Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | DM Spammer\x07")
    print (colored("Discord user DM spammer.",menu1))
    print (colored("0: Back",menu1))
    user = input ("User's ID: ")
    if str(user) == '0':
        main(currentattacks)
    msgtxt = input ("Text to spam (Ascii Spam = ascii): ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),user,msgtxt],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["DM Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def friender(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Friend Request Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Friend Request Spammer\x07")
    print (colored("Discord user mass friender.",menu1))
    print (colored("0: Back",menu1))
    userid = input("User's ID: ")
    if str(userid) == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),userid],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Friender Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def groupdmspam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Spammer\x07")
    print (colored("Discord Group DM message spammer.",menu1))
    print (colored("0: Back",menu1))
    group = input ("Group ID: ")
    if str(group) == '0':
        main(currentattacks)
    msgtxt = input ("Text to spam (Ascii Spam = ascii): ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),msgtxt,group],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Group DM Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def imagespam(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Image Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Image Spammer\x07")
    print (colored("Discord server image spammer.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Random Image Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def gamechange(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing Status Changer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Playing Status Changer\x07")
    print (colored("Discord game playing status changer.",menu1))
    print (colored("0: Back",menu1))
    print ('Name of game to play: ')
    game = input ('Playing ')
    if game == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),game],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Game Status Changing Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def nickchange(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Nickname Changer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Nickname Changer\x07")
    print (colored("Discord random ascii nickname.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Nickname Changer Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def rolemassmention(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Role Mass Mentioner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Role Mass Mentioner\x07")
    print (colored("Discord role mass mentioner.",menu1))
    print (colored("This will spam mention all roles that are mentionable.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),SERVER,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Role Mass Mentioner Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def cleanup(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Cleaner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Cleaner\x07")
    print (colored("Clean up messages sent by a token",menu1))
    print (colored("This will delete all the messages sent by the token.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main(currentattacks)
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Tokens are cleaning up Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def hypesquadchanger(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | HypeSquad Changer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | HypeSquad Changer\x07")
    print (colored("0. Back",menu2))
    print (colored("1. Bravery",menu2))
    print (colored("2. Brilliance",menu2))
    print (colored("3. Ballance",menu2))
    choice = input('Selection: ')
    if int(choice) == 0:
        main(currentattacks)
    elif int(choice) == 1:
        choice = 'Bravery'
    elif int(choice) == 2:
        choice = 'Brilliance'
    elif int(choice) == 3:
        choice = 'Ballance'
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),choice],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Hypesquad Changer Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def reaction(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Emoji Reactor")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Emoji Reactor\x07")
    print (colored("Emoji Reactor.",menu1))
    if not noguimode == 1:
        print('why are you using cli like seriously')
    print (colored("0: Back",menu1))
    chan = input('Channel ID: ')
    if str(chan) == '0':
        main(currentattacks)
    msgid = input ("Message ID: ")
    emoji = input ("Emoji: ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(cliinputs),str(str(threadcount),str(attacks_theme),msgid,chan,"Add",emoji),chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Reaction Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main(currentattacks)

def serversmasher(currentattacks):
    clear()
    if cliinputs == 1:
        print ("The config file for the Server Smasher is in RTBFiles/smconfig.py, please add token before starting.")
    if sys.platform.startswith('win32'):
        if serversmasherinmainwindow == 1:
            p = subprocess.Popen([sys.executable,'RTBFiles/serversmasher.py',smversion,menu1,menu2,str(noguimode)])
            p.wait()
        else:
            subprocess.Popen([sys.executable,'RTBFiles/serversmasher.py',smversion,menu1,menu2,str(noguimode)],creationflags=CREATE_NEW_CONSOLE)
    else:
        if serversmasherinmainwindow == 1:
            p = subprocess.Popen([sys.executable,'RTBFiles/serversmasher.py',smversion,menu1,menu2,str(noguimode)])
            p.wait()
        else:
            subprocess.call(['gnome-terminal', '-x', sys.executable,'RTBFiles/serversmasher.py',smversion,menu1,menu2,str(noguimode)])
    if serversmasherinmainwindow == 1:
        pass
    elif noguimode == 1:
        pass
    elif cliinputs == 1:
        time.sleep(5)
    main(currentattacks)

def viewcurrentat(currentattacks):
    clear()
    acount = -1
    names = []
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Current Attacks")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Current Attacks\x07")
    print (colored("Current Attacks:",menu1))
    print (colored("---------------------",menu1))
    for attack in list(currentattacks):
        if psutil.pid_exists(currentattacks[attack]):
            if not sys.platform.startswith('win32'):
                proc = psutil.Process(currentattacks[attack])
                if proc.status() == psutil.STATUS_ZOMBIE:
                    currentattacks.pop(attack)
                    continue
            acount += 1
            print (colored("{}. {}".format(acount,attack),menu2))
        else:
            currentattacks.pop(attack)
    for attack in list(currentattacks.keys()):
        names.append(attack)
    if currentattacks == {}:
        print (colored('None',"green"))
    print (colored("---------------------\nType 'killall' to end all current attacks, Or type the number to end that attack.",menu1))
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
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Custom Plugins\x07")
    pluginno = -1
    print (colored("Installed Plugins:",menu1))
    print (colored("----------------------",menu1))
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
    print (colored("----------------------\nb: Back",menu1))
    print (colored("e: Kill all plugins\nd: Download plugins from Repo",menu1))
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
    p = subprocess.Popen([sys.executable,'plugins/'+plugchoice,sys.executable,menu1])
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

@animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menu1))
def run_update():
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
    update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
    clear()
    print(colored("Update has been downloaded, Installing...",menu1))
    with open("update.zip", "wb") as handle:
        handle.write(update.content)
    try:
        shutil.copy("RTBFiles/smconfig.py", "smconfig_old.py")
    except Exception:
        pass
    try:
        shutil.unpack_archive("update.zip")
        copy_tree("Raid-Toolbox-master/", ".")
        os.remove("update.zip")
        shutil.rmtree("Raid-Toolbox-master/")
        with open('config.json', 'r+') as handle:
            edit = json.load(handle)
            edit['skin'] = skin
            edit['threadcount'] = threadcount
            edit['cliinputs'] = cliinputs
            handle.seek(0)
            json.dump(edit, handle, indent=4)
            handle.truncate()
    except Exception as e:
        print("Error Updating, {}".format(e))

def info(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    else:
        os.system("printf '\033[8;30;100t'")
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Info")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Info\x07")
    print (colored("  _____       _     _   _______          _ ____            ",menu1))
    print (colored(" |  __ \     (_)   | | |__   __|        | |  _ \           ",menu1))
    print (colored(" | |__) |__ _ _  __| |    | | ___   ___ | | |_) | _____  __",menu1))
    print (colored(" |  _  // _` | |/ _` |    | |/ _ \ / _ \| |  _ < / _ \ \/ /",menu1))
    print (colored(" | | \ \ (_| | | (_| |    | | (_) | (_) | | |_) | (_) >  < ",menu1))
    print (colored(" |_|  \_\__,_|_|\__,_|    |_|\___/ \___/|_|____/ \___/_/\_\ ",menu1))
    print (colored("------------------------------------------------------------",menu1))
    print (colored("Copyright (c) 2019, DeadBread",menu1))
    print (colored("                                                            ",menu1))
    print (colored("https://github.com/DeadBread76/Raid-Toolbox",menu2))
    print (colored("Discord: https://discord.gg/JtvphCQ\nTelegram: https://t.me/DeadBakery",menu2))
    print (colored("                                                            ",menu1))
    if singlefile == True:
        print (colored("SINGLE FILE MODE ACTIVE",menu2))
    if noguimode == 1:
        print (colored("Termux Mode.",menu2))
    print (colored("Raid ToolBox version: "+rtbversion,menu2))
    print (colored("Server Smasher version: "+smversion,menu2))
    print (colored("Discord.py version: "+ discord.__version__,menu2))
    if verbose == 1:
        print(colored("\nStartup Time: {}".format(t1-t0),menu2))
    print (colored("                                                            ",menu1))
    print (colored("------------------------------------------------------------",menu1))
    print (colored("Type 'update' to update Raid ToolBox to the latest version.",menu2))
    print (colored("Type 'reinstall' to reinstall or update requirements",menu2))
    print (colored("Type 'diag' for diagnostics log.",menu2))
    print (colored("Type 'yt' for my YouTube channel.",menu2))
    print (colored("Type 'console' to access console.",menu2))
    print (colored("------------------------------------------------------------",menu1))
    inf = input(colored(">",menu2))
    if inf.lower() == "ree":
        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','ree',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme)])
        currentattacks["GOD Started at: {}".format(datetime.datetime.now().time())] = p.pid
    elif inf.lower() == 'yt':
        clear()
        webbrowser.open("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
        print("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
        input()
        info(currentattacks)
    elif inf.lower() == 'reinstall':
        if sys.platform.startswith('darwin'):
            requirements = open("requirements_mac.txt").read().splitlines()
        elif "com.termux" in sys.executable:
            requirements = open("requirements_termux.txt").read().splitlines()
        else:
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
        else:
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
                elif com == 'os.remove("characters/monika.chr")': # fuck i'm such a weeb
                    text = []
                    list = ['¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ĩ', 'ĩ', 'Ī', 'ī', 'Ĭ', 'ĭ', 'Į', 'į', 'İ', 'ı', 'Ĳ', 'ĳ', 'Ĵ', 'ĵ', 'Ķ', 'ķ', 'ĸ', 'Ĺ', 'ĺ', 'Ļ', 'ļ', 'Ľ', 'ľ', 'Ŀ', 'ŀ', 'Ł', 'ł', 'Ń', 'ń', 'Ņ', 'ņ', 'Ň', 'ň', 'ŉ', 'Ŋ', 'ŋ', 'Ō', 'ō', 'Ŏ', 'ŏ', 'Ő', 'ő', 'Œ', 'œ', 'Ŕ', 'ŕ', 'Ŗ', 'ŗ', 'Ř', 'ř', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş', 'Š', 'š', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ũ', 'ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'ů', 'Ű', 'ű', 'Ų', 'ų', 'Ŵ', 'ŵ', 'Ŷ', 'ŷ', 'Ÿ', 'Ź', 'ź', 'Ż', 'ż', 'Ž', 'ž']
                    for x in range(random.randint(500,800)):
                        text.append(random.choice(list))
                    print("Unable to delete file: characters/monika.chr")
                    time.sleep(0.5)
                    for char in text:
                        time.sleep(0.005)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    clear()
                    print('0. Back')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    for char in 'os.remove("characters/sayori.chr")':
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('\nsayori.chr deleted successfully')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    time.sleep(1)
                    for char in 'os.remove("characters/yuri.chr")':
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('\nyuri.chr deleted successfully')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    time.sleep(1)
                    for char in 'os.remove("characters/natsuki.chr")':
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('\nnatsuki.chr deleted successfully')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    time.sleep(1)
                    for char in 'os.remove("RTB.py")':
                        time.sleep(0.10)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    os.rename("RTB.py", "RTBFiles/RTB.py")
                    print('\nRTB.py deleted successfully')
                    time.sleep(1)
                    while True:
                        print(asciigen(4000))
                exec(com)
            except Exception as e:
                print(e)
    main(currentattacks)

def quickcheck(currentattacks):
    clear()
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','quickcheck',sys.executable,str(cliinputs),str(threadcount),str(attacks_theme),token])
        time.sleep(0.07)
    p.wait()
    input("Checking complete.")
    main(currentattacks)

def tokenmanager(currentattacks):
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Manager")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Token Manager\x07")
    tokenlist = open("tokens.txt").read().splitlines()
    print(colored("====================",menu1))
    print(colored("     Token Menu     ",menu1))
    print(colored("====================",menu1))
    print(colored("0. Return to main menu",menu2))
    print(colored("1. Add Token",menu2))
    print(colored("2. View Tokens",menu2))
    print(colored("3. View Token names and ID",menu2))
    print(colored("4. Token Checker",menu2))
    print(colored("5. Refresh Token list",menu2))
    print(colored("====================",menu1))
    e = input("Choice: ")
    try:
        if int(e) == 0:
            main(currentattacks)
        elif int(e) == 1:
            clear()
            print(colored("Input Token to add to tokens.txt\n0. Back",menu2))
            t = input()
            with open ("tokens.txt","a",errors='ignore') as handle:
                handle.write("{}\n".format(t))
            print (colored("Added {} to file.".format(t.rstrip()),menu1))
            input()
            tokenmanager(currentattacks)
        elif int(e) == 2:
            clear()
            if len(tokenlist) > 30:
                leng = 30
                leng += len(tokenlist)
                if sys.platform.startswith('win32'):
                    os.system('mode con:cols=100 lines={}'.format(leng))
                else:
                    os.system("printf '\033[8;{};100t'".format(leng))
            for token in tokenlist:
                print(colored(token,menu2))
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
                else:
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
                print (colored(x,menu2))
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
        else:
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
            else:
                sys.stdout.write("\x1b]2;{}\x07".format(asciigen(random.randint(1,21))))
        except Exception:
            if sys.platform.startswith('win32'):
                os.system('mode con:cols=100 lines=30')
            else:
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

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

if __name__ == "__main__":
    if sys.platform.startswith('win32'):
        if cliinputs == 1:
            t = threading.Thread(name='Title Update', target=titleupdate)
            t.start()
    main(currentattacks)
