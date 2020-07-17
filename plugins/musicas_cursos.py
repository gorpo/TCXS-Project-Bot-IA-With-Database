
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]


import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

async def musicas_cursos(msg):
    if msg.get('text'):


  
        if 'post malone' in msg['text']:
            await bot.sendMessage(msg['chat']['id'], 'Eu curto esta do Post Malone --> https://www.youtube.com/watch?v=UceaB4D0jpo',reply_to_message_id=msg['message_id'])
        
        if 'gg allin' in msg['text']:
            await bot.sendMessage(msg['chat']['id'], 'Eu curto esta do GG --> https://www.youtube.com/watch?v=hcMD9hO1vg8',reply_to_message_id=msg['message_id'])
        
        if 'barbaric usa' in msg['text']:
            await bot.sendMessage(msg['chat']['id'], 'Eu curto esta do barbaric --> https://www.youtube.com/watch?v=jNr0SUjJy-U',reply_to_message_id=msg['message_id'])
        
        







            return True
