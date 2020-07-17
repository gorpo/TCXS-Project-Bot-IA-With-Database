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
from config import bot, sudoers, logs, bot_username
from datetime import datetime
async def comandos_db(msg):
    # FUNÇÕES DO BOT------------------------------------>
    d = dropbox.Dropbox('qkZ0vNG8-yAAAAAAAAAb6Fezog5XaQPwjRmoFEc-Wv37XTch4Whd8BjedzbJLwig')
    conexao_sqlite = sqlite3.connect('bot.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    if msg['chat']['type'] == 'private':
        grupo = f'@{bot_username}'
    else:
        try:
            grupo = f"https://t.me/{msg['chat']['username']}"
        except:
            grupo = f"Secreto: {msg['chat']['title']}"
            pass
    chat_id = msg['chat']['id']
    usuario = msg['from']['username']
    try:
        texto = msg['text']
    except:
        pass
    data = datetime.now().strftime('%d/%m/%Y %H:%M')
    chat_type = msg['chat']['type']
    if chat_type == 'supergroup':  # se o chat for supergrupo ele manda mensagem
     ## SISTEMA DE FALA AUTOMATICA DO BOT COM BASE NOS POSTS DOS USUARIOS SQLITE3------------------------------------------->
        try:
            if msg.get('sticker'):
                id_sticker = msg['sticker']['file_id']
                await bot.sendSticker(msg['from']['id'], sticker=id_sticker)
                cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem,usuario,grupo,data)VALUES(null,'sticker','{id_sticker}','{usuario}','{grupo}','{data}')""")
                conexao_sqlite.commit()
            if msg.get('photo'):
                id_foto = msg['photo'][0]['file_id']
                cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem,usuario,grupo,data)VALUES(null,'imagem','{id_foto}','{usuario}','{grupo}','{data}')""")
                conexao_sqlite.commit()
                try:
                    await bot.sendPhoto(-1001402280935, id_foto)
                except:
                    pass
                try:
                    await bot.sendPhoto(msg['from']['id'], photo=id_foto, caption='Você mandou esta foto no grupo.')
                except:
                    pass
            if msg.get('document'):
                id_documento = msg['document']['file_id']
                #await  bot.sendDocument(msg['from']['id'], id_documento)
                cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem,usuario,grupo,data)VALUES(null,'documento','{id_documento}','{usuario}','{grupo}','{data}')""")
                conexao_sqlite.commit()
                try:
                    captado = msg['caption']
                except:
                    captado = f'Vem de PV q o Pai ta ON: @{bot_username} '
                await bot.sendDocument(-1001166426209, id_documento, captado)
            if msg.get('audio'):
                id_audio = msg['audio']['file_id']
                cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem,usuario,grupo,data)VALUES(null,'audio','{id_audio}','{usuario}','{grupo}','{data}')""")
                conexao_sqlite.commit()
            if msg.get('video'):
                id_video = msg['video']['file_id']
                cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem,usuario,grupo,data)VALUES(null,'video','{id_video}','{usuario}','{grupo}','{data}')""")
                conexao_sqlite.commit()
                try:
                    await bot.sendVideo(-1001402280935, id_video)
                except:
                    pass
                try:
                    await bot.sendVideo(msg['from']['id'], id_video, caption=f'@{usuario} Você mandou este video no {grupo}.')
                except:
                    pass
            if msg.get('voice'):
                id_voz = msg['voice']['file_id']
                await bot.download_file(msg['voice']['file_id'], 'images/audio_usuario_db.ogg')
                sound = AudioSegment.from_file("images/audio_usuario_db.ogg")
                sound.export("images/audio_usuario_db.wav", format="wav", bitrate="128k")
                r = sr.Recognizer()
                with sr.WavFile('images/audio_usuario_db.wav') as source:
                    audio = r.record(source)
                texto = r.recognize_google(audio, language='pt-BR')
                await bot.sendMessage(chat_id, f"`{msg['from']['first_name']} disse:`\n```{texto}```", 'markdown', reply_to_message_id=msg['message_id'])
                # cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem)VALUES(null,'texto','{texto}')""")
                # conexao_sqlite.commit()
            if msg.get('text'):  # ALTERAR A FREQUENCIA DO BOT------------------------------------------------------------------------------>
                texto = msg['text']
                cursor_sqlite.execute(f"""INSERT INTO mensagens(int_id,tipo,mensagem,usuario,grupo,data)VALUES(null,'texto','{texto}','{usuario}','{grupo}','{data}')""")
                conexao_sqlite.commit()
                if texto.lower().startswith('frequencia'):
                    valor = texto[11:]
                    cursor_sqlite.execute(f"""  INSERT INTO frequencia(valor)VALUES('{valor}')""")
                    conexao_sqlite.commit()
                    if int(valor) == 0:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, estou mutado so irei reponder comandos cadastrados`','markdown')
                    if int(valor) == 1:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, vou tentar falar pouco`','markdown')
                    if int(valor) >= 2:
                        await bot.sendMessage(chat_id, f'🤖 `Frequencia alterada para {valor}, vou falar bastante`\nCaso queira que eu pare de falar defina a frequencia: 0\n Para eu falar menos defina frequencia: 1','markdown')
                cursor_sqlite.execute("""SELECT * FROM frequencia; """)
                frequencia_sqlite = cursor_sqlite.fetchall()
                try:
                    contador = int(random.randint(0, frequencia_sqlite[-1][0] * 2)) - 1
                    frequencia = int(frequencia_sqlite[-1][0])
                except:
                    contador = random.randint(0, 1)
                    frequencia = 1
                    pass
                if contador < frequencia:  # se o contador for menor que a frequencia o bot entrara na conversa enviando alguma mensagem salva no banco de dados
                    pass  # print(f'🚫 Não enviou: contador:{int(contador)}     - menor que a frequencia setada: {frequencia }')
                else:  # print(f'🤖 Bot enviou: contador:{int(contador)} maior/igual que a frequencia setada: {frequencia}')
                    cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                    mensagens_sqlite = cursor_sqlite.fetchall()
                    quantidade_mensagens = len(mensagens_sqlite)
                    randomico = random.randint(0,  quantidade_mensagens - 1)  # fornece um numero randomico para pegarmos as mensagens na db
                    m = mensagens_sqlite[randomico][2]
                    tipo_mensagem = mensagens_sqlite[randomico][1]
                    if m.startswith('fale') or m.lower().startswith('luppy') or 'att' in m or m.startswith('frequencia') or m.startswith('#') or m.startswith('comandos') or m.startswith('%') or m.startswith('$') or m.startswith('/') or m.startswith('permitir') or m.startswith('proibir') or m.startswith('proibidas'):
                        pass
###--->>> SISTEMA DE RESPOSTA AUTOMATICA COM BASE NA VARIAVEL "tipo" DA DATABASE  |  COMENTE E DESCOMENTE LINHAS PARA QUE O BOT ENVIE OU NAO AS MENSAGENS-------------------------------->
                    else:
                        if tipo_mensagem == 'imagem':
                            await bot.sendPhoto(chat_id, photo=m)
                            print(f'🤖 Bot enviou uma imagem no grupo {msg["chat"]["title"]} com a id {m}')
                        if tipo_mensagem == 'documento':
                            #await bot.sendDocument(chat_id, document=m)
                            print(f'🤖 Bot tentou enviar um documento no grupo {msg["chat"]["title"]} com a id {m}')
                        if tipo_mensagem == 'audio':
                            #await bot.sendAudio(chat_id, audio=m)
                            print(f'🤖 Bot tentou enviar um audio no grupo {msg["chat"]["title"]} com a id {m}')
                        if tipo_mensagem == 'video':
                            await bot.sendVideo(chat_id, video=m)
                            print(f'🤖 Bot enviou um video no grupo {msg["chat"]["title"]} com a id {m}')
                        if tipo_mensagem == 'texto':
                            await bot.sendMessage(chat_id, m)
                            print(f'🤖 Bot enviou no grupo {msg["chat"]["title"]}: {m}')
                        if tipo_mensagem == 'sticker':
                            await bot.sendSticker(chat_id, sticker=m)
                            print(f'🤖 Bot enviou sticker no grupo {msg["chat"]["title"]} com a id {m}')
        except Exception as e:
            print(f'Erro no sistema de fala automatica: {e}\nTente remover as linhas dos "canais" que ele envia fotos/videos e que ele envia documentos')
            pass
    # SISTEMA QUE DELETA MENSAGENS PROIBIDAS --------------------------------------------------------------------->
        try:  # verifica se a palavra é proibida, se for deleta a mensagem do usuario e envia um aviso------>
            cursor_sqlite.execute("""SELECT * FROM proibido; """)
            mensagens_proibidas = cursor_sqlite.fetchall()
            for mensagem in mensagens_proibidas:
                if mensagem['termo'] in texto:
                    if texto.lower().startswith('permitir'):
                        pass
                    else:
                        try:
                            await bot.deleteMessage((msg['chat']['id'], msg['reply_to_message']['message_id']))
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `você usou uma palavra proibida, não fale bosta aqui!`",'markdown')
                        except TelegramError:
                            pass
                        try:
                            await bot.deleteMessage((msg['chat']['id'], msg['message_id']))
                            await bot.sendMessage(chat_id,f"@{msg['from']['username']} `você usou uma palavra proibida, não fale bosta aqui!`",'markdown')
                        except TelegramError:
                            pass

            if msg.get('text'):
                texto = msg['text']
                if texto.lower().startswith('proibir'):  # proibe as palavras e as cadastra na Database------------------------------->
                    palavra_proibida = texto[8:]
                    if palavra_proibida.lower() == 'proibir' or palavra_proibida.lower() == '' or palavra_proibida.lower() == ' '  or palavra_proibida.lower() == '' or palavra_proibida.lower() == 'comandos' or palavra_proibida.lower() == '/help' or palavra_proibida.lower() == 'fale sobre' or palavra_proibida.lower() == 'frequencia' or palavra_proibida.lower() == 'cmd' or palavra_proibida.startswith('/') or palavra_proibida.startswith('#') or palavra_proibida.startswith('$') or palavra_proibida.startswith('%') or palavra_proibida.startswith('@'):
                        await bot.sendMessage(chat_id,f"@{msg['from']['username']} `não posso proibir esta palavra, talvez ela seja um comando meu.`",'markdown')
                        pass
                    else:
                        cursor_sqlite.execute(f"""INSERT INTO proibido VALUES('{palavra_proibida}')""")
                        conexao_sqlite.commit()
                        await bot.sendMessage(chat_id,f'🤖🚫 `Proibido:`***{palavra_proibida}***\nPara voltar permitir esta palavra use o comando `permitir`, para ver palavras proibidas use `proibidas`','markdown', reply_to_message_id=msg['message_id'])
                if texto.lower().startswith('permitir'):  # permite novamente as palavras e as descadastra na Database------------------------------->
                    palavra_permitida = texto[9:]
                    cursor_sqlite.execute(f"""DELETE FROM proibido WHERE termo='{palavra_permitida}'""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f'🤖✔️ `Permitido:`***{palavra_permitida}***\nPara voltar proibir esta palavra use o comando `proibir`, para ver palavras proibidas use `proibidas`',reply_to_message_id=msg['message_id'])
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
            pass  # print(f'Erro no sistema de palavras proibidas: {e}')
        # COMANDOS INSERIDOS MANUALMENTE NA PROGRAMAÇAO--------------------------------------------------------------->
        if msg.get('text'):
            texto = msg['text']
            try:
                if texto == 'amigo':
                    await bot.sendVideo(chat_id, video=open('images/marcinho.mp4', 'rb'),
                                  reply_to_message_id=msg['message_id'])
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
            except:
                pass
            try:  # VIDEOS na Database----------------------------------------------------------------->
                if 'video' in msg.get('reply_to_message') and texto.startswith('#'):
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
            except:
                pass
            try:  # DOCUMENTOS na Database------------------------------------------------------------->
                if 'document' in msg.get('reply_to_message') and texto.startswith('#'):
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
            except:
                pass
            try:  # AUDIOS VOZ na Database------------------------------------------------------------>
                if 'voice' in msg.get('reply_to_message') and texto.startswith('#'):
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
            except:
                pass
            try:  # AUDIOS MUSICA na Database--------------------------------------------------------->
                if 'audio' in msg.get('reply_to_message') and texto.startswith('#'):
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
            except:
                pass
            try:  # MENSAGENS de texto na Database---------------------------------------------------------------->
                if 'text' in msg.get('reply_to_message') and texto.startswith('#'):
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
            except:
                pass
            try:  # SISTEMA DE CADASTRO DE COMANDOS DOS USUARIOS USANDO SOMENTE O # -------------------------------------------------------------->
                if texto.startswith('#') and not msg.get('reply_to_message'):
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
            except:
                pass
            try:  # RECADASTRAMENTO DE RESPOSTAS USANDO O $--------------------------------------------------------------------------------------------------->
                if texto.startswith('$'):
                    texto_cadastro = texto[1:].split(' ')
                    comando = str(texto_cadastro[0]).lower()  # gera o texto do comando
                    separador = ' '
                    resposta = separador.join(map(str, texto_cadastro[
                                                       1:]))  # pega todo resto da lista e poe no separador retornando toda lista em uma linha
                    cursor_sqlite.execute(f"""DELETE FROM comandos WHERE comando='{comando}'""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f'Comando: {comando} apagado do sistema.',reply_to_message_id=msg['message_id'])
                    cursor_sqlite.execute(f"""INSERT INTO comandos(tipo,comando,resposta,usuario,grupo,data)VALUES('texto',{comando}','{resposta}','{usuario}','{grupo}','{data}')""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f"🤖 Dados inseridos com exito.`Comando:` {comando}`Resposta:` {resposta}", 'markdown',        reply_to_message_id=msg['message_id'])

            except:
                pass
            try:  # DELETAR COMANDOS CADASTRADOS USANDO O %------------>
                if texto.startswith('%'):
                    comando = texto[1:].lower()  # tira do texto o  comando 'cadastrar'
                    cursor_sqlite.execute(f"""DELETE FROM comandos WHERE comando='{comando}'""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f'🤖 `Comando {comando} apagado do sistema.`', 'markdown',reply_to_message_id=msg['message_id'])
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
                    cursor_sqlite.execute("""DELETE FROM perguntas""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} Todas perguntas foram apagadas!")
            except:
                pass
            # SISTEMA DE UPLOAD PARA DROPBOX | necessario mudar o caminho para sua pasta que quer baixar os arquivos----------------------------------------------------------->
            try:  # UPLOAD DE DOCUMENTOS PARA O DROPBOX
                if 'document' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
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
                        with open(f'images/{nome_arquivo}', "rb") as f:
                            meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                        link = d.sharing_create_shared_link(targetfile)
                        url = link.url
                        dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                        await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei upar seu arquivo no Dropbox`\nlink:{dl_url}",'markdown', reply_to_message_id=msg['message_id'])
                        os.remove(f'images/{nome_arquivo}')
            except:
                pass
            try:  # UPLOAD DE IMAGENS/FOTOS PARA O DROPBOX
                if 'photo' in msg.get('reply_to_message') and texto.lower().startswith('dropbox'):
                    id_arquivo = msg.get('reply_to_message')['photo'][0]['file_id']
                    nome_arquivo = id_arquivo[0:5]
                    await bot.download_file(id_arquivo, f'images/{nome_arquivo}.jpg')
                    await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",'markdown', reply_to_message_id=msg['message_id'])
                    targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}.jpg"
                    time.sleep(1)
                    with open(f'images/{nome_arquivo}.jpg', "rb") as f:
                        meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                    link = d.sharing_create_shared_link(targetfile)
                    url = link.url
                    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                    await bot.sendMessage(chat_id,f"🤖 `{msg['from']['first_name']} acabei upar seu arquivo no Dropbox`\nlink:{dl_url}",'markdown', reply_to_message_id=msg['message_id'])
                    os.remove(f'images/{nome_arquivo}.jpg')
            except:
                pass
            try:  # SISTEMA DE RESPOSTAS COM BASE NA WIKIPEDIA---------------------------------------------------------------->
                if 'fale sobre' in texto.lower():
                    termo = texto[10:]
                    wikipedia.set_lang("pt")
                    pesquisa = wikipedia.summary(termo)
                    await bot.sendMessage(chat_id, pesquisa, reply_to_message_id=msg['message_id'])
            except Exception as e:
                print(e)
                await bot.sendMessage(chat_id, 'Desconheço este assunto...', reply_to_message_id=msg['message_id'])
                pass

    # COMANDOS PARA CANAL-------------------------------------->
    if chat_type == 'channel':
        print(f'canal: {msg}')  # id_zoeiras = -1001402280935    id_hacker = -1001166426209
        pass

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
                if msg.get('text') == 'luppy solta a att':
                    await bot.sendMessage(chat_id, f"@{msg['from']['first_name']} você esta tentando roubar a TCXS Store, cara vou pegar seu ip e te hackear agora mesmo!!! ", 'markdown',reply_to_message_id=msg['message_id'])
                cursor_sqlite.execute("""SELECT * FROM mensagens; """)
                mensagens_sqlite = cursor_sqlite.fetchall()
                quantidade_mensagens = len(mensagens_sqlite)
                randomico = random.randint(0,quantidade_mensagens - 1)  # fornece um numero randomico para pegarmos as mensagens na db
                m = mensagens_sqlite[randomico][2]
                tipo_mensagem = mensagens_sqlite[randomico][1]
                if m.startswith('frequencia') or m.startswith('#') or m.startswith('comandos') or m.startswith('%') or m.startswith('$') or m.startswith('/help') or m.startswith('permitir') or m.startswith('proibir') or m.startswith('proibidas'):
                    pass
                else:  # SISTEMA DE RESPOSTA AUTOMATICA COM BASE NA VARIAVEL "tipo" DA DATABASE-------------------------------->
                    if tipo_mensagem == 'imagem':
                        await bot.sendPhoto(chat_id, photo=m)
                    if tipo_mensagem == 'video':
                        await bot.sendVideo(chat_id, video=m)
                        print(f'🤖 Bot enviou um video no grupo {msg["chat"]["title"]} com a id {m}')
                    if tipo_mensagem == 'texto':
                        await bot.sendMessage(chat_id, m)
                        print(f'🤖 Bot enviou no grupo {msg["chat"]["title"]}: {m}')
                    if tipo_mensagem == 'sticker':
                        await bot.sendSticker(chat_id, sticker=m)
                        print(f'🤖 Bot enviou sticker no grupo {msg["chat"]["title"]} com a id {m}')
        except Exception as e:
            # print(f'Erro no sistema de fala automatica do Privado do Bot: {e}')
            pass
## [+] WARNING [+] | FECHA CONEXAO PARA ESCREVER NO BANCO DE DADOS--------
    conexao_sqlite.close()
    # CONFIGURAÇÕES PARA GRUPOS----------------------------------------------------------------------------------------------------------------------------->
    if msg.get('text') == '/help':
        texto = """
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
***EXTRAS***
🤖`Se usar a palavra dropbox como reposta em documentos e imagens eu farei o upload para seu dropbox`
🤖`Pergunte ao bot com o comando:`
fale sobre robôs
***SOBRE A FREQUENCIA DE MENSAGENS*** 
```Este bot envia mensagens baseado em uma frequencia que deve ser setada entre 2 e 10, onde:```
`frequencia 1 = mudo`
`frequencia 2 = fala pouco`
`frequencia 10 = fala muito`
`apagar mensagens = apaga tudo IA e faz backup da Database (somente adm master)`
***SOBRE PROIBIR E PERMITIR PALAVRAS***
```Este bot pode restringir e permitir palavras com os comandos:```
`proibir uma palavra:` proibir 
`permitir uma palavra:` permtir 
`ver palavras proibidas:` proibidas
"""
        await  bot.sendMessage(chat_id, texto, 'markdown')

        return True
