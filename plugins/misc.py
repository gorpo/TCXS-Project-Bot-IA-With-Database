

import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin


async def misc(msg):
    if msg.get('text'):
#aqui ele repete as coisas com echo kkjjj
        if msg['text'].startswith('fala') or msg['text'].startswith('/echo')or msg['text'].startswith('echo') or msg['text'] == '/echo@' + bot_username:
            print('Usuario {} solicitou echo'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou echo  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg.get('reply_to_message'):
                reply_id = msg['reply_to_message']['message_id']
            else:
                reply_id = None
            await bot.sendMessage(msg['chat']['id'],'{} pra caralho'.format(msg['text'][5:]),
                                  reply_to_message_id=reply_id)
            return True
        #owna nasa ele responde nasa pra caralho kkjj
        elif msg['text'].startswith('owna'):
            print('Usuario {} solicitou owna'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou owna  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg.get('reply_to_message'):
                reply_id = msg['reply_to_message']['message_id']
            else:
                reply_id = None
            await bot.sendMessage(msg['chat']['id'],'{} pra caralho esta porra filho da puta!'.format(msg['text'][5:]),
                                  reply_to_message_id=reply_id)
            return True
        #sla mano
        elif msg['text'].startswith('sla') :
            if msg.get('reply_to_message'):
                reply_id = msg['reply_to_message']['message_id']
            else:
                reply_id = None
            await bot.sendMessage(msg['chat']['id'],'{} ta foda este lance.'.format(msg['text'][4:]),
                                  reply_to_message_id=reply_id)
            return True
            
            
        elif msg['text'].startswith('/mark') or msg['text'].startswith('!mark') or msg['text'] == '/mark@' + bot_username:
            print('Usuario {} solicitou /mark'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /,ark  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg.get('reply_to_message'):
                reply_id = msg['reply_to_message']['message_id']
            else:
                reply_id = None
            await bot.sendMessage(msg['chat']['id'], msg['text'][6:], 'markdown',
                                  reply_to_message_id=reply_id)
            return True


        elif msg['text'] == '/admins' or msg['text'] == '/admin' or msg['text'] == 'admin' or msg['text'] == '/admin@' + bot_username:
            print('Usuario {} solicitou /admins'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /admin  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg['chat']['type'] == 'private':
                await bot.sendMessage(msg['chat']['id'], 'Este comando s? funciona em grupos ?\\_(?)_/?')
            else:
                adms = await bot.getChatAdministrators(msg['chat']['id'])
                names = 'Admins:\n\n'
                for num, user in enumerate(adms):
                    names += '{} - <a href="tg://user?id={}">{}</a>\n'.format(num + 1, user['user']['id'],
                                                                              html.escape(user['user']['first_name']))
                await bot.sendMessage(msg['chat']['id'], names, 'html',
                                      reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].startswith('/token') or msg['text'].startswith('!token') or msg['text'] == '/token@' + bot_username:
            print('Usuario {} solicitou /token'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /token  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            text = msg['text'][7:]
            try:
                bot_token = amanobot.Bot(text).getMe()
                bot_name = bot_token['first_name']
                bot_user = bot_token['username']
                bot_id = bot_token['id']
                await bot.sendMessage(msg['chat']['id'], f'''informacoes do bot:
Nome: {bot_name}
Username: @{bot_user}
ID: {bot_id}''',
                                      reply_to_message_id=msg['message_id'])

            except TelegramError:
                await bot.sendMessage(msg['chat']['id'], 'Token invalido.',
                                      reply_to_message_id=msg['message_id'])
            return True

        elif msg['text'].startswith('/bug') or msg['text'].startswith('!bug') or msg['text'] == '/bug@' + bot_username:
            print('Usuario {} solicitou /bug'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /bug  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            text = msg['text'][5:]
            if text == '' or text == bot_username:
                await bot.sendMessage(msg['chat']['id'], '''*Uso:* `/bug <descrição do bug>` - _Reporta erro/bug para a equipe de desenvolvimento deste bot, so devem ser reportados bugs sobre este bot!_
  obs.: Mal uso há possibilidade de ID\_ban''', 'markdown',
                                      reply_to_message_id=msg['message_id'])
            else:
                await bot.sendMessage(758600965, f"""<a href="tg://user?id={msg['from']['id']}">{msg['from'][
                    'first_name']}</a> reportou um bug:

                     ID: <code>{msg['from']['id']}</code>
                     Mensagem: {text}""", 'HTML')
                

                await bot.sendMessage(msg['chat']['id'], 'O bug foi reportado com sucesso para a minha equipe!',
                                      reply_to_message_id=msg['message_id'])

            return True

        elif msg['text'].startswith('/dogbin') or msg['text'].startswith('!dogbin') or msg['text'] == '/dogbin@' + bot_username or msg['text'] == 'dogbin':
            print('Usuario {} solicitou /dogbin'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /dogbin  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            text = msg['text'][8:] or msg.get('reply_to_message', {}).get('text')
            if not text:
                await bot.sendMessage(msg['chat']['id'],
                                      '''*Uso:* `/dogbin <texto>` - _envia um texto para o del.dog._''',
                                      'markdown',
                                      reply_to_message_id=msg['message_id'])
            else:
                link = await send_to_dogbin(text)
                await bot.sendMessage(msg['chat']['id'], link, disable_web_page_preview=True,
                                      reply_to_message_id=msg['message_id'])
            return True

        elif msg['text'].startswith('/hastebin') or msg['text'].startswith('!hastebin') or msg['text'] == '/hastebin@' + bot_username or msg['text'] == 'hastebin' or msg['text'] == 'pastebin':
                print('Usuario {} solicitou /hastebin'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /hastebin  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                text = msg['text'][9:] or msg.get('reply_to_message', {}).get('text')
                if not text:
                    await bot.sendMessage(msg['chat']['id'],
                                          '''*Uso:* `/hastebin <texto>` - _envia um texto para o hastebin._''',
                                          'markdown',
                                          reply_to_message_id=msg['message_id'])
                else:
                    link = await send_to_hastebin(text)
                    await bot.sendMessage(msg['chat']['id'], link, disable_web_page_preview=True,
                                          reply_to_message_id=msg['message_id'])
                return True

        elif msg['text'].startswith('/html') or msg['text'].startswith('!html') or msg['text'] == '/html@' + bot_username or msg['text'] == 'html':
            print('Usuario {} solicitou /html'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou /html  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg.get('reply_to_message'):
                reply_id = msg['reply_to_message']['message_id']
            else:
                reply_id = None
            await bot.sendMessage(msg['chat']['id'], msg['text'][6:], 'html',
                                  reply_to_message_id=reply_id)
            return True


        elif msg['text'] == 'ban' or msg['text'] == '/ban' or msg['text'] == '/gorpo@' + bot_username:
            print('Usuario {} solicitou ban'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou ban  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            try:
                await bot.unbanChatMember(msg['chat']['id'], msg['from']['id'])
            except TelegramError:
                await bot.sendMessage(msg['chat']['id'],
                                      'Nao deu pra te remover, voce.... deve ser um admin ou eu nao sou admin nesta bosta.',
                                      reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'].startswith('/request') or msg['text'].startswith('!request') or msg['text'] == '/request@' + bot_username or msg['text'] == 'request':
            if re.match(r'^(https?)://', msg['text'][9:]):
                text = msg['text'][9:]
            else:
                text = 'http://' + msg['text'][9:]
            try:
                async with aiohttp.ClientSession() as session:
                    r = await session.get(text)
            except Exception as e:
                return await bot.sendMessage(msg['chat']['id'], str(e),
                                             reply_to_message_id=msg['message_id'])
            headers = '<b>Status-Code:</b> <code>{}</code>\n'.format(str(r.status))
            headers += '\n'.join('<b>{}:</b> <code>{}</code>'.format(x, html.escape(r.headers[x])) for x in r.headers)
            rtext = await r.text()
            if len(rtext) > 3000:
                content = await r.read()
                res = await send_to_dogbin(content)
            else:
                res = '<code>' + html.escape(rtext) + '</code>'
            await bot.sendMessage(msg['chat']['id'], '<b>Headers:</b>\n{}\n\n<b>Conteudo:</b>\n{}'.format(headers, res),
                                  'html', reply_to_message_id=msg['message_id'])
            return True


        elif msg['text'] == 'suco':
            if msg['from']['id'] in sudoers:
                is_sudo = 'é gostozinho'
            else:
                is_sudo = 'tem gosto de bosta'
            await bot.sendMessage(msg['chat']['id'], is_sudo + '?',
                                  reply_to_message_id=msg['message_id'])
            return True

        
        elif msg['text'].lower() == 'rt' and msg.get('reply_to_message'):
            print('Usuario {} solicitou rt'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou rt  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg['reply_to_message'].get('text'):
                text = msg['reply_to_message']['text']
            elif msg['reply_to_message'].get('caption'):
                text = msg['reply_to_message']['caption']
            else:
                text = None
            if text:
                if text.lower() != 'rt' or msg['text'] == '/rt@' + bot_username or msg['text'] == 'rtt':
                    if not re.match('🔃 .* foi gado pra caralho do filho da puta do :\n\n👤 .*', text):
                        await bot.sendMessage(msg['chat']['id'], '''🔃 <b>{}</b> foi gado pra caralho concordando com o -->

👤 <b>{}</b>: <i>{}</i>'''.format(msg['from']['first_name'], msg['reply_to_message']['from']['first_name'],
                                  text),
                                              parse_mode='HTML',
                                              reply_to_message_id=msg['message_id'])
                return True
                #---------------------------------------------------------------------------------------------------------------

        elif msg['text'].lower() == 'gay' and msg.get('reply_to_message'):
            print('Usuario {} solicitou gay'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou gay  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg['reply_to_message'].get('text'):
                text = msg['reply_to_message']['text']
            elif msg['reply_to_message'].get('caption'):
                text = msg['reply_to_message']['caption']
            else:
                text = None
            if text:
                if text.lower() != 'rt' or msg['text'] == 'rtt':
                    if not re.match('🔃 .* chamou de gay e pode sofrer processo do :\n\n👤 .*', text):
                        await bot.sendMessage(msg['chat']['id'], '''<b>{}  pode tomar um processo pois foi estupido para caralho xingando {} de gay, este viado e bicha loca do caralho só porque ele disse</b> <i>{}</i>'''.format(msg['from']['first_name'], msg['reply_to_message']['from']['first_name'],
                                  text),
                                              parse_mode='HTML',
                                              reply_to_message_id=msg['message_id'])
                return True
        
                #---------------------------------------------------------------------------------------------------------------

        elif msg['text'].lower() == 'pau no cu' or msg['text'].lower() == 'pnc'and msg.get('reply_to_message'):
            print('Usuario {} solicitou pau no cu(rt)'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou pau no cu(rt)  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg['reply_to_message'].get('text'):
                text = msg['reply_to_message']['text']
            elif msg['reply_to_message'].get('caption'):
                text = msg['reply_to_message']['caption']
            else:
                text = None
            if text:
                if text.lower() != 'rt' or msg['text'] == 'rtt':
                    if not re.match('🔃 .* chamou de pau no cu e pode sofrer processo do :\n\n👤 .*', text):
                        await bot.sendMessage(msg['chat']['id'], '''<b>{} xingou e nao deixou baixo para {}, eu nao deixava e cagava o filho da puta na porrada so porque ele disse</b> <i>{}</i>'''.format(msg['from']['first_name'], msg['reply_to_message']['from']['first_name'],
                                  text),
                                              parse_mode='HTML',
                                              reply_to_message_id=msg['message_id'])
                return True

        elif msg['text'].lower() == 'filho da puta' or msg['text'].lower() == 'pnc'and msg.get('reply_to_message'):
            print('Usuario {} solicitou filho da puta(rt)'.format(msg['from']['first_name']))
            log = '\nUsuario {} solicitou filho da puta(rt)  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
            arquivo = open('logs/grupos.txt','a')
            arquivo.write(log)
            arquivo.close()
            if msg['reply_to_message'].get('text'):
                text = msg['reply_to_message']['text']
            elif msg['reply_to_message'].get('caption'):
                text = msg['reply_to_message']['caption']
            else:
                text = None
            if text:
                if text.lower() != 'rt' or msg['text'] == 'rtt':
                    if not re.match('🔃 .* xingou a mãe do \n\n👤 .*', text):
                        await bot.sendMessage(msg['chat']['id'], '''<b>{} xingou a mãe do {}, poxa o cara só falou</b> <i>{}</i>'''.format(msg['from']['first_name'], msg['reply_to_message']['from']['first_name'],
                                  text),
                                              parse_mode='HTML',
                                              reply_to_message_id=msg['message_id'])
                return True        
        




               