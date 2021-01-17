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
    endpointname = config['endpointname']
    if endpointname == "stable":
        endpoint = ""
    else:
        endpoint = endpointname "."
    tokenlist = open("./tokens/"+token_list).read().splitlines()
    executor = ThreadPoolExecutor(max_workers=int(threadcount))


def ping(token,channel,server):
    headers = {'Authorization': token, 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    if channel == 'all':
        chanjson = requests.get("https://"+endpoint+"discord.com/api/v8/guilds/{}/channels".format(server),headers=headers).text
        channellist = json.loads(chanjson)
        while True:
            for channel in channellist:
                payload = {"content": "@everyone", "tts": "false"}
                if not channel['type'] == 0:
                    continue
                else:
                    src = requests.post("https://"+endpoint+"discord.com/api/v8/channels/{}/messages".format(channel['id']), headers=headers, json=payload)
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
                        requests.delete("https://"+endpoint+"discord.com/api/v8/channels/{}/messages/{}".format(channel['id'], jsone['id']), headers=headers)
    else:
        while True:
            payload = {"content": "@everyone", "tts": "false"}
            src = requests.post("https://"+endpoint+"discord.com/api/v8/channels/{}/messages".format(channel), headers=headers, json=payload)
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
                requests.delete("https://"+endpoint+"discord.com/api/v8/channels/{}/messages/{}".format(channel, jsone['id']), headers=headers)


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
