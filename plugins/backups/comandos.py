import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

async def comandos(msg):
    if msg.get('text'):
        if '/comandos@gorpo_bot' in msg['text']:
        #if  msg['text'] == "444":
        #if msg['text'].split()[0] == '/comandos@gorpo_bot' or msg['text'] == "comandos":
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
""",reply_to_message_id=msg['message_id'])  

        await bot.sendMessage(msg['chat']['id'], """[*]FERRAMENTAS PARA USUARIOS[*]
/admin - lista os admins do grupo
/dogbin - envia seu material em texto para o dogbin
/hastebin - envia seu material em texto para o hastebin
/coub - Pesquisa de pequenas anima??es.
/echo - Repete o texto informado.
/gif - Pesquisa de GIFs.
/git - Envia informaces de um user do GitHub.
/html - Repete o texto informado usando HTML.
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
/ytdl - Baixa o ?udio de um v?deo no YouTube.            
""",reply_to_message_id=msg['message_id'])  

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
netflix - exibe nosso site de netflix gratis
iptv - exibe nosso site de iptv gratis
anime - exibe nosso site de anime gratis
pkg - exibe nosso site de pkg's para ps3 gratis
biblioteca - exibe nossa biblioteca hacker
curso - exibe nosso site de  cursos
doadores - exibe instruces completas para doadores
mercado pago -  link para doar
doadores - explicaçao sobre como doare porque doar
tutorial segundo plano -  como usar download em segundo plano
tutorial - tutorial para instalar a loja
painel - exibe nosso painel hacker
tcxs - informações sobre nosso nome
codigo de erro - exibe os codigos de erro da PSN/PS3
filho da puta - se usado como resposta bot media uma treta
pau no cu - se usado como resposta bot media uma treta
gay - se usado como resposta bot media uma treta
rt - repete concordando com o usuario na reposta  
fala - Repete o texto que voce pedir para ele falar
""",reply_to_message_id=msg['message_id'])  

        await bot.sendMessage(msg['chat']['id'], """[*]COMANDOS PARA USUARIOS[*]
/admins - Mostra a lista de admins do chat.
/dados - Envia um numero aleatorio de 1 a 6.
/bug - Reporta um bug ao meu desenvolvedor.
/id - Exibe suas informaces ou de um usuario.
/ping - Responde com uma mensagem de ping.
/regras - Exibe as regras do grupo.
/roleta - Para jogar a Roleta Russa.
""",reply_to_message_id=msg['message_id'])  

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
""",reply_to_message_id=msg['message_id'])  


        await bot.sendMessage(msg['chat']['id'], """[+]COMANDOS TROLLAGENS[+]
lolo - receita de original de lolo
ola -  ele da um salve
birl - video de como vc fica macho
amigo - video de nossa realidade
msgames - audio lendario da melhor equipe de PS3
o.O ou O.o ou o.o - vai te xingar
mit - chama o nosso chefe masculo
tchau - ele da tchau pra vc
brick - ele mostra um video de PS3 brickado
gato - exibe foto de gatos
maconha - fala sobre a erva
http injector - versao do http mais antiga/estavel
morre - envia oque ele deseja na sua morte
aham - ele concorda com voce via gif
tapa - 
""",reply_to_message_id=msg['message_id'])  

        await bot.sendMessage(msg['chat']['id'], """[*] COMANDOS ACEITOS APENAS PELO GORPO [*]
sudos - exibe esta lista separada.
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
| - Define desligamento do bot, EX: 12|30
""",reply_to_message_id=msg['message_id'])  

















    
