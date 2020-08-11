import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin

async def trollagens(msg):
    if msg.get('text'):


  

        if 'hack' in msg['text']:
            await bot.sendDocument(msg['chat']['id'], document='CAACAgQAAx0CViT8vwABA68xXl1f1utQEG7Xatfq7iYVa8Rwe8sAAmIJAAJ0TWAPg3dbTwnI2JsYBA', reply_to_message_id=msg['message_id'])
            await bot.sendMessage(msg['chat']['id'], '`{} hacker o caralho, esta merda nao tem hacker nenhum, vcs sao tudo lammer e noob!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])     
        if msg['text'] == 'chartubate':
            await bot.sendMessage(msg['chat']['id'], 'ai noob ja conferiu o chartubate da nossa musa Sherry -->> https://m.chaturbate.com/sherryshen/'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
                  

        if msg['text'] == 'vanessinha':
            await bot.sendMessage(msg['chat']['id'], '`vanessinha tira o gutto do serio {} `'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
            await bot.sendPhoto(msg['chat']['id'], photo='AgADAQADQ6gxG-BOyER2xRrlf-rZJIfSbgYABAEAAwIAA3gAA8puAAIWBA', reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'], document='CQADAQAD_wADqlsJRUl_c63JowABaxYE', reply_to_message_id=msg['message_id']) 
            await bot.sendPhoto(msg['chat']['id'], photo='AgACAgEAAx0CViT8vwABAzm7XjJOmX6bpde3AAFeFwlmMaoRX0RJAAJXqDEbRcuARW6HPRy_x1LI4eprBgAEAQADAgADeAADgkoCAAEYBA', reply_to_message_id=msg['message_id'])
      
        
        if msg['text'] == 'birl' or msg['text'] == 'birll' or msg['text'] == 'bril' or msg['text'] == 'birlll' or msg['text'] == 'birllll' or msg['text'] == 'brill' or msg['text'] == 'bam' or msg['text'] == 'comi pra caralho':
        	await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CViT8vwABAznMXjJQMaQ5gn0oshTJ-aR4hsOxqpQAAmQAA4GqMEULivNNxE7fYhgE', reply_to_message_id=msg['message_id']) 
        
        if msg['text'] == 'amigo' or msg['text'] == 'amigos' or msg['text'] == 'so eu e meu pc' or msg['text'] == 'coddando'  or msg['text'] == 'sem visita' or msg['text'] == 'visita':
        	await bot.sendVideo(msg['chat']['id'], video='BAACAgEAAx0CViT8vwABAznPXjJQ1ZuyAWK6p3j_PB9Sa1LjlIEAAmUAA8xjqUenWqNRGjMDNBgE', reply_to_message_id=msg['message_id']) 
       
        if msg['text'] == 'msgames' or msg['text'] == 'ms games' or msg['text'] == 'Msgames':
        	await bot.sendAudio(msg['chat']['id'], audio='CQACAgEAAx0CViT8vwABAznUXjJRtlW9MtdYUpwNdWPp57PuoqIAAq0AAwNa6UXaOuGG73s6lhgE', reply_to_message_id=msg['message_id']) 
                    
        #com este comando e a id do grupo geral consigo enviar uma mensagem exclusivamente la             
        #if msg['from']['first_name']:
         #   await bot.sendMessage(-1001306342097, '`{} deu nada não feio. `'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        


         #tcxs pyject store creator
        if msg['text'] == 'tcxs pyject' or msg['text'] == 'pyject' or msg['text'] == 'Tcxs pyject' or msg['text'] == 'TCXS Pyject' or msg['text'] == 'Pyject' or msg['text'] == 'Criador de loja' or msg['text'] == 'criador de loja' or msg['text'] == 'programa que cria loja' or msg['text'] == 'cria loja':
            await bot.sendMessage(msg['chat']['id'], 'Salve {}  O @GorpoOrko criou um programa que cria lojas em PKG e tambem cria a loja diretamente no PlayStation3, o programa é super facil de usar!  Caso tenha alguma duvida o @GorpoOrko irá atender a pedidos,perguntas e respostas somente via comentarios no github, siga o @GorpoOrko no Github e fique por dentro dos maiores hacks e programas mais atuais para seu console!  Você pode baixar a souce neste link: https://github.com/gorpo/TCXS_Pyject_PlayStation3_Store_Creator e o tutorial de uso do programa neste link: https://www.youtube.com/watch?v=EQbymbu5htA'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
            



        if msg['text'] == 'qq deu':
            await bot.sendMessage(msg['chat']['id'], '`{} deu nada não feio. `'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'grosso':
            await bot.sendMessage(msg['chat']['id'], '`Grosso meu pau {} seu arrombado!`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'corno':
            await bot.sendMessage(msg['chat']['id'], '`{} corno é teu pai, aquele filho da puta.`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'deixa de ser gado':
            await bot.sendMessage(msg['chat']['id'], '`caralho, {} o cara é gado D+`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ff':
            await bot.sendMessage(msg['chat']['id'], '`{} jogo de corno não né!`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'filho da puta':
            await bot.sendMessage(msg['chat']['id'], '`{} filho da puta teu cu cara, olha como vc fala cmg seu bosta`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ta tarde':
            await bot.sendMessage(msg['chat']['id'], '`{} vai dormir...`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'grupo ta vazio':
            await bot.sendMessage(msg['chat']['id'], '`{} grupo ta morto`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'rip gp':
            await bot.sendMessage(msg['chat']['id'], '`RIP All`','markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'grupo ta parado':
            await bot.sendMessage(msg['chat']['id'], '`grupo ta morto`','markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'tlg':
            await bot.sendMessage(msg['chat']['id'], '`{}, To ligado feio`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if 'kkkk' in msg['text']:
            await bot.sendMessage(msg['chat']['id'], '`{}, kkkkkkjjj`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'cocaina':
            await bot.sendMessage(msg['chat']['id'], '`Tão cherando pó agora seus filho da puta?`','markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'rip grupo':
            await bot.sendMessage(msg['chat']['id'], '`Ta parado mesmo... {}`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if msg['text'] == 'ola':
            await bot.sendMessage(msg['chat']['id'], '`Olá {} como vai vc?`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        if 'aew' in msg['text']:
            await bot.sendMessage(msg['chat']['id'], '`Aewwwwwwwwwwwwwwwwwwwww {} caralho, filho da puta, so dale, vamooooo!!!`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        

#---------------ESTE CODIGO FAZ QUE QUANDO RESPONDIDO ALGO ELE MANDE TOMA NO CU
        #if msg.get('reply_to_message'):
        #    await bot.sendMessage(msg['chat']['id'], '''Toma no cu {} '''.format(msg['from']['first_name']),parse_mode='HTML',reply_to_message_id=msg['message_id'])
       


#------------------ESTE CODIGO FAZ COM QUE O NOME DO USUARIO (pegar com id é apenas o primeiro nome) SEMPRE QUE ELE FALAR ALGO O BOT DIGA OQUE TA NA FRASE OU COMETA OUTRA AÇAO 
        #if msg['from']['first_name'] == '':
        #    await bot.sendMessage(msg['chat']['id'], '`Aewwwwwwwwwwwwwwwwwwwww caralho, filho da puta, so dale, vamooooo!!!`','markdown',reply_to_message_id=msg['message_id'])
        

            


















        if msg['text'] == 'lolo':
            await bot.sendMessage(msg['chat']['id'], '''```{} RECEITA DO LÓLÓ ORIGINAL (repasse)

O intuito desse texto é viralizar e, por sorte, melhorar a  qualidade do lóló encontrado no carnaval do Brasil. Com os anos, os lolozeiros têm depreciado a veracidade do no nosso amado lóló e nos fornecido um produto de qualidade inferior, que nem é digno de receber o título. 

Então vamos lá: 

100ml de Cloroformio 
50ml de Éter ou acetato de etila 
50ml de Acetona ou álcool
(proporção 2:1:1)

Pra quem gosta de enfeitar, curte elevar a qualidade e melhorar o sabor: 5-10ml de essência de menta, baunilha ou tutti-fruti.

PS: Tanto tricoletileno quanto cola acrílica não é lóló e têm maiores chances de causar náuseas, dor de cabeça e ressaca. 

Lembrete: todos os itens descritos acima você encontra na PANVEL. Com excessão da essência, que você pode encontrar nos maiores supermercados. 

Bom carnaval! ```'''.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
         


        elif msg['text'].split()[0] == 'mahay':
            await bot.sendMessage(msg['chat']['id'], '`{}, Esse aí é corno`'.format(msg['from']['first_name']),'markdown',
                                                    reply_to_message_id=msg['message_id'])
        elif msg['text'].split()[0] == '@mahayana66':
            await bot.sendMessage(msg['chat']['id'], '`{} Não marca este filho da puta por favor cara, ja to com raiva dele nmrl!`'.format(msg['from']['first_name']),'markdown',
                                                    reply_to_message_id=msg['message_id'])
        elif msg['text'].split()[0] == '❤️':
            await bot.sendMessage(msg['chat']['id'], '`{} ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️`'.format(msg['from']['first_name']),'markdown',
                                                    reply_to_message_id=msg['message_id'])  
        elif msg['text'].split()[0] == '<3':
            await bot.sendMessage(msg['chat']['id'], '`❤️`','markdown',
                                                    reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == ':/':
            await bot.sendMessage(msg['chat']['id'], '`{} ta inconformado mano?`'.format(msg['from']['first_name']),'markdown',
                                                    reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'o.o':
            await bot.sendMessage(msg['chat']['id'], '`{} tambem fico espantado as vezes...`'.format(msg['from']['first_name']),'markdown',
                                                    reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'o.O':
            await bot.sendMessage(msg['chat']['id'], '`o.O`','markdown',
                                                    reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'O.o':
            await bot.sendMessage(msg['chat']['id'], '`{} sou doidinho pra te estupra e comer teu cuzinho  ❤️`'.format(msg['from']['first_name']),'markdown',
                                                   reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == ':3':
            await bot.sendMessage(msg['chat']['id'], '`:3 `','markdown',
                                                  reply_to_message_id=msg['message_id'])
        elif msg['text'].split()[0] == 'stives':
            await bot.sendMessage(msg['chat']['id'], '`🔪Amigo de ownador de cc dono do Knight chan quele corno ja tem os dois pes no infeno`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'estives':
            await bot.sendMessage(msg['chat']['id'], '`🔪Amigo de ownador de cc dono do Knight chan quele corno ja tem os dois pes no infeno, queria ressaltar que ele é um filho da puta e nao serve para muita coisa no mundo de hoje`','markdown',
                                                  reply_to_message_id=msg['message_id'])  
        elif msg['text'].split()[0] == '@alsnav':
            await bot.sendMessage(msg['chat']['id'], '`🔪`','markdown',
                                                  reply_to_message_id=msg['message_id'])      
        elif msg['text'].split()[0] == '@chata_pra_crlh':
            await bot.sendMessage(msg['chat']['id'], '`{} ela é um amor né? ❤️`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'mit':
            await bot.sendMessage(msg['chat']['id'], '`Vem que teus macho tao te chamando, o {} quer tua raba`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '@Odeiobot':
            await bot.sendMessage(msg['chat']['id'], '`Não marca ele, senao ele vem de viadagem {}}.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        #elif msg['text'].split()[0] == 'dog':
        #    await bot.sendMessage(msg['chat']['id'], '`Dogueeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee`','markdown',
        #                                          reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'krl':
            await bot.sendMessage(msg['chat']['id'], '`Caralho irmao, do krl ne {}!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'pro':
            await bot.sendMessage(msg['chat']['id'], '{} `pro krl nmrl seu pau no cu`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'feio':
            await bot.sendMessage(msg['chat']['id'], '`fei do cel, {}  nmrl vc é fei dms`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'entende':
            await bot.sendMessage(msg['chat']['id'], '`{}, entende oque cara, se liga o pau no cu, vc nao entende porra nenhuma e vem caga tuas teoria imbecil aqui...`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '@usergutto':
            await bot.sendMessage(msg['chat']['id'], '`Deve ta no xone quele bosta`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'guto':
            await bot.sendMessage(msg['chat']['id'], '`Este ano ele vai adotar o caramelo!`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'usergutto':
            await bot.sendMessage(msg['chat']['id'], '`Gurizao gente boa até cara pena que usa avg, opera e ainda usa vga.`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'gutto':
            await bot.sendMessage(msg['chat']['id'], '`Gutto é tarado pela vanessinha, mas lance dele ate hoje é querer volta pra ex.`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '@Perplex_User':
            await bot.sendMessage(msg['chat']['id'], '`{} este gurizao ta em tudo que é grupo que a galera ta, onde vc vai ele esta.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])
        elif msg['text'].split()[0] == 'perplex':
            await bot.sendMessage(msg['chat']['id'], '`ta so de olho no grupo do estives pra poder pega cc do jesse...`','markdown',
                                                  reply_to_message_id=msg['message_id'])
        elif msg['text'].split()[0] == 'gutto':
            await bot.sendMessage(msg['chat']['id'], '`Gutto é tarado pela vanessinha, mas lance dele ate hoje é querer volta pra ex.`','markdown',
                                                  reply_to_message_id=msg['message_id'])     
        elif msg['text'].split()[0] == '@cjbugado':
            await bot.sendMessage(msg['chat']['id'], '`{} so de marcar ele meu sistema chega bugar aqui`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'cyber':
            await bot.sendMessage(msg['chat']['id'], '`{} cyber é noob de mais mano`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'denki':
            await bot.sendMessage(msg['chat']['id'], '`denki é noob`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'gorpo':
            await bot.sendMessage(msg['chat']['id'], '`gorpo = corpo`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '@GorpoOrko':
            await bot.sendMessage(msg['chat']['id'], '`Pro caralho {}, não incomoda meu mestre seu filho da puta! @GorpoOrko vem ver oque este pau no cu quer depois...`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'corpo':
            await bot.sendMessage(msg['chat']['id'], '`gorpo = corpo`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'skiddie':
            await bot.sendMessage(msg['chat']['id'], '`{} skiddie é vc o seu filho da puta!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'lammer':
            await bot.sendMessage(msg['chat']['id'], '`lammer é você o {} pau no cu`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'estuda':
            await bot.sendMessage(msg['chat']['id'], '`{}, isto sai daqui e vai estuda o filho da puta!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'vendo':
            await bot.sendMessage(msg['chat']['id'], '`{} ve meu pau aqui otario!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'rir':
            await bot.sendMessage(msg['chat']['id'], '`{} enfia uma dentadura no cu e vai rir pro caralho!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'entende':
            await bot.sendMessage(msg['chat']['id'], '`{} nem você se entende cara!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'zmod':
            await bot.sendMessage(msg['chat']['id'], '`zmod devia ser zgod o cara é mito demais, cria bug pra lancar fix que contem um bug!`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'lauro':
            await bot.sendMessage(msg['chat']['id'], '`{} não fala o nome deste filho da puta neste grupo!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'cabjones':
            await bot.sendMessage(msg['chat']['id'], '`morreu`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'brwar':
            await bot.sendMessage(msg['chat']['id'], '`❤️ gordinho camarada da porra`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '@628578091':
            await bot.sendMessage(msg['chat']['id'], '`Mostra teta ai cara!`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'site' or msg['text'].split()[0] == '/site':
            await bot.sendMessage(msg['chat']['id'], '`{} Passa la e da um confere nos posts e nos hacks!` http://tcxsproject.com.br'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'facebook' or msg['text'].split()[0] == 'face' or msg['text'].split()[0] == '/facebook' :
            await bot.sendMessage(msg['chat']['id'], '`{} eu sou um bot tão foda q tenho meu proprio facebook, mas dei o nome dele de manicomio, entra la e veja as bizarrice e poste algumas tambem,` http://tcxsproject.com.br/facebook/'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'netflix' or msg['text'].split()[0] == '/netflix':
            await bot.sendMessage(msg['chat']['id'], '`{} Netflix o caralho eu tenho minha propria netflix chamo ela de ManicomioFlix, entra la e confere, cria uma conta é gratis!` http://tcxsproject.com.br/flix/'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'iptv' or msg['text'].split()[0] == '/iptv':
            await bot.sendMessage(msg['chat']['id'], '`{} Tenho um sitezinho de IPTV que estava criando talvez um dia volte alimentar ele, confere la:` http://tcxsproject.com.br/iptv'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'anime' or msg['text'].split()[0] == '/anime':
            await bot.sendMessage(msg['chat']['id'], '`{} Tenho um site de anime, ainda mais com umas bizarrice da um confere la:` http://tcxsproject.com.br/anime'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'pkg' or msg['text'].split()[0] == '/pkg':
            await bot.sendMessage(msg['chat']['id'], '`❤Tenho um site de jogos em PKG para PS3 totalmente gratis, confere meus posts la:` http://tcxsproject.com.br/category/nohan/','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'doadores' or msg['text'].split()[0] == '/doadores':
            await bot.sendMessage(msg['chat']['id'], '`Aqui tem tudo que os doadores precisam saber:` http://tcxsproject.com.br/doadores-tcxs-store-regras/','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'curso' or msg['text'].split()[0] == '/curso':
            await bot.sendMessage(msg['chat']['id'], '`{} Já conferiu os cursos hacker que disponibilizo em meu site, confere la:` http://tcxsproject.com.br/shop/'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'cursos' or msg['text'].split()[0] == '/cursos':
            await bot.sendMessage(msg['chat']['id'], '`Já conferiu os cursos hacker que disponibilizo em meu site, confere la` http://tcxsproject.com.br/shop/','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'biblioteca' or msg['text'].split()[0] == '/biblioteca':
            await bot.sendMessage(msg['chat']['id'], '`Eu tenho uma biblioteca hacker cheinha de livros hacker bem como alguns livros sobre ghoetia, satanismo e anarquia, confere la:` http://tcxsproject.com.br/dev','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'xiu':
            await bot.sendMessage(msg['chat']['id'], '`{} isto, cala boca seu bosta`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'vsf':
            await bot.sendMessage(msg['chat']['id'], '`{} vai vc otario, so fala bosta mano.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'oi':
            await bot.sendMessage(msg['chat']['id'], '`oi {}`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'tchau':
            await bot.sendMessage(msg['chat']['id'], '`tchau {}`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'xau':
            await bot.sendMessage(msg['chat']['id'], '`xau`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'boa':
            await bot.sendMessage(msg['chat']['id'], '`boa teu cu`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'bom':
            await bot.sendMessage(msg['chat']['id'], '`{} queria saber como vcs conseguem acordar com disposicão neste mundo dos diabo.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == '.':
            await bot.sendMessage(msg['chat']['id'], '`.`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'kkk':
            await bot.sendMessage(msg['chat']['id'], '`kkjjjj  {} kkjjj q engracado kkjjj`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'kk':
            await bot.sendMessage(msg['chat']['id'], '`{} kkkkk kkkk kkk mds kkkk gracado dms vc, vai trampa na praca`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'xvideos':
            await bot.sendMessage(msg['chat']['id'], '`{} ja conferiu o feed da bronha hoje? xvideos ta cheio de gostosa.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif 'shema' in msg['text']:
            await bot.sendMessage(msg['chat']['id'], '`{} bom de mais comer um travequinho ne?`'.format(msg['from']['first_name']),'markdown', reply_to_message_id=msg['message_id'])  
            await bot.sendDocument(msg['chat']['id'], document='CgACAgQAAx0CViT8vwABA6-3Xl1vBd53xqknuyULa2YPoYB3w24AAmgJAAIz6iBR5pLYRkLVaC4YBA', reply_to_message_id=msg['message_id'])
                                                    
        elif msg['text'].split()[0] == 'traveco':
            await bot.sendMessage(msg['chat']['id'], '`{} orgia de traveco melhor coisa que ja fiz na vida!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])  
            await bot.sendDocument(msg['chat']['id'], document='CgACAgQAAx0CViT8vwABA6-3Xl1vBd53xqknuyULa2YPoYB3w24AAmgJAAIz6iBR5pLYRkLVaC4YBA', reply_to_message_id=msg['message_id'])
                                                    
        elif msg['text'].split()[0] == 'tmj':
            await bot.sendMessage(msg['chat']['id'], '`{}, tmj o caralho.`'.format(msg['from']['first_name']),'markdown', 
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'pod':
            await bot.sendMessage(msg['chat']['id'], '`{}, pod c o caralho.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id']) 
          
        elif msg['text'].split()[0] == 'carder':
            await bot.sendMessage(msg['chat']['id'], '`{} acho que o melhor carder da cena, Jesse Pinkman foi preso, sumiu dos grupos.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])     
        elif msg['text'].split()[0] == 'cadder':
            await bot.sendMessage(msg['chat']['id'], '`{} acho que o melhor carder da cena, Jesse Pinkman foi preso, sumiu dos grupos.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])     
        elif msg['text'].split()[0] == 'cc':
            await bot.sendMessage(msg['chat']['id'], '`{} to so vendo esta galera nos grupo de telegram ownado as cc tudo por ai.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'brick':
            await bot.sendMessage(msg['chat']['id'], 'https://www.youtube.com/watch?v=AaQJ23Hosc8','markdown',
                                                  reply_to_message_id=msg['message_id'])     
        elif msg['text'].split()[0] == 'da':
            await bot.sendMessage(msg['chat']['id'], '`{} da nada não pjl pra nois meu cupinxa.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])     
        elif msg['text'].split()[0] == 'carder':
            await bot.sendMessage(msg['chat']['id'], '`{} acho que o melhor carder da cena, Jesse Pinkman foi preso, sumiu dos grupos.`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id'])     
        
        elif msg['text'].split()[0] == 'cadder':
            await bot.sendMessage(msg['chat']['id'], '`acho que o melhor carder da cena, Jesse Pinkman foi preso, sumiu dos grupos.`','markdown',
                                                  reply_to_message_id=msg['message_id'])    
        elif msg['text'].split()[0] == 'punheta':
            await bot.sendMessage(msg['chat']['id'], '`{} a forma certa de bater uma é subindo e descendo a mao no pau nao enfiando coisas no cu!`'.format(msg['from']['first_name']),'markdown',
                                                  reply_to_message_id=msg['message_id']) 
        























            return True
