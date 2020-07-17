
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from utils import send_to_dogbin, send_to_hastebin

from datetime import date ,datetime, timezone, timedelta
import keyboard

from amanobot.namedtuple import InlineKeyboardMarkup


from config import bot, version, bot_username, git_repo, logs,sudoers
from db_handler import cursor
from get_strings import strings, Strings

async def tcxs(msg):
    if msg.get('text'):

        if msg['text'] == 'tcxs' or msg['text'] == 'tcxs project' or msg['text'] == 'TCXS' or msg['text'] == 'TCXS Project':
            
            await bot.sendMessage(msg['chat']['id'], '`{} O nome TCXS foi criado com base nos botoes do PlayStation3, TRIANGLE - CIRCLE - X - SQUARE, ou seja, triangulo, bolinha, x e quadrado, kkk. Como nosso dev era publicitario e odiava a cena vendo alguns imbecis AUTO PROMOVER seu nome criando lojas e projetos, ele decidiu entrar na cena com uma nomenclatura que lembrasse a cena hacker, ou seja, siglas! Siglas esyão no cotidiano de todo mundo e é facil sua absorção bem como dentro da parte web e publicitaria a sigla tem um forte papel facilitando a digitacao e pesquisa, entao com este intuito nos denominados de TCXS Project, a palavra Project veio da vontade de que nunca morra, sendo assim um projeto qualquer um que tiver habilidade e capacidade pode entrar na equipe e ajudar a coordenar bem como tocar o projeto, ja vimos na cena varios adms passarem pela TCXS, ela e um projeto feito a varias maos e cada um doa de forma gratuita seu tempo e conhecimento para disponibilizar tudo que temos em nossas redes e arquivos. Ficamos gratos a todos que passaram por esta equipe seja dos adms aos users e seria impossivel enumerar todos, voces que sao a TCXS Project e formam este projeto que ja esta indo para seu terceiro ano!  OBRIGADO COMUNIDADE GAMER, HACKER, EXPLOITER, DEVS, USUARIOS E SIMPATIZANTES, SEM VOCES NAO EXISTIRIAMOS!`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
         
        if msg['text'] == 'proxy' or msg['text'] == 'Proxy' :
            await bot.sendMessage(msg['chat']['id'], '{} quer aumentar a velocidade dos downloads no seu PS3? Primeiro quero que saiba que o PS3 é de 2006 e sua placa de rede trabalha com um protocolo bem lento, logo nao adianta vc ter 100mb de net fibra full, pois sua placa de rede nao le neste tempo, bem como a gravaçao no HD do PS3 tambem é lenta, lembre que ele usa HDD e nao SSD assim eu te digo que  NAO ADIANTA TUA NET SER 100MB e de fibra se seu hd antigo e ja capenga grava no maximo a 30mb/s, porem vc sabia que antes de gravar no hd tudo fica na ram e so depois passa para o HD, tendo isto como afirmaçao entenda que o ps3 tem 256mb de ram e mtos slots desta ram estao ocupados, entao nao espere que o PS3 seja uma super maquina de download, ele era do tempo do final da Internet Discada e inicio da internet a Radio e ADLS na epoca da esturura dele em 2006 a maior velocidade de internet vigente como estavel era em torno de 1mb! Tendo isto em mente siga nosso tutorial de proxy para melhorar sua conexao, o serviço proxy é utilizar de outra maquina para que sua conexao esteja com o IP mais proximo do servidor e um cache seja armazenado neste -proxy- fazendo assim seu download melhorar significativamente, segue tutorial: https://youtu.be/l4o8ySk1Do4'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        
        if msg['text'] == 'fix' or msg['text'] == 'Fix':
            await bot.sendMessage(msg['chat']['id'], '`{} vejo que esta precisando do fix para sua loja aparecer, instale este pkg em seu console e a loja começara aparecer.`'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
            await bot.sendDocument(msg['chat']['id'], document='BQACAgEAAx0CWJNTSQACC7FeXTrapHT8zx-Yz6Rm85I7s6BU2gACxQADxKN4RV4960o0M9ruGAQ', reply_to_message_id=msg['message_id']) 
            
       
        if msg['text'] == 'torrent' or msg['text'] == 'Torrent' or msg['text'] == 'torrents' or msg['text'] == 'Torrents':
           
            await bot.sendMessage(msg['chat']['id'], '{} aqui nosso canal de torrents com pkg para download: https://t.me/tcxsp'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        

        if msg['text'] == 'codigo de erro' or msg['text'] == 'lista de erros' or msg['text'] == 'erro psn' or msg['text'] == 'estou com erro' or msg['text'] == 'ta dando erro' or msg['text'] == 'deu erro' or msg['text'] == 'meu videogame ta com problema':
            
            await bot.sendMessage(msg['chat']['id'], '`Querido usúario do sistema PlayStation3 e praticamente impossivel decorar ou trazer a minha base de dados todos os erros, imagina entao se um humano saberia o erro por um codigo, entao vou te fornecer aqui o site oficial da sony e na lista voce podera encontrar seu erro e solucao, caso seu erro persista seu erro esta ocorrendo com o exploit, ai aconselho que voce refaca todo o seu exploit novamente, nao e dificil mas antes veja aqui se seu erro tem solucao:` https://www.playstation.com/pt-pt/get-help/#!/error-code/ ','markdown',reply_to_message_id=msg['message_id'])
        
        if msg['text'] == 'rap' or msg['text'] == 'raps' or msg['text'] == 'licenca' or msg['text'] == '14.000' or msg['text'] == 'assinatura':
            
            await bot.sendMessage(msg['chat']['id'], 'Agora precisamos apenas do PKG das licenças, no HEN as mesmas licenças servem para todos! Tutorial:https://www.youtube.com/watch?v=EYr_MKaL1Tg    Download: https://www.mediafire.com/file/23nzljx8w83dbl0/14Mil-raps-.pkg/file',reply_to_message_id=msg['message_id'])
        

        if msg['text'] == 'desbloqueio' or msg['text'] == 'o meu ps3' or msg['text'] == 'Desbloqueio' or msg['text'] == 'desbloquear o ps3' or msg['text'] == 'desbloquear' or msg['text'] == 'desbloquear meu videogame' or msg['text'] == 'desbloquear o meu ps3' or msg['text'] == 'desbloquear o playstation' or msg['text'] == 'desbloquear o meu console' or msg['text'] == 'desbloqueei meu videogame' or msg['text'] == 'desbloqueei meu console':
            
            await bot.sendMessage(msg['chat']['id'], '`{} Tem certeza que ele foi feito de forma correta? O Joao PSX alem de fornecer arquivos bugados e ate mesmo mostrar bugs de mais ao vivo acaba nao fornecendo um material confiavel bem como ele nao tem total dominio doque faz como podemos ver nos videos a quantidade de erros ( ele podia editar os videos), enfim aconselho que veja, reveja e se possivel faça o exploit em cima deste tutorial:` https://www.youtube.com/watch?v=XUUieW4bv_Y'.format(msg['from']['first_name']),'markdown',reply_to_message_id=msg['message_id'])
        
        if 'mercado pago' in msg['text'] or msg['text'] == 'Mercado Pago' or msg['text'] == 'Mercado pago':
            
            await bot.sendMessage(msg['chat']['id'],  'Olá que bom que você quer doar, {} aqui esta o link de pagamento  ----->   https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=354396246-315fce8c-d8f9-4aa0-8583-95d678936375'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        
        if msg['text'] == 'tutorial segundo plano' or msg['text'] == 'download segundo plano' or msg['text'] == 'downloads em segundo plano' or msg['text'] == 'Tutorial' or msg['text'] == 'Download em segundo plano' or msg['text'] == 'Downloads em segundo plano'or msg['text'] == 'download em segundo plano':
            
            await bot.sendMessage(msg['chat']['id'], '{} O nosso admin @MsT3Dz  criou um tutorial exclusivo de como fazer os downloads na TCXS Project, bem como os downloads em segundo plano. Confira o tutorial completo: https://youtu.be/_21a5REKhBc'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        
        if msg['text'] == 'tutorial' or msg['text'] == 'instalar' or msg['text'] == 'instalar a loja' or msg['text'] == 'instalar  loja' or msg['text'] == 'como instalar a loja' or msg['text'] == 'Como instalar a loja' or msg['text'] == 'Como instalo a loja'or msg['text'] == 'Instalação' or msg['text'] == 'Tutorial de instalação' or msg['text'] == 'Instalação da tcxs' or msg['text'] == 'instalar a tcxs' or msg['text'] == 'Instalação':
            
            await bot.sendMessage(msg['chat']['id'], '{} O nosso admin @MsT3Dz  criou um tutorial exclusivo de como instalar a loja: https://www.youtube.com/watch?v=aG1jLj8QuBY'.format(msg['from']['first_name']),reply_to_message_id=msg['message_id'])
        
#--------------------------------------------------------------------------------------------------




























        strs = Strings(msg['chat']['id'])
        if msg['text'] == 'lista jogos' or msg['text'] == 'lista de jogos' or msg['text'] == 'Lista jogos' or msg['text'] == 'Lista jogos' or msg['text'] == 'Lista de jogos' or msg['text'] == 'PSN' or msg['text'] == 'PSN Stuff' or msg['text'] == 'PSN stuff' or msg['text'] == 'psn' or msg['text'] == 'psn stuff':
            if msg['chat']['type'] == 'private':
                kb = InlineKeyboardMarkup(inline_keyboard=[])
                smsg = strs.get('pm_start_msg')
            else:
                kb = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text=strs.get('🎮 Jogos de A a B'), callback_data='AaB')]+
                    [dict(text=strs.get('🎮 Jogos de B a D'), callback_data='BaD')]+
                    [dict(text=strs.get('🎮 Jogos de E a G'), callback_data='EaG')],
                    [dict(text=strs.get('🎮 Jogos de G a K'), callback_data='GaK')]+
                    [dict(text=strs.get('🎮 Jogos de K a M'), callback_data='KaM')]+
                    [dict(text=strs.get('🎮 Jogos de M a P'), callback_data='MaP')],
                    [dict(text=strs.get('🎮 Jogos de R a S'), callback_data='RaS')]+
                    [dict(text=strs.get('🎮 Jogos de S a T'), callback_data='SaT')]+
                    [dict(text=strs.get('🎮 Jogos de T a Z'), callback_data='TaZ')]
                    
                    
                ])
                smsg = strs.get('''🎮 Temos jogos para download com link direto 🎮
Basta clicar no botão que te trarei a lista com link direto para download, pedimos sua contribuição para que este projeto se mantenha vivo, Obrigado a todos da TCXS!''')
            await bot.sendMessage(msg['chat']['id'], smsg,
                                  reply_to_message_id=msg['message_id'], reply_markup=kb)
            return True






        
#--------------------------------------------------------------------------------

 
            












      

        


























        