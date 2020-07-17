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
#     |        Github Gorpo Dev: https://github.com/gorpo         |
#     [+]   Thanks: https://github.com/AmanoTeam/amanobot       [+]
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username, keys
from utils import send_to_dogbin, send_to_hastebin


async def git(msg):
    if msg.get('text'):
        if msg['text'].startswith('/git ') or msg['text'].startswith('!git') or msg['text'].startswith('git'):
            text = msg['text'][5:]
            
            async with aiohttp.ClientSession() as session:
                req = await session.get('https://api.github.com/users/' + text)
                res = await req.json()
            if not res.get('login'):
                return await bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                             reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'''*Nome:* `{res["name"]}`
*Login:* `{res["login"]}`
*Localização:* `{res["location"]}`
*Tipo:* `{res["type"]}`
*Bio:* `{res["bio"]}`''', 'Markdown',
                                      reply_to_message_id=msg['message_id'])
            return True


        if msg['text'].startswith('git') :
            text = msg['text'][4:]
            
            async with aiohttp.ClientSession() as session:
                req = await session.get('https://api.github.com/users/' + text)
                res = await req.json()
            if not res.get('login'):
                return await bot.sendMessage(msg['chat']['id'], 'Usuário "{}" não encontrado.'.format(text),
                                             reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], f'''*Nome:* `{res["name"]}`
*Login:* `{res["login"]}`
*Localização:* `{res["location"]}`
*Tipo:* `{res["type"]}`
*Bio:* `{res["bio"]}`''', 'Markdown',
                                      reply_to_message_id=msg['message_id'])
            return True