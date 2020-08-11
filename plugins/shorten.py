
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

async def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('/shorten'):
            text = msg['text'][9:]
            if not text:
                await bot.sendMessage(msg['chat']['id'],
                                      '*Uso:* `/shorten google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml',
                                      'Markdown',
                                      reply_to_message_id=msg['message_id'])
            else:
                async with aiohttp.ClientSession() as session:
                    r = await session.post('https://url-shortener-service.p.rapidapi.com/shorten', data=dict(url=text))
                    res = await r.json()
                await bot.sendMessage(msg['chat']['id'], '*Resultado:* `{}`'.format(res), 'Markdown',
                                      reply_to_message_id=msg['message_id'])
            return True


from config import bot

