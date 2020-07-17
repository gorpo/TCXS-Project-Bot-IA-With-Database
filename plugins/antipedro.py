
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
import json
import aiml
from config import bot
from db_handler import conn, cursor

k = aiml.Kernel()
k.learn("")


def get_antipedro(chat_id):
    cursor.execute('SELECT antipedro_enabled, antipedro_list FROM chats WHERE chat_id = ?', (chat_id,))
    return cursor.fetchone()


def add_user(chat_id, user_id):
    cursor.execute('SELECT antipedro_list FROM chats WHERE chat_id = ?', (chat_id,))
    user_list = json.loads(cursor.fetchone()[0])
    if user_id not in user_list:
        user_list.append(user_id)
        cursor.execute('UPDATE chats SET antipedro_list = ? WHERE chat_id = ?', (json.dumps(user_list), chat_id,))
        conn.commit()
    return True


def set_antipedro(chat_id, toggle):
    cursor.execute('UPDATE chats SET antipedro_enabled = ? WHERE chat_id = ?', (bool(toggle), chat_id))
    conn.commit()
    return True


def remove_user(chat_id, user_id):
    cursor.execute('SELECT antipedro_list FROM chats WHERE chat_id = ?', (chat_id,))
    user_list = json.loads(cursor.fetchone()[0])
    for num, user in enumerate(user_list):
        if user == user_id:
            del user_list[num]
    cursor.execute('UPDATE chats SET antipedro_list = ? WHERE chat_id = ?', (json.dumps(user_list), chat_id,))
    conn.commit()


async def antipedro(msg):
    if msg.get('chat') and msg.get('from') and msg['chat']['type'].endswith('group'):
        ap = get_antipedro(msg['chat']['id'])
        if ap[0] and msg['from']['id'] in json.loads(ap[1]):
            await bot.sendMessage(msg['chat']['id'], k.respond('a'), reply_to_message_id=msg['message_id'])
            return True
