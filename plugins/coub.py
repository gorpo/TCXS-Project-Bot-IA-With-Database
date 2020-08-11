

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

async def coub(msg):
    if msg.get('text'):
       

        if msg['text'].startswith('/coub@gorpo_bot'):
            text = msg['text'][16:]
            
            try:
                print('Usuario {} solicitou /coub@gorpo_bot'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /coub@gorpo_bot  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()

                async with aiohttp.ClientSession() as session:
                    r = await session.get(f'https://coub.com/api/v2/search/coubs?q={text}')
                    rjson = await r.json()
                content = random.choice(rjson['coubs'])
                links = content['permalink']
                title = content['title']

                await bot.sendMessage(msg['chat']['id'], f'*{title}*[\u00AD](https://coub.com/v/{links})',
                                      reply_to_message_id=msg['message_id'], parse_mode="Markdown")
                

            except IndexError:
                await bot.sendMessage(msg['chat']['id'], 'Not Found!', reply_to_message_id=msg['message_id'])
                
            return True
        
        if msg['text'].startswith('/coub') or msg['text'].startswith('coub'):
            text = msg['text'][4:]
            
            try:
                print('Usuario {} solicitou /coub'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /coub  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                async with aiohttp.ClientSession() as session:
                    r = await session.get(f'https://coub.com/api/v2/search/coubs?q={text}')
                    rjson = await r.json()
                content = random.choice(rjson['coubs'])
                links = content['permalink']
                title = content['title']
                
                await bot.sendMessage(msg['chat']['id'], f'*{title}*[\u00AD](https://coub.com/v/{links})',
                                      reply_to_message_id=msg['message_id'], parse_mode="Markdown")

            except IndexError:
                await bot.sendMessage(msg['chat']['id'], 'Not Found!', reply_to_message_id=msg['message_id'])
                
            return True
   