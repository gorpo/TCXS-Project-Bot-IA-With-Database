import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin


async def randomicas(msg):
    if msg.get('text'):

        



    

        if msg['text'].split()[0] == 'doadores' or msg['text'].split()[0] == '/doadores':
            await bot.sendMessage(msg['chat']['id'], '`Aqui tem tudo que os doadores precisam saber:` http://tcxsproject.com.br/doadores-tcxs-store-regras/','markdown',reply_to_message_id=msg['message_id'])      
        if msg['text'] == 'corpo' or msg['text'] == 'gorpo':
            await bot.sendMessage(msg['chat']['id'], '`gorpo = corpo`','markdown', reply_to_message_id=msg['message_id'])      
            #video de bluetooth do ted
        if msg['text'] == 'bluetooth':
            await bot.sendMessage(msg['chat']['id'], 'https://www.youtube.com/watch?v=_wYG7iMa5uY', reply_to_message_id=msg['message_id'])      
            #videos dos jogos
        if msg['text'] == 'ps1':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0EUYaz7wACEbVe_lDehK8EitSnLO-jP2SIqZ00PAACsgADGepZRCV_bEET9yWbGgQ',  reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ps2':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0EUYaz7wACEbde_lDfbzhCcTg7M1iPa0_G_rF6UQACsgADGepZRCV_bEET9yWbGgQ',  reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ps3':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0EUYaz7wACEbZe_lDfCr4OQAUoUIpgaTusH4LRnwACswADGepZRHSHRzFv7pF5GgQ', reply_to_message_id=msg['message_id'])
        if msg['text'] == 'exclusivos':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0EUYaz7wACEbhe_lDfqKXeXTKts9b5692tHUMg7gACsAADGepZRO4jb6TTGEoWGgQ', reply_to_message_id=msg['message_id'])
        if msg['text'] == 'emuladores':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CUYaz7wACEbJe_lDe2zzPbEQaW7cmwysAAbjSkPYAAgYBAAKPeSlGO3j50bdxrn8aBA', reply_to_message_id=msg['message_id'])    
        if msg['text'] == 'psp':
            await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CUYaz7wACEbBe_lDeo13PNB4kKRDH4sAFdn8g2AACBwEAAo95KUbzplnZj4OTAAEaBA', reply_to_message_id=msg['message_id'])    

        #----ATT PARA DOADORES TCXS PROJECT---------------------------------------->
        grupo = msg['chat']['title']
        if msg['text'] == 'luppy solta a att3.9' and grupo == 'Doadores TCXS 2020':
            print('Usuario {} solicitou att DE DOADORES'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou att DE DOADORES --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],  msg['chat']['title'], time.ctime())
            arquivo = open('logs/grupos.txt', 'a')
            arquivo.write(log)
            arquivo.close()
            #-------INSTRUÇÕES------>>
            await bot.sendMessage(msg['chat']['id'], 'Olá, bem vindo a TCXS Project ,agora você faz parte dela, entenda que as doações sao mensais e nossa equipe nao ganha nada por este projeto, todo dinheiro arrecadado neste grupo é para pagar os servidores dos quais dispomos jogos. Logo a PSN STUFF IRÁ ACABAR POIS OS SERVIDORES SERÃO DESLIGADOS e assim nao terá mais os jogos gratuitos por ai, restando apenas este acervo que é mantido por voces doadores!     Vamos a Instalação!!!  --> Espero que tenha um pendrive em mãos!  --> copie os arquivos da VERSÃO 3.6 e caso use o fix de acordo com seu Exploit/Desbloqueio, se voce tem han ou CFW use o FIX HAN, caso contrário e seja o Exploit HEN em seu console use o FIX HEN, é necessaria a instalacao deste arquivo para que a loja apareca em seu console! Ative seu HAN/HEN e instale o FIX, após o FIX instalado instale a TCXS Store 3.6 PKG, recomendamos reiniciar o console após este processo!!',  reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'`TUTORIAL DE COMO INSTALAR A LOJA EXPLOIT HAN E HEN!!`  https://cos.tv/videos/play/1586413688272059934', 'markdown',  reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'`COMO USAR A XML CATEGORY_NETWORK!` https://cos.tv/videos/play/1586411677524278797', 'markdown', reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'`Tutorial Download em Segundo Plano` https://cos.tv/videos/play/1586815808334907474', 'markdown', reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'`COMO USAR A XML CATEGORY_NETWORK! CONSOLES CFW ` https://cos.tv/videos/play/1586411677524278797', 'markdown', reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'`PORQUE DEVE USAR PROXY NO PS3!!` https://cos.tv/videos/play/1586410545470952204', 'markdown', reply_to_message_id=msg['message_id'])
            #----LOJA---->
            #loja = old 'BQACAgEAAx0CUYaz7wACEYZe_kwPq97APw9PwRKzTyfLSkkFpgACaAADRIeZRwjQp6a3o_6pGgQ'
            loja = 'BQACAgEAAx0CUYaz7wACFEZfApczkmQTFelb-6C5M1EC43C70QACyQADqcgRRKnKO9HMqEJWGgQ'
            await bot.sendDocument(msg['chat']['id'], document=loja, reply_to_message_id=msg['message_id'])  
            #-----FIX HAN --->
            await bot.sendDocument(msg['chat']['id'],document='BQACAgEAAx0CUYaz7wACEYde_kwP9-8vtzTSJ1IuT4NeFgt-pQACvgADLPo4RYFzaJYmxRZzGgQ', reply_to_message_id=msg['message_id'])
           #----- FIX HEN --->
            await bot.sendDocument(msg['chat']['id'],document='BQACAgEAAx0CUYaz7wACEYhe_k9C8usdKQMOiHhKfUkpEi3eRAACvQADLPo4RftACvMcsCLuGgQ',  reply_to_message_id=msg['message_id'])
            #---XML'S EXCLUSIVOS---->
            await bot.sendMessage(msg['chat']['id'], '`XML exclusivo para quem usa CFW`  ', 'markdown',   reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'],document='BQACAgEAAx0CUYaz7wACDApef8UGQqTwS7Xh3fThcfxWewGafgACtwAD1OsAAURuvfK3r_LK1BgE', reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],'`XML exclusivo para quem usa HEN`  ', 'markdown', reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'],document='BQACAgEAAx0CUYaz7wACDBVef8j2N23B2YiwceDPGNeR2z4Y6gACuAAD1OsAAUQ-0e8Svu_T-RgE',reply_to_message_id=msg['message_id'])
  
            
       
















            # ----------------att gratuita pros pau no cu
        if msg['text'] == 'loja gratis' or msg['text'] == 'free pkg' or msg['text'] == 'Loja gratis' or msg[
            'text'] == 'gratis' or msg['text'] == 'Gratis' or msg['text'] == 'pkg':
            print('Usuario {} solicitou Loja Gratis'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou Loja Gratis --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],
                                                                                             msg['chat']['title'],
                                                                                             time.ctime())
            arquivo = open('logs/grupos.txt', 'a')
            arquivo.write(log)
            arquivo.close()
            await bot.sendMessage(msg['chat']['id'],
                                  'Salve, venho trazer a você nossa nova att GRATUITA, espero que goste!      ----    ----     ----   Caso tenha dificuldades com o download em segundo plano confira este tutorial exclusivo feito para você doador amado que contribui para este projeto se manter em pe: https://youtu.be/_21a5REKhBc',
                                  reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],
                                  'Espero que tenha um pendrive em mãos e saiba usar a loja, não daremos suporte para USUARIOS GRATUITOS, agora  copie os arquivos abaixo para a raiz de um pendrive e coloque na USB direita do seu console, caso use HAN ative o debug ou se usa HEN ative o hen. ESTA ATT NAO USA NENHUM TIPO DE PATCH OU FIX!',
                                  reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'],
                                   document='BQACAgEAAx0CTd0y0QABAfACXkmA716o7XaNW82C3Mr7O2c0bX8AApEAA0oQUUaFcnOHb037rhgE',
                                   reply_to_message_id=msg['message_id'])













            # EHI e o HTTP injector id /jsondump
        if msg['text'] == 'http injector':
            await bot.sendDocument(msg['chat']['id'], document='BQADAQADaAADLwfYRuyWgyR0n8a4FgQ',
                                   reply_to_message_id=msg['message_id'])

        if msg['text'] == 'ehi secreta do behemoth':
            await bot.sendDocument(msg['chat']['id'], document='BQADAQADjAADUmHxR6cWprvULnsfFgQ',
                                   reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'],
                                  '`Nome: TCXS  -  Senha: 1234 - Limite: 100 - Validade: 02/11/2020`', 'markdown',
                                  reply_to_message_id=msg['message_id'])
            await bot.sendAnimation(msg['chat']['id'], animation='CgADAQAD2wEAArGrywvbWKz2FOpQcxYE',
                                    reply_to_message_id=msg['message_id'])

            # exemplo de foto com ID para pegar vai na foto e usa /jsondump
        if 'aham' in msg['text']:
            await bot.sendAnimation(msg['chat']['id'], animation='CgADBAADsgEAAmPDvFLYWdDUh36QARYE',
                                    reply_to_message_id=msg['message_id'])
            # if msg['text'].split()[0] == 'marky':
        #    await bot.sendAnimation(msg['chat']['id'], animation='CgADBAADUQEAAtqMjFDEnwhDdGuoJRYE`', reply_to_message_id=msg['message_id'])
        
            # Exemplo de uma mensagem randomica do bot.....
        
    
        if 'seu cu' in msg['text']:
            print('Usuario {} solicitou seu cu random'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou seu u random --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],
                                                                                              msg['chat']['title'],
                                                                                              time.ctime())
            arquivo = open('logs/grupos.txt', 'a')
            arquivo.write(log)
            arquivo.close()
            cu1 = str('`Pau no seu cu filho da puta!`')
            cu2 = str('`Seu cu o caralho para de fala merda mano!`')
            cu3 = str('`É mais arregaçado que o da minha mão quela vaca vadia galinah piranha!`')
            cu4 = str('`O da sua namorada quela puta rampeira!`')
            cu5 = str('`Ah legal, chegou o mano que só fala bosta no grupo!`')
            cu6 = str('`Seu cu, meu cu, teu cu o cu de todo mundo, foda-se!`')
            cu7 = str('`Eu lambo!`')
            cu8 = str('`Empurro a bosta com o pau!`')
            cu9 = str('`Ta arregaçado!`')
            cu10 = str('`Não tem mais nenhuma prega!`')
            cu11 = str('`Estourei ele!`')
            cu12 = str('`O meu ta suave!`')
            cu13 = str('`Eu o @Gorpo Orko @usergutto @mahayana66 fizemos um estrago!`')
            lista = [cu1, cu2, cu3, cu4, cu5, cu6, cu7, cu8, cu9, cu10, cu11, cu12, cu13]
            escolhido = random.choice(lista)
            await bot.sendMessage(msg['chat']['id'], escolhido, 'markdown', reply_to_message_id=msg['message_id'])
            


        if 'sherry' in msg['text']:
            print('Usuario {} solicitou seu sherry random'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou seu u random --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'], msg['chat']['title'], time.ctime())
            arquivo = open('logs/grupos.txt', 'a')
            arquivo.write(log)
            arquivo.close()
            sherry1 = str('https://i.imgur.com/i8PURpP.jpg')
            sherry2 = str('https://i.imgur.com/lO5r9xj.jpg')
            sherry3 = str('https://i.imgur.com/eoSUKOq.jpg')
            sherry4 = str('https://i.imgur.com/cSimPV4.jpg')
            sherry5 = str('https://i.imgur.com/Sf0FKPD.jpg')
            sherry6 = str('https://i.imgur.com/E9FuuiZ.jpg')
            sherry7 = str('https://i.imgur.com/DKQudSD.jpg')
            sherry8 = str('https://i.imgur.com/SrqbEWJ.jpg')
            sherry9 = str('https://i.imgur.com/zawDBEu.jpg')
            sherry10 = str('https://i.imgur.com/sc3xwaz.jpg')
            sherry11 = str('https://i.imgur.com/xakVPza.jpg')
            sherry12 = str('https://i.imgur.com/6JKY8zl.jpg')
            sherry13 = str('https://i.imgur.com/XN1VAIp.jpg')
            sherry14 = str('https://i.imgur.com/g1Xo6wM.jpg')
            sherry15 = str('https://i.imgur.com/5lVbxmP.jpg')
            lista = [sherry1, sherry2, sherry3, sherry4, sherry5, sherry6, sherry7, sherry8, sherry9, sherry10, sherry11, sherry12, sherry13,sherry14,sherry15]
            escolhido = random.choice(lista)
            await bot.sendMessage(msg['chat']['id'], escolhido, reply_to_message_id=msg['message_id'])
                
        


        if msg['text'].split()[0] == '/comandos@gorpo_bot' or msg['text'] == "/comandos" or msg['text'] == "Comandos" or msg['text'] == "comandos do bot" or msg['text'] == "oque o bot faz" or msg['text'] == "oque teu bot faz" or msg['text'] == "oque este bot faz" or msg['text'] == "Oque teu bot faz":
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

            return True
