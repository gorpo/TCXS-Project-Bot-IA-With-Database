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
#     |        Github Gorpo Dev: https://github.com/gorpo         |
#     [+]   Thanks: https://github.com/AmanoTeam/amanobot       [+]

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, bot_username


async def users(msg):
    if msg.get('text') and msg['chat']['type'] == 'supergroup':
        if msg['from']['first_name']:
            print('->Usuario:{} ->Envio:{} ->Grupo:{} ->Data/Hora:{} '.format(msg['from']['first_name'],msg['text'],msg['chat']['title'],time.ctime()))
            log = '\n->Usuario:{} ->Envio:{} ->Grupo:{} ->Data/Hora:{} '.format(msg['from']['first_name'],msg['text'],msg['chat']['title'],time.ctime())
            #arquivo = open('logs/users.txt','a')
            #arquivo.write(log)
            #arquivo.close()

        if msg['text'].split()[0] == 'logs':
            await bot.sendDocument(msg['chat']['id'], open('logs/users.txt','rb'), reply_to_message_id=msg['message_id'])    
            await bot.sendMessage(msg['chat']['id'], '`{} Esta aqui o log de conversas que tenho armazenado, espero que não tenha nada neste log que te incrimine!`'.format(msg['from']['first_name']),'markdown', reply_to_message_id=msg['message_id'])

        if msg['text'].split()[0] == '/comandos@gorpo_bot' or msg['text'] == "/comandos" or msg['text'].lower() == "comandos" or msg['text'] == "comandos do bot" or msg['text'] == "oque o bot faz" or msg['text'] == "Oque teu bot faz":
            await bot.sendMessage(msg['chat']['id'], """Nem todos os comandos do bot podem funcionar para os usuarios, administradores tem privilegios em cima de alguns comandos: 
    /start - inicia o bot
    /welcome - Define a mensagem de welcome.
    /ban- bane usuario
    /unban - desbane usuario
    /kick -kicka usuario
    /mute - muta usuario
    /unmute - desmuta usuario
    /unwarn - Remove as advert?ncias do usuario.
    /warn - Adverte um usuario.
    /pin - fixa posts
    /unpin - desfixa os posts
    /title - muda o titulo do grupo
    /defregras - define regras
    /regras - ve as regras
    /config - informacoes ser?o enviadas no privado
    /admdebug -  debug do admin
    /tr - Traduz um texto.
    /yt - Pesquisa videos no YouTube.
    /ytdl - Baixa o audio de um video no YouTube.
    /r - pesquisa um termo no redit
    /clima - Exibe informacoes de clima
    /coub - Pesquisa de pequenas anima??es
    /dados - jogo de dados
    /gif - gif do giphy
    /git - usuario do github
    /id - id do usuario
    /ip - informa dados de um ip
    /jsondump - retorna dados formatados
    /stickerid - pega id de um sticker
    /getsticker - baixa um sticker
    /criar_sticker - cria um pacote de stickers
    /kibar  - copia um sticker para o pacote de stickers
    /pypi - pesquisa libs python
    /rextester - interpretador de varias linguagens de programação
    /mark - Repete o texto informado usando Markdown
    /html - Repete o texto informado usando HTML
    /request - Faz uma requisicao a um site
    /ps1 - cria xml para loja
    /ps2 - cria xml para loja 
    /psp - cria xml para loja
    /ps3 - cria xml para loja
    E temos muitos mais comandos de zoeira e informativos ocultos!
    """, reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'], """[*]FERRAMENTAS PARA USUARIOS[*]
    /admin - lista os admins do grupo
    /dogbin - envia seu material em texto para o dogbin
    /hastebin - envia seu material em texto para o hastebin
    /coub - Pesquisa de pequenas anima??es.
    /echo - Repete o texto informado.
    /gif - Pesquisa de GIFs.
    /git - Envia informaces de um user do GitHub.
    /ip - Exibe informaces sobre um IP/dominio.
    /jsondump - Envia o json da mensagem.
    /mark - Repete o texto informado usando Markdown.
    /print - Envia uma print de um site.
    /pypi - Pesquisa de m?dulos no PyPI.
    /r - Pesquisa de topicos no Reddit
    /request - Faz uma requisicao a um site.
    /shorten - Encurta uma URL.
    /token - Exibe informaces de um token de bot.
    /tr - Traduz um texto.
    /yt - Pesquisa v?deos no YouTube.            
    """, reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'], """[+]COMANDOS SEM O BARRA /[+]
    lista jogos - lista com jogos PS3 para download direto
    fix - tras o fix para aparecer a loja do usuario
    free pkg - tras a loja gratuita para o usuario baixar e instalar
    tcxs pyject - programa para criar lojas no pc
    proxy - ajuda o usuario com velocidade no PS3
    torrent - jogos em pkg torrent
    rap - apresenta como usar as licencas
    desbloqueio - ajuda o usuario com erros no desbloqueio
    site - exibe o site da equipe
    facebook - exibe o facebook da equipe, cadastre-se
    iptv - exibe nosso site de iptv gratis
    anime - exibe nosso site de anime gratis
    pkg - exibe nosso site de pkg's para ps3 gratis
    biblioteca - exibe nossa biblioteca hacker
    doadores - exibe instruces completas para doadores
    mercado pago -  link para doar
    doadores - explicaçao sobre como doare porque doar
    tutorial segundo plano -  como usar download em segundo plano
    tutorial - tutorial para instalar a loja
    tcxs - informações sobre nosso nome
    codigo de erro - exibe os codigos de erro da PSN/PS3
    rt - repete concordando com o usuario na reposta  
    fala - Repete o texto que voce pedir para ele falar
    """, reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'], """[*]COMANDOS PARA USUARIOS[*]
    /admins - Mostra a lista de admins do chat.
    /dados - Envia um numero aleatorio de 1 a 6.
    /bug - Reporta um bug ao meu desenvolvedor.
    /id - Exibe suas informaces ou de um usuario.
    /ping - Responde com uma mensagem de ping.
    /regras - Exibe as regras do grupo.
    /roleta - Para jogar a Roleta Russa.
    """, reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'], """[+]COMANDOS DOS ADMINISTRADORES[+]
    /ban - Bane um usuario.
    /config - Envia um menu de configuraces.
    /defregras - Define as regras do grupo.
    /kick - Kicka um inscrito.
    /mute - Restringe um usuario.
    /pin - Fixa uma mensagem no grupo.
    /title - Define o titulo do grupo.
    /unban - Desbane um usuario.
    /unmute - Desrestringe um usucrio.
    /unpin - Desfixa a mensagem fixada no grupo.
    /unwarn - Remove as advert?ncias do usuario.
    /warn - Adverte um usuario.
    /welcome - Define a mensagem de welcome.
    """, reply_to_message_id=msg['message_id'])











  
