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
from plugins.ia_global import ia_global
from plugins.ia_local import ia_local

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
        conexao_sqlite = sqlite3.connect('bot.db')
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
        #inicio da inteligencia artificial---------------------------------------->
        if chat_type == 'supergroup':  # se o chat for supergrupo ele manda mensagem
            if msg.get('text'):
                cursor_sqlite.execute("""SELECT * FROM inteligencia; """)
                inteligencias = cursor_sqlite.fetchall()
                for inteligencia in inteligencias:  # loop em todos resultados da Database
                    idgp = str(msg['chat']['id'])
                    if inteligencia['inteligencia'] == 'global':
                        pass
                        if inteligencia['id_grupo'] == idgp:
                            #print(f'Inteligencia Global setada no grupo {grupo}')
                            inteligencia_global = await ia_global(msg)
                    if inteligencia['inteligencia'] == 'local':
                        pass
                        if inteligencia['id_grupo'] == idgp:
                            #print(f'Inteligencia Local setada no grupo {grupo}')
                            inteligencia_local = await ia_local(msg)

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
                                conexao_sqlite.commit()#,grupo , tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia
                                cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','{tipo}','{data}','{inteligencia}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"@{msg['from']['username']} `Inteligencia Artificial:`***{inteligencia}***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown')
                            except Exception as e:
                                print(f'banco de dados inteligencia erro: {e}')
                                #cursor_sqlite.execute(f"""INSERT INTO inteligencia (int_id, grupo, tipo_grupo, id_grupo, usuario, id_usuario, linguagem, tipo, data,inteligencia)VALUES(null,'{grupo}','{chat_type}','{id_grupo}','{usuario}','{id_usuario}','{linguagem}','{tipo}','{data}','{inteligencia}')""")
                                #conexao_sqlite.commit()
                                #await bot.sendMessage(chat_id,f"@{msg['from']['username']} `Inteligencia Artificial:`***{inteligencia}***\nAgora vocês irão receber coisas que aprendi nesta categoria.",'markdown')
                if msg.get('text') == 'inteligencia':
                    await bot.sendMessage(chat_id,f"`Inteligencia Artificial:`***Tenho um sistema de IA que aprendo tudo em todos os lugares que estou, para selecionar oque devo falar use os comandos como exemplo:***\n`comando:`inteligencia global\n```---- Com o comando inteligencia global irei falar oque aprendi em todos os lugares que estive.```\n`comando:`inteligencia local\n```Com o comando inteligencia local irei falar oque aprendi aqui.```\n***Para selecionar a frequência de minha interação no grupo use o comando frêquencia***", 'markdown')

                if msg.get('text').split()[0] == 'inteligencia' and adm['user'] == False:
                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')


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
                    await bot.sendMessage(chat_id, f"`{msg['from']['first_name']} disse:`\n```{texto}```", 'markdown', reply_to_message_id=msg['message_id'])
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


            # SISTEMA QUE DELETA MENSAGENS PROIBIDAS --------------------------------------------------------------------->
            if chat_type == 'supergroup' and msg.get('text'):# verifica se a palavra é proibida, se for deleta a mensagem do usuario e envia um aviso------>
                    cursor_sqlite.execute("""SELECT * FROM proibido; """)
                    mensagens_proibidas = cursor_sqlite.fetchall()
                    for mensagem in mensagens_proibidas:
                        if mensagem['termo'] in texto:
                            try:#em caso de erro inverter este try except pelo de baixo pois da erro entre message_id e reply_to_message
                                await bot.deleteMessage((msg['chat']['id'], msg['message_id']))
                                await bot.sendMessage(chat_id,f"@{msg['from']['username']} `você usou uma palavra proibida, não fale bosta aqui!`",'markdown')
                            except TelegramError:

                                try:
                                    await bot.deleteMessage((msg['chat']['id'], msg['reply_to_message']['message_id']))
                                    await bot.sendMessage(chat_id,f"@{msg['from']['username']} `você usou uma palavra proibida, não fale bosta aqui!`",'markdown')
                                except TelegramError:
                                    pass

            try:
                if msg.get('text'):
                    texto = msg['text']
                    if texto.lower().startswith('proibir') and adm['user'] == True:  # proibe as palavras e as cadastra na Database------------------------------->
                        palavra_proibida = texto[8:]
                        if palavra_proibida.lower() == 'proibir' or palavra_proibida.lower() == '' or palavra_proibida.lower() == ' '  or palavra_proibida.lower() == '' or palavra_proibida.lower() == 'comandos' or palavra_proibida.lower() == '/help' or palavra_proibida.lower() == 'fale sobre' or palavra_proibida.lower() == 'frequencia' or palavra_proibida.lower() == 'cmd' or palavra_proibida.startswith('/') or palavra_proibida.startswith('#') or palavra_proibida.startswith('$') or palavra_proibida.startswith('%') or palavra_proibida.startswith('@'):
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `não posso proibir esta palavra, talvez ela seja um comando meu.`",'markdown')
                            pass
                        else:
                            cursor_sqlite.execute(f"""INSERT INTO proibido VALUES('{palavra_proibida}')""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id,f'🤖🚫 `Proibido:`***{palavra_proibida}***\nPara voltar permitir esta palavra use o comando `permitir`, para ver palavras proibidas use `proibidas`','markdown', reply_to_message_id=msg['message_id'])
                    if texto.lower().startswith('proibir') and adm['user'] == False:
                        await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                    if texto.lower().startswith('permitir') and adm['user'] == True:  # permite novamente as palavras e as descadastra na Database------------------------------->
                        palavra_permitida = texto[9:]
                        cursor_sqlite.execute(f"""DELETE FROM proibido WHERE termo='{palavra_permitida}'""")
                        conexao_sqlite.commit()
                        await bot.sendMessage(chat_id, f'🤖✔️ `Permitido:`***{palavra_permitida}***\nPara voltar proibir esta palavra use o comando `proibir`, para ver palavras proibidas use `proibidas`','markdown', reply_to_message_id=msg['message_id'])
                    if texto.lower().startswith('permitir') and adm['user'] == False:
                        await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')

                    if texto.lower().startswith('proibidas'):  # lista as palavras proibidas cadastradas  na Database------------------------------->
                        cursor_sqlite.execute("""SELECT * FROM proibido; """)
                        mensagens_proibidas = cursor_sqlite.fetchall()
                        todas_proibidas = []
                        separador = ' \n'
                        for result in mensagens_proibidas:
                            todas_proibidas.append(result['termo'])
                        await bot.sendMessage(chat_id,f'🤖 `Palavras Proibidas:`\n ***{separador.join(map(str, todas_proibidas))}***','markdown', reply_to_message_id=msg['message_id'])
                        await bot.sendMessage(chat_id, 'Para proibir use `proibir` e para permitir use `permitir`', 'markdown')
            except Exception as e:
                pass
            #comandos inseridos manualmente na programaçao com uso de #
            if msg.get('text'):
                texto = msg['text']
                try:
                    if texto == 'amigo':
                        await bot.sendVideo(chat_id, video=open('images/marcinho.mp4', 'rb'), reply_to_message_id=msg['message_id'])
                    if texto == 'canal':
                        #await bot.sendMessage(chat_id, "🤖 `Tenho um canal o qual pego todos documentos que vocês mandam e envio para la.`\n`Tenho outro canal que envio as zoeiras postadas nos grupos:`",
                        #        'markdown', reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                        #        [InlineKeyboardButton(text='Acervo Hacker', url="https://t.me/marcinho_hacker"),
                        #         InlineKeyboardButton(text='Acervo Zoeira', url="https://t.me/acervo_zoeira")]]))
                        await bot.sendMessage(chat_id, '<a href="https://t.me/marcinho_hacker"> <b>Canal Hacker</b></a>',  parse_mode='html', disable_web_page_preview=False)

                    # sistema que uso para xingar------------------------------------>
                    quantidade = texto[0:2]
                    comando_falar = texto[2]
                    frase_cortada = texto[4:]
                    if comando_falar == 'x':
                        if int(quantidade) > 20:
                            await bot.sendMessage(chat_id, 'Estou limitado a floodar somente 20x no maximo!', 'markdown')
                        else:
                            for i in range(int(quantidade)):
                                await bot.sendMessage(chat_id, f'***{frase_cortada}***', 'markdown')
                except Exception as e:
                    pass  # print(f'Erro no sistema de comandos manuais #:{e}')
                # SISTEMA DE RESPOSTA COM BASE NOS COMANDOS CADASTRADOS MANUALMENTE NO GRUPO | CRUD--------------------------------------------------->
                try:
                    cursor_sqlite.execute("""SELECT * FROM comandos; """)
                    resultados = cursor_sqlite.fetchall()
                    for resultado in resultados:
                        comando = resultado['comando']
                        resposta = resultado['resposta']
                        tipo = resultado['tipo']
                        if tipo == 'texto' and comando == texto.lower():
                            await bot.sendMessage(chat_id, f"{resposta}", reply_to_message_id=msg['message_id'])
                        if tipo == 'imagem' and comando == texto.lower():
                            await bot.sendPhoto(chat_id, photo=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'voz' and comando == texto.lower():
                            await bot.sendVoice(chat_id, voice=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'audio' and comando == texto.lower():
                            await bot.sendAudio(chat_id, audio=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'documento' and comando == texto.lower():
                            await bot.sendDocument(chat_id, document=resposta, reply_to_message_id=msg['message_id'])
                        if tipo == 'video' and comando == texto.lower():
                            await bot.sendVideo(chat_id, video=resposta, reply_to_message_id=msg['message_id'])
                except Exception as e:
                    print(f'Erro no sistema de respostas CDRUD: {e}')
    # SISTEMA CADASTRO DE RESPOSTAS COM BASE NOS COMANDOS CADASTRADOS MANUALMENTE NO GRUPO | CRUD---------------------------------------------------------------------->


                ##SISTEMA DE CADASTRO USANDO REPLY------------------------------------------------>
                try:  # IMAGENS na Database-------------------------------------------------------------->
                    if 'photo' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_imagem = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando and 'photo' in msg.get('reply_to_message'):
                                    existe_cadastro_imagem = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_imagem == 1:
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('imagem','{comando}','{id_foto}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_foto}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # VIDEOS na Database----------------------------------------------------------------->
                    if 'video' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_video = msg.get('reply_to_message')['video']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_video = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_video = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_video == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('video','{comando}','{id_video}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_video}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # DOCUMENTOS na Database------------------------------------------------------------->
                    if 'document' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_documento = msg.get('reply_to_message')['document']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_document = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_document = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_document == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('documento','{comando}','{id_documento}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_documento}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # AUDIOS VOZ na Database------------------------------------------------------------>
                    if 'voice' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_voz = msg.get('reply_to_message')['voice']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_voz = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                # se o comando ja existir o valor existe_cadastro passa ser 1
                                if res['comando'] == comando:
                                    existe_cadastro_voz = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_voz == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('voz','{comando}','{id_voz}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_voz}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # AUDIOS MUSICA na Database--------------------------------------------------------->
                    if 'audio' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_audio = msg.get('reply_to_message')['audio']['file_id']
                            cursor_sqlite.execute("""SELECT * FROM comandos """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_audio = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_audio = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_audio == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('audio','{comando}','{id_audio}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_audio}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # MENSAGENS de texto na Database---------------------------------------------------------------->
                    if 'text' in msg.get('reply_to_message') and texto.startswith('#'):
                        if adm['user'] == True:
                            comando = texto[1:]
                            id_text = msg.get('reply_to_message')['text']
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro_text = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro_text = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro_text == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                            elif existe_cadastro_text == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                                cursor_sqlite.execute(f"""INSERT INTO comandos(tipo,comando,resposta,usuario,grupo,data)VALUES('texto','{comando}','{id_text}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"`🤖 Dados inseridos com exito.\nComando:` {comando}\n`File_id:` {id_text}",'markdown')
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # SISTEMA DE CADASTRO DE COMANDOS DOS USUARIOS USANDO SOMENTE O # -------------------------------------------------------------->
                    if texto.startswith('#') and not msg.get('reply_to_message'):
                        if adm['user'] == True:
                            texto_cadastro = texto[1:].split(' ')
                            comando = str(texto_cadastro[0]).lower()  # gera o texto do comando
                            separador = ' '
                            resposta = separador.join(map(str, texto_cadastro[1:]))
                            cursor_sqlite.execute("""SELECT * FROM comandos; """)
                            resultados = cursor_sqlite.fetchall()
                            existe_cadastro = 0  # contador para verificar se o comando ja existe
                            for res in resultados:  # loop em todos resultados da Database
                                if res['comando'] == comando:
                                    existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                            if existe_cadastro == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                                await bot.sendMessage(chat_id, "Comando já cadastrado, tente outro",
                                                reply_to_message_id=msg['message_id'])
                            else:
                                cursor_sqlite.execute(f"""INSERT INTO comandos (tipo,comando,resposta,usuario,grupo,data) VALUES ('texto','{comando}','{resposta}','{usuario}','{grupo}','{data}')""")
                                conexao_sqlite.commit()
                                await bot.sendMessage(chat_id,f"🤖 Dados inseridos com exito.\nComando: {comando}\nResposta: {resposta}",reply_to_message_id=msg['message_id'])
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
                try:  # RECADASTRAMENTO DE RESPOSTAS USANDO O $--------------------------------------------------------------------------------------------------->
                    if texto.startswith('$'):
                        if adm['user'] == True:
                            texto_cadastro = texto[1:].split(' ')
                            comando = str(texto_cadastro[0]).lower()  # gera o texto do comando
                            separador = ' '
                            resposta = separador.join(map(str, texto_cadastro[1:]))  # pega todo resto da lista e poe no separador retornando toda lista em uma linha
                            cursor_sqlite.execute(f"""DELETE FROM comandos WHERE comando='{comando}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f'Comando: {comando} apagado do sistema.',reply_to_message_id=msg['message_id'])
                            cursor_sqlite.execute(f"""INSERT INTO comandos(tipo,comando,resposta,usuario,grupo,data)VALUES('texto','{comando}','{resposta}','{usuario}','{grupo}','{data}')""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f"🤖 Dados inseridos com exito.`Comando:` {comando}`Resposta:` {resposta}", 'markdown',reply_to_message_id=msg['message_id'])
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except Exception as e:
                    print(e)
                    pass
                try:  # DELETAR COMANDOS CADASTRADOS USANDO O %------------>
                    if texto.startswith('%'):
                        if adm['user'] == True:
                            comando = texto[1:].lower()  # tira do texto o  comando 'cadastrar'
                            cursor_sqlite.execute(f"""DELETE FROM comandos WHERE comando='{comando}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f'🤖 `Comando {comando} apagado do sistema.`', 'markdown',reply_to_message_id=msg['message_id'])
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    await bot.sendMessage(chat_id, f'🤖 `Comando {comando} inexistente ou ocorreu um erro.`', 'markdown',reply_to_message_id=msg['message_id'])
                try:  # LISTAR COMANDOS CADASTRADOS PELOS USUARIOS NA DATABASE------------>
                    if texto.lower() == 'comandos' or texto == '/comandos':
                        cursor_sqlite.execute("""SELECT * FROM comandos; """)
                        resultados = cursor_sqlite.fetchall()
                        todos_comandos = []
                        separador = ' \n'
                        for result in resultados:
                            todos_comandos.append(result['comando'])
                        await bot.sendMessage(chat_id,f'`Comandos cadastrados:`\n ***{separador.join(map(str, todos_comandos))}***','markdown', reply_to_message_id=msg['message_id'])
                except Exception as e:
                    print(e)
                    pass
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
                    if texto.lower() == 'limpar perguntas':
                        if adm['user'] == True:
                            cursor_sqlite.execute("""DELETE FROM perguntas""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} Todas perguntas foram apagadas!")
                        else:
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
                except:
                    pass
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
                #sistema de respostas com base na wikipedia
                try:
                    if 'fale sobre' in texto.lower():
                        termo = texto[10:]
                        wikipedia.set_lang("pt")
                        pesquisa = wikipedia.summary(termo)
                        await bot.sendMessage(chat_id, f"```{pesquisa}```",'markdown', reply_to_message_id=msg['message_id'])
                except Exception as e:
                    await bot.sendMessage(chat_id, '`Desconheço este assunto...`\n```---- Caso queira que eu aprenda fale sobre o assunto converse comigo sobre ele até que eu aprenda ou use o comando # informando o tema e após ele a explicação que devo aprender conforme exemplo:``` #tema ***informações que devo aprender***','markdown', reply_to_message_id=msg['message_id'])
                    #await bot.sendMessage(chat_id, f'Tente uma destas opções: {e}', reply_to_message_id=msg['message_id'])
                    pass
            # excessão final caso de pau em tudo--->
    except Exception as e:
        print(f'Ocorreu um erro em alguma parte do codigo da inteligencia estou na linha final:{e}')
        pass
    # COMANDOS PARA CANAL-------------------------------------->
    #if chat_type == 'channel':
    #    print(f'{usuario} mandou mensagem no canal: {msg}')  # id_zoeiras = -1001402280935    id_hacker = -1001166426209
    #    pass

    # COMANDOS DO CHAT PRIVADO-------------------------------------------------------------------------------------------------------------------------->
    if chat_type == 'private':
        ## SISTEMA DE FALA AUTOMATICA DO BOT COM BASE NOS POSTS DOS USUARIOS SQLITE3------------------------------------------->
        try:
            if msg.get('voice'):
                id_voz = msg['voice']['file_id']
                await bot.download_file(msg['voice']['file_id'], 'images/audio_usuario_db.ogg')
                sound = AudioSegment.from_file("images/audio_usuario_db.ogg")
                sound.export("images/audio_usuario_db.wav", format="wav", bitrate="128k")
                r = sr.Recognizer()
                with sr.WavFile('images/audio_usuario_db.wav') as source:
                    audio = r.record(source)
                texto = r.recognize_google(audio, language='pt-BR')
                await bot.sendMessage(chat_id, f"`{msg['from']['first_name']} disse:`\n```{texto}```", 'markdown',reply_to_message_id=msg['message_id'])
            if msg.get('text'):
                if msg.get('text') == 'att':
                    await bot.sendMessage(chat_id, f"@{msg['from']['first_name']} você esta tentando roubar a TCXS Store, cara vou pegar seu ip e te hackear agora mesmo!!! ", 'markdown',reply_to_message_id=msg['message_id'])

                cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                mensagens_sqlite = cursor_sqlite.fetchall()
                quantidade_mensagens = len(mensagens_sqlite)
                randomico = random.randint(0,  quantidade_mensagens - 1)  # fornece um numero randomico para pegarmos as mensagens na db
                mensagem_bot = mensagens_sqlite[randomico][10]
                tipo_mensagem = mensagens_sqlite[randomico][7]
                proibir_bot = ['fale','luppy','att','frequencia','#','$','%','att','comando','proibidas',]
                #if mensagem_bot in proibir_bot:
                #    pass
                #else:
                if tipo_mensagem == 'imagem':
                    await bot.sendPhoto(chat_id, photo=mensagem_bot)
                    print(f'🤖 Bot enviou uma imagem no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'documento':
                    #await bot.sendDocument(chat_id, document=mensagem_bot)
                    print(f'🤖 Bot tentou enviar um documento no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'audio':
                    #await bot.sendAudio(chat_id, audio=mensagem_bot)
                    print(f'🤖 Bot tentou enviar um audio no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'video':
                    await bot.sendVideo(chat_id, video=mensagem_bot)
                    print(f'🤖 Bot enviou um video no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
                if tipo_mensagem == 'texto':
                    await bot.sendMessage(chat_id, mensagem_bot)
                    print(f'🤖 Bot enviou no grupo {msg["chat"]["title"]}: {mensagem_bot}')
                if tipo_mensagem == 'sticker':
                    await bot.sendSticker(chat_id, sticker=mensagem_bot)
                    print(f'🤖 Bot enviou sticker no grupo {msg["chat"]["title"]} com a id {mensagem_bot}')
        except Exception as e:
            # print(f'Erro no sistema de fala automatica do Privado do Bot: {e}')
            pass


## [+] WARNING [+] | FECHA CONEXAO PARA ESCREVER NO BANCO DE DADOS--------
    conexao_sqlite.close()
    # CONFIGURAÇÕES PARA GRUPOS----------------------------------------------------------------------------------------------------------------------------->
    if msg.get('text') == '/helppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp':
        texto = """
***SOBRE A FREQUENCIA DE MENSAGENS*** 
```Este bot envia mensagens baseado em uma frequencia que deve ser setada entre 2 e 10, onde:```
`frequencia 1 = mudo`
`frequencia 2 = fala pouco`
`frequencia 10 = fala muito`
`apagar mensagens = apaga tudo IA e faz backup da Database (somente adm master)`
***SOBRE FALA LOCAL | GLOBAL***
```Este bot se espressa de duas formas, local e global, quando setado local ele irá falar apenas coisas que aprendeu no grupo, ja se setada global ele vai falar tudo que ele aprendeu durante sua webvida:```
`falar apenas coisas do grupo:` inteligencia local 
`falar tudo que ele aprendeu:` inteligencia global 
`AVISO:` setando a IA como global ela pode falar palavrões e coisas ofensivas caso tenha aprendido
***CADASTRO DE COMANDOS E REPOSTAS NA DATABASE***        
🤖`Para cadastrar um comando no banco de dados:`
#comando resposta que o usuário vai receber
🤖`Para recadastrar um comando no banco de dados:`
$comando resposta que o usuário vai receber
🤖`Para deletar um comando`
%comando 
***CADASTRO DE PERGUNTA DOS USUARIOS*** 
```Sempre que um usuário enviar alguma pergunta com o ponto de interrogação ela será cadastrada na Database```
🤖`Para ver as perguntas feitas pelo usuario digite:`
perguntas 
🤖`Para limpar as perguntas da Database digite:`
limpar perguntas
***SOBRE PROIBIR E PERMITIR PALAVRAS***
```Este bot pode restringir e permitir palavras com os comandos:```
`proibir uma palavra:` proibir 
`permitir uma palavra:` permtir 
`ver palavras proibidas:` proibidas
***SOBRE O SISTEMA DE BANIMENTO AUTOMATICO***
```Este bot pode cadastrar usuários de forma automática e os banir após um perido de tempo, por padrão quando um usuário entrar no grupo ele terá 30 dias de permanencia no grupo, com 7 dias ele irá avisar que o usuario será banido marcando ele, caso queira cadastrar usuarios manualmente ou deletar cadastros, para isto responda o texto ou qualquer coisa de um usuario com o comando /id e você terá a id_usuario, após isto siga os comandos:```
`restringir usuario [restringir @usuario id_usuario dias]:`  restringir @xbadcoffee 1367451130 30 
`permitir uma palavra:` permtir 
`ver palavras proibidas:` proibidas
***EXTRAS***
🤖`Se usar a palavra dropbox como reposta em documentos e imagens eu farei o upload para seu dropbox`
🤖`Pergunte ao bot com o comando:`
fale sobre robôs
"""
        await  bot.sendMessage(chat_id, texto, 'markdown')










