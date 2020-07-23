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
from plugins.admins import is_admin
from plugins.inteligencias.ia_global import ia_global
from plugins.inteligencias.ia_local import ia_local
from plugins.inteligencias.ia_cadastro_perguntas import ia_cadastro_perguntas
from plugins.inteligencias.ia_cadastro_manual import ia_cadastro_manual
from plugins.inteligencias.ia_mensagens_proibidas import ia_mensagens_proibidas
from plugins.inteligencias.ia_wikipedia import ia_wikipedia
from plugins.inteligencias.ia_privado_bot import ia_privado_bot
from plugins.inteligencias.ia_crawler_sites import crawling
from plugins.inteligencias.ia_reconhecimento import ia_reconhecimento
from plugins.inteligencias.ia_deepnude import ia_deepnude

#IA depende da IA_global e IA_local
#IA_global = manda mensagem de todo lugar pra todo lugar
#IA_local = manda mensagem do grupo somente no grupo
#Para desativar uma IA basta deletar ou comentar ela
#Novas IA's devem ser adicionadas aqui


async def inteligencia(msg):
    try:#verifica se o usuario é um admin de grupo ou canal
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    try:
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']

        #SISTEMA DA IA QUANDO ENVIAR UMA MENSAGEM NO PRIVADO DO BOT
        #CARREGAR PLUGINS DE IA PERTINTENTE AO BOT NO SISTEMA ABAIXO
        #se a mensagem for no privado do bot ele irá realizar os plugins e comandos aqui listados-------------->
        if msg['chat']['type'] == 'private':
            #plugins do bot
            ativa_privado_bot = await ia_privado_bot(msg)
            #variaveis para o sistema de cadastro caso enviem coisas no privado do bot:
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
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        chat_type = msg['chat']['type']
        id_grupo = msg['chat']['id']
        #inicio da inteligencia artificial---------------------------------------->
        if chat_type == 'supergroup':  # se o chat for supergrupo ele manda mensagem
            if msg.get('text'):
                #PLUGINS EXTERNOS DA INTELIGENCIA ARTIFICIAL | PASTA INTELIGENCIAS
                ativa_cadastro_perguntas = await ia_cadastro_perguntas(msg)
                ativa_cadastro_manual = await ia_cadastro_manual(msg)
                ativa_mensagens_proibidas = await ia_mensagens_proibidas(msg)
                ativa_wikipedia = await ia_wikipedia(msg)
                ativa_crawling = await crawling(msg)
                ativa_reconhecimento = await ia_reconhecimento(msg)
                ativa_deepnude = await ia_deepnude(msg)



                #variavies iniciais--------------------------------->
                cursor_sqlite.execute("""SELECT * FROM inteligencia; """)
                inteligencias = cursor_sqlite.fetchall()
                for inteligencia in inteligencias:  # loop em todos resultados da Database
                    idgrupo = str(msg['chat']['id'])
                    if inteligencia['inteligencia'] == 'global':
                        pass
                        if inteligencia['id_grupo'] == idgrupo:
                            #print(f'Inteligencia Global setada no grupo {grupo}')
                            inteligencia_global = await ia_global(msg)
                    if inteligencia['inteligencia'] == 'local':
                        pass
                        if inteligencia['id_grupo'] == idgrupo:
                            #print(f'Inteligencia Local setada no grupo {grupo}')
                            inteligencia_local = await ia_local(msg)

                # ATIVA A INTELIGENCIA BASEADO NA IA GLOBAL/LOCAL
                #COMANDO PARA MUDAR ENTRE A INTELIGENCIA GLOBAL/LOCAL--------------------->>
                #sistema de mudança da ia entre global ou local | comando inteligencia ou ia
                if msg.get('text').split()[0] == 'inteligencia':
                    if adm['user'] == True:
                        if len(msg['text'].split()) > 1 and msg['text'].split()[1] == 'global' or len(msg['text'].split()) > 1 and msg['text'].split()[1] == 'local':
                            inteligencia = msg['text'].split()[1]
                            try:
                                tipo = msg['text'].split()[2]
                            except:
                                tipo = 'IA'
                                pass
                            try:
                                linguagem = msg['from']['language_code']
                            except:
                                linguagem = 'none'
                                pass
                            try:
                                cursor_sqlite.execute(f"""DELETE FROM inteligencia WHERE id_grupo='{msg['chat']['id']}' """)
                                cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','{tipo}','{data}','{inteligencia}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"@{msg['from']['username']} `Inteligencia Artificial:`***{inteligencia}***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown')
                            except Exception as e:
                                print(f'banco de dados inteligencia erro: {e}')
                if msg.get('text') == 'inteligencia':
                    await bot.sendMessage(chat_id,f"`Inteligencia Artificial:`***Tenho um sistema de IA que aprendo tudo em todos os lugares que estou, para selecionar oque devo falar use os comandos como exemplo:***\n`comando:`inteligencia global\n```---- Com o comando inteligencia global irei falar oque aprendi em todos os lugares que estive.```\n`comando:`inteligencia local\n```Com o comando inteligencia local irei falar oque aprendi aqui.```\n***Para selecionar a frequência de minha interação no grupo use o comando frêquencia***", 'markdown')
                if msg.get('text').split()[0] == 'inteligencia' and adm['user'] == False:
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')

        #CADASTRO AUTOMATICO INTELIGENCIA DATABASE
        #CADASTRA AUTOMATICAMENTE TUDO QUE POSTAREM NA DATABASE, MANTENDO ASSIM CONHECIMENTO PARA IA
        # sistema de cadastro automatico dos posts dos grupos na Database------------------------------------------------------------
        if chat_type == 'supergroup' or chat_type == 'private' or chat_type == 'channel':
            try:
                try:
                    linguagem = msg['from']['language_code']
                except:
                    linguagem = 'none'
                    pass
                if msg.get('sticker'):
                    id_sticker = msg['sticker']['file_id']
                    id_mensagem = msg['sticker']['thumb']['file_unique_id']
                    await bot.sendSticker(msg['from']['id'], sticker=id_sticker)
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','sticker','{data}','{id_mensagem}','{id_sticker}')""")
                        conexao_sqlite.commit()
                if msg.get('photo'):
                    id_foto = msg['photo'][0]['file_id']
                    id_mensagem = msg['photo'][0]['file_unique_id']
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','imagem','{data}','{id_mensagem}','{id_foto}')""")
                        conexao_sqlite.commit()
                    try:
                        await bot.sendPhoto(-1001363303197, id_foto)  #canal para marcinho = -1001402280935
                    except:
                        pass
                    try:
                        await bot.sendPhoto(msg['from']['id'], photo=id_foto, caption='Você mandou esta foto no grupo.')
                    except:
                        pass

                if msg.get('document'):#grava os dados pelo nome pois a unique id nao fica mesma se mesmo arquivo
                    id_documento = msg['document']['file_id']
                    try:
                        id_mensagem = msg['document']['file_name']
                    except:
                        id_mensagem = msg['document']['file_unique_id']
                        pass
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        #await  bot.sendDocument(msg['from']['id'], id_documento)
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','documento','{data}','{id_mensagem}','{id_documento}')""")
                        conexao_sqlite.commit()
                    try:
                        captado = msg['caption']
                    except:
                        captado = f'Vem de PV q o Pai ta ON: @{bot_username} '
                    #await bot.sendDocument(-1001363303197, id_documento, captado)  #para marcinho -1001166426209
                if msg.get('audio'):
                    id_audio = msg['audio']['file_id']
                    id_mensagem = msg['audio']['file_unique_id']
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','audio','{data}','{id_mensagem}','{id_audio}')""")
                        conexao_sqlite.commit()
                if msg.get('video'):
                    id_video = msg['video']['file_id']
                    id_mensagem = msg['video']['file_unique_id']
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','video','{data}','{id_mensagem}','{id_video}')""")
                        conexao_sqlite.commit()
                    try:
                        await bot.sendVideo(-1001363303197, id_video)  #marcinho -1001402280935
                    except:
                        pass
                    try:
                        await bot.sendVideo(msg['from']['id'], id_video, caption=f'@{usuario} Você mandou este video no {grupo}.')
                    except:
                        pass


                if msg.get('voice'):#MELHOR NAO APLICAR AQUI A REGRA SE JA EXISTE SENAO NAO VAI CADASTRAR
                    id_voz = msg['voice']['file_id']
                    #id_mensagem = msg['voice']['file_unique_id']
                    await bot.download_file(msg['voice']['file_id'], 'images/audio_usuario_db.ogg')
                    sound = AudioSegment.from_file("images/audio_usuario_db.ogg")
                    sound.export("images/audio_usuario_db.wav", format="wav", bitrate="128k")
                    r = sr.Recognizer()
                    with sr.WavFile('images/audio_usuario_db.wav') as source:
                        audio = r.record(source)
                    texto = r.recognize_google(audio, language='pt-BR')
                    await bot.sendMessage(chat_id, f"`{msg['from']['first_name']} disse:`\n```----  {texto}```", 'markdown', reply_to_message_id=msg['message_id'])
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    id_mensagem = texto
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','voz decodificada','{data}','{id_mensagem}','{texto}')""")
                        conexao_sqlite.commit()
                if msg.get('text'):
                    texto = msg['text']#aqui tenho que comparar o texto com texto para nao gravar textos iguais
                    id_mensagem = texto
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens = cursor_sqlite.fetchall()
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for mensagem in mensagens:  # loop em todos resultados da Database
                        if mensagem['id_mensagem'] == id_mensagem:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO mensagens (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,id_mensagem, mensagem)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','texto','{data}','{id_mensagem}','{texto}')""")
                        conexao_sqlite.commit()
            except Exception as e:
                print(f'Sistema de cadastro automatico IA, erro: {e}')
                pass



            # COMANDO PARA MUDAR A FREQUENCIA COM QUE A IA FALA | CADA GRUPO TEM SUA FREQUENCIA PRÓPRIA--------------------->>
            #seta a frequencia da IA | comando frequencia + 0  a 10 onde 0 muta o bot e 10 fala muito
            texto = msg['text']
            if texto.lower().startswith('frequencia') and  texto.split()[1].isdigit():
                try:
                    valor = texto[11:]
                    cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                    frequencias = cursor_sqlite.fetchall()
                    comparar_vazio = []
                    freq = list(frequencias)
                    if freq == comparar_vazio:
                        cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{id_grupo}','{grupo}','{valor}')""")
                        conexao_sqlite.commit()
                    else:
                        for frequencia in frequencias:  # loop em todos resultados da Database
                            if frequencia['id_grupo'] == msg['chat']['id']:
                                cursor_sqlite.execute(f"""DELETE FROM frequencia WHERE id_grupo='{msg['chat']['id']}'""")
                                conexao_sqlite.commit()
                                cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{id_grupo}','{grupo}','{valor}')""")
                                conexao_sqlite.commit()
                            if frequencia['id_grupo'] != msg['chat']['id']:
                                cursor_sqlite.execute(f"""INSERT INTO frequencia(id_grupo, grupo, valor)VALUES('{id_grupo}','{grupo}','{valor}')""")
                                conexao_sqlite.commit()
                    if int(valor) == 0:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, estou mutado so irei reponder comandos cadastrados`','markdown')
                    if int(valor) == 1:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, vou tentar falar pouco`','markdown')
                    if int(valor) >= 2:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, vou falar bastante`\nCaso queira que eu pare de falar defina a frequencia: 0\n Para eu falar menos defina frequencia: 1','markdown')
                except Exception as e:
                    print(f'Erro no sistema de cadastro da frequencia: {e}')
                    pass
        conexao_sqlite.close()
    # excessão final caso de pau em tudo e fechar o banco de dados--->
    except Exception as e:
        #print(f'Ocorreu um erro em alguma parte do codigo da inteligencia estou na linha final:{e}')
        pass















