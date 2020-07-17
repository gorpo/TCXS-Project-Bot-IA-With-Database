import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username, keys
from utils import send_to_dogbin, send_to_hastebin

giphy_key = keys['giphy']


async def gif(msg):
    if msg.get('text'):
        if msg['text'].startswith('/gif') or msg['text'].startswith('gif'):
            text = msg['text'][5:]
            
            async with aiohttp.ClientSession() as session:
                r = await session.get("http://api.giphy.com/v1/gifs/search",
                                      params=dict(q=text, api_key=giphy_key, limit=7))
                rjson = await r.json()
            if rjson["data"]:
                res = random.choice(rjson["data"])
                result = res["images"]["original_mp4"]["mp4"]
                await bot.sendVideo(msg['chat']['id'], result,
                                    reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], "Sem resultados",
                                      reply_to_message_id=msg['message_id'])
            return True

        if msg['text'].startswith('/gif@gorpo_bot'):
            
            text = msg['text'][14:]
            async with aiohttp.ClientSession() as session:
                r = await session.get("http://api.giphy.com/v1/gifs/search",
                                      params=dict(q=text, api_key=giphy_key, limit=7))
                rjson = await r.json()
            if rjson["data"]:
                res = random.choice(rjson["data"])
                result = res["images"]["original_mp4"]["mp4"]
                await bot.sendVideo(msg['chat']['id'], result,
                                    reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(msg['chat']['id'], "Sem resultados",
                                      reply_to_message_id=msg['message_id'])
            return True    
