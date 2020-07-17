import amanobot
import amanobot.aio
import asyncio
import os


#LOCAL CONFIG rodar em local host use as linhas abaixo--->
token = "1186597860:AAGVtPY-1nHFdufqXDe06lI66UG9ttlwbVM"
logs = -1001215401730
sudoers = [522510051]

#HEROKU CONFIG - rodar no heroku use as linhas abaixo------->
#token = os.environ['TELEGRAM_TOKEN']
#logs = os.environ['LOGS']
#sudoers = os.environ['SUDOERS']


#----------------------------------------------------
loop = asyncio.get_event_loop()  # Do not change this
bot = amanobot.aio.Bot(token)
na_bot = amanobot.Bot(token)
me = loop.run_until_complete(bot.getMe())
bot_username = me['username']
bot_id = me['id']
keys = dict(
    here = {'app_id': 'key_id_here', 'app_code': 'key_code_here'},  #You can get a key at https://here.com
    yandex = 'trnsl.1.1.20190811T184100Z.f3e1e6d6d3507525.7ea9c786af32b18cedeb125ca46cc2d9ee154e09',                                            #You can get a key at https://tech.yandex.com/translate
    giphy = '7f6ws7EvslO9BuaAKie9BieyYnD3OkkT',#You can get a key at https://developers.giphy.com
)

git_repo = ('https://github.com/', 'master') #Repository where your bot is in

max_time = 60

version = open('version.txt').read()

backups_chat = 0  # Put a 0, False or None to disable.
backup_hours = ['00:00', '12:00']

enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'shorten',
    'sed',
    'kibe',
    'translate',
    'rextester',
    'inlines',
    'welcome',
    'admins',
    'warns',
    'prints',
    'pypi',
    'weather',
    'youtube',
    'ping',
    'gif',
    'git',
    'reddit',
    'coub',
    'sudos',
    'ids',
    'ip',
    'jsondump',
    'dice',
    'misc',
    'antipedro',
    'tcxs',
    'hora_data',
    'trollagens',
    'randomicas',
    'tcxs_xml',
]