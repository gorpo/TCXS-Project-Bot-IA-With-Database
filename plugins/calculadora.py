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

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin


async def calculadora(msg):
    if msg.get('text'):
        try:
            if '+' in msg['text']:
                n1 = int(msg['text'].split('+')[0])
                n2 = int(msg['text'].split('+')[1])
                calc = n1 + n2
                await bot.sendMessage(msg['chat']['id'],'`Sua soma  {}+{}={} {} seu pau no cu!`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                          reply_to_message_id=msg['message_id'])
                return True

            if '-' in msg['text']:
                n1 = int(msg['text'].split('-')[0])
                n2 = int(msg['text'].split('-')[1])
                calc = n1 - n2
                await bot.sendMessage(msg['chat']['id'],'`Sua subtração  {}-{}={} {}seu filho da puta!`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                          reply_to_message_id=msg['message_id'])
                return True

            if '*' in msg['text']:
                n1 = int(msg['text'].split('*')[0])
                n2 = int(msg['text'].split('*')[1])
                calc = n1 * n2

                await bot.sendMessage(msg['chat']['id'],'`Sua multiplicação {}*{}={} {} seu arrombado do caralho!`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                          reply_to_message_id=msg['message_id'])
                return True

            if 'div' in msg['text']:
                n1 = int(msg['text'].split('/')[0])
                n2 = int(msg['text'].split('/')[1])
                calc = n1 / n2

                await bot.sendMessage(msg['chat']['id'],'`Sua divisão {}/{}={} {} seu lixo`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                          reply_to_message_id=msg['message_id'])
        except:
            pass
            return True              

        