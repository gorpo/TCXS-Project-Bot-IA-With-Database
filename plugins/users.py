

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, bot_username


async def users(msg):
    if msg.get('text'):
        if msg['from']['first_name']:

            print('->Usuario:{} ->Envio:{} ->Grupo:{} ->Data/Hora:{} '.format(msg['from']['first_name'],msg['text'],msg['chat']['title'],time.ctime()))
            log = '\n->Usuario:{} ->Envio:{} ->Grupo:{} ->Data/Hora:{} '.format(msg['from']['first_name'],msg['text'],msg['chat']['title'],time.ctime())
            #arquivo = open('logs/users.txt','a')
            #arquivo.write(log)
            #arquivo.close()

        
        if msg['text'].split()[0] == 'logs':

            await bot.sendDocument(msg['chat']['id'], open('logs/users.txt','rb'), reply_to_message_id=msg['message_id'])    
            await bot.sendMessage(msg['chat']['id'], '`{} Esta aqui o log de conversas que tenho armazenado, espero que não tenha nada neste log que te incrimine!`'.format(msg['from']['first_name']),'markdown', reply_to_message_id=msg['message_id'])    
       
    











  
