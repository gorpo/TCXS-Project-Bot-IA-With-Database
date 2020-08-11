
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

from db_handler import conn, cursor
from .admins import is_admin


def get_rules(chat_id):
    cursor.execute('SELECT rules FROM chats WHERE chat_id = (?)', (chat_id,))
    try:
        return cursor.fetchone()[0]
    except IndexError:
        return None


def set_rules(chat_id, rules):
    cursor.execute('UPDATE chats SET rules = ? WHERE chat_id = ?', (rules, chat_id))
    conn.commit()


async def rules(msg):
    if msg.get('text'):

        if msg['text'].startswith('/start_rules'):
            chat_id = msg['text'].split('_')[1]
            print('Usuario {} solicitou /start_rules'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /start_rules  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            rules = get_rules(int(chat_id)) or 'Sem regras!'

            await bot.sendMessage(msg['chat']['id'], rules, 'Markdown')
            return True


        elif msg['text'] == '/rules' or msg['text'] == '!rules' or msg['text'] == '/regras' or msg[
            'text'] == 'regras' or msg['text'] == '/regras@' + bot_username or msg['text'] == '/rules@' + bot_username:
            print('Usuario {} solicitou /rules'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /rules  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            rules = get_rules(msg['chat']['id']) or 'Sem regras!'

            await bot.sendMessage(msg['chat']['id'], rules, 'Markdown',reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].split()[0] == '/defrules' or msg['text'].split()[0] == '/defregras' or msg['text'].split()[
            0] == '/defregras' or msg['text'].split()[0] == '!defregras' or msg['text'].split()[
            0] == '/defregras@' + bot_username or msg['text'].split()[0] == '/defrules@' + bot_username:
            print('Usuario {} solicitou /def_rules'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /def_rules  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if (await is_admin(msg['chat']['id'], msg['from']['id']))['user']:
                if len(msg['text'].split()) == 1:
                    await bot.sendMessage(msg['chat']['id'], 'Uso: /defregras Regras do grupo (suporta Markdown)',
                                          reply_to_message_id=msg['message_id'])
                elif msg['text'].split()[1] == 'reset':
                    set_rules(msg['chat']['id'], None)
                    await bot.sendMessage(msg['chat']['id'], 'As regras do grupo foram redefinidas com sucesso.',
                                          reply_to_message_id=msg['message_id'])
                else:
                    set_rules(msg['chat']['id'], msg['text'].split(' ', 1)[1])
                    await bot.sendMessage(msg['chat']['id'], 'As regras do grupo foram definidas com sucesso.',
                                          reply_to_message_id=msg['message_id'])
            return True
