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
import pymysql.cursors
import sys
import os
import dropbox
import re
import wikipedia


async def comandos_db(msg):
    # transcodifica vox em texto, recebendo audio do usuario e reenviando em texto no grupo--------------------------------------------------------------->
    if msg.get('voice'):  # or msg.get('reply_to_message')
        try:
            await bot.download_file(msg['voice']['file_id'], 'audio_usuario.ogg')
            sound = AudioSegment.from_file("audio_usuario.ogg")
            sound.export("audio_usuario.wav", format="wav", bitrate="128k")
            r = sr.Recognizer()
            with sr.WavFile('audio_usuario.wav') as source:
                audio = r.record(source)
            texto = r.recognize_google(audio, language='pt-BR')
            await bot.sendMessage(msg['chat']['id'], f"`{msg['from']['first_name']} disse:`\n```{texto}```", 'markdown',
                                  reply_to_message_id=msg['message_id'])
        except Exception as e:
            print(e)
            pass

    # mensagem de boas vindas ao usuario--------------->>
    if msg.get('new_chat_member'):
        user_novo = msg.get('new_chat_member')['first_name']
        await bot.sendMessage(chat_id, f"Bem vindo {user_novo} ao {msg['chat']['title']}")


    d = dropbox.Dropbox('qkZ0vNG8-yAAAAAAAAAbzVLfdP5vdx64GEdmlc1YcugJowBDHmXbDR3-wiM0xvQo')
    texto = msg['text']
    chat_id = msg['chat']['id']
    nome_usuario = msg['from']['first_name']
    if msg.get('text'):        
        # faz a conexao com o banco de dados---------------->
        conexao = pymysql.connect(host='localhost',
                                  port=3306,
                                  user='gorpo',
                                  password='daimonae',
                                  db='luppy_bot',
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

        # sistema de RESPOSTA com database-------------->
        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from comandos')
                resultados = cursor.fetchall()  # pega todos resultados da db
                cursor.close()
                for resultado in resultados:
                    comando = resultado['comando']
                    resposta = resultado['resposta']
                    tipo = resultado['tipo']
                    if tipo == 'texto' and comando == texto:
                        await bot.sendMessage(chat_id, f"{resposta}", reply_to_message_id=msg['message_id'])
                    if tipo == 'imagem' and comando == texto:
                        await bot.sendPhoto(chat_id, photo=resposta, reply_to_message_id=msg['message_id'])
                    if tipo == 'voz' and comando == texto:
                        await bot.sendVoice(chat_id, voice=resposta, reply_to_message_id=msg['message_id'])
                    if tipo == 'audio' and comando == texto:
                        await bot.sendAudio(chat_id, audio=resposta, reply_to_message_id=msg['message_id'])
                    if tipo == 'documento' and comando == texto:
                        await bot.sendDocument(chat_id, document=resposta, reply_to_message_id=msg['message_id'])
                    if tipo == 'video' and comando == texto:
                        await bot.sendVideo(chat_id, video=resposta, reply_to_message_id=msg['message_id'])
        except:
            pass
        # sistema de RESPOSTA sem database----------------------------->
        try:
            if 'fale sobre' in texto:
                try:
                    termo = texto[10:]
                    wikipedia.set_lang("pt")
                    pesquisa = wikipedia.summary(termo)
                    await bot.sendMessage(chat_id, pesquisa, reply_to_message_id=msg['message_id'])
                except Exception as e:
                    print(e)
                    await bot.sendMessage(chat_id, 'Desconheço este assunto...', reply_to_message_id=msg['message_id'])
        except:
            pass
            """
        # CADASTRO PERGUNTAS DOS USUARIOS---------------------------------------------------------->
        try:
            if texto[-1] == '?':
                with conexao.cursor() as cursor:
                    grupo = msg['chat']['title']
                    usuario = f"@{msg['from']['username']}"
                    cursor.execute(f"insert into perguntas values (id,'{usuario}','{grupo}','{texto}')")
                    conexao.commit()  # gravação do comando no banco de dados
                    cursor.close()
                    await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} `sua pergunta foi cadastrada.`",
                                          'markdown')
        except:
            pass
        # VERIFICAR PERGUNTAS DOS USUARIOS------------------->
        try:
            if texto == 'perguntas':
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from perguntas')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    if resultados == ():
                        await bot.sendMessage(chat_id,
                                              f"🤖 {msg['from']['first_name']} `não tenho perguntas cadastradas, tente outra hora ou cadastre algumas perguntas.`",
                                              'markdown')
                    else:
                        for resultado in resultados:
                            usuario = resultado['usuario']
                            grupo = resultado['grupo']
                            pergunta = resultado['pergunta']
                            await bot.sendMessage(chat_id, f"`Usuário:`{usuario}\n`Grupo:`{grupo}\n`Pergunta:`{pergunta}",
                                                  'markdown')
        except:
            pass
        # LIMPAR PERGUNTAS DOS USUARIOS------------------->
        try:
            if texto == 'limpar perguntas':
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('TRUNCATE TABLE perguntas')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    await bot.sendMessage(chat_id, f"🤖 {msg['from']['first_name']} Todas perguntas foram apagadas!")
        except:
            pass   """
                      
        # CRUD DO BOT ABAIXO, sistema de cadastro de video, imagem, audio, voz, texto e comandos personalizados----------------------------------------->
        # IMAGENS na Database------------------------------------->
        try:
            if 'photo' in msg.get('reply_to_message') and texto.startswith('#'):
                comando = texto[1:]
                id_foto = msg.get('reply_to_message')['photo'][0]['file_id']
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro_imagem = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro_imagem = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro_imagem == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    elif existe_cadastro_imagem == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'imagem','{comando}','{id_foto}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_foto}",
                                                  'markdown')
        except:
            pass
        # VIDEOS na Database--------------------------------------->
        try:
            if 'video' in msg.get('reply_to_message') and texto.startswith('#'):
                comando = texto[1:]
                id_video = msg.get('reply_to_message')['video']['file_id']
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro_video = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro_video = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro_video == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    elif existe_cadastro_video == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'video','{comando}','{id_video}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_video}",
                                                  'markdown')
        except:
            pass
        # DOCUMENTOS na Database-------------------------------------------->
        try:
            if 'document' in msg.get('reply_to_message') and texto.startswith('#'):
                comando = texto[1:]
                id_documento = msg.get('reply_to_message')['document']['file_id']
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro_document = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro_document = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro_document == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    elif existe_cadastro_document == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'documento','{comando}','{id_documento}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_documento}",
                                                  'markdown')
        except:
            pass
        # AUDIOS VOZ na Database-------------------------------------------->
        try:
            if 'voice' in msg.get('reply_to_message') and texto.startswith('#'):
                comando = texto[1:]
                id_voz = msg.get('reply_to_message')['voice']['file_id']
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro_voz = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro_voz = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro_voz == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    elif existe_cadastro_voz == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'voz','{comando}','{id_voz}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_voz}",
                                                  'markdown')
        except:
            pass
        # AUDIOS MUSICA na Database-------------------------------------------->
        try:
            if 'audio' in msg.get('reply_to_message') and texto.startswith('#'):
                comando = texto[1:]
                id_audio = msg.get('reply_to_message')['audio']['file_id']
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro_audio = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro_audio = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro_audio == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    elif existe_cadastro_audio == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'audio','{comando}','{id_audio}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`File_id:` {id_audio}",
                                                  'markdown')
        except:
            pass
        # MENSAGENS na Database-------------------------------------------->
        try:
            if 'text' in msg.get('reply_to_message') and texto.startswith('#'):
                comando = texto[1:]
                id_text = msg.get('reply_to_message')['text']
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro_text = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro_text = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro_text == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "🤖 `Comando já cadastrado, tente outro`", 'markdown')
                    elif existe_cadastro_text == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'texto','{comando}','{id_text}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"`🤖 Dados inseridos com exito.\nComando:` {comando}\n`File_id:` {id_text}",
                                                  'markdown')
        except:
            pass

        # CADASTRO de RESPOSTAS para o BOT ------------>
        if texto.startswith('#') and not msg.get('reply_to_message'):
            texto_cadastro = texto[1:].split(' ')
            comando = str(texto_cadastro[0])  # gera o texto do comando
            separador = ' '
            resposta = separador.join(map(str, texto_cadastro[1:]))
            with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                try:
                    # seleciona tudo na tabela usuarios
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    existe_cadastro = 0  # contador para verificar se o comando ja existe
                    for res in resultados:  # loop em todos resultados da Database
                        # se o comando ja existir o valor existe_cadastro passa ser 1
                        if res['comando'] == comando:
                            existe_cadastro = 1  # troca o valor de existe_cadastro para 1
                    if existe_cadastro == 1:  # se o valor existe_cadastro esta como 1 ele avisa que ja existe cadastro
                        await bot.sendMessage(chat_id, "Comando já cadastrado, tente outro",
                                              reply_to_message_id=msg['message_id'])
                    elif existe_cadastro == 0:  # se o valor de existe_cadastro nao foi alterado ele cadastra novo comando
                        with conexao.cursor() as cursor:
                            # insere os valores na tabela
                            cursor.execute(f"insert into comandos values (id,'texto','{comando}','{resposta}')")
                            conexao.commit()  # gravação do comando no banco de dados
                            cursor.close()
                            await bot.sendMessage(chat_id,
                                                  f"🤖 Dados inseridos com exito.\nComando: {comando}\nResposta: {resposta}",
                                                  reply_to_message_id=msg['message_id'])
                except:
                    pass
        # RECADASTRO de respostas------------>
        try:
            if texto.startswith('$'):
                texto_cadastro = texto[1:].split(' ')
                comando = str(texto_cadastro[0])  # gera o texto do comando
                separador = ' '
                resposta = separador.join(map(str, texto_cadastro[
                                                   1:]))  # pega todo resto da lista e poe no separador retornando toda lista em uma linha
    
                with conexao.cursor() as cursor:
                    # executa o codigo mysql no banco de dados
                    cursor.execute(f"DELETE FROM comandos WHERE comando='{comando}'")
                    conexao.commit()  # grava o codigo no banco de dados
                    cursor.close()
                    await bot.sendMessage(chat_id, f'Comando: {comando} apagado do sistema.',
                                          reply_to_message_id=msg['message_id'])
                with conexao.cursor() as cursor:
                    # insere os valores na tabela
                    cursor.execute(f"insert into comandos values (id,'texto','{comando}','{resposta}')")
                    conexao.commit()  # gravação do comando no banco de dados
                    cursor.close()
                    await bot.sendMessage(chat_id,
                                          f"🤖 Dados inseridos com exito.\n`Comando:` {comando}\n`Resposta:` {resposta}",
                                          'markdown')
        except:
            pass
    
        # DELETAR respostas------------>
        if texto.startswith('%'):
            comando = texto[1:]  # tira do texto o  comando 'cadastrar'
            try:
                with conexao.cursor() as cursor:
                    # executa o codigo mysql no banco de dados
                    cursor.execute(f"DELETE FROM comandos WHERE comando='{comando}';")
                    conexao.commit()  # grava o codigo no banco de dados
                    cursor.close()
                    await bot.sendMessage(chat_id, f'🤖 `Comando {comando} apagado do sistema.`', 'markdown',
                                          reply_to_message_id=msg['message_id'])
            except:
                await bot.sendMessage(chat_id, f'🤖 `Comando {comando} inexistente ou ocorreu um erro.`', 'markdown',
                                      reply_to_message_id=msg['message_id'])
    
        # LISTAR comandos------------>
        if texto == 'comando':
            try:
                with conexao.cursor() as cursor:  # faz a conexao com o cursor do mysql
                    # seleciona tudo na tabela usuarios
                    cursor.execute('select * from comandos')
                    resultados = cursor.fetchall()  # tras os resultados da tabela mysql
                    cursor.close()  # sempre fechar a conexao para nao dar erro no mysql
                    todos_comandos = []
                    separador = ' \n'
                    for result in resultados:
                        todos_comandos.append(result['comando'])
                # separador.join(map(str, todos_comandos)) descompacta lista em uma coisa so
                await bot.sendMessage(chat_id,
                                      f'`Comandos cadastrados:`\n ***{separador.join(map(str, todos_comandos))}***',
                                      'markdown', reply_to_message_id=msg['message_id'])
            except Exception as e:
                print(e)
                pass
    
        # SISTEMA DROPBOX----------------------------------------------------------->
        # upload documentos dropbox
        try:
            if 'document' in msg.get('reply_to_message') and texto.startswith('dropbox'):
                id_arquivo = msg.get('reply_to_message')['document']['file_id']
                nome_arquivo = msg.get('reply_to_message')['document']['file_name']
                tamanho = msg.get('reply_to_message')['document']['file_size']
                if tamanho > 10000000:
                    await bot.sendMessage(chat_id, '🤖 `Tamanho maximo para envio de 10mb`', 'markdown',
                                          reply_to_message_id=msg['message_id'])
                if tamanho < 10000000:
                    await bot.download_file(id_arquivo, f'arquivos/{nome_arquivo}')
                    await bot.sendMessage(chat_id,
                                          f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",
                                          'markdown', reply_to_message_id=msg['message_id'])
                    targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}"
                    with open(f'{nome_arquivo}', "rb") as f:
                        meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                    link = d.sharing_create_shared_link(targetfile)
                    url = link.url
                    dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                    await bot.sendMessage(chat_id,
                                          f"🤖 `{msg['from']['first_name']} acabei upar seu arquivo no Dropbox`\nlink:{dl_url}",
                                          'markdown', reply_to_message_id=msg['message_id'])
                    os.remove(f'{nome_arquivo}')
        except:
            pass
        # upload fotos dropbox
        try:
            if 'photo' in msg.get('reply_to_message') and texto.startswith('dropbox'):
                id_arquivo = msg.get('reply_to_message')['photo'][0]['file_id']
                nome_arquivo = id_arquivo[0:5]
                await bot.download_file(id_arquivo, f'{nome_arquivo}.jpg')
                await bot.sendMessage(chat_id,
                                      f"🤖 `{msg['from']['first_name']} acabei de baixar seu arquivo, vou upar ele para o Dropbox`",
                                      'markdown', reply_to_message_id=msg['message_id'])
                targetfile = f"/GDRIVE_TCXSPROJECT/MARCINHO_BOT/{nome_arquivo}.jpg"
                with open(f'{nome_arquivo}.jpg', "rb") as f:
                    meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
                link = d.sharing_create_shared_link(targetfile)
                url = link.url
                dl_url = re.sub(r"\?dl\=0", "?dl=1", url)
                await bot.sendMessage(chat_id,
                                      f"🤖 `{msg['from']['first_name']} acabei upar seu arquivo no Dropbox`\nlink:{dl_url}",
                                      'markdown', reply_to_message_id=msg['message_id'])
                os.remove(f'{nome_arquivo}.jpg')
        except:
            pass
    
    
        
    
        return True
