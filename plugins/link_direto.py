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
from config import bot, sudoers, logs, bot_username,token_dropbox,token,administradores
from datetime import datetime

from plugins.admins import is_admin
from bitlyshortener import Shortener


async def link_direto(msg):
    try:#verifica se o usuario é um admin de grupo ou canal
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    try:
        chat_id = msg['chat']['id']
        #SISTEMA DA IA QUANDO ENVIAR UMA MENSAGEM NO PRIVADO DO BOT
        #CARREGAR PLUGINS DE IA PERTINTENTE AO BOT NO SISTEMA ABAIXO
        #se a mensagem for no privado do bot ele irá realizar os plugins e comandos aqui listados-------------->
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
        # SISTEMA DA IA QUANDO ENVIAR UMA MENSAGEM NO CANAL DO BOT
        # CARREGAR PLUGINS DE IA PERTINTENTE AO BOT NO SISTEMA ABAIXO
        # se a mensagem for no privado do bot ele irá realizar os plugins e comandos aqui listados-------------->
        if msg['chat']['type'] == 'channel':
            grupo = f'Canal: @{bot_username}'
            usuario = f'Administrador do: @{bot_username}'
            try:
                texto = msg['text']
            except:
                pass
        #SISTEMA DA IA PARA QUANDO ENVIAREM MENSAGENS EM GRUPOS E SUPERGRUPOS
        #TUDO QUE FOR REFERENTE A GRUPOS É COLOCADO ABAIXO
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
        chat_type = msg['chat']['type']
        id_grupo = msg['chat']['id']
        texto = msg['text']
        tokens_pool = ["a001cef9d44ed8083ed4d952d475e98079e60577", ]
        shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)
        if chat_type == 'supergroup':

            if msg.get('text') == 'avatar':
                a = await bot.getUserProfilePhotos(msg.get('reply_to_message')['from']['id'])
                b = a['photos'][0][0]['file_id']
                await bot.sendPhoto(chat_id,b)




            try:  # DOCUMENTOS
                if 'document' in msg.get('reply_to_message') and texto == '/link' or 'document' in msg.get('reply_to_message') and texto == 'link':
                    #if adm['user'] == True:
                    id_documento = msg.get('reply_to_message')['document']['file_id']
                    nome = msg.get('reply_to_message')['document']['file_name']
                    arquivo = await bot.getFile(id_documento)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                        #await bot.sendMessage(msg['chat']['id'], '*Link Encurtado:* {}'.format(a[0]), 'Markdown', reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass
            try:  # IMAGENS
                if 'photo' in msg.get('reply_to_message') and texto == '/link' or 'photo' in msg.get('reply_to_message') and texto == 'link':
                    #if adm['user'] == True:
                    id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                    nome = 'imagem'
                    arquivo = await bot.getFile(id_foto)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                        #await bot.sendMessage(msg['chat']['id'], '*Link Encurtado:* {}'.format(a[0]), 'Markdown', reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass
            try:  # AUDIOS
                if 'audio' in msg.get('reply_to_message') and texto == '/link' or 'audio' in msg.get('reply_to_message') and texto == 'link':
                    #if adm['user'] == True:
                    id_documento = msg.get('reply_to_message')['audio']['file_id']
                    nome = msg.get('reply_to_message')['audio']['title']
                    arquivo = await bot.getFile(id_documento)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                        #await bot.sendMessage(msg['chat']['id'], '*Link Encurtado:* {}'.format(a[0]), 'Markdown', reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass
            try:  # VIDEOS
                if 'video' in msg.get('reply_to_message') and texto == '/link' or 'video' in msg.get('reply_to_message') and texto == 'link':
                    #if adm['user'] == True:
                    id_documento = msg.get('reply_to_message')['video']['file_id']
                    nome = 'video'
                    arquivo = await bot.getFile(id_documento)
                    tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nTamanho:{tamanho}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass
            try:  # VOZ
                if 'voice' in msg.get('reply_to_message') and texto == 'link' or 'voice' in msg.get('reply_to_message') and texto == '/link':
                    #if adm['user'] == True:
                    id_documento = msg.get('reply_to_message')['voice']['file_id']
                    nome = f"audio do {msg['from']['first_name']}"
                    arquivo = await bot.getFile(id_documento)
                    #tamanho = arquivo['file_size']
                    link = f"https://api.telegram.org/file/bot{token}/{arquivo['file_path']}"
                    try:
                        a = shortener.shorten_urls([link])
                        await bot.sendMessage(chat_id,f"🤖 Aqui está seu link direto.\nArquivo:{nome}\nLink:{a[0]}",reply_to_message_id=msg['message_id'])
                    except:
                        await bot.sendMessage(msg['chat']['id'], '`Não foi possivel encurtar seu link, tente novamente, talves o serviço esteja offline.`', 'Markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                pass
    # excessão final caso de pau em tudo e fechar o banco de dados--->
    except Exception as e:
        #print(f'Erro no sistema de link direto:{e}')
        pass















