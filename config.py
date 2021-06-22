# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]

import amanobot
import amanobot.aio
import asyncio
import os



#LOCAL CONFIG rodar em local host use as linhas abaixo---> "893192395:AAGUm_2rdfwz9Uxc_O7H8WneEzup3XSfNYU"
token = "893192395:AAGUm_2rdfwz9Uxsdfsdfsdfsfsdfsdf"
# marcinho'1096480409:AAE6sg6eJZtH5Zeeeewer_TEIzgq10SQtCvGf4KYSc' #TOken do
# luppy"893192395:AAGUm_2rdfwz9Uxc_O7H8Wnwerg44eEzup3XSfNYU"

token_dropbox = 's4rxVFP2mcAAAAAAAAC2eXinDL33K444sdfx0tSIhnR1csdfsdfsdfm5'


#permissoes
logs = -1001215sdfsdf401730    #-100121540173sdfsdfsdf0
sudoers = [522510sdfsdf051,]
administradores = [52251sdfsdf0051,]



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
    here = {'app_id': 'key_id_here', 'app_code': 'key_code_here'},  # https://here.com
    yandex = 'trnsl.1.1.20190811T184100Z.f3e1e6d6d350752sdfsdfsdf5.7ea9c786af32b18cedeb125ca46cc2d9ee154e09',#https://tech.yandex.com/translate
    giphy = '7f6ws7EvslO9BuaAKsdfsdfsdfie9BieyYnD3OkkT',# https://developers.giphy.com
)


backups_chat = 52251eeeeee0051  # Put a 0, False or None to disable ou seu id privado ou id privado de um canal ou grupo
backup_hours = ['12:45']

git_repo = ('https://github.com/gorpoorko/Manicomio-Bot-IA', 'master') #repositorio para upgrade do bot
max_time = 60
version = '7.0'

enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'shorten',
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
    'tcxs',
    'hora_data',
    'trollagens',
    'randomicas',
    'calculadora',
    'users',
    'inteligencia',
    'permanencia',
    'dropbox_upload',
    'link_direto',
    'antiflood',
    'avatar',
    'notepad_telegraph',
    'cria_site_telegraph',
    'qrcode',
    'ia_privado_bot'

]
