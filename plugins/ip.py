
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin



async def ip(msg):
    if msg.get('text'):
        if msg['text'].split()[0] == '/ip' or msg['text'].split()[0] == '!ip':
            text = msg['text'][4:].split('://')[-1]
            
            if text == '':
                await bot.sendMessage(msg['chat']['id'], '*Uso:* `/ip IP/endereço`',
                                      parse_mode='Markdown',
                                      reply_to_message_id=msg['message_id'])
            else:
                async with aiohttp.ClientSession() as session:
                    r = await session.get('http://ip-api.com/json/' + text)
                    req = await r.json()
                x = ''
                for i in req:
                    x += "*{}*: `{}`\n".format(i.title(), req[i])
                await bot.sendMessage(msg['chat']['id'], x, 'Markdown',
                                      reply_to_message_id=msg['message_id'])
       
            














































            return True
