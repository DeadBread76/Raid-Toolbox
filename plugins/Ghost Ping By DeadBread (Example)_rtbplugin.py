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
import json
import datetime
import importlib
import subprocess
sys.path.append('..')
import RTBFiles.attack_dict

def plugin_launch():
    with open('./config.json', 'r') as handle:
        config = json.load(handle)
        skin = config['skin']
    mdl = importlib.import_module("themes.{}".format(skin))
    if "__all__" in mdl.__dict__:
        names = mdl.__dict__["__all__"]
    else:
        names = [x for x in mdl.__dict__ if not x.startswith("_")]
    globals().update({k: getattr(mdl, k) for k in names})
    p = subprocess.Popen([sys.executable, 'plugins/Additional/ghostpingmenu.py', str(attacks_theme)], stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    RTBFiles.attack_dict.currentattacks["Ghost Ping Spammer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
