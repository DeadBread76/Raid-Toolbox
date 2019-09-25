import sys
import datetime
import importlib
import subprocess
import plugins.helper

def plugin_launch():
    mdl = importlib.import_module("themes.{}".format(plugins.helper.skin))
    if "__all__" in mdl.__dict__:
        names = mdl.__dict__["__all__"]
    else:
        names = [x for x in mdl.__dict__ if not x.startswith("_")]
    globals().update({k: getattr(mdl, k) for k in names})
    p = subprocess.Popen([sys.executable, 'plugins/Additional/ghostpingmenu.py', str(attacks_theme)], stdout=open("errors.log", "a+"), stderr=subprocess.STDOUT)
    plugins.helper.attack_dict["Ghost Ping Spammer | Started at: {}".format(datetime.datetime.now().time())] = p.pid
