# -*- coding: utf-8 -*-
#███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
#████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
#██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
#██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
#██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
#╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
#     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
#     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
#     |        Github Gorpo Dev: https://github.com/gorpo         |
#     [+]   Thanks: https://github.com/AmanoTeam/amanobot       [+]
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username, bot_id
from amanobot.namedtuple import InlineKeyboardMarkup
from utils import escape_markdown
from db_handler import conn, cursor
from .admins import is_admin


def get_welcome(chat_id):
    cursor.execute('SELECT welcome, welcome_enabled FROM chats WHERE chat_id = (?)', (chat_id,))
    try:
        return cursor.fetchone()
    except IndexError:
        return None


def set_welcome(chat_id, welcome):
    cursor.execute('UPDATE chats SET welcome = ? WHERE chat_id = ?', (welcome, chat_id))
    conn.commit()


def enable_welcome(chat_id):
    cursor.execute('UPDATE chats SET welcome_enabled = ? WHERE chat_id = ?', (True, chat_id))
    conn.commit()


def disable_welcome(chat_id):
    cursor.execute('UPDATE chats SET welcome_enabled = ? WHERE chat_id = ?', (False, chat_id))
    conn.commit()


async def welcome(msg):
    if msg.get('text'):
        if msg['text'].split()[0] == '/welcome' or msg['text'].split()[0] == '/welcome@' + bot_username or \
                msg['text'].split()[0] == '!welcome':

            if msg['chat']['type'] == 'private':
                await bot.sendMessage(msg['chat']['id'], 'Este comando só funciona em grupos ¯\\_(ツ)_/¯')

            elif (await is_admin(msg['chat']['id'], msg['from']['id']))['user']:
                text = msg['text'].split(' ', 1)
                
                if len(text) == 1:

                    await bot.sendMessage(msg['chat']['id'],
                                          'Uso: /welcome on/off/reset/mensagem de boas-vindas do grupo (suporta Markdown e as tags $name, $title, $id e $rules)',
                                          reply_to_message_id=msg['message_id'])
                elif text[1] == 'on':
                    enable_welcome(msg['chat']['id'])
                    await bot.sendMessage(msg['chat']['id'], 'A mensagem de boas-vindas foi ativada.',
                                          reply_to_message_id=msg['message_id'])
                elif text[1] == 'off':
                    disable_welcome(msg['chat']['id'])
                    await bot.sendMessage(msg['chat']['id'], 'A mensagem de boas-vindas foi desativada.',
                                          reply_to_message_id=msg['message_id'])
                elif text[1] == 'reset':
                    set_welcome(msg['chat']['id'], None)
                    await bot.sendMessage(msg['chat']['id'], 'A mensagem de boas-vindas foi redefinida.',
                                          reply_to_message_id=msg['message_id'])
                else:
                    try:
                        sent = await bot.sendMessage(msg['chat']['id'], text[1], parse_mode='Markdown',
                                                     reply_to_message_id=msg['message_id'])
                        set_welcome(msg['chat']['id'], text[1])
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  'A mensagem de boas-vindas foi definida.')
                    except TelegramError as e:
                        await bot.sendMessage(msg['chat']['id'], '''Ocorreu um erro ao definir a mensagem de boas-vindas:
{}

Se esse erro persistir entre em contato com @GorpoOrko.'''.format(e.description),
                                              reply_to_message_id=msg['message_id'])

            return True


    elif msg.get('new_chat_member'):
        chat_title = msg['chat']['title']
        chat_id = msg['chat']['id']
        first_name = msg['new_chat_member']['first_name']
        user_id = msg['new_chat_member']['id']
        if msg['new_chat_member']['id'] == bot_id:
            pass
        else:
            welcome = get_welcome(chat_id)
            if welcome[1]:
                if welcome[0] is not None:
                    welcome = welcome[0].replace('$name', escape_markdown(first_name)).replace('$title',
                                                                                               escape_markdown(
                                                                                                   chat_title)).replace(
                        '$id', str(user_id))
                else:
                    welcome = 'Olá {}, seja bem-vindo(a) ao {}!'.format(first_name, escape_markdown(chat_title))
                if '$rules' in welcome:
                    welcome = welcome.replace('$rules', '')
                    rules_markup = InlineKeyboardMarkup(inline_keyboard=[
                        [dict(text='Leia as regras',
                              url='https://t.me/{}?start=rules_{}'.format(bot_username, chat_id))]
                    ])
                else:
                    rules_markup = None
                await bot.sendMessage(chat_id, welcome, 'Markdown',
                                      reply_to_message_id=msg['message_id'],
                                      reply_markup=rules_markup,
                                      disable_web_page_preview=True)
        return True
