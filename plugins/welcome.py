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
#     [+]        Github Gorpo Dev: https://github.com/gorpo     [+]

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
import sqlite3
import os
from plugins.admins import is_admin
from datetime import datetime
from dateutil.relativedelta import relativedelta


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
        else:   #daqui para baixo e codigo novo meu-------------------------------------------------->>>>>>>>>>>>>>
            ############SISTEMA DE CADASTRO DOS USUARIOS AUTOMATICAMENTE NO BANCO DE DADOS PARA BANIMENTO------

            try:
                doador = msg['new_chat_member']['username']
            except:
                doador = f"{msg['new_chat_member']['id']} ({msg['new_chat_member']['first_name']})"
            try:
                conexao_sqlite = sqlite3.connect('bot.db')
                conexao_sqlite.row_factory = sqlite3.Row
                cursor_sqlite = conexao_sqlite.cursor()
                chat_id = msg['chat']['id']
                print(f"Novo usuário: {doador} entrou no Grupo {msg['chat']['title']}")
                id_doador = msg['new_chat_member']['id']
                admin = 'cadastro automatico'
                dias = 30 #QUANTIDADE DE DIAS SETADA MANUALMENTE, POR ISTO COMO COMANDO NA DATABASE
                hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                data_inicial = hoje
                dias_restantes = datetime.now() + relativedelta(minutes=int(dias))#--------------------------------
                data_final = dias_restantes.strftime('%d/%m/%Y %H:%M:%S')
                data_avisar = dias_restantes - relativedelta(minutes=int(7))#-------------------------------------
                data_aviso = data_avisar.strftime('%d/%m/%Y %H:%M:%S')
                #verifica se existe cadastro:
                cursor_sqlite.execute("""SELECT * FROM permanencia; """)
                resultados = cursor_sqlite.fetchall()
                existe_cadastro = 0  # contador para verificar se o comando ja existe
                for res in resultados:  # loop em todos resultados da Database
                    if res['id_doador'] == id_doador:
                        existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                if existe_cadastro == 1:
                    await bot.sendMessage(chat_id, "🤖 `Usuário ja cadastrado, apague ele manualmente e insira os dados novamente`", 'markdown')
                else:
                    cursor_sqlite.execute(f"""INSERT INTO permanencia(int_id,grupo,id_grupo, admin, doador, id_doador, dias, data_inicial, data_final,data_aviso)VALUES(null,'{msg['chat']['title']}','{msg['chat']['id']}','{admin}','{doador}','{id_doador}','{dias}','{data_inicial}','{data_final}','{data_aviso}')""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id,f"🤖 ***Dados inseridos com exito no cadastro de permanência do grupo de doadores.***\n`Admin:` {admin}\n`Doador:` {doador}\n`Id_Doador:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_final}\n`Aviso Vencimento:` {data_aviso}\n`Permanência:` {dias}",'markdown')
                    #print(admin, doador, id_doador, dias, data_inicial, data_final)
            except Exception as e:
                await bot.sendMessage(chat_id,f"🤖 `Ocorreu um erro ao inserir os dados na Database.Envie novamente o comando manualmente conforme exemplo:` ```restringir @doador id_doador dias``` ***Exemplo:*** restringir @xbadcoffee 1367451130 30 ",'markdown')
            ###########FIM DO SISTEMA DE BANIMENTO---------------------------------------------------------------------------
            #ACIMA TUDO CODIGO MEU------------------------->


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
