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
        if '+' in msg['text']:
            n1 = int(msg['text'].split('+')[0])
            n2 = int(msg['text'].split('+')[1])
            calc = n1 + n2

            print('Usuario {} solicitou a calculadora  {}+{}={} '.format(msg['from']['first_name'],n1,n2,calc))
            log = '\nUsuario {} solicitou a calculadora  {}+{}={} --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],n1,n2,calc,msg['chat']['title'],time.ctime())
            arquivo = open('logs/calc.txt','a')
            arquivo.write(log)
            arquivo.close()

            await bot.sendMessage(msg['chat']['id'],'`Sua soma  {}+{}={} {} seu pau no cu!`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True    

        if '-' in msg['text']:
            n1 = int(msg['text'].split('-')[0])
            n2 = int(msg['text'].split('-')[1])
            calc = n1 - n2
            print('Usuario {} solicitou a calculadora  {}-{}={}'.format(msg['from']['first_name'],n1,n2,calc))
            log = '\nUsuario {} solicitou a calculadora  {}-{}={} --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],n1,n2,calc,msg['chat']['title'],time.ctime())
            arquivo = open('logs/calc.txt','a')
            arquivo.write(log)
            arquivo.close()
            await bot.sendMessage(msg['chat']['id'],'`Sua subtração  {}-{}={} {}seu filho da puta!`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True  
            
        if '*' in msg['text']:
            n1 = int(msg['text'].split('*')[0])
            n2 = int(msg['text'].split('*')[1])
            calc = n1 * n2
            print('Usuario {} solicitou a calculadora  {}*{}={}'.format(msg['from']['first_name'],n1,n2,calc))
            log = '\nUsuario {} solicitou a calculadora  {}*{}={} --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],n1,n2,calc,msg['chat']['title'],time.ctime())
            arquivo = open('logs/calc.txt','a')
            arquivo.write(log)
            arquivo.close()
            await bot.sendMessage(msg['chat']['id'],'`Sua multiplicação {}*{}={} {} seu arrombado do caralho!`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True  
            
        if 'div' in msg['text']:
            n1 = int(msg['text'].split('/')[0])
            n2 = int(msg['text'].split('/')[1])
            calc = n1 / n2
            print('Usuario {} solicitou a calculadora  {}/{}={}'.format(msg['from']['first_name'],n1,n2,calc))
            log = '\nUsuario {} solicitou a calculadora  {}/{}={} --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],n1,n2,calc,msg['chat']['title'],time.ctime())
            arquivo = open('logs/calc.txt','a')
            arquivo.write(log)
            arquivo.close()
            await bot.sendMessage(msg['chat']['id'],'`Sua divisão {}/{}={} {} seu lixo`'.format(n1,n2,calc,msg['from']['first_name']), 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True              

        