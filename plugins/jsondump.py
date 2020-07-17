
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin


import json
from io import BytesIO



async def jsondump(msg):
    if msg.get('text'):
        if msg['text'].startswith('/jsondump') or msg['text'].startswith('!jsondump') or msg[
            'text'] == '/jsondump@' + bot_username or msg['text'].startswith('jsondump'):
            msgjson = json.dumps(msg, indent=2, sort_keys=False)
            print('Usuario {} solicitou /jsondump'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /jsondump  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if '-f' not in msg['text'] and len(msgjson) < 4080:
                await bot.sendMessage(msg['chat']['id'], '<pre>' + html.escape(msgjson) + '</pre>',
                                      'html', reply_to_message_id=msg['message_id'])
            else:
                await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                file = BytesIO(msgjson.encode())
                file.name = "dump.json"
                await bot.sendDocument(msg['chat']['id'], file,
                                       reply_to_message_id=msg['message_id'])
            return True
