import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username, keys
from utils import send_to_dogbin, send_to_hastebin

from datetime import date ,datetime, timezone, timedelta
async def hora_data(msg):
    if msg.get('text'):
        #hora e data  --- obrigado ao guanabara pelo curso gratis kkjj
        if msg['text'] == 'que dia e hoje' or msg['text'] == 'Que dia é hoje' or msg['text'] == 'que dia é hoje' or msg['text'] == 'data':
            print('Usuario {} solicitou data'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou data  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
        	#d = date.today()
            t = time.localtime()
            await bot.sendMessage(msg['chat']['id'],'Hoje é  {}/{}/{} e faltam poucos dias para começar a guerra!'.format(t[2],t[1],t[0]),reply_to_message_id=msg['message_id'])
        if msg['text'] == 'que hora é agora' or msg['text'] == 'que horas são agora' or msg['text'] == 'que hora e agora' or msg['text'] == 'que horas sao agora' or msg['text'] == 'Que hora é agora' or msg['text'] == 'Que hora é agora?' or  msg['text'] == 'Que horas são agora' or msg['text'] == 'Que horas são agora?' or msg['text'] == 'Que horas são?' or msg['text'] == 'Que horas são ' or msg['text'] == 'que horas são ' or msg['text'] == 'que horas sao' or msg['text'] == 'hora' or msg['text'] == 'que hora e agora':
            t = time.localtime()
            print('Usuario {} solicitou hora'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou hora  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            await bot.sendMessage(msg['chat']['id'],'Agora são {}:{}:{} e você pode morrer a qualquer momento!'.format(t[3],t[4],t[5]),reply_to_message_id=msg['message_id'])
       



        






























            return True
