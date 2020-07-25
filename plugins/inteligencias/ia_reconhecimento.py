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
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2



async def ia_reconhecimento(msg):
    try:
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    try:
        chat_id = msg['chat']['id']
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        chat_type = msg['chat']['type']
        texto = msg['text']
        if chat_type == 'supergroup':
            #if msg.get('text'):
            if 'photo' in msg.get('reply_to_message') and texto.startswith('recog'):
                if adm['user'] == True:
                    id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                    await bot.download_file(id_foto,'images/recognition.jpg')
                    image = cv2.imread('images/recognition.jpg')
                    bbox, label, conf = cv.detect_common_objects(image)
                    #print(bbox, label, conf)
                    out = draw_bbox(image, bbox, label, conf)
                    #cv2.imshow("object_detection", out)
                    #cv2.waitKey()
                    cv2.imwrite("images/recognition_out.jpg", out)
                    #cv2.destroyAllWindows()
                    await bot.sendPhoto(chat_id,photo=open('images/recognition_out.jpg','rb'), reply_to_message_id=msg['message_id'])
                    os.remove('images/recognition.jpg')
                    os.remove('images/recognition_out.jpg')






                    #await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    #await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')




#excessao final para tratar do codigo todo--->
    except:
        pass
        return True
