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
from utils import send_to_dogbin, send_to_hastebin
from amanobot.namedtuple import InlineKeyboardMarkup
import keyboard
from config import bot, version, bot_username, git_repo,logs,sudoers
from db_handler import cursor
from get_strings import strings, Strings
from config import bot, version, bot_username, git_repo,logs,sudoers,grupo_permanencia
import sqlite3
import os
from plugins.admins import is_admin
from datetime import datetime
from dateutil.relativedelta import relativedelta



async def permanencia(msg):
    try:# FUNÇÕES DO BOT------------------------------------>
        conexao_sqlite = sqlite3.connect('bot_database.db')
        conexao_sqlite.row_factory = sqlite3.Row
        cursor_sqlite = conexao_sqlite.cursor()
        chat_id = msg['chat']['id']
        chat_type = msg['chat']['type']
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)  # and adm['user'] == True
        ## SISTEMA DE BANIMENTO----------------------------->
        if msg['chat']['title'] in grupo_permanencia:
            if msg['text'] == 'verificar': #adm['user'] == False:
                try:
                    hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    cursor_sqlite.execute("""SELECT * FROM permanencia; """)
                    resultados = cursor_sqlite.fetchall()
                    for resutado in resultados:
                        data_inicial = resutado['data_inicial']
                        data_ban = resutado['data_final']
                        id_doador = resutado['id_doador']
                        doador = resutado['doador']
                        dias = resutado['dias']
                        aviso = resutado['data_aviso']
                        #ALERTA DE AVISO PARA O DOADOR----:
                        if hoje[0:2] == aviso[0:2]:
                            await bot.sendMessage(chat_id,f"🤖 {doador} ***Falta uma semana para você grupo de doadores, caso ainda tenha interesse em continuar usando a loja faça uma doação, envie o comprovante aqui no grupo que um de nossos administradores irá colocar mas dias em sua permanencia.***\n`Doador:` {doador}\n`Id_Doador:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Data Aviso:` {aviso}\n`Permanência:` {dias}",'markdown')
                        #BANE O USUARIO CASO A DATA TENHA SIDO IGUAL A DO DIA HOJE
                        if hoje[0:6] <= data_ban[0:6]:
                            await bot.kickChatMember(msg['chat']['id'], id_doador)
                            cursor_sqlite.execute(f"""DELETE FROM permanencia WHERE doador='{doador}'""")
                            conexao_sqlite.commit()
                            await bot.sendMessage(chat_id,f"🤖 ***Removido do grupo pois deu a sua permanência do grupo de doadores.***\n`Doador:` {doador}\n`Id_Doador:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Permanência:` {dias}",'markdown')
                            await bot.unbanChatMember(msg['chat']['id'], id_doador)
                except Exception as e:
                    print(e)
            #consulta a frequencia que o doador ainda pode ficar no grupo---------------------------->
            if   msg['text'].split()[0] == 'consulta':
                try:
                    cursor_sqlite.execute("""SELECT * FROM permanencia; """)
                    resultados = cursor_sqlite.fetchall()
                    for resutado in resultados:
                        data_inicial = resutado['data_inicial']
                        data_ban = resutado['data_final']
                        id_doador = resutado['id_doador']
                        doador = resutado['doador']
                        dias = resutado['dias']
                        data_aviso = resutado['data_aviso']
                        if msg['text'].split()[1] == doador:
                            await bot.sendMessage(chat_id,f"🤖 {doador} ***Sua permanência do grupo de doadores.***\n`Doador:` {doador}\n`Id_Doador:` {id_doador}\n`Início:` {data_inicial}\n`Termino:` {data_ban}\n`Aviso Vencimento:` {data_aviso}\n`Permanência:` {dias}",'markdown')
                except Exception as e:
                    print(e)


        #sistema cadastro de restriçao de doadores no grupo--------------------------------------------->
        if 'restringir' in msg['text'].split()[0]  and msg['chat']['title'] in grupo_permanencia:
            if adm['user'] == True:
                try:
                    admin = msg['from']['username']
                    doador = msg['text'].split()[1]
                    id_doador = msg['text'].split()[2]
                    dias = msg['text'].split()[3]
                    hoje = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                    data_inicial = hoje
                    dias_restantes = datetime.now() + relativedelta(days=int(dias))#--------------------------------
                    data_final = dias_restantes.strftime('%d/%m/%Y %H:%M:%S')
                    data_avisar = dias_restantes - relativedelta(days=int(7))#-------------------------------------
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
                    await bot.sendMessage(chat_id,f"🤖 `Ocorreu um erro ao inserir os dados na Database,este comando funciona somente para administradores, tente novamente e verifique se usou o comando da forma correta, qualquer espaço ou dados invalidos podem dar erro ao cadastrar, evitando assim dados invalidos na Database.Envie novamente o comando  exemplo:` ```restringir @doador id_doador dias``` ***Exemplo:*** restringir @xbadcoffee 1367451130 30 ",'markdown')



#SISTEMA PARA LIMPAR OS DOADORES CADASTRADOS NA DATABASE DE PERMANENCIA NO GRUPO DE DOADORES---------------------->
        if 'limpar' in msg['text'].split()[0] and msg['chat']['title'] in grupo_permanencia:
            if adm['user'] == True:
                try:
                    doador = msg['text'].split()[1]
                    cursor_sqlite.execute(f"""DELETE FROM permanencia WHERE doador='{doador}'""")
                    conexao_sqlite.commit()
                    await bot.sendMessage(chat_id, f'🤖 `Usuário {doador} apagado do sistema de permanência no grupo de doadores.`', 'markdown',reply_to_message_id=msg['message_id'])

                except Exception as e:
                    await bot.sendMessage(chat_id,f"🤖 `Ocorreu um erro ao deletar os dados na Database,este comando funciona somente para administradores, tente novamente e verifique se usou o comando da forma correta, qualquer espaço ou dados invalidos podem dar erro ao cadastrar, evitando assim dados invalidos na Database.Envie novamente o comando  exemplo:` ```restringir @doador id_doador dias``` ***Exemplo:*** restringir @xbadcoffee 1367451130 30 ",'markdown')
            #se o doador nao for um admin ele avisa:
            if adm['user'] == False:
                await bot.sendMessage(chat_id, f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')

    except Exception as e:
        #print(e)
        pass