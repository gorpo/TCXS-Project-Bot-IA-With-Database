
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin


async def dice(msg):
    if msg.get('text'):
        if msg['text'] == '/dados' or msg['text'] == 'dados' or msg['text'] == '/dados@' + bot_username:
            

            dados = random.randint(1, 6)
            print('Usuario {} solicitou /dados'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /dados  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            await bot.sendMessage(msg['chat']['id'], '🎲 O dado parou no número: {}'.format(dados),
                                  reply_to_message_id=msg['message_id'])
            return True
        if msg['text'] == 'shemale':
            dados = random.randint(1,100)
            await bot.sendMessage(msg['chat']['id'], 'Você esta {}% shemale hoje.'.format(dados),
                                  reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'], document='CgACAgQAAx0CViT8vwABA6-3Xl1vBd53xqknuyULa2YPoYB3w24AAmgJAAIz6iBR5pLYRkLVaC4YBA', reply_to_message_id=msg['message_id'])
            
            return True
