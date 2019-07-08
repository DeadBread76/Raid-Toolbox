# Server Smasher Config File
# The options here should be used for quick destruction presets.
# If You somehow messed up this file, get a replacement here: https://raw.githubusercontent.com/DeadBread76/Raid-Toolbox/master/spammer/smconfig.py

usemultiple = True #Use multiple tokens, add them into the text file called "smtokens.txt"
token = "TOKEN HERE" #Supports user accounts, although it is untested
clienttype = "bot" #'bot' is for bot accounts, 'user' is for user accounts (with the perms)
threadcount = 800 #Ammount of threads to use, You shouldnt need to change this.


#Legacy Preset#
changegameonlogin = False #True Changes the playing game on login.
logingame = "game here" #Name of the name to play on login.
namechange = False #True to change name. Can sometimes glitch and not let anyone change the name.
servname = "Server name" #only required if the above is True
iconbegone = False #True removes icon. Do not use with chnage icon enabled also.
changeicon = False #True Changes icon to a file specified below.
iconfile = 'path to icon here' #Put the image in the "serversmasher" folder
rembans = False #True Removes all banned users for a server
chandel = False #True deletes all channels
roledel = False #True deletes all roles underneath the bots role
userban = False #True bans all members, except the ones below. you can add as many as you like.
banreason = "Ban Reason here"
userid = [] # Example: ['user#3981','user#7579']
senddm = False #True sends everyone a DM, specified below.
dmcontent = "DM HERE"
createchan = False #True creates channels, using the method below
chanmethod = "ascii" #'ascii' for random ascii name, 'set' for set name below, 'voice' for a voice channel with the name below(If voice and channel deletion is enabled you will not be able to use spam methods).
channame = "" #Name of the channels to create
channelno = "100" #ammount of channels, the limit for discord is 500
usespam = False #True enables spam after everything is complete.
spammethod = "everyone" #"massment" for mass mention, "asc" for random ascii spam, "text" for custom text spam, everyone for fast @everyone spam.
usetts = "false" #(true or false), for the spam.
customtxt = "" #only if you use text spam method
gimmieadmin = False #True Gives you an admin role.
me = 'ID HERE' #put your client ID here if you enable gimmieadmin
giveeveryoneadmin = False #True gives @everyone admin. Works best if you dont ban them ¯\_(ツ)_/¯
createroles = False #True creates roles, amount specified below
crolecount = 100 #Amount of roles to create
rolesname = "ascii" #'set' for custom names, 'ascii' for random ascii names.
custrolename = 'ROLE NAME HERE' #Name for the set roles
deleteemojis = False
createemojis = False
emojipath = 'Path to emoji image here'
emojinum = 30
