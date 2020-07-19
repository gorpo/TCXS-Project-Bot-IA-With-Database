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
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin
import subprocess
import time
import speech_recognition as sr
from pydub import AudioSegment
import os
import dropbox
import re
import wikipedia
import sqlite3
from config import bot, sudoers, logs, bot_username,token_dropbox,administradores
from datetime import datetime
from plugins.admins import is_admin



async def ia_cadastro_perguntas(msg):
    try:
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    try:
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']
        # se a mensagem e no privado do bot-------------->
        if msg['chat']['type'] == 'private':
            grupo = f'Privado: @{bot_username}'
            try:
                usuario = msg['from']['username']
            except:
                usuario = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
            try:
                texto = msg['text']
            except:
                pass
        #se a mensagem e no canal do bot-------------->
        if msg['chat']['type'] == 'channel':
            grupo = f'Canal: @{bot_username}'
            usuario = f'Administrador do: @{bot_username}'
            try:
                texto = msg['text']
            except:
                pass
        # se for um supergrupo ou grupo secreto ele trata o nome do grupo e o usuario se ele tem ou nao um username
        if msg['chat']['type'] == 'supergroup':
            try:
                grupo = f"https://t.me/{msg['chat']['username']}"
            except:
                grupo = f"Secreto: {msg['chat']['title']}"
                pass
            try:
                usuario = msg['from']['username']
            except:
                usuario = f"@{msg['from']['id']}({msg['from']['first_name']})"
                pass
            try:
                texto = msg['text']
            except:
                pass
            try:
                linguagem = msg['from']['language_code']
            except:
                linguagem = 'none'
                pass
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        chat_type = msg['chat']['type']
        id_grupo = msg['chat']['id']
        if chat_type == 'supergroup':  # or chat_type == 'private'
            if msg.get('text'):
                texto = msg['text']
                try:  # CADASTRO PERGUNTAS DOS USUARIOS---------------------------------------------------------->
                    if '??' in texto:
                        usuario = f"@{msg['from']['username']}"
                        cursor_sqlite.execute(f"""INSERT INTO perguntas VALUES (null,'{usuario}','{texto}')""")
                        conexao_sqlite.commit()
                        await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} `sua pergunta foi cadastrada.`",'markdown')
                except Exception as e:
                    print(e)
                    pass
                try:  # VERIFICAR PERGUNTAS DOS USUARIOS----------------------------------------------------------->
                    if texto.lower() == 'perguntas':
                        cursor_sqlite.execute("""SELECT * FROM perguntas""")
                        resultados = cursor_sqlite.fetchall()
                        if resultados == []:
                            await bot.sendMessage(chat_id,f"🤖 {msg['from']['first_name']} `não tenho perguntas cadastradas, tente outra hora ou cadastre algumas perguntas.`",'markdown')
                        else:
                            for resultado in resultados:
                                usuario = resultado['usuario']
                                pergunta = resultado['pergunta']
                                await bot.sendMessage(chat_id, f"`Usuário:`{usuario}\n`Pergunta:`{pergunta}", 'markdown')
                except Exception as e:
                    print(e)
                    pass
                try:  # LIMPAR PERGUNTAS DOS USUARIOS------------------------------------------------------------->
                    if texto.lower() == 'apagar perguntas' and msg['from']['id'] in administradores:#admin manual setado no confis.py
                        if adm['user'] == True:
                            cursor_sqlite.execute("""DELETE FROM perguntas""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} Todas perguntas foram apagadas!")
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

#excessao final para tratar do codigo todo--->
    except:
        pass
        return True
