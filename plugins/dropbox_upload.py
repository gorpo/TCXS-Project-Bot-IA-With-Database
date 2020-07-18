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
from config import bot, sudoers, logs, bot_username,token_dropbox
from datetime import datetime
from plugins.admins import is_admin
from plugins.inteligencias.ia_global import ia_global
from plugins.inteligencias.ia_local import ia_local
from plugins.inteligencias.ia_cadastro_manual import ia_cadastro_manual
from plugins.inteligencias.ia_cadastro_perguntas import ia_cadastro_perguntas

async def dropbox_upload(msg):
    try:#verifica se o usuario é um admin de grupo ou canal
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    try:
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        if chat_type == 'supergroup':
            if msg.get('text'):
                texto = msg['text']
                #sistea de upload para o dropbox | necessario mudar o caminho para sua pasta que quer baixar os arquivos----------------------------------------------------------->
                try:  # UPLOAD DE DOCUMENTOS PARA O DROPBOX
                    if 'document' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                        if adm['user'] == True:
                            id_arquivo = msg.get('reply_to_message')['document']['file_id']
                            nome_arquivo = msg.get('reply_to_message')['document']['file_name']
                            tamanho = msg.get('reply_to_message')['document']['file_size']
                            if tamanho > 10000000:
                                await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',
                                                reply_to_message_id=msg['message_id'])
                            if tamanho < 10000000:
                                await bot.download_file(id_arquivo, f'images/{nome_arquivo}')
                                await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                                targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}"
                                d = dropbox.Dropbox(token_dropbox)
                                with open(f'images/{nome_arquivo}', "rb") as f:
                                    meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                                link = d.sharing_create_shared_link(targetfile)
                                url = link.url
                                dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                                await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei upar seu arquivo no Dropbox`\nlink:{dl_url}",'markdown', reply_to_message_id=msg['message_id'])
                                os.remove(f'images/{nome_arquivo}')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # UPLOAD DE IMAGENS/FOTOS PARA O DROPBOX
                    if 'photo' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                        if adm['user'] == True:
                            id_arquivo = msg.get('reply_to_message')['photo'][0]['file_id']
                            nome_arquivo = id_arquivo[0:5]
                            await bot.download_file(id_arquivo, f'images/{nome_arquivo}.jpg')
                            await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                            targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}.jpg"
                            time.sleep(1)
                            d = dropbox.Dropbox(token_dropbox)
                            with open(f'images/{nome_arquivo}.jpg', "rb") as f:
                                meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                            link = d.sharing_create_shared_link(targetfile)
                            url = link.url
                            dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                            await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei upar seu arquivo no Dropbox`\nlink:{dl_url}",'markdown', reply_to_message_id=msg['message_id'])
                            os.remove(f'images/{nome_arquivo}.jpg')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass

        # excessão final caso de pau em tudo--->
    except Exception as e:
        print(f'Ocorreu um erro no sistema de upload do Dropbox:{e}')
        pass







