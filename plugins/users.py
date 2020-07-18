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
from config import bot, version, bot_username, git_repo,logs,sudoers
import sqlite3
import os
from plugins.admins import is_admin




async def users(msg):
    # variaveis que iniciam a Database para enviar a att paga pelos BOTOES
    conexao_sqlite = sqlite3.connect('bot.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    try:
        id_usuario = msg['from']['id']
        adm = await is_admin(msg['chat']['id'], msg['from']['id'], id_usuario)
    except Exception as e:
        pass
    if msg.get('text') and msg['chat']['type'] == 'supergroup':
        if msg['from']['first_name']:
            pass#print('->Usuario:{} ->Envio:{} ->Grupo:{} ->Data/Hora:{} '.format(msg['from']['first_name'],msg['text'],msg['chat']['title'],time.ctime()))
## SISTEMA DE GRAVAÇÃO E ENVIO DE LOGS ---------------------------------------------------------------------------------------------------------------->
        if msg['text'].lower() == 'logs':
            if adm['user'] == True:
                cursor_sqlite.execute("""SELECT * FROM logs_usuarios; """)
                mensagens_sqlite = cursor_sqlite.fetchall()
                arquivo_logs = open('images/logs.txt', 'a',encoding='utf-8')
                arquivo_logs.write('-------[+] REGISTO DE MENSAGENS CAPTADAS PELO BOT NOS GRUPOS E PRIVADO [+]-------\n\n')
                for mensagem in mensagens_sqlite:
                    tipo = mensagem['tipo']
                    usuario = mensagem['usuario']
                    grupo = mensagem['grupo']
                    data = mensagem['data']
                    mensagem = mensagem['mensagem']
                    try:
                        texto = f"Usuario: {usuario} | Grupo: {grupo} | Tipo: {tipo} | Data: {data} ----->\nMensagem: {mensagem}\n"
                    except:
                        texto = ''
                    arquivo_logs.write(texto)
                arquivo_logs.close()
                await bot.sendDocument(msg['chat']['id'], open('images/logs.txt','rb'), reply_to_message_id=msg['message_id'])
                await bot.sendMessage(msg['chat']['id'], '`{} Esta aqui o log de conversas que tenho armazenado, espero que não tenha nada neste log que te incrimine!`'.format(msg['from']['first_name']),'markdown', reply_to_message_id=msg['message_id'])
                os.remove('images/logs.txt')
            else:
                await bot.sendMessage(msg['chat']['id'], f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')
        #LIMPAR OS LOGS
        if msg['text'].lower() == 'limpar logs' or msg['text'].lower() == 'apagar logs' or msg['text'].lower() == 'backup logs':
            if adm['user'] == True:
                cursor_sqlite.execute("""SELECT * FROM logs_usuarios; """)
                mensagens_sqlite = cursor_sqlite.fetchall()
                arquivo_logs = open('images/logs.txt', 'a',encoding='utf-8')
                arquivo_logs.write('-------[+] REGISTO DE MENSAGENS CAPTADAS PELO BOT NOS GRUPOS E PRIVADO [+]-------\n\n')
                for mensagem in mensagens_sqlite:
                    tipo = mensagem['tipo']
                    usuario = mensagem['usuario']
                    grupo = mensagem['grupo']
                    data = mensagem['data']
                    mensagem = mensagem['mensagem']
                    try:
                        texto = f"Usuario: {usuario} | Grupo: {grupo} | Tipo: {tipo} | Data: {data} ----->\nMensagem: {mensagem}\n"
                    except:
                        texto = ''
                    arquivo_logs.write(texto)
                arquivo_logs.close()
                await bot.sendDocument(msg['chat']['id'], open('images/logs.txt', 'rb'),reply_to_message_id=msg['message_id'])
                await bot.sendMessage(msg['chat']['id'],'`{} Esta aqui o Backup de logs de conversas que tenho armazenado, caso preciso guarde este arquivo pois irei limpar a Database`'.format(msg['from']['first_name']), 'markdown', reply_to_message_id=msg['message_id'])
                os.remove('images/logs.txt')
                cursor_sqlite.execute("""DELETE FROM logs_usuarios""")
                conexao_sqlite.commit()
                await bot.sendMessage(msg['chat']['id'], f"🤖 {msg['from']['first_name']} Todas os logs de usuários e grupos foram apagados!")
            else:
                await bot.sendMessage(msg['chat']['id'], f"@{msg['from']['username']} `este comando é permitido so para admin's`",'markdown')

#SISTEMA DE BOTOES INICIO ---------------------------------------------------------------->
        strs = Strings(msg['chat']['id'])
        if  msg['text'].lower() == 'comando' or msg['text'] == '/comando'  or msg['text'] == '/comandos' or msg['text'] == 'comandos' or 'help' in msg['text'].lower() or 'ajuda' in msg['text'].lower():
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=strs.get('Store Free'), callback_data='store_free')] +
                [dict(text=strs.get("Store Doadores"), callback_data='store_doadores')],
                [dict(text=strs.get('Usuários'), callback_data='comandos_usuarios')] +
                [dict(text=strs.get("Admin's"), callback_data='comandos_admins')],
                [dict(text=strs.get('Ferramentas'), callback_data='ferramentas_gerais')] +
                [dict(text=strs.get('Info | Extras'), callback_data='infos_extras')],])
            await bot.sendMessage(msg['chat']['id'],f"***{msg['from']['first_name']} {strs.get('pm_comandos_msg')}***" ,'markdown',  reply_markup=kb)
        #return True
#PEGA OS DADOS DO keyboard.py ----------------------:
    elif msg.get('data') and msg.get('message'):
        strs = Strings(msg['message']['chat']['id'])
        if msg['data'] == 'inicio_menu':# precisa de dois menus para voltar para o inicio criando um loop entre os dois----->
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [dict(text=strs.get('Store Free'), callback_data='store_free')] +
                [dict(text=strs.get("Store Doadores"), callback_data='store_doadores')],
                [dict(text=strs.get('Usuários'), callback_data='comandos_usuarios')] +
                [dict(text=strs.get("Admin's"), callback_data='comandos_admins')],
                [dict(text=strs.get('Ferramentas'), callback_data='ferramentas_gerais')] +
                [dict(text=strs.get('Info | Extras'), callback_data='infos_extras')], ])
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***{msg['from']['first_name']} {strs.get('pm_comandos_msg')}***", 'markdown',reply_markup=kb)
            #return True

#TCXS STORE FREE PKG    ------------------------------------------------------------------------------------------------------------------------->
        elif msg['data'] == 'store_free':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------  Espero que tenha um pendrive em mãos e saiba usar a\n loja, não daremos suporte para USUARIOS GRATUITOS, agora  copie os arquivos abaixo para a raiz de um pendrive e coloque na USB direita do seu console, caso use HAN instale o FIX, caso use HEN apenas instale a loja!```",'markdown', reply_markup=keyboard.store_free)
            #return True
        #entrega da loja free:
        elif msg['data'].split()[0] == 'download_store_free':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`INSTRUÇÕES:` ```------ Abaixo temos a ultima atualização da TCXS Store para PlayStation3, baixe  e insira no pendrive, plugue o pendrive em seu console, ative o Hen e instale ela pelo Package Manager.\nCaso seja usuário de HAN será necessário usar o Fix,baixe ele, depois basta inserir o FIx e a Loja em seu pendrive e através do seu Han instalar ambos arquivos, ambos processos concluidos reinicie seu console!```",'markdown', reply_markup=keyboard.store_free)
            await bot.sendDocument(msg['message']['chat']['id'], document='BQACAgEAAx0CTd0y0QABAfACXkmA716o7XaNW82C3Mr7O2c0bX8AApEAA0oQUUaFcnOHb037rhgE', caption='')
            #return True
        #entrega do fix
        elif msg['data'].split()[0] == 'download_fix':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`INSTRUÇÕES:` ```------ Abaixo temos o Fix da TCXS Store para PlayStation3, baixe  e insira no pendrive, plugue o pendrive em seu console com o Fix e a Loja, através do seu Han instalar ambos arquivos, ambos processos concluidos reinicie seu console!```",'markdown', reply_markup=keyboard.store_free)
            await bot.sendDocument(msg['message']['chat']['id'], document='BQACAgEAAx0CUYaz7wACJ_lfC5DOrfOmVoy_LlQ6UQtse3bVgAACxQADxKN4RUyRO66RWR8DGgQ', caption='')
            #return True
        elif msg['data'].split()[0] == 'tutorial_segundo_plano':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store ensinando como fazer os Downloads em Segundo Plano em seu PlayStation3!```",'markdown', reply_markup=keyboard.store_free)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://youtu.be/_21a5REKhBc')
            #return True
        elif msg['data'].split()[0] == 'fone_bluetooth':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Sabia que você pode usar seu fone bluetooth para jogos em seu PlayStation3?```",'markdown', reply_markup=keyboard.store_free)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://www.youtube.com/watch?v=_wYG7iMa5uY')
            #return True
        elif msg['data'].split()[0] == 'proxy_usuarios':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Siga nosso tutorial de proxy para melhorar sua conexão e evitar banimento do seu PlayStation3!```",'markdown', reply_markup=keyboard.store_free)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://youtu.be/l4o8ySk1Do4')
            #return True

#TCXS STORE PKG DOADORES |  PAYD------------------->
        elif msg['data'] == 'store_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Leia atentamente como adquirir acesso a Loja para Doadores, caso discorde basta não doar. Caso queira doar agora ou renovar sua entrada no grupo de doadores clique em Doar Agora, você será redirecionado para o Mercado Pago da TCXS Project. Não prestamos reembolsos e após doar basta enviar um comprovante no privado dos administradores.```\n`Pra ver os administradores digite:` /admin",'markdown', reply_markup=keyboard.store_doadores)
            #return True
        elif msg['data'] == 'como_participar':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Para participar você precisa fazer uma doação, pagamos mensalmente Dropbox de 5tb para armazenamento dos jogos e o valor é cobrado em dolar, a doação é mensal e doando você não esta comprando um produto, mas sim participando de uma vaquinha, todo dinheiro arrecadado fica retido na conta do Mercado Pago  para pagarmos o servidor, resumindo contribuindo você faz parte de uma vaquinha de doadores que mantem o servidor, nós da TCXS Project não temos lucro e nosso trabalho é voluntário, caso queira ajudar em algo e se juntar a equipe é bem vindo. Leia atentamente esta documentação e caso discorde de algo pedimos que não doe, não prestamos reembolsos.```\n`Pra ver os administradores digite:` /admin",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'], 'http://tcxsproject.com.br/doadores-tcxs-store-regras/')
            #return True
        elif msg['data'] == 'mercado_pago':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Vejo que tem interesse em ser doador, usamos o sistema do Mercado Pago somente, favor nao insistir com outras formas.\nO Mercado Pago aceita pagamentos online e com cartão de crédito e boletos, este sistema é o mais seguro para nos da equipe e para vocês doadores, lembre que a doação é mensal e doando você faz parte da vaquina que mantem os servidores de 5tb da Dropbox onde encontram-se nossos jogos. Pedimos que antes de doar leia atentamente as regras como mencionado antes e após fazer sua doação envie o comprovante no privado de um de nossos administradores.```\n`Pra ver os administradores digite:` /admin",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'], 'https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375')
            #return True


##  ATUALIZAÇÃO PARA DOADORES ATRAVÉS DO SISTEMA DE BOTÕES------------------------------------------------------------------------------>>
        #LOJA PAGA PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_store_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`INSTRUÇÕES:` ```------ Bem vindo a TCXS Project ,agora você faz parte dela, entenda que as doações sao mensais e nossa equipe nao ganha nada por este projeto, todo dinheiro arrecadado neste grupo é para pagar os servidores dos quais dispomos jogos. Logo a PSN STUFF IRÁ ACABAR POIS OS SERVIDORES SERÃO DESLIGADOS e assim nao terá mais os jogos gratuitos por ai, restando apenas este acervo que é mantido por voces doadores!     Vamos a Instalação!!!  --> Espero que tenha um pendrive em mãos!  --> copie os arquivos da VERSÃO 3.6 e caso use o fix de acordo com seu Exploit/Desbloqueio, se voce tem han ou CFW use o FIX HAN, caso contrário e seja o Exploit HEN em seu console use o FIX HEN, é necessaria a instalacao deste arquivo para que a loja apareca em seu console! Ative seu HAN/HEN e instale o FIX, após o FIX instalado instale a TCXS Store PKG, recomendamos reiniciar o console após este processo!!```",'markdown', reply_markup=keyboard.store_doadores)
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM loja_doadores""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho lojas cadastradas, insira o banco de dados com dados ou cadastre um PKG enviando ela no meu privado com nome inicinando com TCXS, exexmplo:` ***TCXS_Store_3.9.pkg***",'markdown', reply_markup=keyboard.store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        nome_pkg = resultado['versao']
                        data_att = resultado['data']
                        uploader_id = resultado['uploader']
                    await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption=f'{nome_pkg} upada em {data_att} por @{uploader_id}')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.store_doadores)
            #return True

        #FIX HAN PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_han_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`INSTRUÇÕES:` ```------ Abaixo temos o Fix da TCXS Store para PlayStation3, baixe  e insira no pendrive, plugue o pendrive em seu console com o Fix e a Loja, ambos processos concluidos reinicie seu console!```",'markdown', reply_markup=keyboard.store_doadores)
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_han""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix han, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HAN.pkg***",'markdown', reply_markup=keyboard.store_doadores)
                else:
                    for resultado in resultados:
                        nome_pkg = resultado['versao']
                        data_att = resultado['data']
                        id_pkg = resultado['pkg']
                        uploader_id = resultado['uploader']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EXPLOIT HAN E HEN! no menu abaixo ```",'markdown', reply_markup=keyboard.store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários HAN')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.store_doadores)
            #return True

        # FIX HEN PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_hen_doadores':
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_hen""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix hen, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***FIX_HEN.pkg***",'markdown', reply_markup=keyboard.store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EXPLOIT HAN E HEN! no menu abaixo ```",'markdown', reply_markup=keyboard.store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários HEN')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.store_doadores)
            #return True

        # FIX CFW XML DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_cfw_doadores':
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_cfw_xml""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix cfw xml, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***category_network_tool2.xml***",'markdown', reply_markup=keyboard.store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EM CONSOLES CFW no menu abaixo ```",'markdown', reply_markup=keyboard.store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg,caption='Fix para usuários CFW')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.store_doadores)
            #return True

        # FIX HEN XML PARA DOADORES COM DATABASE E BOTOES------------>
        elif msg['data'].split()[0] == 'download_fix_hen_xml_doadores':
            if msg['message']['chat']['title'] == 'Doadores TCXS 2020':
                cursor_sqlite.execute("""SELECT * FROM fix_hen_xml""")
                resultados = cursor_sqlite.fetchall()
                if resultados == []:
                    await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🤖 ***Bot diz:*** `não tenho o fix hen xml, insira o banco de dados com dados ou cadastre um PKG enviando ele no meu privado com nome de:` ***category_network.xml***",'markdown', reply_markup=keyboard.store_doadores)
                else:
                    for resultado in resultados:
                        id_pkg = resultado['pkg']
                        await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Veja o tutorial INSTALAÇÃO EM CONSOLES CFW no menu abaixo ```",'markdown', reply_markup=keyboard.store_doadores)
                        await bot.sendDocument(msg['message']['chat']['id'], document=id_pkg, caption='Fix XML para usuários HEN avançados')
            else:
                await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"🚨 `ATENÇÃO`🚨  ```------ Este comando só funciona no grupo de doadores.```",'markdown', reply_markup=keyboard.store_doadores)
            #return True

        #ACIMA DISTO PARTE DA ATT QUE PRECISA DE DB | SEGUE CODIGOS DOS DOADORES E DA ATT PAGA--------------------->
        elif msg['data'].split()[0] == 'tutorial_loja':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store instalar a loja em seu PlayStation3!```",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://cos.tv/videos/play/1586413688272059934')
            #return True
        elif msg['data'].split()[0] == 'tutorial_cfw':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store ensinando como usar em consoles CFW PlayStation3!```",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://cos.tv/videos/play/1586411677524278797')
            #return True
        elif msg['data'].split()[0] == 'tutorial_segundo_plano_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Abaixo temos o Tutorial TCXS Store ensinando como fazer os Downloads em Segundo Plano em seu PlayStation3!```",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://youtu.be/_21a5REKhBc')
            #return True
        elif msg['data'].split()[0] == 'fone_bluetooth_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Sabia que você pode usar seu fone bluetooth para jogos em seu PlayStation3?```",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://www.youtube.com/watch?v=_wYG7iMa5uY')
            #return True
        elif msg['data'].split()[0] == 'proxy_usuarios_doadores':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"`TUTORIAL:` ```------ Siga nosso tutorial de proxy para melhorar sua conexão e evitar banimento do seu PlayStation3!```",'markdown', reply_markup=keyboard.store_doadores)
            await bot.sendMessage(msg['message']['chat']['id'],'https://youtu.be/l4o8ySk1Do4')
            #return True




# COMANDOS_USUARIOS  ------------------------------------------------->
        elif msg['data'] == 'comandos_usuarios':#esta tabela pela a reply_markup da primeira e le os dados do keyboard.py e oque respondido volta pra ca ou nao, para usar local "palavra" para usar la
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"***Comandos para usuários:***",'markdown', reply_markup=keyboard.comandos_usuarios)
            #return True
        elif msg['data'] == 'comandos_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                      f"""/start   -inicia o bot
/regras  -leia nossas regras
/admin   -admins do grupo
/freepkg -loja gratuita PS3 
/fix -fix han
/tutorial -como instalar a loja
/rap -licenças dos jogos  
/desbloqueio -desbloquear PS3
/segundoplano -download 
/codigoerro  -codigos PSN/PS3
/listajogos -download direto
/doadores -instruções
/mercadopago -doar/loja 
/tcxs -informações sobre 
/tcxspyject -criar lojas
/ps1 -cria xml para loja
/ps2 -cria xml para loja 
/psp -cria xml para loja
/ps3 -cria xml para loja
/proxy -velocidade no PS3
""",'markdown', reply_markup=keyboard.comandos_usuarios)
            #return True
        elif msg['data'] == 'sites_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"/torrent -pkg torrent\n/pkg_games -pkg's\n/site -doadores\n/facebook -facebook cadastre-se\n/anime -anime gratis\n/onion -deepweb\n/dev -hacker ", reply_markup=keyboard.comandos_usuarios)
            #return True
        elif msg['data'] == 'cria_xml_users':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""***Temos um programa de computador que cria lojas diretamente no console PlayStation3***
/tcxspyject -criar lojas

***Criar XML PSP Instruções:*** 
`comando:`/psp -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"
    
    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /psp gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/psp` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```

***Criar XML PS1 Instruções:*** 
`comando:`/ps1 -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"

    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /ps1 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/ps1` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```
    
***Criar XML PS2 Instruções:*** 
`comando:`/ps2 -cria xml para loja
    ```
    1 - meu comando sempre começa com /xml
    2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
    3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
    `Copie de dentro das aspas o caractere invisivel:`"⠀"
    
    **VAMOS AO COMANDO EM SI**
    `Exemplo com caractere invisivel:`
    ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
    `Exemplo sem caractere visivel:`
    ``` /ps2 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
    **Onde cada campo:**
    `/ps2` ```- chama comando```
    `gow` ```- nome do xml```
    `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
    `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
    `www.linkdropbox.com` ```- Link do Dropbox```
  
***Criar XML PS3 Instruções:*** 
`comando:`/ps3 -cria xml para loja
    ```
     1 - meu comando sempre começa com /xml
     2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
     3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!
     4 - meu sistema para por jogos de PS3 aceitam apenas 3 links preciso deles como exemplos.``` 
     `Copie de dentro das aspas o caractere invisivel:`"⠀"
    
     **VAMOS AO COMANDO EM SI**
     `Exemplo com caractere invisivel:`
     ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com  www.linkdropbox.com  www.linkdropbox.com```
     `Exemplo sem caractere visivel:`
     ``` /ps3 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com www.linkdropbox.com www.linkdropbox.com```
     **Onde cada campo:**
     `/ps3` ```- chama comando```
     `gow` ```- nome do xml```
     `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
     `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
     `www.linkdropbox.com` ```- Link do Dropbox, preciso de 3 links separados por espaço```
/ps3 -cria xml para loja""",'markdown', reply_markup=keyboard.comandos_usuarios)
            #return True





        #COMANDOS ADMINS------------------->
        elif msg['data'] == 'comandos_admins':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Os comandos aqui listados funcionam apenas para administradores de grupos e o menu Desenvolvedor somente quem hospeda pode usar. ```",'markdown', reply_markup=keyboard.comandos_admins)
            #return True
        elif msg['data'] == 'gerenciar_grupos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""/start - inicia o bot
/welcome -boas vindas
/ban -bane usuario
/unban -desbane usuario
/kick -kicka usuario
/mute -muta usuario
/unmute -desmuta usuario
/unwarn -remove advertencias
/warn -adverte usuario
/pin -fixa posts
/unpin -desfixa posts
/title -muda titulo grupo
/defregras -define regras
/regras -ler regras
/config -privado
/admdebug -debug admin
/id -id usuario
/ip -dados ip
/jsondump -retorna dados 
/stickerid -id sticker
/getsticker -baixa sticker
/criar_sticker -cria pacote stickers
/kibar -copia sticker para o pacote de stickers
/mark -repete o texto markdown
/html -repete o texto HTML
/request -requisição site""", reply_markup=keyboard.comandos_admins)
            #return True
        elif msg['data'] == 'cadastrar_comandos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
💾***CADASTRAR ARQUIVOS LOJAS DOADORES/FREE*** 
```Este bot cadastra as lojas para doadores e free, cadastra também os fix pkg e os fix xml, para atualizar as lojas ou fix pkg e xml basta enviar elas no privado do bot, e ele cadastrará seus arquivos desde que estejam de acordo com as instruções abaixo. Pode ocorrer falhas na hora de cadastrar️, caso não tenha cadastrado envie novamente o arquivo, jamais envie mais de um arquivo por vez.```

🤖***Cadastrar Loja Free:*** `Cadastre a LOJA GRATUITA FREE PKG enviando ela no meu privado com nome terminando com free.pkg, antes disto você pode por qualquer coisa no nome no arquivo como exemplo:` ***TCXS_3.6_free.pkg***

🤖***Cadastrar Loja Doadores:*** `Cadastre a LOJA PARA DOADORES PKG enviando ela no meu privado com nome inicinando com TCXS, após este nome você pode escrever oque quiser no arquivo como  exemplo:` ***TCXS_Store3.9.pkg***

🤖***Cadastrar Fix HAN PKG:*** `Cadastre o FIX HAN PKG enviando ela no meu privado exatamente conforme exemplo:` ***FIX_HAN.pkg***

🤖***Cadastrar Fix HEN PKG:*** `Cadastre o FIX HEN PKG enviando ela no meu privado exatamente conforme exemplo:` ***FIX_HEN.pkg***

🤖***Cadastrar Fix CFW XML:*** `Cadastre o FIX CFW XML enviando ela no meu privado exatamente conforme exemplo:` ***category_network_tool2.xml***

🤖***Cadastrar Fix HEN XML:*** `Cadastre o FIX HEN XML enviando ela no meu privado exatamente conforme exemplo:` ***category_network.xml***


💾***CADASTRO DE COMANDOS E REPOSTAS NA DATABASE***        
🤖`Para cadastrar um comando no banco de dados:`
#comando resposta que o usuário vai receber
🤖`Para recadastrar um comando no banco de dados:`
$comando resposta que o usuário vai receber
🤖`Para deletar um comando`
%comando 

💾***CADASTRO DE PERGUNTA DOS USUARIOS*** 
```Sempre que um usuário enviar alguma pergunta com o ponto de interrogação ela será cadastrada na Database```
🤖`Para ver as perguntas feitas pelo usuario digite:`
perguntas 
🤖`Para limpar as perguntas da Database digite:`
limpar perguntas
`Apaga tudo IA e faz backup da Database (somente adm master)`

💾***EXTRAS***
```Se usar a palavra dropbox como reposta em documentos e imagens eu farei o upload para seu dropbox```
🤖`Pergunte ao bot com o comando:`
fale sobre robôs

💾***SOBRE A FREQUENCIA DE MENSAGENS*** 
```Este bot envia mensagens baseado em uma frequencia que deve ser setada entre 2 e 10, onde:```
🤖`frequencia 0 = mudo`
🤖`frequencia 2 = fala pouco`
🤖`frequencia 10 = fala muito`

💾***SOBRE PROIBIR E PERMITIR PALAVRAS***
```Este bot pode restringir/permitir palavras com os comandos:```
🤖`proibir uma palavra:` proibir 
🤖`permitir uma palavra:` permtir 
🤖`ver palavras proibidas:` proibidas
    """,'markdown', reply_markup=keyboard.comandos_admins)
            #return True
        elif msg['data'] == 'area_dev':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
apagar mensagens - apaga tudo IA e faz backup da Database.
backup - Faz backup do bot.
cmd - Executa um comando.
chat - Obtem infos de um chat.
del - Deleta a mensagem respondida.
doc - Envia um documento do server.
eval - Executa uma função Python.
exec - Executa um código Python.
leave - O bot sai do chat.
plist - Lista os plugins ativos.
promote - Promove alguém a admin.
restart - Reinicia o bot.
upgrade - Atualiza a base do bot.(deprecated)
upload - Envia um arquivo para o servidor.
baixar - baixa um documento para o server
| - Define desligamento do bot, EX: 12|30""",'markdown', reply_markup=keyboard.comandos_admins)
            #return True


        #FERRAMENTAS GERAIS------------------->
        elif msg['data'] == 'ferramentas_gerais':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Informações extras ou complementares sobre o Bot ou Projeto TCXS Store PS3 Hacker Team.```",'markdown', reply_markup=keyboard.ferramentas_gerais)
            #return True
        elif msg['data'] == 'ferramenta_comandos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),"""
/tr      -traduz um texto
/yt      -pesquisa videos no YouTube
/r       -pesquisa um termo no redit
/clima   -exibe informacoes de clima
/coub    -pesquisa de pequenas anima??es
/dados   -jogo de dados
/gif     -gif do giphy
/git     -usuario do github
/id      -id do usuario
/ip      -informa dados de um ip
/jsondump -retorna dados formatados
/stickerid -pega id de um sticker
/getsticker -baixa um sticker
/pypi -pesquisa libs python
/rextester -interpretador de varias linguagens de programação
/mark -repete o texto informado usando Markdown
/html -repete o texto informado usando HTML
/request -faz uma requisicao a um site
/rt -repete concordando com o usuario na reposta  
/fala -Repete o texto que voce pedir para ele falar
/print -gera um print doque falou
/dogbin - envia seu material em texto para o dogbin
/hastebin - envia seu material em texto para o hastebin
/echo - Repete o texto informado.    
/shorten - Encurta uma URL.
/token - Exibe informaces de um token de bot.""", reply_markup=keyboard.ferramentas_gerais)
            #return True


        #INFORMAÇÕES E EXTRAS------------------->
        elif msg['data'] == 'infos_extras':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Confira ferramentas de Machine e Deep Learning em nossa IA (em breve mais comandos).```",'markdown', reply_markup=keyboard.info_extras)
            #return True
        elif msg['data'] == 'info_adquirir':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ A TCXS Project fornece e desenvolve o aplicativo para PlayStation3 TCXS Store, para poder ter nosso aplicativo em seu console basta fazer uma doação nos botões deste site, logo após doar você deve ir em nosso grupo de telegram e procurar por @MsT3Dz ou @Odeiobot e mostrar seu comprovante de doação assim você estará dentro do grupo que contém as novidades, jogos e nossa TCXS Store PKG PlayStation3.```",'markdown', reply_markup=keyboard.info_extras)
            #return True
        elif msg['data'] == 'info_doacao':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"""```------ As doações são feitas pelo mercado pago, onde aceitamos todos os cartões, pagamentos online e boletos.
Não prestamos reembolsos pois se trata de doações e não uma venda direta para uso dos serviços!
O material completo é apenas para doadores. Além do projeto para PlayStation3  a TCXS Project conta com inumeros projetos e Sites para seu entreterimento. Após fazer sua doação basta ir no grupo de TELEGRAM e procurar pelo nosso administrador @MsT3Dz  ou @Odeiobot , enviar um print de seu comprovante de pagamento que ele irá fornecer acesso a todo material, exigimos que seja feito o pedido no grupo! Outros administradores não irão te responder no privado, contamos com seu bom senso e cordialidade! NÃO PRESTAMOS REEMBOLSOS!
Queremos deixar a todos cientes que as doações feitas são exclusivas para pagar os servidores da Dropbox e serviços como hospedagem de site, sendo assim nos adm’s declaramos não receber nenhum valor neste projeto sendo assim nosso trabalho voluntário e todo e qualquer que queira entrar na equipe para ajudar a contribuir de forma expontanêa é bem vindo. Nossa equipe desenvolve sem cobrar nada pela sua mão de obra os sites acima citados bem como o desenvolvimento da TCXS Store PKG e a conversão e upload de jogos dentro dos servidores da Dropbox para assim os fornecer em formato NO-HAN para os usuários, fornecemos dentro da Plataforma PlayStation3 jogos de PS2, PS2, PsP, Emuladores das mais diversas plataformas! Álem disto disponibilizamos aos usuários a experiencia de ter sites para download de jogos nas mais variadas paltaformas e em especial jogos de PS3 PKG tudo aberto gratuitamente a comunidade bem como este site e outros sites mencionados aqui e que encontram-se nos menus.```""",'markdown', reply_markup=keyboard.info_extras)
            #return True
        elif msg['data'] == 'info_requisitos':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"""```------ Para usar a TCXS Store PKG você precisa ter seu console exploitado ou desbloqueado, nossa loja funciona nos consoles CFW, OFW, nas versões HAN e HEN, porém precis atender alguns requisitos para usar a TCXS Store PKG:
- Console Desbloqueado/exploitado.
- Versão exploit Han/Hen.
- Assinaturas previamente inseridas ( Raps’).
- Configurações de internet corretas.
- Espaço para download de jogos em seu hd.
- Conhecer previamente tudo sobre seu sistema de desbloqueio/exploit.
- Saber solucionar seus erros.
- Estar ciente que ao doar para a TCXS Store você não esta fazendo uma compra e sim ajudando a pagar os servidores da Dropbox onde upamos os jogos.CONSIDERE SE PARTICIPANDO DE UMA VAQUINHA COLETIVA ONDE TODOS USUARIOS DA TCXS AJUDAM NESTA VAQUINHA PARA MANTER O SERVIDOR```""",'markdown', reply_markup=keyboard.info_extras)
            #return True
        elif msg['data'] == 'info_suporte':
            await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"""```------ Prestamos suporte somente para nosso aplicativo e jogos, estejam cientes que:
Suporte será prestado somente para a TCXS Store.
Suporte será prestado somente para jogos que são convertidos pela equipe.
Por se tratar de copias modificadas de jogos nossos jogos constantemente são reupados.
Por se tratar de copias modificadas ao cair dos links, os mesmos após conteúdo upado, são substitúidos na TCXS Store PKG.
Tenha ciencia de que links podem vir a cair ( não temos frequencia disto).
Saiba que a administração não presta suporte para seu desbloqueio e exploit, mas aconselhamos levar em um técnico competente caso não saiba realizar as operações básicas e avançadas de seu console.
Caso queira se aventurar em aprender tudo sobre seu desbloqueio ou exploit aconselhamos o fórum da PSX Place que são os desenvolvedores do desbloqueio e exploit, não iremos dar suporte ao material de terceiros ou erros cometidos por usuarios ou consoles vindo de tecnicos que não fizeram um bom exploit ou um bom desbloqueio.```""",'markdown', reply_markup=keyboard.info_extras)
            #return True

        #MODELO PARA NAO TER Q FICAR LIMPANDO CODIGO PARA CRIAR MAIS MENUS--------------->
        #elif msg['data'] == 'infos_extras':
            #await bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),f"```------ Informações extras ou complementares sobre o Bot ou Projeto TCXS Store PS3 Hacker Team.```",'markdown', reply_markup=keyboard.infos_extras)
            #return True

















