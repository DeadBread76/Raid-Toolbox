#!/usr/bin/env python3
# Ghost Ping Spammer (Example Plugin)
# Author: DeadBread76 - https://github.com/DeadBread76/
# August 6th, 2019
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
#
#
#
# Quick little Documentation
# Open Config To load Token File, skin, etc.:
#
# with open('./config.json', 'r') as handle:
#     config = json.load(handle)
#     token_list = config['token_list']
#
# Load Attack manager dict:
#
# sys.path.append('..')
# import RTBFiles.attack_dict
#
# Write to attack manager dict:
# RTBFiles.attack_dict.currentattacks["Example"] = p.pid
#
#
# Please refer to this code as an example on making your own plugin.

import sys
import ast
import json
import time
import requests
from concurrent.futures import ThreadPoolExecutor
if not sys.platform.startswith('darwin'):
    import PySimpleGUI as sg
else:
    import PySimpleGUIQt as sg

theme = ast.literal_eval(sys.argv[1])
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

with open('./config.json', 'r') as handle:
    config = json.load(handle)
    token_list = config['token_list']
    threadcount = config['thread_count']
    tokenlist = open("./tokens/"+token_list).read().splitlines()
    executor = ThreadPoolExecutor(max_workers=int(threadcount))


def ping(token,channel,server):
    headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if channel == 'all':
        chanjson = requests.get("https://canary.discordapp.com/api/v6/guilds/{}/channels".format(server),headers=headers).text
        channellist = json.loads(chanjson)
        while True:
            for channel in channellist:
                payload = {"content": "@everyone", "tts": "false"}
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
                        jsone = json.loads(src.content)
                        requests.delete("https://canary.discordapp.com/api/v6/channels/{}/messages/{}".format(channel['id'], jsone['id']), headers=headers)
    else:
        while True:
            payload = {"content": "@everyone", "tts": "false"}
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
                jsone = json.loads(src.content)
                requests.delete("https://canary.discordapp.com/api/v6/channels/{}/messages/{}".format(channel, jsone['id']), headers=headers)


layout = [
        [sg.Text('Ghost Ping Spammer Example Plugin')],
        [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all')],
        [sg.Text('Server ID', size=(15, 1)), sg.InputText()],
        [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
window = sg.Window('RTB | Ghost Ping Spammer', layout, keep_on_top=True)
event, values = window.Read()
window.Close()
if event == "Start":
    channelid = values[0]
    SERVER = values[1]
else:
    sys.exit()

for token in tokenlist:
    executor.submit(ping,token, channelid, SERVER)
