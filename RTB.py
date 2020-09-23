#!/usr/bin/env python3
# Raid Toolbox
# Author: DeadBread76 - https://github.com/DeadBread76/
# February 23rd, 2019 - Yikes
#
# Copyright 2019, DeadBread
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


rtbversion = "1.2.5"

# Load Config
try:
    import sys
    import json
    with open('config.json', 'r') as handle:
        config = json.load(handle)
        skin = config['skin']
        token_list = config['token_list']
        thread_count = config['thread_count']
        use_proxies = config['use_proxies']
        proxy_type = config['proxy_type']
        proxy_list = config['proxy_list']
        proxy_auth = config['proxy_auth']
        proxy_user = config['proxy_user']
        proxy_pass = config['proxy_pass']
        disable_theme_music = config['disable_theme_music']
        verbose = config['verbose']
        command_line_mode = config['command_line_mode']
        no_tk_mode = config['no_tk_mode']
        disable_cloudflare_check = config['disable_cloudflare_check']
        disable_update_check = config['disable_update_check']
        combine_uverified_and_verified = config['combine_uverified_and_verified']
        server_smasher_in_main_window = config['server_smasher_in_main_window']
        ignore_ffmpeg_missing = config['ignore_ffmpeg_missing']
        show_licence = config['show_licence']

except Exception:
    # TRY to fix itself
    print("Unable to read config file.\nImporting necessary modules and checking installation...")
    import os
    import sys
    import urllib.request
    import subprocess
    if not os.path.exists("RTBFiles/"):
        print("RTBFiles Directory not found.")
    print("Downloading config.json...")
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/config.json')
    data = response.read()
    data = data.decode('utf-8')
    with open("config.json","w+") as handle:
        handle.write(data)
    print("Downloading requirements.txt...")
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/requirements.txt')
    data = response.read()
    data = data.decode('utf-8')
    with open("requirements.txt","w+") as handle:
        handle.write(data)
    print("Downloading DeadRed.py...")
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/themes/DeadRed.py')
    data = response.read()
    data = data.decode('utf-8')
    try:
        os.mkdir("themes")
    except Exception:
        pass
    with open("themes/DeadRed.py","w+") as handle:
        handle.write(data)
    print("Downloading attack_dict.py...")
    response = urllib.request.urlopen('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/RTBFiles/attack_dict.py')
    data = response.read()
    data = data.decode('utf-8')
    try:
        os.mkdir("RTBFiles")
    except Exception:
        pass
    with open("RTBFiles/attack_dict.py","w+") as handle:
        handle.write(data)
    try:
        with open('config.json', 'r') as handle:
            config = json.load(handle)
            skin = config['skin']
            token_list = config['token_list']
            thread_count = config['thread_count']
            disable_theme_music = config['disable_theme_music']
            verbose = config['verbose']
            command_line_mode = config['command_line_mode']
            no_tk_mode = config['no_tk_mode']
            disable_cloudflare_check = config['disable_cloudflare_check']
            disable_update_check = config['disable_update_check']
            combine_uverified_and_verified = config['combine_uverified_and_verified']
            server_smasher_in_main_window = config['server_smasher_in_main_window']
            ignore_ffmpeg_missing = config['ignore_ffmpeg_missing']
            show_licence = config['show_licence']
    except Exception:
        print("Unable to start.")
        input()
        sys.exit()
    if sys.platform.startswith('win32'):
        try:
            import pip
        except Exception as e:
            print("Hmmm, pip doesn't seem to be installed.\nDownload errorfixer script?")
            x = input("(Y/N): ")
            if x.lower() == "y":
                response = urllib.request.urlopen('https://raw.githubusercontent.com/Mattlau04/RTB-error-fixer/master/Errorfixer.bat')
                data = response.read()
                data = data.decode('utf-8')
                with open("Errorfixer.bat","w+") as handle:
                    handle.write(data)
                er = subprocess.Popen(["Errorfixer.bat"])
                er.wait()
                sys.exit()
    requirements = open("requirements.txt").read().splitlines()
    log = open("install.log", "w")
    for package in requirements:
        print("Attempting to install {}".format(package))
        p = subprocess.call([sys.executable, "-m", "pip", "install", package, "--user", "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
        if p == 1:
            print("There was an error with installing the package {}, Refer to Install.log".format(package))
        elif p == 0:
            print("Installed {} Successfully.".format(package))

# Check for no_gui flag on command line
if len(sys.argv) > 1:
    if sys.argv[1] == "disable_all_gui":
        command_line_mode = 1
        no_tk_mode = 1
        with open('config.json', 'r+') as handle:
            edit = json.load(handle)
            edit['command_line_mode'] = command_line_mode
            edit['no_tk_mode'] = no_tk_mode
            handle.seek(0)
            json.dump(edit, handle, indent=4)
            handle.truncate()
        print("Option acknowledged, Saved to config.")
    elif sys.argv[1] == "no_gui":
        no_tk_mode = 1
        with open('config.json', 'r+') as handle:
            edit = json.load(handle)
            edit['no_tk_mode'] = no_tk_mode
            handle.seek(0)
            json.dump(edit, handle, indent=4)
            handle.truncate()
        print("Option acknowledged, Saved to config.")
    elif sys.argv[1] == "command_line":
        command_line_mode = 1
        with open('config.json', 'r+') as handle:
            edit = json.load(handle)
            edit['command_line_mode'] = command_line_mode
            handle.seek(0)
            json.dump(edit, handle, indent=4)
            handle.truncate()
        print("Option acknowledged, Saved to config.")

# Enable Command line mode for no_tk_mode
if no_tk_mode == 1:
    server_smasher_in_main_window = 1
    command_line_mode = 1

# Load System Modules
import os, time, ctypes, random, base64, datetime, platform, shutil, subprocess, threading, webbrowser, importlib, traceback
from distutils.dir_util import copy_tree
if sys.platform.startswith('win32'):
    from subprocess import CREATE_NEW_CONSOLE
if sys.platform.startswith('win32'):
    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading...")
else:
    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading...\x07")

# Import Dictionary Module
import RTBFiles.attack_dict
currentattacks = RTBFiles.attack_dict.currentattacks  # Dict for attacks (Shared with plugins)

t0 = time.time()  # Startup Time Counter thanks to https://github.com/Mattlau04

# Load PySimpleGUI
if command_line_mode == 0:
    try:
        if not sys.platform.startswith('darwin'):
            import PySimpleGUI as sg
        else:
            import PySimpleGUIQt as sg
    except Exception:
        print("PySimpleGUI Is not installed.")
        if sys.platform.startswith('darwin'):
            log = open("install.log", "w")
            p = subprocess.call([sys.executable, "-m", "pip", "install", "PySimpleGUIQt", "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
            if p == 1:
                print("There was an error with installing the package PySimpleGUIQt, Refer to Install.log")
            elif p == 0:
                print("Installed PySimpleGUIQt Successfully.")
            p = subprocess.call([sys.executable, "-m", "pip", "install", "PySide2", "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
            if p == 1:
                print("There was an error with installing the package PySide2, Refer to Install.log")
            elif p == 0:
                print("Installed PySide2 Successfully.")
            input("Press Enter To Exit.")
            sys.exit()
        else:
            log = open("install.log", "w")
            p = subprocess.call([sys.executable, "-m", "pip", "install", "PySimpleGUI", "--user", "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
            if p == 1:
                print("There was an error with installing the package PySimpleGUI, Refer to Install.log")
            elif p == 0:
                print("Installed PySimpleGUI Successfully.")
            input("Press Enter To Exit.")
            sys.exit()

# Load Skin
if not skin == "DeadRed":
    # Import Default Incase loaded skin has Missing Features/ Compatibility for older skins.
    mdl = importlib.import_module("themes.DeadRed")
    if "__all__" in mdl.__dict__:
        names = mdl.__dict__["__all__"]
    else:
        names = [x for x in mdl.__dict__ if not x.startswith("_")]
    globals().update({k: getattr(mdl, k) for k in names})

# Import New Skin
try:
    mdl = importlib.import_module("themes.{}".format(skin))
    if "__all__" in mdl.__dict__:
        names = mdl.__dict__["__all__"]
    else:
        names = [x for x in mdl.__dict__ if not x.startswith("_")]
    globals().update({k: getattr(mdl, k) for k in names})
except Exception as e:
    print("LAST USED THEME MISSING: {}".format(e))
    with open('config.json', 'r+') as handle:
        edit = json.load(handle)
        edit['skin'] = "DeadRed"
        handle.seek(0)
        json.dump(edit, handle, indent=4)
        handle.truncate()

# Create Icon Image
with open("RTBFiles/rtb_icon.png", "wb") as f:
    f.write(base64.b64decode(rtb_icon))

colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
if menu1.lower() == 'random':
    menu1 = random.choice(colours)
if menu2.lower() == 'random':
    menu2 = random.choice(colours)
if not command_line_mode == 1:
    if use_preset_theme:
        sg.ChangeLookAndFeel(preset_window_theme)
    elif use_preset_theme is False:
        sg.SetOptions(background_color=background_color,
                     text_element_background_color=text_element_background_color,
                     element_background_color=element_background_color,
                     scrollbar_color=scrollbar_color,
                     input_elements_background_color=input_elements_background_color,
                     input_text_color=input_text_color,
                     button_color=button_color,
                     text_color=text_color)

#Splash Screen
if __name__ == "__main__":
    if not command_line_mode == 1:
        layout = [
            [sg.Image(data=rtb_splash, pad=((0, 0), 0))]
        ]
        if sys.platform.startswith("darwin"):
            window = sg.Window("DeadBread's Raid ToolBox v{} | Loading...".format(rtbversion), icon=rtb_icon, no_titlebar=True, grab_anywhere=True).Layout(layout)
        else:
            window = sg.Window("DeadBread's Raid ToolBox v{} | Loading...".format(rtbversion), icon=rtb_icon, no_titlebar=True, grab_anywhere=True, margins=(0,0)).Layout(layout)
        window.Read(timeout=0)

# Clear() Function setting
if sys.platform.startswith('win32'):
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

# Find Plugins (GUI)
if not command_line_mode == 1:
    try:
        from pluginbase import PluginBase
    except Exception:
        log = open("install.log", "w")
        sg.PopupNonBlocking("pluginbase not installed.\nAttempting to install now.", title="Missing Module.")
        p = subprocess.call([sys.executable, "-m", "pip", "install", "pluginbase", "--user", "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
        if p == 1:
            sg.Popup("Unable to install Pluginbase, Refer to install.log for the error.")
            sys.exit()
        elif p == 0:
            sg.Popup("Installed pluginbase Successfully.")
    plugin_base = PluginBase(package='RTBFiles.plugins')
    plugin_source = plugin_base.make_plugin_source(
        searchpath=['plugins'])

# Termux Load
if "com.termux" in sys.executable:
    print("Termux Detected.")
    no_tk_mode = 1
    o = os.system('termux-vibrate -d 500 -f')
    if not o == 0:
        log = open("install.log", "w")
        print("Installing Termux API..")
        p = subprocess.call(['pkg', 'install', 'termux-api'], stdout=log, stderr=subprocess.STDOUT)
        if p == 1:
            print("There was an error with installing termux API, Refer to Install.log")
            sys.exit()
        elif p == 0:
            print("Installed Termux API Successfully.")
    os.system('termux-toast -b black -c red Welcome to Raid Toolbox, Termux User!')
    try:
        import requests
        import animation
        import cpuinfo
        import psutil
        import emoji
        from colorama import init
        from termcolor import colored
    except Exception as i:
        print ("Module error: " + str(i))
        install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
        if install.lower() == 'y':
            requirements = open("requirements_termux.txt").read().splitlines()
            log = open("install.log", "w")
            for package in requirements:
                print("Attempting to install {}".format(package))
                p = subprocess.call([sys.executable, "-m", "pip", "install", package, "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
                if p == 1:
                    print("There was an error with installing the package {}, Refer to Install.log".format(package))
                elif p == 0:
                    print("Installed {} Successfully.".format(package))
            print("Please Restart Raid Toolbox.")
            input()
            sys.exit()
        else:
            sys.exit()

# Verbose Load
elif verbose == 1:
    print ("Loading modules...")
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox is loading... | Verbose Mode")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox is loading... | Verbose Mode\x07")
    with open ("load.log", "a") as handle:
        try:
            print ("Loading requests...")
            import requests
            print ("Loaded requests")
            handle.write("Loaded requests\n")
        except Exception as i:
            print ("Error Loading requests")
            handle.write("Error Loading requests\n")
        try:
            print ("Loading animation...")
            import animation
            print ("Loaded animation")
            handle.write("Loaded animation\n")
        except Exception as i:
            print ("Error Loading animation")
            handle.write("Error Loading animation\n")
        try:
            print ("Loading cpuinfo...")
            import cpuinfo
            print ("Loaded cpuinfo")
            handle.write("Loaded cpuinfo\n")
        except Exception as i:
            print ("Error Loading cpuinfo")
            handle.write("Error Loading cpuinfo\n")
        try:
            print ("Loading psutil...")
            import psutil
            print ("Loaded psutil")
            handle.write("Loaded psutil\n")
        except Exception as i:
            print ("Error Loading psutil")
            handle.write("Error Loading psutil\n")
        try:
            print ("Loading emoji...")
            import emoji
            print ("Loaded emoji")
            handle.write("Loaded emoji\n")
        except Exception as i:
            print ("Error Loading emoji")
            handle.write("Error Loading emoji\n")
        try:
            print ("Loading pyperclip...")
            import pyperclip
            print ("Loaded pyperclip")
            handle.write("Loaded pyperclip\n")
        except Exception as i:
            print ("Error Loading pyperclip")
            handle.write("Error Loading pyperclip\n")
        try:
            print ("Loading playsound...")
            import playsound
            print ("Loaded playsound")
            handle.write("Loaded playsound\n")
        except Exception as i:
            print ("Error Loading playsound")
            handle.write("Error Loading playsound\n")
        try:
            print ("Loading selenium...")
            from selenium import webdriver
            print ("Loaded selenium")
            handle.write("Loaded selenium\n")
        except Exception as i:
            print ("Error Loading selenium")
            handle.write("Error Loading selenium\n")
        try:
            print ("Loading colorama...")
            from colorama import init
            print ("Loaded colorama")
            handle.write("Loaded colorama\n")
        except Exception as i:
            print ("Error Loading colorama")
            handle.write("Error Loading colorama\n")
        try:
            print ("Loading termcolor...")
            from termcolor import colored
            print ("Loaded termcolor")
            handle.write("Loaded termcolor\n")
        except Exception as i:
            print ("Error Loading termcolor")
            handle.write("Error Loading termcolor\n")
    print("Finished Loading modules")

# Normal Load
else:
    try:
        import requests
        import animation
        import cpuinfo
        import psutil
        import emoji
        import pyperclip
        import playsound
        from selenium import webdriver
        from colorama import init
        from termcolor import colored
    except Exception as i:
        try:
            window.Close()
        except Exception:
            pass
        print ("Module error: " + str(i))
        install = input ("Would you like Raid ToolBox to try and install it for you?(Y/N)")
        if install.lower() == 'y':
            if sys.platform.startswith('win32'):
                try:
                    import pip
                except Exception as e:
                    print("Hmmm, pip doesn't seem to be installed.\nDownload errorfixer script?")
                    x = input("(Y/N): ")
                    if x.lower() == "y":
                        response = urllib.request.urlopen('https://raw.githubusercontent.com/Mattlau04/RTB-error-fixer/master/Errorfixer.bat')
                        data = response.read()
                        data = data.decode('utf-8')
                        with open("Errorfixer.bat","w+") as handle:
                            handle.write(data)
                        er = subprocess.Popen(["Errorfixer.bat"])
                        er.wait()
                        sys.exit()
            if sys.platform.startswith('darwin'):
                requirements = open("requirements_mac.txt").read().splitlines()
            else:
                requirements = open("requirements.txt").read().splitlines()
            log = open("install.log", "w")
            for package in requirements:
                print("Attempting to install {}".format(package))
                p = subprocess.call([sys.executable, "-m", "pip", "install", package, "--user", "--upgrade"],stdout=log, stderr=subprocess.STDOUT)
                if p == 1:
                    print("There was an error with installing the package {}, Refer to Install.log".format(package))
                elif p == 0:
                    print("Installed {} Successfully.".format(package))
            print("Please Restart Raid Toolbox.")
            if sys.platform.startswith('win32'):
                clear()
                os.system('cmd /C RTB.py')
                sys.exit()
            else:
                clear()
                os.system('python3 RTB.py')
                sys.exit()
        else:
            sys.exit()
init()

# File Downloader (Updates, Etc.)
def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return local_filename
if __name__ == "__main__":
    # Check For Updates
    if disable_update_check == 1:
        pass
    else:
        if "b" in rtbversion:
            pass
        else:
            try:
                if verbose == 1:
                    print("Checking for updates...")
                vercheck = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/version").text.rstrip().split("|")
                versionno = vercheck[0].split(".")
                myversion = rtbversion.split(".")
                if versionno[0] > myversion[0]:
                    update = True
                elif versionno[1] > myversion[1]:
                    update = True
                elif versionno[2] > myversion[2]:
                    update = True
                else:
                    update = False
                if update:
                    if command_line_mode == 1:
                        print(colored("There is an update for RTB, Download update?", menu1))
                        verchoice = input("(Y/N): ")
                        if verchoice.lower() == "y":
                            @animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menu1))
                            def run_update():
                                if sys.platform.startswith('win32'):
                                    ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
                                else:
                                    sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
                                update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
                                clear()
                                print(colored("Update has been downloaded, Installing...",menu1))
                                return update
                            update = run_update()
                            with open("update.zip", "wb") as handle:
                                handle.write(update.content)
                            try:
                                shutil.copy("RTBFiles/smconfig.py", "RTBFiles/smconfig_old.py")
                            except Exception:
                                pass
                            try:
                                shutil.unpack_archive("update.zip")
                                copy_tree("Raid-Toolbox-master/", ".")
                                os.remove("update.zip")
                                shutil.rmtree("Raid-Toolbox-master/")
                                print ("Update complete, exiting.")
                                with open('config.json', 'r+') as handle:
                                    edit = json.load(handle)
                                    edit['skin'] = skin
                                    edit['token_list'] = token_list
                                    edit['thread_count'] = thread_count
                                    edit['verbose'] = verbose
                                    edit['disable_theme_music'] = disable_theme_music
                                    edit['command_line_mode'] = command_line_mode
                                    edit['no_tk_mode'] = no_tk_mode
                                    edit['disable_cloudflare_check'] = disable_cloudflare_check
                                    edit['disable_update_check'] = disable_update_check
                                    edit['server_smasher_in_main_window'] = server_smasher_in_main_window
                                    edit['ignore_ffmpeg_missing'] = ignore_ffmpeg_missing
                                    edit['combine_uverified_and_verified'] = combine_uverified_and_verified
                                    edit['show_licence'] = show_licence
                                    edit['use_proxies'] = use_proxies
                                    edit['proxy_type'] = proxy_type
                                    edit['proxy_list'] = proxy_list
                                    edit['proxy_auth'] = proxy_auth
                                    edit['proxy_user'] = proxy_user
                                    edit['proxy_pass'] = proxy_pass
                                    handle.seek(0)
                                    json.dump(edit, handle, indent=4)
                                    handle.truncate()
                            except Exception as e:
                                print("Error Updating, {}".format(e))
                            time.sleep(3)
                            os.kill(os.getpid(), 15)
                    else:
                        try:
                            window.Close()
                        except Exception:
                            pass
                        verchoice = sg.PopupYesNo("There is an update for RTB, Download update?", title="Raid ToolBox Update Available")
                        if verchoice == "Yes":
                            with open('RTBFiles/ServerSmasher/ssconfig.json', 'r') as handle:
                                ssconfig = json.load(handle)
                            update = download_file('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
                            shutil.unpack_archive(update)
                            copy_tree("Raid-Toolbox-master/", ".")
                            os.remove(update)
                            shutil.rmtree("Raid-Toolbox-master/")
                            with open('config.json', 'r+') as handle:
                                edit = json.load(handle)
                                edit['skin'] = skin
                                edit['token_list'] = token_list
                                edit['thread_count'] = thread_count
                                edit['verbose'] = verbose
                                edit['disable_theme_music'] = disable_theme_music
                                edit['command_line_mode'] = command_line_mode
                                edit['no_tk_mode'] = no_tk_mode
                                edit['disable_cloudflare_check'] = disable_cloudflare_check
                                edit['disable_update_check'] = disable_update_check
                                edit['server_smasher_in_main_window'] = server_smasher_in_main_window
                                edit['ignore_ffmpeg_missing'] = ignore_ffmpeg_missing
                                edit['combine_uverified_and_verified'] = combine_uverified_and_verified
                                edit['show_licence'] = show_licence
                                edit['use_proxies'] = use_proxies
                                edit['proxy_type'] = proxy_type
                                edit['proxy_list'] = proxy_list
                                edit['proxy_auth'] = proxy_auth
                                edit['proxy_user'] = proxy_user
                                edit['proxy_pass'] = proxy_pass
                                handle.seek(0)
                                json.dump(edit, handle, indent=4)
                                handle.truncate()
                            with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
                                edit = json.load(handle)
                                edit['ss_token_list'] = ssconfig['ss_token_list']
                                edit['startup_status'] = ssconfig['startup_status']
                                edit['startup_activity_name'] = ssconfig['startup_activity_name']
                                edit['startup_activity_type'] = ssconfig['startup_activity_type']
                                edit['last_used'] = ssconfig['last_used']
                                edit['last_used_type'] = ssconfig['last_used_type']
                                edit['bots_cached'] = ssconfig['bots_cached']
                                edit['users_cached'] = ssconfig['users_cached']
                                edit['bot_token_cache'] = ssconfig['bot_token_cache']
                                edit['user_token_cache'] = ssconfig['user_token_cache']
                                handle.seek(0)
                                json.dump(edit, handle, indent=4)
                                handle.truncate()
                            print ("Update complete, exiting.")
                            os.kill(os.getpid(), 15)
            except Exception as e:
                if command_line_mode == 1:
                    print("Error Updating: {}".format(e))
                else:
                    sg.PopupError("Error Updating Raid Toolbox.\n ({})".format(e), title="Update Error")

    if not os.path.exists("RTBFiles/"):
        clear()
        singlefile = True
        if command_line_mode == 1:
            print("RTB is Running in Single File mode.\nPlease use the update function to download the complete program.")
            input(colored("Press enter to continue.",menu1))
        else:
            try:
                window.Close()
            except Exception:
                pass
            sg.PopupOK("RTB is Running in Single File mode.\nPlease use the update function to download the complete program.", title="SINGLE FILE MODE")
    else:
        singlefile = False
        if sys.platform.startswith('win32'):
            if ignore_ffmpeg_missing == 0:
                if not os.path.isfile("ffmpeg.exe"):
                    if verbose == 1:
                        print("FFmpeg is missing")
                    if command_line_mode == 1:
                        print(colored("Download FFMpeg? (Needed For Voice Chat Spammer)", menu1))
                        fmpg = input("(Y/N):")
                        if fmpg.lower() == "y":
                            clear()
                            @animation.wait(colored('Downloading FFMpeg, Please Wait ',menu1))
                            def ffmpegdownload():
                                data = requests.get("https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.1.3-win64-static.zip")
                                return data
                            data = ffmpegdownload()
                            print(colored("Download Complete.","green"))
                            with open("ffmpeg.zip", "wb") as handle:
                                handle.write(data.content)
                            shutil.unpack_archive("ffmpeg.zip")
                            time.sleep(0.5)
                            os.remove("ffmpeg.zip")
                            copy_tree("ffmpeg-4.1.3-win64-static/bin/", ".")
                            time.sleep(0.5)
                            shutil.rmtree("ffmpeg-4.1.3-win64-static")
                    else:
                        try:
                            window.Close()
                        except Exception:
                            pass
                        fmpg = sg.PopupYesNo("Download FFMpeg?\n(Needed For Voice Chat Spammer)")
                        if fmpg == "Yes":
                            sg.PopupNonBlocking('Downloading FFMpeg, Please Wait.', title="Downloading")
                            ff = download_file("https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.1.3-win64-static.zip")
                            shutil.unpack_archive(ff)
                            time.sleep(0.5)
                            os.remove(ff)
                            copy_tree("ffmpeg-4.1.3-win64-static/bin/", ".")
                            time.sleep(0.5)
                            shutil.rmtree("ffmpeg-4.1.3-win64-static")

    # Display License
    if not show_licence == 0:
        licfile = requests.get("https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/LICENSE").text
        lic = f"DeadBread's Raid Toolbox v{rtbversion}, Copyright (C) 2019, DeadBread\n"
        if command_line_mode == 1:
            print(lic+"\n"+"Please Read the licence at https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/LICENSE")
            time.sleep(5)
            input("Press Enter to continue.")
        else:
            sg.PopupScrolled(lic + "\n" + licfile, title="LICENSE", size=(60,20))
        try:
            with open('config.json', 'r+') as handle:
                edit = json.load(handle)
                edit['show_licence'] = 0
                handle.seek(0)
                json.dump(edit, handle, indent=4)
                handle.truncate()
        except Exception as e:
            print(e)


    # CloudFlare Checks
    if disable_cloudflare_check == 1:
        pass
    elif not "b" in rtbversion:
        if verbose == 1:
            print("Checking CloudFlare Status")
        try:
            cloudflarecheck = requests.get("https://canary.discordapp.com/api/v6/invite/DEADBREAD")
        except Exception as e:
            print(e)
        else:
            try:
                json.loads(cloudflarecheck.content)
            except Exception:
                if command_line_mode == 1:
                    print("Your IP is CloudFlare Banned.\nThis means you can't use the Joiner or the Regular Checker.\nUse a VPN to get around this.")
                    input(colored("Press enter to continue.",'red'))
                else:
                    try:
                        window.Close()
                    except Exception:
                        pass
                    sg.Popup("Your IP is CloudFlare Banned.\nThis means you can't use the Joiner or the Regular Checker.\nUse a VPN to get around this.")

# Title Update Function (Command line mode on Windows)
def titleupdate():
    global currentattacks
    while True:
        for attack in list(currentattacks):
            if psutil.pid_exists(currentattacks[attack]):
                pass
            else:
                currentattacks.pop(attack)
        if "b" in rtbversion:
            if len(currentattacks) == 0:
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION)".format(rtbversion))
            elif len(currentattacks) == 1:
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION) | ({} Attack Running.)".format(rtbversion,len(currentattacks)))
            else:
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION) | ({} Attacks Running.)".format(rtbversion,len(currentattacks)))
        else:
            if len(currentattacks) == 0:
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{}".format(rtbversion))
            elif len(currentattacks) == 1:
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} | ({} Attack Running.)".format(rtbversion,len(currentattacks)))
            else:
                ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} | ({} Attacks Running.)".format(rtbversion,len(currentattacks)))
        time.sleep(2)


# Finished Loading
if not command_line_mode == 1:
    try:
        window.Close()
    except Exception:
        pass
t1 = time.time()
if verbose == 1:
    print(f'Startup time: {t1 - t0:.2f}s')
    with open("load.log","a",errors='ignore') as handle:
        handle.write(f'================================\nStartup time: {t1 - t0:.2f}s\n================================\n\n\n')
    print("Starting...")


def main():
    global currentattacks
    global skin
    global token_list
    global thread_count
    global use_proxies
    global proxy_type
    global proxy_list
    global proxy_auth
    global proxy_user
    global proxy_pass
    global verbose
    global disable_theme_music
    global command_line_mode
    global no_tk_mode
    global disable_cloudflare_check
    global disable_update_check
    global server_smasher_in_main_window
    global ignore_ffmpeg_missing
    global show_licence
    clear()
    try:
        with open("tokens/"+token_list,'r') as handle:
            line = handle.readlines()
            tcounter = len(line)
    except Exception as e:
        if command_line_mode == 0:
            sg.Popup("Unable to load token list.")
        else:
            print("Unable to load token list.")
            input()
    if sys.platform.startswith('win32'):
        if "b" in rtbversion:
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{} (TEST VERSION)".format(rtbversion))
        else:
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox v{}".format(rtbversion))
    else:
        if "b" in rtbversion:
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{} (TEST VERSION)\x07".format(rtbversion))
        else:
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox v{}\x07".format(rtbversion))
    #  _____                        __  __
    # |_   _|__ _ _ _ __ _  ___ __ |  \/  |___ _ _ _  _
    #   | |/ -_) '_| '  \ || \ \ / | |\/| / -_) ' \ || |
    #   |_|\___|_| |_|_|_\_,_/_\_\ |_|  |_\___|_||_\_,_|
    if no_tk_mode == 1:
        if sys.platform.startswith('win32'):
            os.system('mode con:cols=41 lines=35')
        else:
            os.system("printf '\033[8;35;41t'")
        print(colored("=========================================",menu1))
        print(colored("   Welcome to DeadBread's Raid Toolbox",menu2))
        print(colored("=========================================",menu1))
        print(colored("          {} tokens available.".format(tcounter),menu2))
        print(colored("=========================================",menu1))
        print(colored("0.  Exit",menu2))
        print(colored("1.  Joiner",menu2))
        print(colored("2.  Leaver",menu2))
        print(colored("3.  Group DM leaver",menu2))
        print(colored("4.  Token Checker",menu2))
        print(colored("5.  Message spammer",menu2))
        print(colored("6.  Ascii spammer",menu2))
        print(colored("7.  Mass mention spammer",menu2))
        print(colored("8.  Voice Chat Spammer",menu2))
        print(colored("9.  User DM Spammer",menu2))
        print(colored("10. Friend Request Spammer",menu2))
        print(colored("11. Group DM spammer",menu2))
        print(colored("12. Random Image Spammer",menu2))
        print(colored("13. Status Changer",menu2))
        print(colored("14. Nickname Changer",menu2))
        print(colored("15. Embed Spammer",menu2))
        print(colored("16. Avatar Changer",menu2))
        print(colored("17. Role Mass Mentioner",menu2))
        print(colored("18. Channel Message Cleaner",menu2))
        print(colored("19. HypeSquad House Changer",menu2))
        print(colored("20. Message Reaction Adder",menu2))
        print(colored("21. ServerSmasher",menu2))
        print(colored("22. View Running Attacks",menu2))
        print(colored("23. Custom attack plugins",menu2))
        print(colored("24. Quick Checker",menu2))
        print(colored("25. Token options",menu2))
        print(colored("26. Theme menu",menu2))
        print(colored("27. Settings menu",menu2))
        choice = input(colored(">",menu2))
    #   ___ _   _ ___
    #  / __| | | |_ _|
    # | (_ | |_| || |
    #  \___|\___/|___|
    elif command_line_mode == 0:
        tokenlist = open("tokens/"+token_list).read().splitlines()
        if sys.platform.startswith("darwin"):
            menu_def = [
                ['&RTB', ['&Attack Manager', 'RTB Options', ['Updater', '&Settings', '&Themes', ['Change Theme', 'Theme Repo']], 'Tools', ['Proxy Checker/Scraper', 'CPU Widget', 'CF Check'], 'About', ['Info', 'Diagnostics']]],
                ['&Tokens', ['View/Add Tokens', 'Change Token List', 'View Token List Names', 'Token Stealer Builder', 'Token Toolkit']],
                ['&Help', ['Wiki', 'My YouTube', '!Discord Server', 'Telegram']],
                ['&ServerSmasher', ['Launch GUI', 'Launch Legacy']],
                ['&Plugins', ['View Plugins', 'Plugin Repo']]
            ]
            layout =[
                [sg.Menu(menu_def)],
                [sg.Button('', image_data=rtb_banner, size=banner_size, pad=banner_padding, button_color=background_color)],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_joiner, key="Joiner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_leaver, key="Leaver"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_group_leaver, key="Group Leaver")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_token_checker, key="Checker"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_checker_v2, key="Checker V2"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_message_spammer, key="Message Spammer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_ascii_spammer, key="Ascii Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_mass_mentioner, key="Mass Mentioner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_role_mass_mentioner, key="Role Mass Mentioner")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_vc_spammer, key="VC Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_dm_spammer, key="DM Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_friend_bomber, key="Friend Bomber")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_group_spammer, key="Group Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_image_spammer, key="Image Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_status_changer, key="Status Changer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_nickname_changer, key="Nickname Changer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_embed_spammer, key="Embed Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_avatar_changer, key="Avatar Changer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_server_cleaner, key="Server Cleaner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_hypesquad_changer, key="HypeSquad Changer"),  sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_reaction_adder, key="Reaction Adder")],
            ]
            window = sg.Window("DeadBread's Raid ToolBox v{} | [{} Tokens available.]".format(rtbversion,len(tokenlist)), icon=rtb_icon).Layout(layout)
        else:
            menu_def = [
                ['&RTB', ['&Attack Manager', '&Options', ['Updater', '&Settings', '&Themes', ['Change Theme', 'Theme Repo']], 'Tools', ['Proxy Checker/Scraper', 'CPU Widget', 'CF Check'], 'About', ['Info', 'Diagnostics']]],
                ['&Tokens', ['View/Add Tokens', 'Change Token List', 'View Token List Names', 'Token Stealer Builder', 'Token Toolkit']],
                ['&Help', ['Wiki', 'My YouTube', '!Discord Server', 'Telegram']],
                ['&ServerSmasher', ['Launch GUI', 'Launch Legacy']],
                ['&Plugins', ['View Plugins', 'Plugin Repo']]
            ]
            layout =[
                [sg.Menu(menu_def)],
                [sg.Image(data=rtb_banner, size=banner_size, pad=banner_padding)],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_joiner, key="Joiner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_leaver, key="Leaver"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_group_leaver, key="Group Leaver")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_token_checker, key="Checker"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_checker_v2, key="Checker V2"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_message_spammer, key="Message Spammer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_ascii_spammer, key="Ascii Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_mass_mentioner, key="Mass Mentioner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_role_mass_mentioner, key="Role Mass Mentioner")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_vc_spammer, key="VC Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_dm_spammer, key="DM Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_friend_bomber, key="Friend Bomber")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_group_spammer, key="Group Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_image_spammer, key="Image Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_status_changer, key="Status Changer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_nickname_changer, key="Nickname Changer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_embed_spammer, key="Embed Spammer"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_avatar_changer, key="Avatar Changer")],
                [sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_server_cleaner, key="Server Cleaner"), sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_hypesquad_changer, key="HypeSquad Changer"),  sg.Button('', button_color=(button_colour,button_colour), border_width=0, image_data=button_reaction_adder, key="Reaction Adder")],
            ]
            window = sg.Window("DeadBread's Raid ToolBox v{} | [{} Tokens available.]".format(rtbversion,len(tokenlist)), icon=rtb_icon, transparent_color=transparent_colour).Layout(layout)
        while True:
            event, values = window.Read(timeout=100)
            if event is None:
                sys.exit()
            elif event == sg.TIMEOUT_KEY:
                tokenlist = open("tokens/"+token_list).read().splitlines()
                for attack in list(currentattacks):
                    if psutil.pid_exists(currentattacks[attack]):
                        if not sys.platform.startswith('win32'):
                            proc = psutil.Process(currentattacks[attack])
                            if proc.status() == psutil.STATUS_ZOMBIE:
                                currentattacks.pop(attack)
                                continue
                    else:
                        currentattacks.pop(attack)
                if not sys.platform.startswith('darwin'):
                    if len(currentattacks) == 0:
                         window.TKroot.title("DeadBread's Raid ToolBox v{} | [{} Tokens available.]".format(rtbversion,len(tokenlist)))
                    elif len(currentattacks) == 1:
                         window.TKroot.title("DeadBread's Raid ToolBox v{} | [{} Tokens available.] | [{} Attack Running.]".format(rtbversion,len(tokenlist),len(currentattacks)))
                    else:
                         window.TKroot.title("DeadBread's Raid ToolBox v{} | [{} Tokens available.] | [{} Attacks Running.]".format(rtbversion,len(tokenlist),len(currentattacks)))
            #    _  _   _           _     __  __
            #   /_\| |_| |_ __ _ __| |__ |  \/  |__ _ _ _  __ _ __ _ ___ _ _
            #  / _ \  _|  _/ _` / _| / / | |\/| / _` | ' \/ _` / _` / -_) '_|
            # /_/ \_\__|\__\__,_\__|_\_\ |_|  |_\__,_|_||_\__,_\__, \___|_|
            #                                                  |___/
            elif event == "Attack Manager":
                window.Close()
                for attack in list(currentattacks):
                    if psutil.pid_exists(currentattacks[attack]):
                        if not sys.platform.startswith('win32'):
                            proc = psutil.Process(currentattacks[attack])
                            if proc.status() == psutil.STATUS_ZOMBIE:
                                currentattacks.pop(attack)
                                continue
                    else:
                        currentattacks.pop(attack)
                layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                for attack in list(currentattacks.keys()):
                    layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                if not currentattacks == {}:
                    if not len(currentattacks) == 1:
                        layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                else:
                    layout.append([sg.Button("No Attacks Running",size=(60,1))])
                window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
                c = 0
                while True:
                    event, values = window.Read(timeout=10)
                    if event is None:
                        window.Close()
                        main()
                    elif event == "No Attacks Running":
                        c += 1
                        if c == 17:
                            freeze = requests.get("https://gist.githubusercontent.com/DeadBread76/e03d526b8b097ab5f4bae27de3a03b78/raw/bf68293122f1d7805acf8907a3c43ebc338fdf3e/freeze.txt")
                            so = base64.b64decode(freeze.text)
                            with open ("RTBFiles/Now Freeze.mp3", "wb") as handle:
                                handle.write(so)
                            playsound.playsound('RTBFiles/Now Freeze.mp3', block=False)
                            sg.PopupNonBlocking("Now, everything will freeze.", title="FreEeEeEeEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEZe", keep_on_top=True)
                    elif event == sg.TIMEOUT_KEY:
                        for attack in list(currentattacks):
                            if psutil.pid_exists(currentattacks[attack]):
                                if not sys.platform.startswith('win32'):
                                    proc = psutil.Process(currentattacks[attack])
                                    if proc.status() == psutil.STATUS_ZOMBIE:
                                        currentattacks.pop(attack)
                                        layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                                        for attack in list(currentattacks.keys()):
                                            layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                                        if not currentattacks == {}:
                                            if not len(currentattacks) == 1:
                                                layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                                        else:
                                            layout.append([sg.Button("No Attacks Running",size=(60,1))])
                                        window.Close()
                                        window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
                            else:
                                currentattacks.pop(attack)
                                layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                                for attack in list(currentattacks.keys()):
                                    layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                                if not currentattacks == {}:
                                    if not len(currentattacks) == 1:
                                        layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                                else:
                                    layout.append([sg.Button("No Attacks Running",size=(60,1))])
                                window.Close()
                                window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
                    elif event == "Stop All":
                        for attack in currentattacks:
                            try:
                                os.kill(int(currentattacks[attack]), 9)
                            except Exception:
                                pass
                        for attack in list(currentattacks):
                            if psutil.pid_exists(currentattacks[attack]):
                                if not sys.platform.startswith('win32'):
                                    proc = psutil.Process(currentattacks[attack])
                                    if proc.status() == psutil.STATUS_ZOMBIE:
                                        currentattacks.pop(attack)
                                        layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                                        for attack in list(currentattacks.keys()):
                                            layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                                        if not currentattacks == {}:
                                            if not len(currentattacks) == 1:
                                                layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                                        else:
                                            layout.append([sg.Button("No Attacks Running",size=(60,1))])
                                        window.Close()
                                        window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
                            else:
                                currentattacks.pop(attack)
                                layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                                for attack in list(currentattacks.keys()):
                                    layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                                if not currentattacks == {}:
                                    if not len(currentattacks) == 1:
                                        layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                                else:
                                    layout.append([sg.Button("No Attacks Running",size=(60,1))])
                                window.Close()
                                window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
                    elif event in currentattacks:
                        try:
                            os.kill(int(currentattacks[event]), 9)
                        except Exception as e:
                            print(e)
                        for attack in list(currentattacks):
                            if psutil.pid_exists(currentattacks[attack]):
                                if not sys.platform.startswith('win32'):
                                    proc = psutil.Process(currentattacks[attack])
                                    if proc.status() == psutil.STATUS_ZOMBIE:
                                        currentattacks.pop(attack)
                                        layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                                        for attack in list(currentattacks.keys()):
                                            layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                                        if not currentattacks == {}:
                                            if not len(currentattacks) == 1:
                                                layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                                        else:
                                            layout.append([sg.Button("No Attacks Running",size=(60,1))])
                                        window.Close()
                                        window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
                            else:
                                currentattacks.pop(attack)
                                layout = [[sg.Text("Running Attacks: {}".format(len(currentattacks)))]]
                                for attack in list(currentattacks.keys()):
                                    layout.append([sg.Text(attack,size=(50,1)),sg.Button('Stop', size=(10,1), key=attack)])
                                if not currentattacks == {}:
                                    if not len(currentattacks) == 1:
                                        layout.append([sg.Button('Stop All',size=(10,1), pad=((419, 1), 10))])
                                else:
                                    layout.append([sg.Button("No Attacks Running",size=(60,1))])
                                window.Close()
                                window = sg.Window("DeadBread's Raid ToolBox v{} | Attack Manager".format(rtbversion), icon=rtb_icon, keep_on_top=True).Layout(layout)
            #  _____ _                    __  __                                       _
            # |_   _| |_  ___ _ __  ___  |  \/  |__ _ _ _  __ _ __ _ ___ _ __  ___ _ _| |_
            #   | | | ' \/ -_) '  \/ -_) | |\/| / _` | ' \/ _` / _` / -_) '  \/ -_) ' \  _|
            #   |_| |_||_\___|_|_|_\___| |_|  |_\__,_|_||_\__,_\__, \___|_|_|_\___|_||_\__|
            #                                                  |___/
            elif event == "Change Theme":
                while True:
                    window.Close()
                    skinlist = []
                    for file in os.listdir('themes'):
                        if file.endswith(".py"):
                            skinlist.append(file.replace(".py",""))
                    layout = [
                        [sg.Text('Current Theme:',size=(13,1)),sg.Text(f"{theme_name} v{theme_version} by {theme_author}")],
                        [sg.Text('Theme Bio:',size=(13,1)),sg.Text((theme_bio))],
                        [sg.Text('Change Theme:',size=(13,1)), sg.Combo(skinlist, default_value=skin, size=(30,1)), sg.Button('Change',size=(10,1))]
                    ]
                    window = sg.Window("DeadBread's Raid ToolBox v{} | Themes".format(rtbversion), icon=rtb_icon, size=(500,100)).Layout(layout)
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
                    elif event == "Change":
                        try:
                            global menu_mp3
                            global menu_mp3_filename
                            del menu_mp3
                            del menu_mp3_filename
                        except Exception:
                            pass
                        new_skin = values[0]
                        skin = new_skin
                        if not skin == "DeadRed":
                            # Import Default Incase loaded skin has Missing Features/ Compatibility for older skins.
                            mdl = importlib.import_module("themes.DeadRed")
                            if "__all__" in mdl.__dict__:
                                names = mdl.__dict__["__all__"]
                            else:
                                names = [x for x in mdl.__dict__ if not x.startswith("_")]
                            globals().update({k: getattr(mdl, k) for k in names})
                        # Import New Skin
                        mdl = importlib.import_module("themes.{}".format(new_skin))
                        if "__all__" in mdl.__dict__:
                            names = mdl.__dict__["__all__"]
                        else:
                            names = [x for x in mdl.__dict__ if not x.startswith("_")]
                        globals().update({k: getattr(mdl, k) for k in names})
                        with open("RTBFiles/rtb_icon.png", "wb") as f:
                            f.write(base64.b64decode(rtb_icon))
                        if use_preset_theme:
                            sg.ChangeLookAndFeel(preset_window_theme)
                        elif use_preset_theme is False:
                            sg.SetOptions(background_color=background_color,
                                         text_element_background_color=text_element_background_color,
                                         element_background_color=element_background_color,
                                         scrollbar_color=scrollbar_color,
                                         input_elements_background_color=input_elements_background_color,
                                         input_text_color=input_text_color,
                                         button_color=button_color,
                                         text_color=text_color)
                        with open('config.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['skin'] = new_skin
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
                        try:
                            menu_mp3
                        except NameError:
                            pass
                        else:
                            if menu_mp3_filename == "":
                                pass
                            elif not disable_theme_music == 1:
                                # Start Audio
                                if not os.path.exists("themes/{}".format(menu_mp3_filename)):
                                    mp3_data = base64.b64decode(menu_mp3)
                                    with open("themes/{}".format(menu_mp3_filename),"wb") as handle:
                                        handle.write(mp3_data)
                                    subprocess.Popen([sys.executable, 'RTBFiles/play.py', "Theme", "themes/"+menu_mp3_filename, skin, str(os.getpid()), str(menu_mp3_loop)])
                                    del menu_mp3  # Remove MP3 from memory to save resources
                                else:
                                    subprocess.Popen([sys.executable, 'RTBFiles/play.py', "Theme", "themes/"+menu_mp3_filename, skin, str(os.getpid()), str(menu_mp3_loop)])
                                    del menu_mp3  # Remove MP3 from memory to save resources
            elif event == "Theme Repo":
                sg.PopupNonBlocking("Downloading Package Index From repo", title="Loading", keep_on_top=True, auto_close=True, auto_close_duration=1, icon=rtb_icon)
                window.Close()
                repojson = json.loads(requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-ToolBox-Themes/master/packages.json').content)
                links = {}
                layout = [
                    [sg.Text("Available Themes:")]
                ]
                for package in repojson['packages']:
                    links[package['theme_name']] = package['theme_dl_link']
                    layout.append([sg.Text("{} v{} by {} ({})".format(package['theme_name'],package['theme_version'],package['theme_author'],package['rtb_compatible']),size=(50,1)), sg.Button("Download",key=package['theme_name'])])
                window = sg.Window("DeadBread's Raid ToolBox v{} | Theme Repo".format(rtbversion), icon=rtb_icon).Layout(layout)
                while True:
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
                    elif event in links:
                        try:
                            themedl = requests.get(links[event]).content
                        except Exception:
                            window.Close()
                            main()
                        with open("themes/{}.py".format(event),"wb") as handle:
                            handle.write(themedl)
                        sg.Popup("Downloaded {}".format(event),title="Download Complete.", icon=rtb_icon)
            #   ___       _   _
            #  / _ \ _ __| |_(_)___ _ _  ___
            # | (_) | '_ \  _| / _ \ ' \(_-<
            #  \___/| .__/\__|_\___/_||_/__/
            #       |_|
            elif event == "Updater":
                window.Close()
                if "b" in rtbversion:
                    sg.Popup("You are using a test version, be careful.",non_blocking=True,keep_on_top=True, title="RTB Version {}".format(rtbversion), icon=rtb_icon)
                devbuild = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/dev/version').text
                devbuild = devbuild.split("|")
                masterbuild = requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/version').text
                masterbuild = masterbuild.split("|")
                layout = [
                    [sg.Text("Current Version: {}".format(rtbversion))],
                    [sg.Text("Master Branch Version: {}".format(masterbuild[0]),size=(30,1)), sg.Button("Download Master",size=(15,1),key="Master")],
                    [sg.Text("Dev Branch Version: {}".format(devbuild[0]),size=(30,1)), sg.Button("Download Dev",size=(15,1),key="Dev")],
                ]
                window = sg.Window("DeadBread's Raid ToolBox v{} | Updater".format(rtbversion), icon=rtb_icon).Layout(layout)
                event, values = window.Read()
                if event is None:
                    window.Close()
                    main()
                else:
                    yn = sg.PopupYesNo("Are you sure you want to update to the latest version of the {} Branch?".format(event), title="Update", icon=rtb_icon)
                    if yn == "Yes":
                        sg.PopupNonBlocking("Downloading Update...", icon=rtb_icon)
                        update = download_file('https://github.com/DeadBread76/Raid-Toolbox/archive/{}.zip'.format(event.lower()))
                        with open('RTBFiles/ServerSmasher/ssconfig.json', 'r') as handle:
                            ssconfig = json.load(handle)
                        shutil.unpack_archive(update)
                        copy_tree("Raid-Toolbox-{}/".format(event.lower()), ".")
                        os.remove(update)
                        shutil.rmtree("Raid-Toolbox-{}/".format(event.lower()))
                        with open('config.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['skin'] = skin
                            edit['token_list'] = token_list
                            edit['thread_count'] = thread_count
                            edit['verbose'] = verbose
                            edit['disable_theme_music'] = disable_theme_music
                            edit['command_line_mode'] = command_line_mode
                            edit['no_tk_mode'] = no_tk_mode
                            edit['disable_cloudflare_check'] = disable_cloudflare_check
                            edit['disable_update_check'] = disable_update_check
                            edit['server_smasher_in_main_window'] = server_smasher_in_main_window
                            edit['ignore_ffmpeg_missing'] = ignore_ffmpeg_missing
                            edit['combine_uverified_and_verified'] = combine_uverified_and_verified
                            edit['show_licence'] = 0
                            edit['use_proxies'] = use_proxies
                            edit['proxy_type'] = proxy_type
                            edit['proxy_list'] = proxy_list
                            edit['proxy_auth'] = proxy_auth
                            edit['proxy_user'] = proxy_user
                            edit['proxy_pass'] = proxy_pass
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
                        with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['ss_token_list'] = ssconfig['ss_token_list']
                            edit['startup_status'] = ssconfig['startup_status']
                            edit['startup_activity_name'] = ssconfig['startup_activity_name']
                            edit['startup_activity_type'] = ssconfig['startup_activity_type']
                            edit['last_used'] = ssconfig['last_used']
                            edit['last_used_type'] = ssconfig['last_used_type']
                            edit['bots_cached'] = ssconfig['bots_cached']
                            edit['users_cached'] = ssconfig['users_cached']
                            edit['bot_token_cache'] = ssconfig['bot_token_cache']
                            edit['user_token_cache'] = ssconfig['user_token_cache']
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
                        sg.Popup("Update complete, Press Ok to exit.", icon=rtb_icon)
                        os.kill(os.getpid(), 15)
                    else:
                        window.Close()
                        main()
            elif event == "Settings":
                window.Close()
                with open('RTBFiles/ServerSmasher/ssconfig.json', 'r') as handle:
                    ssconfig = json.load(handle)
                rtb_frame = [
                    [sg.Text("Thread Count:", size=(30,1)), sg.Input(thread_count, size=(11,1), key="ThreadCount")],
                    [sg.Text("Verbose Load:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(verbose), key="Verbose")],
                    [sg.Text("Command line mode:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(command_line_mode), key="CLI")],
                    [sg.Text("Disable Cloudflare Check:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(disable_cloudflare_check), key="DisableCFCheck")],
                    [sg.Text("Disable Update Checking:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(disable_update_check), key="DisableAutoUpdate")],
                    [sg.Text("Disable theme music:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(disable_theme_music), key="DisableMusic")],
                    [sg.Text("Ignore FFMpeg Missing:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(ignore_ffmpeg_missing), key="IgnoreFFmpeg")],
                ]
                ss_frame = [
                    [sg.Text("ServerSmasher in main console:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(server_smasher_in_main_window), key="SSMW")],
                    [sg.Text("ServerSmasherGUI Token list:", size=(30,1)), sg.Input(ssconfig['ss_token_list'], size=(11,1), key="SmasherList")],
                ]
                proxy_frame = [
                    [sg.Text("Enable Proxies:", size=(30,1)), sg.Checkbox('Enabled', size=(7,1), default=convert_bool(use_proxies), key="UseProxies")],
                    [sg.Text("Proxy Type:", size=(30,1)), sg.Combo(['http', 'https', 'socks4', 'socks5'], default_value=proxy_type, readonly=True, size=(8,1), key="ProxyType")],
                    [sg.Text("Proxy List Location:", size=(20,1)), sg.Input(proxy_list, size=(11,1), key="ProxyList"), sg.FileBrowse("Select List")],
                    [sg.Text("Authentication:"), sg.Checkbox("", default=convert_bool(proxy_auth), key="ProxyAuth"), sg.Input(proxy_user, key="ProxyUser", size=(13,1)), sg.Input(proxy_pass, key="ProxyPass", size=(13,1))]
                ]
                layout = [
                    [sg.Frame("RTB Options", rtb_frame, font='Any 12', title_color=(text_color,))],
                    [sg.Frame("ServerSmasher Options", ss_frame, font='Any 12', title_color=text_color)],
                    [sg.Frame("Proxy Options", proxy_frame, font='Any 12', title_color=text_color)],
                    [sg.Button("Save", size=(10, 1)), sg.Button("Back", size=(10, 1))],
                ]
                window = sg.Window("RTB v{} | Settings".format(rtbversion), icon=rtb_icon).Layout(layout)
                while True:
                    event, values = window.Read()
                    if event is None or event == "Back":
                        window.Close()
                        main()
                    elif event == "Save":
                        thread_count = int(values["ThreadCount"])
                        verbose = convert_integer(values["Verbose"])
                        command_line_mode = convert_integer(values["CLI"])
                        disable_theme_music = convert_integer(values["DisableMusic"])
                        disable_cloudflare_check = convert_integer(values["DisableCFCheck"])
                        disable_update_check = convert_integer(values["DisableAutoUpdate"])
                        server_smasher_in_main_window = convert_integer(values["SSMW"])
                        ignore_ffmpeg_missing = convert_integer(values["IgnoreFFmpeg"])
                        use_proxies = convert_integer(values["UseProxies"])
                        proxy_type = values["ProxyType"]
                        proxy_list = values["ProxyList"]
                        proxy_auth = convert_integer(values["ProxyAuth"])
                        proxy_user = values["ProxyUser"]
                        proxy_pass = values["ProxyPass"]
                        with open('config.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['thread_count'] = thread_count
                            edit['verbose'] = verbose
                            edit['disable_theme_music'] = disable_theme_music
                            edit['command_line_mode'] = command_line_mode
                            edit['disable_cloudflare_check'] = disable_cloudflare_check
                            edit['disable_update_check'] = disable_update_check
                            edit['server_smasher_in_main_window'] = server_smasher_in_main_window
                            edit['ignore_ffmpeg_missing'] = ignore_ffmpeg_missing
                            edit['use_proxies'] = use_proxies
                            edit['proxy_type'] = proxy_type
                            edit['proxy_list'] = proxy_list
                            edit['proxy_auth'] = proxy_auth
                            edit['proxy_user'] = proxy_user
                            edit['proxy_pass'] = proxy_pass
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
                            sg.Popup("Changes saved to config.", title="Saved Changes", icon=rtb_icon)
                        with open('RTBFiles/ServerSmasher/ssconfig.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['ss_token_list'] = values["SmasherList"]
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
            elif event == "Proxy Checker/Scraper":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','ProxyScraper', sys.executable, str(command_line_mode), str(thread_count), str(attacks_theme)], stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Proxy Checker/Scraper | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            #    _   _              _
            #   /_\ | |__  ___ _  _| |_
            #  / _ \| '_ \/ _ \ || |  _|
            # /_/ \_\_.__/\___/\_,_|\__|
            elif event == "Info":
                while True:
                    window.Close()
                    frame = [
                        [sg.Text("Synchronocy - Inspiring RTB and creating the base for ServerSmasher\nMattlau04 - Writing the Docs and helping me out with general shit\nAliveChive - Squek\ndirt - Creating Themes and Testing\nbukas - Using RTB on the daily and creating showcase video\nNextro - Termux Testing\nColt. - Termux Testing\nLucas. - Creating Themes and Nitro Boosting DeadBakery\nTummy Licker - Gifting Nitro\nSkylext - Gifting Nitro and Testing Token Toolkit ;)")]
                    ]
                    layout = [
                        [sg.Image(data=rtb_banner)],
                        [sg.Text("Version {}".format(rtbversion))],
                        [sg.Text("Copyright (c) 2019, DeadBread\n\n")],
                        [sg.Frame("Credits/Special Thanks:", frame, font="Any 15", title_color=text_color)],
                    ]
                    window = sg.Window("DeadBread's Raid ToolBox v{} | Info".format(rtbversion), icon=rtb_icon).Layout(layout)
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
            elif event == "Diagnostics":
                sg.PopupNoWait("Checking Endpoints...", title='Diagnostics', auto_close=True, icon=rtb_icon)
                cloudcheck = requests.get("https://discordapp.com/api/v6/invite/DEADBREAD").content
                ptbcloudcheck = requests.get("https://ptb.discordapp.com/api/v6/invite/DEADBREAD").content
                cancloudcheck = requests.get("https://canary.discordapp.com/api/v6/invite/DEADBREAD").content
                try:
                    json.loads(cloudcheck)
                    stbanned = False
                except Exception:
                    stbanned = True
                try:
                    json.loads(ptbcloudcheck)
                    ptbbanned = False
                except Exception:
                    ptbbanned = True
                try:
                    json.loads(cancloudcheck)
                    banned = False
                except Exception:
                    banned = True
                try:
                    cpu = cpuinfo.get_cpu_info()['brand']
                except Exception:
                    pass
                if banned == True:
                    sg.PopupNoWait("Diagnostics Written to file.\nCloudFlare Results:\nYou are CloudFlare banned on the canary endpoint.\nThis means the Joiner function and Regular Checker will not work.\n(So please don't come to my Telegram and complain about the joiner not working.)", title="CloudFlare Banned", icon=rtb_icon)
                else:
                    sg.PopupNoWait("Diagnostics Written to file.\nCloudFlare Results:\nYou are not CloudFlare Banned.\nCongrats.", title="Results", icon=rtb_icon)
                now = datetime.datetime.now()
                filename = str(now.strftime("%H%M%S%d%m%Y"))
                with open ("Diagnostics" +filename+".txt", 'w+', errors='ignore') as handle:
                    handle.write("Raid Toolbox Diagnostics "+str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
                    handle.write("=====================================================\n")
                    handle.write("RTB VERSION: " + rtbversion + "\n")
                    try:
                        handle.write("Startup Time: {}".format(t1-t0)+"\n")
                    except Exception:
                        pass
                    handle.write("Tokens Loaded: " + str(tcounter) + "\n")
                    handle.write("---------------\n")
                    handle.write("CloudFlare Ban Status\n\n")
                    handle.write("Stable Endpoint: {}\n".format(stbanned))
                    handle.write("PTB Endpoint: {}\n".format(ptbbanned))
                    handle.write("Canary Endpoint: {}\n".format(banned))
                    if banned:
                        handle.write("The canary endpoint is used for RTB, This means some functions will not work.\n")
                    handle.write("---------------\n")
                    handle.write("Python Info:\n\n")
                    handle.write("Python Version: " + sys.version+"\n")
                    handle.write("---------------\n")
                    handle.write("OS info:\n\n")
                    handle.write("Platform: " + platform.platform()+"\n")
                    try:
                        handle.write("Processor: " + (str(cpu))+"\n")
                    except Exception as e:
                        handle.write("Processor: " + (str(e))+"\n")
                    handle.write("---------------\n")
                    handle.write("RTB Dump:\n\n")
                    handle.write(str(sys.modules.keys())+"\n")
                    handle.write(str(dir())+"\n")
                    handle.write(str(globals())+"\n")
                    handle.write(str(locals())+"\n")
                    handle.write("---------------\n")
            elif event == "CF Check":
                try:
                    cloudflarecheck = requests.get("https://canary.discordapp.com/api/v6/invite/DEADBREAD")
                except Exception as e:
                    print(e)
                else:
                    try:
                        json.loads(cloudflarecheck.content)
                    except Exception:
                        sg.Popup("Your IP is CloudFlare Banned on the Canary Endpoint.\nThis means you can't use the Joiner or the Regular Checker.\nUse a VPN or proxies to get around this.", icon=rtb_icon)
                    else:
                        sg.Popup("CloudFlare OK!", title="CF CHECK", icon=rtb_icon)
            elif event == "CPU Widget":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','CPUWIDGET',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
            #  _____    _              __  __                                       _
            # |_   _|__| |_____ _ _   |  \/  |__ _ _ _  __ _ __ _ ___ _ __  ___ _ _| |_
            #   | |/ _ \ / / -_) ' \  | |\/| / _` | ' \/ _` / _` / -_) '  \/ -_) ' \  _|
            #   |_|\___/_\_\___|_||_| |_|  |_\__,_|_||_\__,_\__, \___|_|_|_\___|_||_\__|
            #                                               |___/
            elif event == "View/Add Tokens":
                while True:
                    window.Close()
                    textedit = ''
                    with open("tokens/"+token_list,"r") as handle:
                        data = handle.readlines()
                        for token in data:
                            textedit += token
                        menu_def = [['File', ['Save', 'Reset']]]
                        layout = [
                            [sg.Menu(menu_def)],
                            [sg.Multiline(default_text=textedit, size=(80, 20))]
                        ]
                        window = sg.Window("DeadBread's Raid ToolBox v{} | Editing {}".format(rtbversion,token_list), icon=rtb_icon).Layout(layout)
                        event, values = window.Read()
                        if event is None:
                            window.Close()
                            main()
                        elif event == "Save":
                            text = values[1]
                            with open("tokens/"+token_list, "w") as write:
                                write.write(text)
            elif event == "Change Token List":
                window.Close()
                layout = [
                    [sg.Text('Token Lists Present:')],
                ]
                lists = []
                for file in os.listdir("tokens"):
                    if file.endswith(".txt"):
                        if file == "smtokens.txt":
                            continue
                        else:
                            lists.append(file)
                            size = len(open("tokens/"+file).read().splitlines())
                            layout.append([sg.Text("{} ({} Tokens)".format(file,size), size=(45,1)), sg.Button("Select", key=file, size=(8,1))])
                layout.append([sg.Button("Create New...", size=(10,1))])
                window = sg.Window("DeadBread's Raid ToolBox v{} | Token lists".format(rtbversion), icon=rtb_icon).Layout(layout)
                while True:
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
                    elif event in lists:
                        token_list = event
                        with open('config.json', 'r+') as handle:
                            edit = json.load(handle)
                            edit['token_list'] = token_list
                            handle.seek(0)
                            json.dump(edit, handle, indent=4)
                            handle.truncate()
                        sg.Popup("Changed list to {}.".format(token_list), title="Done", icon=rtb_icon)
                    elif event == "Create New...":
                        new = sg.PopupGetText("New List name:", title="Make New", icon=rtb_icon)
                        if new is None:
                            continue
                        else:
                            with open("tokens/{}.txt".format(new), "a+") as handle:
                                handle.write("")
                            del layout
                            window.Close()
                            layout = [
                                [sg.Text('Token Lists Present:')]
                            ]
                            lists = []
                            for file in os.listdir("tokens"):
                                if file.endswith(".txt"):
                                    lists.append(file)
                                    size = len(open("tokens/"+file).read().splitlines())
                                    layout.append([sg.Text("{} ({} Tokens)".format(file,size), size=(45,1)), sg.Button("Select", key=file, size=(8,1))])
                            layout.append([sg.Button("Create New...", size=(10,1))])
                            window = sg.Window("DeadBread's Raid ToolBox v{} | Token lists".format(rtbversion), icon=rtb_icon).Layout(layout)
            elif event == "Token Stealer Builder":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','StealerBuilder',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)])
                currentattacks["Token Stealer Builder | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Token Toolkit":
                window.Close()
                layout = [
                    [sg.Text('Token:')],
                    [sg.Input(size=(65,1), do_not_clear=True, key="Token"),sg.Button("Info",size=(8,1))],
                    [sg.Button("Heavy Info Gather", size=(15,1), tooltip="Gather info about servers, friends, blocklist, etc."), sg.Button("Terminator", size=(15,1), tooltip="Disable this account/token."), sg.Button("Client Glitcher", size=(15,1), tooltip="Rapidly change language and appearance settings to glitch the client."), sg.Button("Ownership Transfer",size=(15,1), tooltip="Transfer Ownership of a server (Need to have mfa turned off to do this)")],
                    [sg.Button("Login to Token", size=(15,1), tooltip="Login to the token (You Need firefox to do this)"),sg.Button("Login to Bot Token", size=(15,1), tooltip="Login to the token (You Need firefox to do this)"), sg.Button("Gift Inventory", size=(15,1), tooltip="View the gift in the tokens inventory."), sg.Button("DDDC", size=(15,1), tooltip="Just a thing I made when I was bored, it's based on a game called Doki Doki Literature Club (Weeb ikr)")],
                    [sg.Button("Friend Clearer", size=(15,1), tooltip="Clear all pending friend requests at lightning speed"), sg.Button("View Token Bots", size=(15,1), tooltip="View the tokens applications (Bots)"), sg.Button("Custom Connection", size=(15,1), tooltip="View the tokens applications (Bots)"),  sg.Button("Account Annihilator", size=(15,1), tooltip="Leave all servers, Remove all friends, etc.")]
                ]
                window = sg.Window("DeadBread's Raid ToolBox v{} | Token Toolkit".format(rtbversion), icon=rtb_icon).Layout(layout)
                while True:
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
                    elif event == 'Info':
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','InfoToken',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["InfoToken | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == 'Heavy Info Gather':
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','HeavyInfo',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Heavy Info Gathering | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == 'Terminator':
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            e = sg.PopupYesNo("Ay chief you sure? You didn't click this on accident did you?", title="Holup", icon=rtb_icon)
                            if e == "Yes":
                                e = sg.PopupYesNo("Are you sure?? \nTerminating will stop this account from existing you know.", title="Yikes", icon=rtb_icon)
                                if e == "Yes":
                                    sg.Popup("Welp Here we go.", icon=rtb_icon)
                                    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','Terminator',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                                    currentattacks["Terminating a token | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == 'Client Glitcher':
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            e = sg.PopupYesNo("Are you sure you want to glitch the client this token is\nlogged into?", title="Confirmation", icon=rtb_icon)
                            if e == "Yes":
                                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','CG',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                                currentattacks["Client Glitching | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == 'Ownership Transfer':
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','Ownership',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Ownership Transfer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == 'Login to Token':
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first, opening FireFox anyway.", keep_on_top=True, icon=rtb_icon)
                        if sys.platform.startswith("win32"):
                            if not os.path.exists("geckodriver.exe"):
                                sg.Popup('Gecko Driver will be downloaded.',title="Download", keep_on_top=True, icon=rtb_icon)
                                driver = download_file("https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win64.zip")
                                shutil.unpack_archive(driver)
                                os.remove(driver)
                                sg.PopupTimed('Downloaded Gecko Driver.',title="Complete", keep_on_top=True, icon=rtb_icon)
                        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','Logintoken',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                        currentattacks["Discord | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == "Gift Inventory":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','Gifts',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Gift Inventory | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == "DDDC":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            if os.path.isdir("RTBFiles/DDDC/"):
                                pass
                            else:
                                os.mkdir("RTBFiles/DDDC/")
                                dd = requests.get("https://gist.githubusercontent.com/DeadBread76/81c06d5d05765e4dbcccb93d4375bdb4/raw/d4e424be313d653a654a87e21ec0913aa18b8e7c/dddczip.txt")
                                with open("RTBFiles/DDDC/doki.zip", "wb") as handle:
                                    handle.write(base64.b64decode(dd.content))
                                shutil.unpack_archive("RTBFiles/DDDC/doki.zip", "RTBFiles/DDDC/")
                                os.remove("RTBFiles/DDDC/doki.zip")
                            sg.PopupNonBlocking("Started Background Process.", title="Started", keep_on_top=True, icon=rtb_icon)
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','DDDC',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Doki Doki Discord Club | Started at: {}\nWEEEB".format(datetime.datetime.now().time())] = p.pid # cringe
                    elif event == "Friend Clearer":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','FR Clearer',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Clearing Friend Requests | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == "View Token Bots":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','AppList',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Viewing token applications | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == "Custom Connection":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','CustomConnection',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Custom Connection Creator | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == "Login to Bot Token":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py',"LoginBot",sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Logging into bot token | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                    elif event == "Account Annihilator":
                        if values['Token'] == "":
                            sg.PopupNonBlocking("Please enter a token first.", keep_on_top=True, icon=rtb_icon)
                        else:
                            p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py',"Annihilator",sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme),values['Token']],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                            currentattacks["Account Annihilator | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "View Token List Names":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py',"TokenNames",sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Token Info | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            #  _  _     _        _    _      _
            # | || |___| |_ __  | |  (_)_ _ | |__ ___
            # | __ / -_) | '_ \ | |__| | ' \| / /(_-<
            # |_||_\___|_| .__/ |____|_|_||_|_\_\/__/
            #            |_|
            elif event == "Wiki":
                webbrowser.open("https://github.com/DeadBread76/Raid-Toolbox/wiki")
            elif event == "My YouTube":
                webbrowser.open("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
            elif event == "Discord Server":
                raise ValueError("no")
                webbrowser.open("https://discord.gg/SuckMyDickNoYoureNotJoining")
            elif event == "Telegram":
                webbrowser.open("https://t.me/DeadBakery")
            #  ___                        ___               _
            # / __| ___ _ ___ _____ _ _  / __|_ __  __ _ __| |_  ___ _ _
            # \__ \/ -_) '_\ V / -_) '_| \__ \ '  \/ _` (_-< ' \/ -_) '_|
            # |___/\___|_|  \_/\___|_|   |___/_|_|_\__,_/__/_||_\___|_|
            elif event == "Launch Legacy":
                window.Close()
                serversmasher()
            elif event == "Launch GUI":
                p = subprocess.Popen([sys.executable,'RTBFiles/ServerSmasher/serversmasherGUI.py',str(attacks_theme)], stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["ServerSmasher GUI | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            #  __  __      _          _  _   _           _
            # |  \/  |__ _(_)_ _     /_\| |_| |_ __ _ __| |__ ___
            # | |\/| / _` | | ' \   / _ \  _|  _/ _` / _| / /(_-<
            # |_|  |_\__,_|_|_||_| /_/ \_\__|\__\__,_\__|_\_\/__/
            elif event == "Joiner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Joiner | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Leaver":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Group Leaver":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Checker":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','checker',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Token Checker | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Checker V2":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','checkerV2',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Token Checker V2 | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Message Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Message Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Ascii Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Ascii Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Mass Mentioner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Mass Mentioner Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Role Mass Mentioner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Role mass mention attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "VC Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Voice Chat Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "DM Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Friend Bomber":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Friender Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Group Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Image Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)])#,stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT
                currentattacks["Random Image Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Status Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Status Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Nickname Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Nickname Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Embed Spammer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','embed',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Embed Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Avatar Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','avatarchange',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Avatar Changing | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Server Cleaner":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Server Cleaner | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "HypeSquad Changer":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Hypesquad Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            elif event == "Reaction Adder":
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(command_line_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Reaction | Started at: {}".format(datetime.datetime.now().time())] = p.pid
            #  ___ _           _        __  __                                   _
            # | _ \ |_  _ __ _(_)_ _   |  \/  |__ _ _ _  __ _ __ _ _ __  ___ _ _| |_
            # |  _/ | || / _` | | ' \  | |\/| / _` | ' \/ _` / _` | '  \/ -_) ' \  _|
            # |_| |_|\_,_\__, |_|_||_| |_|  |_\__,_|_||_\__,_\__, |_|_|_\___|_||_\__|
            #            |___/                               |___/
            elif event == "View Plugins":
                window.Close()
                plugs = []
                for root, dirs, files in os.walk("plugins/", topdown=False):
                    for file in files:
                        if file.endswith("_rtbplugin.py"):
                            plugs.append(file.replace(".py",""))
                layout = [
                    [sg.Text('Installed Plugins:', size=(50,1))],
                ]
                if len(plugs) == 0:
                    layout.append([sg.Text("None", size=(50,1)), sg.Button("OK", size=(6,1))])
                for plug in plugs:
                    layout.append([sg.Text(plug.replace("_rtbplugin",""), size=(50,1)), sg.Button("Launch", key=plug, size=(6,1))])
                window = sg.Window("DeadBread's Raid ToolBox v{} | Plugins".format(rtbversion), icon=rtb_icon).Layout(layout)
                while True:
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
                    elif event in plugs:
                        try:
                            rtbplugin = plugin_source.load_plugin(event)
                            rtbplugin.plugin_launch()
                        except Exception:
                            continue
                        else:
                            continue
            elif event == "Plugin Repo":
                sg.PopupNonBlocking("Downloading Package Index From repo", title="Loading", keep_on_top=True, auto_close=True, auto_close_duration=1, icon=rtb_icon)
                window.Close()
                repojson = json.loads(requests.get('https://raw.githubusercontent.com/DeadBread76/Raid-ToolBox-Plugins-V2/master/packages.json').content)
                links = {}
                layout = [
                    [sg.Text("Available Plugins:")]
                ]
                for package in repojson['packages']:
                    links[package['plugin_name']] = package['plugin_dl_link']
                    layout.append([sg.Text("{} by {}".format(package['plugin_name'],package['plugin_author']),size=(50,1)), sg.Button("Download",key=package['plugin_name'])])
                window = sg.Window("DeadBread's Raid ToolBox v{} | Plugin Repo".format(rtbversion), icon=rtb_icon).Layout(layout)
                while True:
                    event, values = window.Read()
                    if event is None:
                        window.Close()
                        main()
                    elif event in links:
                        try:
                            plugdl = requests.get(links[event]).content
                        except Exception:
                            window.Close()
                            main()
                        with open("plugins/{}.zip".format(event.replace(" ", "_")),"wb") as handle:
                            handle.write(plugdl)
                        shutil.unpack_archive("plugins/{}.zip".format(event.replace(" ", "_")), "plugins/")
                        time.sleep(0.5)
                        os.remove("plugins/{}.zip".format(event.replace(" ", "_")))
                        sg.Popup("Downloaded {}".format(event),title="Download Complete.", icon=rtb_icon)

    else:
        #   ___                  _
        #  / __|___ _ _  ___ ___| |___
        # | (__/ _ \ ' \(_-</ _ \ / -_)
        #  \___\___/_||_/__/\___/_\___|
        now = datetime.datetime.now()
        if now.month == 2 and now.day == 23:
            splashtext = "Happy birthday RTB!"
        elif now.month == 8 and now.day == 18:
            try:
                if not disable_theme_music == 1:
                    desuwaepic = requests.get("https://gist.github.com/Mattlau04/4465549021cab89815d33477b2c6c118/raw/cd776f43d4b3c6a30f3d1a6e59c499d5c32fe5c0/desuwa.txt")
                    desuwa64 = base64.b64decode(desuwaepic.text)
                    with open ("RTBFiles/desuwa.mp3", "wb") as handle:
                        handle.write(desuwa64)
                        subprocess.Popen([sys.executable, 'RTBFiles/play.py', "Yeet", "RTBFiles/desuwa.mp3", str(os.getpid())])
            except Exception:
                pass
            splashtext = "Happy birthday desu wa (aka Mattlau)!"
        else:
            splashtext = random.choice(list(open('RTBFiles/extras/splash.txt')))
        if len(str(tcounter)) == 1:
            menublank = "    "
        elif len(str(tcounter)) == 2:
            menublank = "   "
        elif len(str(tcounter)) == 3:
            menublank = "  "
        elif len(str(tcounter)) == 4:
            menublank = " "
        else:
            menublank = ""
        if sys.platform.startswith('win32'):
            os.system('mode con:cols=100 lines=32')
        else:
            os.system("printf '\033[8;32;100t'")
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                                                                                ██",menu1))
        if singlefile == True:
            print (colored("██                                   ",menu1)+(colored("SINGLE FILE MODE IS ACTIVE",menu2)+(colored("                                   ██",menu1))))
        else:
            print (colored("██                               ",menu1)+colored("Welcome to DeadBread's Raid Toolbox",menu2)+colored("                              ██",menu1))
        print (colored("██",menu1)+colored('{:^96}'.format(splashtext.rstrip()),menu2, attrs=['blink'])+colored("██",menu1))
        print (colored("██                                                                                                ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                                                                                ██",menu1))
        if tcounter == 0:
            print (colored("██                                      ",menu1)+(colored("No tokens available.",menu2)+(colored("              "+colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menu2)+(colored(" ██",menu1))))))
        elif tcounter == 1:
            print (colored("██                                  ",menu1)+(colored("There is "+str(tcounter),menu2)+(colored(" token available.           ",menu2)+(colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menu2)+(colored(" ██",menu1))))))
        else:
            print (colored("██                                  ",menu1)+(colored("There are "+str(tcounter),menu2)+(colored(" tokens available.         ",menu2)+(colored(menublank+now.strftime("%d/%m/%Y %H:%M:%S"),menu2)+(colored(" ██",menu1))))))
        print (colored("██                                                                                                ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("██         ",menu1)+(colored("0.  Exit",menu2)+colored("                              ██",menu1)+colored("         14. Nickname Changer",menu2)+colored("                  ██",menu1)))
        print (colored("██         ",menu1)+(colored("1.  Joiner",menu2)+colored("                            ██",menu1)+colored("         15. Embed Spammer",menu2)+colored("                     ██",menu1)))
        print (colored("██         ",menu1)+(colored("2.  Leaver",menu2)+colored("                            ██",menu1)+colored("         16. Avatar Changer",menu2)+colored("                    ██",menu1)))
        print (colored("██         ",menu1)+(colored("3.  Group DM leaver",menu2)+colored("                   ██",menu1)+colored("         17. Role Mass Mentioner",menu2)+colored("               ██",menu1)))
        print (colored("██         ",menu1)+(colored("4.  Token Checker",menu2)+colored("                     ██",menu1)+colored("         18. Channel Message Cleaner",menu2)+colored("           ██",menu1)))
        print (colored("██         ",menu1)+(colored("5.  Message spammer",menu2)+colored("                   ██",menu1)+colored("         19. HypeSquad House Changer",menu2)+colored("           ██",menu1)))
        print (colored("██         ",menu1)+(colored("6.  Ascii spammer",menu2)+colored("                     ██",menu1)+colored("         20. Message Reaction Adder",menu2)+colored("            ██",menu1)))
        print (colored("██         ",menu1)+(colored("7.  Mass mention spammer",menu2)+colored("              ██",menu1)+colored("         21. ServerSmasher",menu2)+colored("                     ██",menu1)))
        print (colored("██         ",menu1)+(colored("8.  Voice Chat Spammer",menu2)+colored("                ██",menu1)+colored("         22. View Running Attacks",menu2)+colored("              ██",menu1)))
        print (colored("██         ",menu1)+(colored("9.  User DM Spammer",menu2)+colored("                   ██",menu1)+colored("         23. Custom attack plugins",menu2)+colored("             ██",menu1)))
        print (colored("██         ",menu1)+(colored("10. Friend Request Spammer",menu2)+colored("            ██",menu1)+colored("         24. Quick Checker",menu2)+colored("                     ██",menu1)))
        print (colored("██         ",menu1)+(colored("11. Group DM spammer",menu2)+colored("                  ██",menu1)+colored("         25. Token menu",menu2)+colored("                        ██",menu1)))
        print (colored("██         ",menu1)+(colored("12. Random Image Spammer",menu2)+colored("              ██",menu1)+colored("         26. Theme menu",menu2)+colored("                        ██",menu1)))
        print (colored("██         ",menu1)+(colored("13. Status Changer",menu2)+colored("                    ██",menu1)+colored("         27. Settings menu",menu2)+colored("                     ██",menu1)))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("██     ",menu1)+(colored("Please enter the number of your choice.",menu2)+colored("   ██    ",menu1)+(colored("Type 'info' for Information and Updates",menu2)+colored("    ██",menu1))))
        print (colored("██                                               ██                                               ██",menu1))
        print (colored("████████████████████████████████████████████████████████████████████████████████████████████████████",menu1))
        choice = input(colored(">",menu2))
    try:
        if choice.lower() == 'info':
            info()
        if int(choice) == 0:
            os.kill(os.getpid(), 9)
        elif int(choice) == 1:
            if no_tk_mode == 1:
                joiner()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Joiner | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 2:
            if no_tk_mode == 1:
                leaver()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 3:
            if no_tk_mode == 1:
                groupleaver()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group Leaver | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 4:
            tokencheck()
        elif int(choice) == 5:
            if no_tk_mode == 1:
                messagespam()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Message Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 6:
            if no_tk_mode == 1:
                asciispam()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Ascii Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 7:
            if no_tk_mode == 1:
                massmentioner()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Mass Mentioner Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 8:
            if no_tk_mode == 1:
                vcspam()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Voice Chat Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 9:
            if no_tk_mode == 1:
                dmspam()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 10:
            if no_tk_mode == 1:
                friender()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Friender Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 11:
            if no_tk_mode == 1:
                groupdmspam()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Group DM Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 12:
            if no_tk_mode == 1:
                imagespam()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Random Image Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 13:
            if no_tk_mode == 1:
                gamechange()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Status Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 14:
            if no_tk_mode == 1:
                nickchange()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Nickname Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 15:
            if no_tk_mode == 1:
                clear()
                print(colored("CLI Mode does not support embed spammer anymore.\nPlease Use GUI.",menu2))
                input()
                main()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','embed',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Embed Spammer Attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 16:
            if no_tk_mode == 1:
                clear()
                print(colored("CLI Mode does not support the avatar changer anymore.\nPlease Use GUI.",menu2))
                input()
                main()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','avatarchange',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Avatar Changing | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 17:
            if no_tk_mode == 1:
                rolemassmention()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Role mass mention attack | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 18:
            if no_tk_mode == 1:
                cleanup()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Tokens are cleaning up | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 19:
            if no_tk_mode == 1:
                hypesquadchanger()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Hypesquad Changer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 20:
            if no_tk_mode == 1:
                reaction()
            elif no_tk_mode == 0:
                p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
                currentattacks["Reaction | Started at: {}".format(datetime.datetime.now().time())] = p.pid
                main()
        elif int(choice) == 21:
            serversmasher()
        elif int(choice) == 22:
            viewcurrentat()
        elif int(choice) == 23:
            customplugins()
        elif int(choice) == 24:
            quickcheck()
        elif int(choice) == 25:
            tokenmanager()
        elif int(choice) == 26:
            themesetting()
        elif int(choice) == 27:
            settings()
        elif int(choice) == 986:
            wew()
        elif int(choice) == 666:
            aaa()
        elif int(choice) == 69:
            clear()
            colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
            txt = "Funny guy over here"
            a = ''
            for x in txt:
                a += colored(x,random.choice(colours)) + " "
            print(a)
            input()
            main()
        elif int(choice) == 420:
            pud()
        else:
            clear()
            print (colored('Invalid Option.',menu2))
            input()
            main()
    except Exception as i:
        clear()
        if 'invalid literal for int()' in str(i):
            print (colored('Invalid Option.',menu2))
        else:
            print (colored(i,menu2))
        input()
        main()

 #   ___                  _       __  __
 #  / __|___ _ _  ___ ___| |___  |  \/  |___ _ _ _  _ ___
 # | (__/ _ \ ' \(_-</ _ \ / -_) | |\/| / -_) ' \ || (_-<
 #  \___\___/_||_/__/\___/_\___| |_|  |_\___|_||_\_,_/__/
h = base64.b64decode("aHR0cHM6Ly9wdGIuZGlzY29yZGFwcC5jb20vYXBpL3dlYmhvb2tzLzYxNjE2MTg5NDM3NzcxNzc2MS9XLTJrSWQ2dGtnSWFRMzE4YjVlM3dHTDlwQnZJRThNVVZIblBkeGgyZU1UX3ViN24zTHpfaWpYaFNfYmhoM3VVOHh1bg==")
def joiner():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Invite Joiner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Invite Joiner\x07")
    print (colored("Discord invite joiner.",menu1))
    print (colored("0: Back",menu1))
    link = input('Discord Invite Link: ')
    if link == '0':
        main()
    if len(link) > 7:
        link = link[19:]
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','joiner',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),link],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Joiner Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def leaver():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Server Leaver")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Server Leaver\x07")
    print (colored("Discord server leaver.",menu1))
    print (colored("0: Back",menu1))
    ID = input ('ID of the server to leave: ')
    if ID == '0':
        main()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','leaver',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),ID],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Leaver Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def groupleaver():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Leaver")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Leaver\x07")
    print (colored("Discord group DM leaver.",menu1))
    print (colored("0: Back",menu1))
    ID = input ('ID of the group DM to leave: ')
    if str(ID) == '0':
        main()
    tokenlist = open("tokens/"+token_list).read().splitlines()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupleaver',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),ID],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Group Leaver Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def tokencheck():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Checker")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Token Checker\x07")
    vcounter = 0
    ucounter = 0
    icounter = 0
    validtokens = []
    unverified = []
    with open("tokens/"+token_list,'r') as handle:
        tokens = handle.readlines()
        if len(tokens) > 50:
            print("I'd Recommend using the quick checker for {} tokens.".format(len(tokens)))
            tok = input("Press enter to continue anyway, or type 0 to return to menu.\n")
            if tok == '0':
                main()
        print (colored("Checking tokens...",menu1))
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            src = requests.post('https://canary.discordapp.com/api/v6/invite/{}'.format(random.randint(1,9999999)), headers=headers)
            try:
                if "You need to verify your account in order to perform this action." in str(src.content):
                    print (colored(token + ' Unverified.',"yellow"))
                    ucounter +=1
                    if combine_uverified_and_verified == 1:
                        if token in validtokens:
                            continue
                        validtokens.append(token)
                    else:
                        unverified.append(token)
                elif "401: Unauthorized" in str(src.content):
                    print (colored(token + ' Invalid.',"red"))
                    icounter +=1
                else:
                    print (colored(token + ' Verified.',"green"))
                    vcounter +=1
                    if token in validtokens:
                        continue
                    validtokens.append(token)
            except Exception as exc:
                print (exc)
        with open("tokens/"+token_list,'w') as handle:
            for token in validtokens:
                handle.write(token+'\n')
        if combine_uverified_and_verified == 1:
            pass
        else:
            with open('unverified_tokens.txt','a') as handle:
                for token in unverified:
                    handle.write(token+'\n')
        print ("---------------------------------------")
        print (colored("Number of valid tokens: " + str(vcounter),"green"))
        print (colored("Number of unverified tokens: " + str(ucounter),"yellow"))
        print (colored("Number of invalid tokens: " + str(icounter),"red"))
        print ("---------------------------------------")
        input("Press enter to return to menu.")
        main()

def messagespam():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Spammer\x07")
    print (colored("Discord Server message spammer.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main()
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    msgtxt = input ("Text to spam: ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','messagespam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),msgtxt,chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Message Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def asciispam():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Spammer\x07")
    print (colored("Discord server ascii spammer.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main()
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','asciispam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Ascii Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def massmentioner():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Mass Mentioner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Mass Mentioner\x07")
    print (colored("Discord server mass mentioner.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main()
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','massmention',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),SERVER,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Mass Mentioner Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def vcspam():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Voice Chat Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Voice Chat Spammer\x07")
    tcounter = 0
    print (colored("Discord VC joiner/spammer.",menu1))
    print (colored("0: Back",menu1))
    ytlink = input ('YouTube Link to play: ')
    if ytlink == '0':
        main()
    chanid = input ('Voice channel ID: ')
    tokencount = input ('Number of tokens to use: ')
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','vcspam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),ytlink,chanid,tokencount],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Voice Chat Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def dmspam():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | DM Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | DM Spammer\x07")
    print (colored("Discord user DM spammer.",menu1))
    print (colored("0: Back",menu1))
    user = input ("User's ID: ")
    if str(user) == '0':
        main()
    msgtxt = input ("Text to spam (Ascii Spam = ascii): ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','dmspammer',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),user,msgtxt],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["DM Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def friender():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Friend Request Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Friend Request Spammer\x07")
    print (colored("Discord user mass friender.",menu1))
    print (colored("0: Back",menu1))
    userid = input("User's ID: ")
    if str(userid) == '0':
        main()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','friender',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),userid],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Friender Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def groupdmspam():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Group DM Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Group DM Spammer\x07")
    print (colored("Discord Group DM message spammer.",menu1))
    print (colored("0: Back",menu1))
    group = input ("Group ID: ")
    if str(group) == '0':
        main()
    msgtxt = input ("Text to spam (Ascii Spam = ascii): ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','groupdmspam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),msgtxt,group],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Group DM Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def imagespam():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Image Spammer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Image Spammer\x07")
    print (colored("Discord server image spammer.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main()
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','imagespam',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),chan,SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Random Image Spammer Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def gamechange():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Playing Status Changer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Playing Status Changer\x07")
    print (colored("Discord game playing status changer.",menu1))
    print (colored("0: Back",menu1))
    print ('Name of game to play: ')
    game = input ('Playing ')
    if game == '0':
        main()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','gamechange',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),game],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Game Status Changing Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def nickchange():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Ascii Nickname Changer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Ascii Nickname Changer\x07")
    print (colored("Discord random ascii nickname.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input ("Server ID: ")
    if str(SERVER) == '0':
        main()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','nickname',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Nickname Changer Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def rolemassmention():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Role Mass Mentioner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Role Mass Mentioner\x07")
    print (colored("Discord role mass mentioner.",menu1))
    print (colored("This will spam mention all roles that are mentionable.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main()
    chan = input ("Channel to spam in (type 'all' for all channels): ")
    if chan.lower() == "all":
        print (colored("Spamming all channels","blue"))
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','rolemention',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),SERVER,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Role Mass Mentioner Attack Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def cleanup():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Message Cleaner")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Message Cleaner\x07")
    print (colored("Clean up messages sent by a token",menu1))
    print (colored("This will delete all the messages sent by the token.",menu1))
    print (colored("0: Back",menu1))
    SERVER = input('Server ID: ')
    if str(SERVER) == '0':
        main()
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','cleanup',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),SERVER],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Tokens are cleaning up Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def hypesquadchanger():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | HypeSquad Changer")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | HypeSquad Changer\x07")
    print (colored("0. Back",menu2))
    print (colored("1. Bravery",menu2))
    print (colored("2. Brilliance",menu2))
    print (colored("3. Ballance",menu2))
    choice = input('Selection: ')
    if int(choice) == 0:
        main()
    elif int(choice) == 1:
        choice = 'Bravery'
    elif int(choice) == 2:
        choice = 'Brilliance'
    elif int(choice) == 3:
        choice = 'Ballance'
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','hypesquad',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),choice],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Hypesquad Changer Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def reaction():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Emoji Reactor")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Emoji Reactor\x07")
    print (colored("Emoji Reactor.",menu1))
    if not no_tk_mode == 1:
        print('why are you using cli like seriously')
    print (colored("0: Back",menu1))
    chan = input('Channel ID: ')
    if str(chan) == '0':
        main()
    msgid = input ("Message ID: ")
    emoji = input ("Emoji: ")
    p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','reaction',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),msgid,chan,"Add",emoji,chan],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Reaction Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def serversmasher():
    global currentattacks
    clear()
    if command_line_mode == 1:
        print ("The config file for the ServerSmasher is in RTBFiles/smconfig.py, please add token before starting.")
    if sys.platform.startswith('win32'):
        if server_smasher_in_main_window == 1:
            p = subprocess.Popen([sys.executable,'RTBFiles/ServerSmasher/serversmasher.py',"?",menu1,menu2,str(no_tk_mode)])
            p.wait()
        else:
            subprocess.Popen([sys.executable,'RTBFiles/ServerSmasher/serversmasher.py',"?",menu1,menu2,str(no_tk_mode)],creationflags=CREATE_NEW_CONSOLE)
    else:
        if server_smasher_in_main_window == 1:
            p = subprocess.Popen([sys.executable,'RTBFiles/ServerSmasher/serversmasher.py',"?",menu1,menu2,str(no_tk_mode)])
            p.wait()
        else:
            subprocess.call(['gnome-terminal', '-x', sys.executable,'RTBFiles/ServerSmasher/serversmasher.py',"?",menu1,menu2,str(no_tk_mode)])
    if server_smasher_in_main_window == 1:
        pass
    elif no_tk_mode == 1:
        pass
    elif command_line_mode == 1:
        time.sleep(5)
    main()

def viewcurrentat():
    global currentattacks
    clear()
    acount = -1
    names = []
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Current Attacks")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Current Attacks\x07")
    print (colored("Current Attacks:",menu1))
    print (colored("---------------------",menu1))
    for attack in list(currentattacks):
        if psutil.pid_exists(currentattacks[attack]):
            if not sys.platform.startswith('win32'):
                proc = psutil.Process(currentattacks[attack])
                if proc.status() == psutil.STATUS_ZOMBIE:
                    currentattacks.pop(attack)
                    continue
            acount += 1
            print (colored("{}. {}".format(acount,attack),menu2))
        else:
            currentattacks.pop(attack)
    for attack in list(currentattacks.keys()):
        names.append(attack)
    if currentattacks == {}:
        print (colored('None',"green"))
    print (colored("---------------------\nType 'killall' to end all current attacks, Or type the number to end that attack.",menu1))
    attacks = input()
    if attacks == '':
        main()
    elif attacks.lower() == 'killall':
        for attack in currentattacks:
            try:
                print(int(currentattacks[attack]))
                os.kill(int(currentattacks[attack]), 15)
            except Exception:
                pass
        currentattacks = {}
    else:
        try:
            os.kill(int(currentattacks[names[int(attacks)]]), 15)
        except Exception as e:
            print(e)
            input()
    main()

def customplugins():
    global currentattacks
    clear()
    pluginlist = {}
    pluginfile = []
    pluginfolder = []
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Custom Plugins (Legacy)")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Custom Plugins (Legacy)\x07")
    pluginno = -1
    print (colored("Installed Plugins:",menu1))
    print (colored("----------------------",menu1))
    for root, dirs, files in os.walk("legacyplugins/", topdown=False):
        for folder in dirs:
            try:
                plugdir = os.listdir('legacyplugins/{}/'.format(folder))
            except Exception:
                continue
            for file in plugdir:
                if str(file).startswith("main_"):
                    pluginlist[folder] = file
    for plugin in pluginlist:
        pluginno += 1
        pluginfolder.append(plugin)
        print (str(pluginno) +". "+ plugin)
    for plugin in pluginlist.items():
        pluginfile.append(plugin[1])
    print (colored("----------------------\nb: Back",menu1))
    print (colored("e: Kill all plugins\nd: Download plugins from Repo",menu1))
    plug = input ("Choice of plugin: ")
    if plug == 'b':
        main()
    if plug == 'e':
        pluginpids = open("pluginpids").readlines()
        for pid in pluginpids:
            try:
                os.kill(int(pid), 15)
            except Exception:
                pass
        os.remove('pluginpids')
        customplugins()
    if plug == 'd':
        clear()
        down = requests.get("https://github.com/DeadBread76/Raid-Toolbox-Plugins/archive/master.zip")
        with open("legacyplugins/package.zip", "wb") as handle:
            handle.write(down.content)
        shutil.unpack_archive("legacyplugins/package.zip","legacyplugins/")
        os.remove("legacyplugins/package.zip")
        for root, dirs, files in os.walk("legacyplugins/Raid-Toolbox-Plugins-master/", topdown=False):
            for folder in dirs:
                copy_tree("legacyplugins/Raid-Toolbox-Plugins-master/{}/".format(folder), "legacyplugins/{}/".format(folder+"/"))
        shutil.rmtree("legacyplugins/Raid-Toolbox-Plugins-master/")
        print("Downloaded plugins from Repo.")
        input("Press enter to reload plugins")
        customplugins()
    plugchoice = "{}/{}".format(pluginfolder[int(plug)],pluginfile[int(plug)])
    clear()
    p = subprocess.Popen([sys.executable,'legacyplugins/'+plugchoice,sys.executable,menu1])
    p.wait()
    customplugins()

def diagrun():
    global currentattacks
    print("Checking if CloudFlare Banned...")
    print("Checking Stable Endpoint...")
    cloudcheck = requests.get("https://discordapp.com/api/v6/invite/DEADBREAD")
    print("Checking PTB Endpoint...")
    ptbcloudcheck = requests.get("https://ptb.discordapp.com/api/v6/invite/DEADBREAD")
    print("Checking Canary Endpoint...")
    cancloudcheck = requests.get("https://canary.discordapp.com/api/v6/invite/DEADBREAD")
    try:
        json.loads(cloudcheck.content)
        stbanned = False
    except Exception:
        stbanned = True
    try:
        json.loads(ptbcloudcheck.content)
        ptbbanned = False
    except Exception:
        ptbbanned = True
    try:
        json.loads(cancloudcheck.content)
        banned = False
    except Exception:
        banned = True
    if no_tk_mode == 1:
        pass
    else:
        print("Getting CPU info...")
        cpu = cpuinfo.get_cpu_info()['brand']
    clear()
    print("CloudFlare Banned: {}".format(banned))
    if banned == True:
        print("You are CloudFlare banned on the canary endpoint.\nThis means the Joiner function and Regular Checker will not work.")
    now = datetime.datetime.now()
    filename = str(now.strftime("%H%M%S%d%m%Y"))
    with open ("Diagnostics" +filename+".txt", 'w+') as handle:
        handle.write("Raid Toolbox Diagnostics "+str(now.strftime("%d/%m/%Y %H:%M:%S"))+"\n")
        handle.write("=====================================================\n")
        handle.write("RTB VERSION: " + rtbversion + "\n")
        handle.write("SM VERSION: " + smversion + "\n")
        try:
            handle.write("Startup Time: {}".format(t1-t0)+"\n")
        except Exception:
            pass
        handle.write("Tokens Loaded: " + str(tcounter) + "\n")
        handle.write("---------------\n")
        handle.write("CloudFlare Ban Status\n\n")
        handle.write("Stable Endpoint: {}\n".format(stbanned))
        handle.write("PTB Endpoint: {}\n".format(ptbbanned))
        handle.write("Canary Endpoint: {}\n".format(banned))
        if banned:
            handle.write("The canary endpoint is used for RTB, This means some functions will not work.\n")
        handle.write("---------------\n")
        handle.write("Python Info:\n\n")
        handle.write("Python Version: " + sys.version+"\n")
        handle.write("---------------\n")
        handle.write("OS info:\n\n")
        handle.write("Platform: " + platform.platform()+"\n")
        if no_tk_mode == 1:
            handle.write("Processor: Not Supported on Termux\n")
        else:
            handle.write("Processor: " + (str(cpu))+"\n")
        handle.write("---------------\n")
        handle.write("RTB Dump:\n\n")
        plugindir = os.listdir('plugins/')
        handle.write(str(sys.modules.keys())+"\n")
        handle.write(str(dir())+"\n")
        handle.write(str(globals())+"\n")
        handle.write(str(locals())+"\n")
        handle.write("---------------\n")

@animation.wait(colored('Downloading update for Raid ToolBox, Please Wait ',menu1))
def run_update():
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Updating...")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Updating...\x07")
    update = requests.get('https://github.com/DeadBread76/Raid-Toolbox/archive/master.zip')
    clear()
    print(colored("Update has been downloaded, Installing...",menu1))
    with open("update.zip", "wb") as handle:
        handle.write(update.content)
    try:
        shutil.copy("RTBFiles/smconfig.py", "smconfig_old.py")
    except Exception:
        pass
    try:
        shutil.unpack_archive("update.zip")
        copy_tree("Raid-Toolbox-master/", ".")
        os.remove("update.zip")
        shutil.rmtree("Raid-Toolbox-master/")
        with open('config.json', 'r+') as handle:
            edit = json.load(handle)
            edit['skin'] = skin
            edit['thread_count'] = thread_count
            edit['verbose'] = verbose
            edit['disable_theme_music'] = disable_theme_music
            edit['command_line_mode'] = command_line_mode
            edit['no_tk_mode'] = no_tk_mode
            edit['disable_cloudflare_check'] = disable_cloudflare_check
            edit['disable_update_check'] = disable_update_check
            edit['server_smasher_in_main_window'] = server_smasher_in_main_window
            edit['ignore_ffmpeg_missing'] = ignore_ffmpeg_missing
            edit['combine_uverified_and_verified'] = combine_uverified_and_verified
            edit['show_licence'] = show_licence
            handle.seek(0)
            json.dump(edit, handle, indent=4)
            handle.truncate()
    except Exception as e:
        print("Error Updating, {}".format(e))

def info():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        os.system('mode con:cols=100 lines=30')
    else:
        os.system("printf '\033[8;30;100t'")
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Info")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Info\x07")
    print (colored("  _____       _     _   _______          _ ____            ",menu1))
    print (colored(" |  __ \     (_)   | | |__   __|        | |  _ \           ",menu1))
    print (colored(" | |__) |__ _ _  __| |    | | ___   ___ | | |_) | _____  __",menu1))
    print (colored(" |  _  // _` | |/ _` |    | |/ _ \ / _ \| |  _ < / _ \ \/ /",menu1))
    print (colored(" | | \ \ (_| | | (_| |    | | (_) | (_) | | |_) | (_) >  < ",menu1))
    print (colored(" |_|  \_\__,_|_|\__,_|    |_|\___/ \___/|_|____/ \___/_/\_\ ",menu1))
    print (colored("------------------------------------------------------------",menu1))
    print (colored("Copyright (c) 2019, DeadBread",menu1))
    print (colored("                                                            ",menu1))
    print (colored("https://github.com/DeadBread76/Raid-Toolbox",menu2))
    print (colored("Discord: https://discord.gg/7RtuZEe\nTelegram: https://t.me/DeadBakery",menu2))
    print (colored("                                                            ",menu1))
    if singlefile == True:
        print (colored("SINGLE FILE MODE ACTIVE",menu2))
    if no_tk_mode == 1:
        print (colored("Termux Mode.",menu2))
    print (colored("Raid ToolBox version: "+rtbversion,menu2))
    if verbose == 1:
        print(colored("\nStartup Time: {}".format(t1-t0),menu2))
    print (colored("                                                            ",menu1))
    print (colored("------------------------------------------------------------",menu1))
    print (colored("Type 'update' to update Raid ToolBox to the latest version.",menu2))
    print (colored("Type 'reinstall' to reinstall or update requirements",menu2))
    print (colored("Type 'diag' for diagnostics log.",menu2))
    print (colored("Type 'yt' for my YouTube channel.",menu2))
    print (colored("Type 'console' to access console.",menu2))
    print (colored("------------------------------------------------------------",menu1))
    inf = input(colored(">",menu2))
    if inf.lower() == "ree":
        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','ree',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme)])
        currentattacks["GOD Started at: {}".format(datetime.datetime.now().time())] = p.pid
    elif inf.lower() == 'yt':
        clear()
        webbrowser.open("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
        print("https://www.youtube.com/channel/UCqYFFmU9acsi2HBFItNH6bQ")
        input()
        info()
    elif inf.lower() == 'reinstall':
        if sys.platform.startswith('darwin'):
            requirements = open("requirements_mac.txt").read().splitlines()
        elif "com.termux" in sys.executable:
            requirements = open("requirements_termux.txt").read().splitlines()
        else:
            requirements = open("requirements.txt").read().splitlines()
        log = open("install.log", "w")
        for package in requirements:
            print("Installing {}...".format(package))
            p = subprocess.call([sys.executable, "-m", "pip", "install", package],stdout=log, stderr=subprocess.STDOUT)
            if p == 1:
                print("There was an error with installing the package {}, Refer to Install.log".format(package))
            elif p == 0:
                print("Installed {} Successfully.".format(package))
        input("Installation Complete.")
        info()
    elif inf.lower() == 'diag':
        clear()
        if singlefile == True:
            print("Not while Single file mode is active you don't.")
            input()
            info()
        if sys.platform.startswith('win32'):
            ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Diagnostics")
        else:
            sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Diagnostics\x07")
        diagrun()
        print ("Diagnostics Written to file.")
        input()
    elif inf.lower() == 'update':
        clear()
        if "b" in rtbversion:
            print("This is a test version of RTB, Please do not update.")
            input()
        else:
            u = input("Are you sure you want to update?(Y/N)\n")
            if u.lower() == 'y':
                clear()
                run_update()
                print ("Update complete, exiting.")
                time.sleep(3)
                sys.exit()
            else:
                info()
    elif inf.lower() == 'console':
        clear()
        print("0. Back")
        while True:
            try:
                com = input(">")
                if com == '0':
                    break
                elif com == 'os.remove("characters/monika.chr")':  # fuck i'm such a weeb
                    text = []
                    list = ['¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ā', 'ā', 'Ă', 'ă', 'Ą', 'ą', 'Ć', 'ć', 'Ĉ', 'ĉ', 'Ċ', 'ċ', 'Č', 'č', 'Ď', 'ď', 'Đ', 'đ', 'Ē', 'ē', 'Ĕ', 'ĕ', 'Ė', 'ė', 'Ę', 'ę', 'Ě', 'ě', 'Ĝ', 'ĝ', 'Ğ', 'ğ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ĥ', 'ĥ', 'Ħ', 'ħ', 'Ĩ', 'ĩ', 'Ī', 'ī', 'Ĭ', 'ĭ', 'Į', 'į', 'İ', 'ı', 'Ĳ', 'ĳ', 'Ĵ', 'ĵ', 'Ķ', 'ķ', 'ĸ', 'Ĺ', 'ĺ', 'Ļ', 'ļ', 'Ľ', 'ľ', 'Ŀ', 'ŀ', 'Ł', 'ł', 'Ń', 'ń', 'Ņ', 'ņ', 'Ň', 'ň', 'ŉ', 'Ŋ', 'ŋ', 'Ō', 'ō', 'Ŏ', 'ŏ', 'Ő', 'ő', 'Œ', 'œ', 'Ŕ', 'ŕ', 'Ŗ', 'ŗ', 'Ř', 'ř', 'Ś', 'ś', 'Ŝ', 'ŝ', 'Ş', 'ş', 'Š', 'š', 'Ţ', 'ţ', 'Ť', 'ť', 'Ŧ', 'ŧ', 'Ũ', 'ũ', 'Ū', 'ū', 'Ŭ', 'ŭ', 'Ů', 'ů', 'Ű', 'ű', 'Ų', 'ų', 'Ŵ', 'ŵ', 'Ŷ', 'ŷ', 'Ÿ', 'Ź', 'ź', 'Ż', 'ż', 'Ž', 'ž']
                    for x in range(random.randint(500,800)):
                        text.append(random.choice(list))
                    print("Unable to delete file: characters/monika.chr")
                    time.sleep(0.5)
                    for char in text:
                        time.sleep(0.005)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    clear()
                    print('0. Back')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    for char in 'os.remove("characters/sayori.chr")':
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('\nsayori.chr deleted successfully')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    time.sleep(1)
                    for char in 'os.remove("characters/yuri.chr")':
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('\nyuri.chr deleted successfully')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    time.sleep(1)
                    for char in 'os.remove("characters/natsuki.chr")':
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    print('\nnatsuki.chr deleted successfully')
                    sys.stdout.write('>')
                    sys.stdout.flush()
                    time.sleep(1)
                    for char in 'os.remove("RTB.py")':
                        time.sleep(0.10)
                        sys.stdout.write(char)
                        sys.stdout.flush()
                    os.rename("RTB.py", "RTBFiles/RTB.py")
                    print('\nRTB.py deleted successfully')
                    time.sleep(1)
                    while True:
                        print(asciigen(4000))
                exec(com)
            except Exception as e:
                print(e)
    main()

def quickcheck():
    global currentattacks
    clear()
    tokenlist = open("tokens/"+token_list).read().splitlines()
    for token in tokenlist:
        p = subprocess.Popen([sys.executable,'RTBFiles/attack_controller.py','quickcheck',sys.executable,str(no_tk_mode),str(thread_count),str(attacks_theme),token])
        time.sleep(0.07)
    p.wait()
    input("Checking complete.")
    main()

def tokenmanager():
    global currentattacks
    clear()
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | Token Manager")
    else:
        sys.stdout.write("\x1b]2;DeadBread's Raid ToolBox | Token Manager\x07")
    tokenlist = open("tokens/"+token_list).read().splitlines()
    print(colored("====================",menu1))
    print(colored("     Token Menu     ",menu1))
    print(colored("====================",menu1))
    print(colored("0. Return to main menu",menu2))
    print(colored("1. Add Token",menu2))
    print(colored("2. View Tokens",menu2))
    print(colored("3. View Token names and ID",menu2))
    print(colored("4. Token Checker",menu2))
    print(colored("5. Refresh Token list",menu2))
    print(colored("====================",menu1))
    e = input("Choice: ")
    try:
        if int(e) == 0:
            main()
        elif int(e) == 1:
            clear()
            print(colored("Input Token to add to tokens.txt\n0. Back",menu2))
            t = input()
            with open ("tokens/"+token_list,"a",errors='ignore') as handle:
                handle.write("{}\n".format(t))
            print (colored("Added {} to file.".format(t.rstrip()),menu1))
            input()
            tokenmanager()
        elif int(e) == 2:
            clear()
            if len(tokenlist) > 30:
                leng = 30
                leng += len(tokenlist)
                if sys.platform.startswith('win32'):
                    os.system('mode con:cols=100 lines={}'.format(leng))
                else:
                    os.system("printf '\033[8;{};100t'".format(leng))
            for token in tokenlist:
                print(colored(token,menu2))
            input()
            tokenmanager()
        elif int(e) == 3:
            clear()
            list = []
            if len(tokenlist) > 30:
                print("This May take a while, Continue? (Y/N)")
                h = input()
                if h.lower() == 'y':
                    pass
                else:
                    tokenmanager()
            if len(tokenlist) > 30:
                leng = 30
                leng += len(tokenlist)
                if sys.platform.startswith('win32'):
                    os.system('mode con:cols=100 lines={}'.format(leng))
                else:
                    os.system("printf '\033[8;{};100t'".format(leng))
            for token in tokenlist:
                apilink = 'https://canary.discordapp.com/api/v6/users/@me'
                headers = {'Authorization': token.rstrip(), 'Content-Type': 'application/json'}
                src = requests.get(apilink, headers=headers)
                if "401: Unauthorized" in str(src.content):
                    pass
                else:
                    response = json.loads(src.content.decode())
                    list.append(response['username']+"#"+response['discriminator']+" (ID: "+str(response['id'])+") ")
            for x in list:
                print (colored(x,menu2))
            input()
            tokenmanager()
        elif int(e) == 4:
            tokencheck()
        elif int(e) == 5:
            tokenlist.close()
            tokencheck()
    except Exception:
        tokenmanager()

def themesetting():
    global skin
    clear()
    while True:
        skinc = -1
        skinlist = []
        for file in os.listdir('themes'):
            if file.endswith(".py"):
                skinlist.append(file.replace(".py",""))
        print(colored("b. Go Back", menu2))
        for skin in skinlist:
            skinc += 1
            print(colored("{}. {}".format(skinc, skin), menu2))
        print(colored("====================\nType Number To Change Theme.",menu1))
        re = input("> ")
        if re.upper() == "B": # Fuck consistency
            main()
        else:
            try:
                new_skin = skinlist[int(re)]
                skin = new_skin
                if not skin == "DeadRed":
                    # Import Default Incase loaded skin has Missing Features/ Compatibility for older skins.
                    mdl = importlib.import_module("themes.DeadRed")
                    if "__all__" in mdl.__dict__:
                        names = mdl.__dict__["__all__"]
                    else:
                        names = [x for x in mdl.__dict__ if not x.startswith("_")]
                    globals().update({k: getattr(mdl, k) for k in names})
                # Import New Skin
                mdl = importlib.import_module("themes.{}".format(new_skin))
                if "__all__" in mdl.__dict__:
                    names = mdl.__dict__["__all__"]
                else:
                    names = [x for x in mdl.__dict__ if not x.startswith("_")]
                globals().update({k: getattr(mdl, k) for k in names})
                with open('config.json', 'r+') as handle:
                    edit = json.load(handle)
                    edit['skin'] = new_skin
                    handle.seek(0)
                    json.dump(edit, handle, indent=4)
                    handle.truncate()
            except Exception as e:
                print(e)
                input()
            else:
                main()


def settings():
    global currentattacks
    global thread_count
    global verbose
    global disable_theme_music
    global command_line_mode
    global no_tk_mode
    global disable_cloudflare_check
    global disable_update_check
    global server_smasher_in_main_window
    global ignore_ffmpeg_missing
    with open('config.json', 'r') as handle:
        toggleopts = json.load(handle)
    clear()
    while True:
        try:
            clear()
            print (colored("s:  Save Changes",menu2))
            print (colored("0.  Go back",menu2))
            print (colored("1.  Thread Count: {}".format(toggleopts['thread_count']),menu2))
            if toggleopts['verbose'] == 0:
                print (colored("2.  Verbose Load: False",menu2))
            elif toggleopts['verbose'] == 1:
                print (colored("2.  Verbose Load: True",menu2))
            else:
                toggleopts['verbose'] = 0
                print (colored("2.  Verbose Load: False",menu2))
            if toggleopts['disable_theme_music'] == 0:
                print (colored("3.  Disable theme music: False",menu2))
            elif toggleopts['disable_theme_music'] == 1:
                print (colored("3.  Disable theme music: True",menu2))
            else:
                toggleopts['disable_theme_music'] = 0
                print (colored("3.  Disable theme music: False",menu2))
            if toggleopts['command_line_mode'] == 0:
                print (colored("4.  Command line mode: False",menu2))
            elif toggleopts['command_line_mode'] == 1:
                print (colored("4.  Command line mode: True",menu2))
            else:
                toggleopts['command_line_mode'] = 0
                print (colored("4.  Command line mode: False",menu2))
            if toggleopts['disable_cloudflare_check'] == 0:
                print (colored("5.  Disable Cloudflare Check: False",menu2))
            elif toggleopts['disable_cloudflare_check'] == 1:
                print (colored("5.  Disable Cloudflare Check: True",menu2))
            else:
                toggleopts['disable_cloudflare_check'] = 0
                print (colored("5.  Disable Cloudflare Check: False",menu2))
            if toggleopts['disable_update_check'] == 0:
                print (colored("6.  Disable Update Checking: False",menu2))
            elif toggleopts['disable_update_check'] == 1:
                print (colored("6.  Disable Update Checking: True",menu2))
            else:
                toggleopts['disable_update_check'] = 0
                print (colored("6.  Disable Update Checking: False",menu2))
            if toggleopts['server_smasher_in_main_window'] == 0:
                print (colored("7.  ServerSmasher in main console: False",menu2))
            elif toggleopts['server_smasher_in_main_window'] == 1:
                print (colored("7.  ServerSmasher in main console: True",menu2))
            else:
                toggleopts['server_smasher_in_main_window'] = 0
                print (colored("7.  ServerSmasher in main console: False",menu2))
            if toggleopts['ignore_ffmpeg_missing'] == 0:
                print (colored("8.  Ignore FFMpeg Missing: False",menu2))
            elif toggleopts['ignore_ffmpeg_missing'] == 1:
                print (colored("8.  Ignore FFMpeg Missing: True",menu2))
            else:
                toggleopts['ignore_ffmpeg_missing'] = 0
                print (colored("8.  Ignore FFMpeg Missing: False",menu2))
            if toggleopts['no_tk_mode'] == 0:
                print (colored("9.  No tk mode: False",menu2))
            elif toggleopts['no_tk_mode'] == 1:
                print (colored("9.  No tk mode: True",menu2))
            else:
                toggleopts['no_tk_mode'] = 0
                print (colored("9.  No tk mode: False",menu2))
            if toggleopts['combine_uverified_and_verified'] == 0:
                print (colored("10. Combine uverified and verified: False",menu2))
            elif toggleopts['combine_uverified_and_verified'] == 1:
                print (colored("10. Combine uverified and verified: True",menu2))
            else:
                toggleopts['combine_uverified_and_verified'] = 0
                print (colored("10. Combine uverified and verified: False",menu2))
            settingsmenu = input("Item to toggle or change:\n")
            if settingsmenu.lower() == "s":
                thread_count = toggleopts['thread_count']
                disable_theme_music = toggleopts['disable_theme_music']
                verbose = toggleopts['verbose']
                command_line_mode = toggleopts['command_line_mode']
                no_tk_mode = toggleopts['no_tk_mode']
                disable_cloudflare_check =toggleopts['disable_cloudflare_check']
                disable_update_check = toggleopts['disable_update_check']
                combine_uverified_and_verified = toggleopts['combine_uverified_and_verified']
                server_smasher_in_main_window = toggleopts['server_smasher_in_main_window']
                ignore_ffmpeg_missing = toggleopts['ignore_ffmpeg_missing']
                with open('config.json', 'r+') as handle:
                    edit = json.load(handle)
                    edit['thread_count'] = thread_count
                    edit['token_list'] = token_list
                    edit['verbose'] = verbose
                    edit['disable_theme_music'] = disable_theme_music
                    edit['command_line_mode'] = command_line_mode
                    edit['disable_cloudflare_check'] = disable_cloudflare_check
                    edit['disable_update_check'] = disable_update_check
                    edit['server_smasher_in_main_window'] = server_smasher_in_main_window
                    edit['ignore_ffmpeg_missing'] = ignore_ffmpeg_missing
                    handle.seek(0)
                    json.dump(edit, handle, indent=4)
                    handle.truncate()
                    with open('config.json', 'r') as handle:
                        config = json.load(handle)
                        skin = config['skin']
                        thread_count = config['thread_count']
                        disable_theme_music = config['disable_theme_music']
                        verbose = config['verbose']
                        command_line_mode = config['command_line_mode']
                        no_tk_mode = config['no_tk_mode']
                        disable_cloudflare_check = config['disable_cloudflare_check']
                        disable_update_check = config['disable_update_check']
                        combine_uverified_and_verified = config['combine_uverified_and_verified']
                        server_smasher_in_main_window = config['server_smasher_in_main_window']
                        ignore_ffmpeg_missing = config['ignore_ffmpeg_missing']
                    clear()
                    print("Changes saved to config.")
                    input()
            elif int(settingsmenu) == 0:
                clear()
                main()
            elif int(settingsmenu) == 1:
                toggleopts['thread_count'] = input("Number of threads to use: ")
            elif int(settingsmenu) == 2:
                if toggleopts['verbose'] == 0:
                    toggleopts['verbose'] = 1
                elif toggleopts['verbose'] == 1:
                    toggleopts['verbose'] = 0
                else:
                    toggleopts['verbose'] = 0
            elif int(settingsmenu) == 3:
                if toggleopts['disable_theme_music'] == 0:
                    toggleopts['disable_theme_music'] = 1
                elif toggleopts['disable_theme_music'] == 1:
                    toggleopts['disable_theme_music'] = 0
                else:
                    toggleopts['disable_theme_music'] = 0
            elif int(settingsmenu) == 4:
                if toggleopts['command_line_mode'] == 0:
                    toggleopts['command_line_mode'] = 1
                elif toggleopts['command_line_mode'] == 1:
                    toggleopts['command_line_mode'] = 0
                else:
                    toggleopts['command_line_mode'] = 0
            elif int(settingsmenu) == 5:
                if toggleopts['disable_cloudflare_check'] == 0:
                    toggleopts['disable_cloudflare_check'] = 1
                elif toggleopts['disable_cloudflare_check'] == 1:
                    toggleopts['disable_cloudflare_check'] = 0
                else:
                    toggleopts['disable_cloudflare_check'] = 0
            elif int(settingsmenu) == 6:
                if toggleopts['disable_update_check'] == 0:
                    toggleopts['disable_update_check'] = 1
                elif toggleopts['disable_update_check'] == 1:
                    toggleopts['disable_update_check'] = 0
                else:
                    toggleopts['disable_update_check'] = 0
            elif int(settingsmenu) == 7:
                if toggleopts['server_smasher_in_main_window'] == 0:
                    toggleopts['server_smasher_in_main_window'] = 1
                elif toggleopts['server_smasher_in_main_window'] == 1:
                    toggleopts['server_smasher_in_main_window'] = 0
                else:
                    toggleopts['server_smasher_in_main_window'] = 0
            elif int(settingsmenu) == 8:
                if toggleopts['ignore_ffmpeg_missing'] == 0:
                    toggleopts['ignore_ffmpeg_missing'] = 1
                elif toggleopts['ignore_ffmpeg_missing'] == 1:
                    toggleopts['ignore_ffmpeg_missing'] = 0
                else:
                    toggleopts['ignore_ffmpeg_missing'] = 0
            elif int(settingsmenu) == 9:
                if toggleopts['no_tk_mode'] == 0:
                    toggleopts['no_tk_mode'] = 1
                elif toggleopts['no_tk_mode'] == 1:
                    toggleopts['no_tk_mode'] = 0
                else:
                    toggleopts['no_tk_mode'] = 0
            elif int(settingsmenu) == 10:
                if toggleopts['combine_uverified_and_verified'] == 0:
                    toggleopts['combine_uverified_and_verified'] = 1
                elif toggleopts['combine_uverified_and_verified'] == 1:
                    toggleopts['combine_uverified_and_verified'] = 0
                else:
                    toggleopts['combine_uverified_and_verified'] = 0
        except Exception as e:
            print(e)
            input()

def wew():
    global currentattacks
    if sys.platform.startswith('win32'):
        clear()
        ctypes.windll.kernel32.SetConsoleTitleW("DeadBread's Raid ToolBox | ¯\_(ツ)_/¯")
    else:
        main()
    p = subprocess.Popen([sys.executable,'RTBFiles/player.py',sys.executable],stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    currentattacks["Music! | Started at: {}".format(datetime.datetime.now().time())] = p.pid
    main()

def pud():
    clear()
    while True:
        if sys.platform.startswith('win32'):
            os.system('mode con:cols={} lines={}'.format(random.randint(10,100),random.randint(10,100)))
        else:
            os.system("printf '\033[8;{};{}t'".format(random.randint(10,100),random.randint(10,100)))
        time.sleep(0.1)

def asciigen(length):
    asc = ''
    for x in range(int(length)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc

def convert_bool(integer):
    if integer == 1:
        return True
    else:
        return False

def convert_integer(bool):
    if bool:
        return 1
    else:
        return 0

def aaa():
    clear()
    colours = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'grey', 'white']
    while True:
        try:
            if sys.platform.startswith('win32'):
                ctypes.windll.kernel32.SetConsoleTitleW("{}".format(asciigen(random.randint(51,101))))
            else:
                sys.stdout.write("\x1b]2;{}\x07".format(asciigen(random.randint(1,21))))
        except Exception:
            if sys.platform.startswith('win32'):
                os.system('mode con:cols=100 lines=30')
            else:
                os.system("printf '\033[8;30;100t'")
            clear()
            a = ""
            for x in range(100):
                a += "A"
            for x in range(30):
                print(colored(a,random.choice(colours)))
            time.sleep(1)
            aaa()
        text = ''
        for x in range(9999):
            text += colored(asciigen(1), random.choice(colours))
        print(text)

if __name__ == "__main__":
    # Token List Checking
    if not os.path.isdir("tokens"):
        os.mkdir("tokens")
    try:
        with open("tokens/{}".format(token_list),"r") as handle:
            line = handle.readlines()
            tcounter = len(line)
            if verbose == 1:
                print("Loaded {} Tokens".format(tcounter))
    except Exception:
        if command_line_mode == 0:
            window.Close()
            sg.Popup("No Token list set in config, Please choose one.", title="No token list.")
            layout = [
                [sg.Text('Choose a token list.')],
            ]
            lists = []
            for file in os.listdir("tokens"):
                if file.endswith(".txt"):
                    lists.append(file)
                    size = len(open("tokens/"+file).read().splitlines())
                    layout.append([sg.Text("{} ({} Tokens)".format(file,size), size=(45,1)), sg.Button("Select", key=file, size=(8,1))])
            if len(lists) == 0:
                layout.append([sg.Text("No Files in the tokens folder.", size=(45,1)), sg.Button("Create New...", size=(10,1))])
            else:
                layout.append([sg.Button("Create New...", size=(10,1)), sg.Button("Close", size=(10,1))])
            window = sg.Window("DeadBread's Raid ToolBox v{} | Choose Token list".format(rtbversion)).Layout(layout)
            while True:
                event, values = window.Read()
                if event is None:
                    main()
                elif event in lists:
                    token_list = event
                    with open('config.json', 'r+') as handle:
                        edit = json.load(handle)
                        edit['token_list'] = token_list
                        handle.seek(0)
                        json.dump(edit, handle, indent=4)
                        handle.truncate()
                    sg.Popup("List is now {}.".format(token_list), title="Done")
                elif event == "Create New...":
                    window.Close()
                    lay = [
                        [sg.Text('New List Name:', size=(16,1)), sg.Input(size=(20,1), key="LISTO")],
                        [sg.Button("OK", size=(7,1))]
                    ]
                    win = sg.Window("New Token list").Layout(lay)
                    while True:
                        ev, val = win.Read()
                        if ev is None:
                            del layout
                            win.Close()
                            layout = [
                                [sg.Text('Choose a token list.')],
                            ]
                            lists = []
                            for file in os.listdir("tokens"):
                                if file == "smtokens.txt":
                                    continue
                                else:
                                    lists.append(file)
                                    size = len(open("tokens/"+file).read().splitlines())
                                    layout.append([sg.Text("{} ({} Tokens)".format(file,size), size=(45,1)), sg.Button("Select", key=file, size=(8,1))])
                            if len(lists) == 0:
                                layout.append([sg.Text("No Files in the tokens folder.", size=(45,1)), sg.Button("Create New...", size=(8,1))])
                            else:
                                layout.append([sg.Button("Create New...", size=(10,1)), sg.Button("Close", size=(10,1))])
                            window = sg.Window("DeadBread's Raid ToolBox v{} | Choose Token list".format(rtbversion)).Layout(layout)
                            break
                        else:
                            try:
                                with open("tokens/{}.txt".format(val['LISTO']), "a+") as handle:
                                    handle.write("")
                            except Exception:
                                sg.Popup("Error Creating File (Is it a valid name?)", title="Error making file.")
                            del layout
                            win.Close()
                            layout = [
                                [sg.Text('Choose a token list.')],
                            ]
                            lists = []
                            for file in os.listdir("tokens"):
                                if file.endswith(".txt"):
                                    lists.append(file)
                                    size = len(open("tokens/"+file).read().splitlines())
                                    layout.append([sg.Text("{} ({} Tokens)".format(file,size), size=(45,1)), sg.Button("Select", key=file, size=(10,1))])
                            if len(lists) == 0:
                                layout.append([sg.Text("No Files in the tokens folder.", size=(45,1)), sg.Button("Create New...", size=(8,1))])
                            else:
                                layout.append([sg.Button("Create New...", size=(10,1)), sg.Button("Close", size=(10,1))])
                            window = sg.Window("DeadBread's Raid ToolBox v{} | Choose Token list".format(rtbversion)).Layout(layout)
                            break
                elif event == "Close":
                    window.Close()
                    main()

        else:
            print("No Token list found, Creating tokens.txt")
            with open("tokens/tokens.txt","w+") as handle:
                line = handle.readlines()
                tcounter = len(line)
                token_list = "tokens.txt"
            with open('config.json', 'r+') as handle:
                edit = json.load(handle)
                edit['token_list'] = token_list
                handle.seek(0)
                json.dump(edit, handle, indent=4)
                handle.truncate()


if __name__ == "__main__":
    # Check if audio is present in skin
    if command_line_mode == 0:
        try:
            menu_mp3
        except NameError:
            pass
        else:
            if menu_mp3_filename == "":
                pass
            elif not disable_theme_music == 1:
                # Start Audio
                if not os.path.exists("themes/{}".format(menu_mp3_filename)):
                    mp3_data = base64.b64decode(menu_mp3)
                    with open("themes/{}".format(menu_mp3_filename),"wb") as handle:
                        handle.write(mp3_data)
                    subprocess.Popen([sys.executable, 'RTBFiles/play.py', "Theme", "themes/"+menu_mp3_filename, skin, str(os.getpid()), str(menu_mp3_loop)])
                    del menu_mp3  # Remove MP3 from memory to save resources
                else:
                    subprocess.Popen([sys.executable, 'RTBFiles/play.py', "Theme", "themes/"+menu_mp3_filename, skin, str(os.getpid()), str(menu_mp3_loop)])
                    del menu_mp3  # Remove MP3 from memory to save resources
    if sys.platform.startswith('win32'):
        if command_line_mode == 1:
            t = threading.Thread(name='Title Update', target=titleupdate)
            t.start()
    while True:
        try:
            main()
        except Exception as e:
            if command_line_mode == 1 or no_tk_mode ==1:
                clear()
                exception = ''
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
                for line in trace:
                    exception += line
                yesno = input(f"Raid ToolBox Crashed: {repr(e)}\nDetails:\n{exception}\n\nReport to DeadBread? (No revealing data is sent.)[Y/N]: ")
                if yesno.lower() == "y":
                    payload = {"content": f"```{exception}```"}
                    try:
                        requests.post(h, json=payload)
                    except Exception:
                        pass
            else:
                try:
                    window.Close()
                except Exception:
                    pass
                exception = ''
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
                for line in trace:
                    exception += line
                yesno = sg.PopupYesNo(f"Raid ToolBox Crashed: {repr(e)}\nDetails:\n{exception}\n\nReport to DeadBread? (No revealing data is sent.)", title="Raid ToolBox Crashed :'(")
                if yesno == "Yes":
                    payload = {"content": f"```{exception}```"}
                    try:
                        requests.post(h, json=payload)
                    except Exception:
                        pass
                    else:
                        sg.PopupNonBlocking('Reported to DeadBread. Thanks!', title="Done.",keep_on_top=True)
