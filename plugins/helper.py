#!/usr/bin/env python3
# plugins.helper
# Author: DeadBread76 - https://github.com/DeadBread76/
# August 12th, 2019
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

"""
Documentation

Load plugin helper:

import plugins.helper

Config.json values are stored as plugins.helper.skin, plugins.helper.token_list, etc.

Write to Attack Manager dict (This is for using subprocess):

plugins.helper.attack_dict["Example"] = p.pid

"""

import sys
import json
import importlib
sys.path.append('..')
import RTBFiles.attack_dict

attack_dict = RTBFiles.attack_dict.currentattacks
with open('./config.json', 'r') as handle:
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
