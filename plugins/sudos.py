

import random
import amanobot
import aiohttp
import time
import html
import io
import os
import re
import asyncio
import sys
from datetime import datetime
import traceback
from contextlib import redirect_stdout

from amanobot.exception import TelegramError
from emoji import emojize

import db_handler as db
from utils import backup_sources
from config import bot, bot_id, bot_username, git_repo, sudoers,logs


async def sudos(msg):
    if msg.get('text') and msg['chat']['type'] != 'channel':
        if msg['from']['id'] in sudoers:

            if msg['text'] == '!sudos' or msg['text'] == '/sudos' or msg['text'] == 'sudos':
                print('Usuario {} solicitou /sudos'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /sudos  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                await bot.sendMessage(msg['chat']['id'], '''*Lista de sudos:*

[*] COMANDOS ACEITOS APENAS PELO GORPO [*]
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
| - Define desligamento do bot, EX: 12|30''',
                                      'Markdown',
                                      reply_to_message_id=msg['message_id'])
                return True


            elif msg['text'].split()[0] == '!eval' or msg['text'].split()[0] == 'eval' or msg['text'].split()[0] == 'funcao' or msg['text'].split()[0] == '/eval':
                print('Usuario {} solicitou /eval(executar função python)'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /eval(executar função python) --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()

                text = msg['text'][6:]
                try:
                    res = (await eval(text[6:]) if re.match(r'(\W+)?await', text) else eval(text))
                except:
                    res = traceback.format_exc()
                try:
                    await bot.sendMessage(msg['chat']['id'], str(res), reply_to_message_id=msg['message_id'])
                except TelegramError as e:
                    await bot.sendMessage(msg['chat']['id'], e.description, reply_to_message_id=msg['message_id'])
                return True


                   

           



    


            elif msg['text'].split()[0] == '!plist' or msg['text'].split()[0] == 'plist':
                print('Usuario {} solicitou /plist(listar plugins)'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /plist(listar plugins)  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                from bot import ep, n_ep
                if msg['text'].split(' ', 1)[-1] == 'errors':
                    if n_ep:
                        res = '<b>Tracebacks:</b>\n' + '\n'.join(f"<b>{pname}:</b>\n{html.escape(n_ep[pname])}" for pname in n_ep)
                    else:
                        res = 'All plugins loaded without any errors.'
                    await bot.sendMessage(msg['chat']['id'],  res,
                                          parse_mode="html",
                                          reply_to_message_id=msg['message_id'])
                else:
                    res = f'<b>Active plugins ({len(ep)}):</b>\n' + '; '.join(sorted(ep))
                    res += (f'\n\n<b>Inactive plugins ({len(n_ep)}):</b>\n' + '; '.join(sorted(n_ep)) + '\n\nTo see the traceback of these plugins, just type <code>!plist errors</code>') if n_ep else ''
                    await bot.sendMessage(msg['chat']['id'], res,
                                          parse_mode="html",
                                          reply_to_message_id=msg['message_id'])
                return True


            elif msg['text'].startswith('!upload'):
                print('Usuario {} solicitou /upload'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /upload  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                text = msg['text'][8:]
                if msg.get('reply_to_message'):
                    sent = await bot.sendMessage(msg['chat']['id'], '⏰ Enviando o arquivo para o servidor...',
                                                 reply_to_message_id=msg['message_id'])
                    try:
                        file_id = msg['reply_to_message']['document'] ['file_id']
                        
                        file_name = msg['reply_to_message']['document']['file_name']
                        if len(text) >= 1:
                            file_name = text + '/' + file_name
                        await bot.download_file(file_id, file_name)
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  '✅ Envio concluído! Localização: {}'.format(file_name))
                    except Exception as e:
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  '❌ Ocorreu um erro!\n\n{}'.format(traceback.format_exc()))



            elif msg['text'].startswith('upload'):
                print('Usuario {} solicitou upload'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou upload  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()

                text = msg['text'][7:]
                if msg.get('reply_to_message'):
                    sent = await bot.sendMessage(msg['chat']['id'], '⏰ Enviando o arquivo para o servidor...',
                                                 reply_to_message_id=msg['message_id'])
                    try:
                        file_id = msg['reply_to_message']['document'] ['file_id']
                        
                        file_name = msg['reply_to_message']['document']['file_name']
                        if len(text) >= 1:
                            file_name = text + '/' + file_name
                        await bot.download_file(file_id, file_name)
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  '✅ Envio concluído! Localização: {}'.format(file_name))
                    except Exception as e:
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  '❌ Ocorreu um erro!\n\n{}'.format(traceback.format_exc()))

            elif msg['text'].startswith('baixar'):
                print('Usuario {} solicitou baixar'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou baixar  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                text = msg['text'][7:]
                if msg.get('reply_to_message'):
                    sent = await bot.sendMessage(msg['chat']['id'], '⏰ Enviando o arquivo para o servidor...',
                                                 reply_to_message_id=msg['message_id'])
                    try:
                        file_id = msg['reply_to_message']['document'] ['file_id']
                        
                        file_name = msg['reply_to_message']['document']['file_name']
                        if len(text) >= 1:
                            file_name = text + '/' + file_name
                        await bot.download_file(file_id, file_name)
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  '✅ Envio concluído! Localização: {}'.format(file_name))
                    except Exception as e:
                        await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                                  '❌ Ocorreu um erro!\n\n{}'.format(traceback.format_exc()))



            elif msg['text'] == '!restart' or msg['text'] == '/restart@gorpo_bot' + bot_username or msg['text'] == 'restart' or msg['text'] == 'reiniciar':
                print('Usuario {} solicitou /restart'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /restart  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                sent = await bot.sendMessage(msg['chat']['id'], 'Reiniciando...',
                                             reply_to_message_id=msg['message_id'])
                db.set_restarted(sent['chat']['id'], sent['message_id'])
                await asyncio.sleep(3)
                os.execl(sys.executable, sys.executable, *sys.argv)


            elif msg['text'].split()[0] == 'cmd' :
                print('Usuario {} solicitou cmd'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou cmd  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                text = msg['text'][4:]
                if re.match('(?i).*poweroff|halt|shutdown|reboot', text):
                    res = 'Comando proibido.'
                else:
                    proc = await asyncio.create_subprocess_shell(text,
                                                                 stdout=asyncio.subprocess.PIPE,
                                                                 stderr=asyncio.subprocess.PIPE)
                    stdout, stderr = await proc.communicate()
                    res = (f"<b>Output:</b>\n<code>{stdout.decode()}</code>"  if stdout else '') + (
                           f"\n\n<b>Errors:</b>\n<code>{stderr.decode()}</code>"  if stderr else '')

                await bot.sendMessage(msg['chat']['id'], res or 'Comando executado.',
                                      parse_mode="HTML",
                                      reply_to_message_id=msg['message_id'])
                return True

            elif msg['text'].split()[0] == '!doc' or msg['text'].split()[0] == 'doc':
                print('Usuario {} solicitou /doc'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /doc --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                text = msg['text'][5:]
                if text:
                    try:
                        await bot.sendChatAction(msg['chat']['id'], 'upload_document')
                        await bot.sendDocument(msg['chat']['id'], open(text, 'rb'),
                                               reply_to_message_id=msg['message_id'])
                    except FileNotFoundError:
                        await bot.sendMessage(msg['chat']['id'], 'Arquivo não encontrado.',
                                              reply_to_message_id=msg['message_id'])
                    except TelegramError as e:
                        await bot.sendMessage(msg['chat']['id'], e.description,
                                              reply_to_message_id=msg['message_id'])
                return True


            elif msg['text'] == '!del' or msg['text'] == 'del' or msg['text'] == 'deletar':
                print('Usuario {} solicitou /del'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /del  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                if msg.get('reply_to_message'):
                    try:
                        await bot.deleteMessage((msg['chat']['id'], msg['reply_to_message']['message_id']))
                    except TelegramError:
                        pass
                    try:
                        await bot.deleteMessage((msg['chat']['id'], msg['message_id']))
                    except TelegramError:
                        pass
                return True


            elif msg['text'].split()[0] == '!exec' or msg['text'].split()[0] == 'exec':
                print('Usuario {} solicitou /exec'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /exec  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                text = msg['text'][6:]

                # Merge global and local variables
                globals().update(locals())

                try:
                    # Create an async function so we can run async code without issues.
                    exec('async def __ex(c, m): ' + ' '.join('\n ' + l for l in text.split('\n')))
                    with io.StringIO() as buf, redirect_stdout(buf):
                        await locals()['__ex'](bot, msg)
                        res = buf.getvalue() or 'Código sem retornos.'
                except:
                    res = traceback.format_exc()
                try:
                    await bot.sendMessage(msg['chat']['id'], res, reply_to_message_id=msg['message_id'])
                except TelegramError as e:
                    await bot.sendMessage(msg['chat']['id'], e.description, reply_to_message_id=msg['message_id'])
                return True


            elif msg['text'] == '':#aqui era !upgrade
                print('Usuario {} solicitou /upgrade'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /upgrade  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                sent = await bot.sendMessage(msg['chat']['id'], 'Atualizando a base do bot...',
                                             reply_to_message_id=msg['message_id'])
                proc = await asyncio.create_subprocess_shell(
                    'git fetch {} && git rebase FETCH_HEAD'.format(' '.join(git_repo)),
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE)
                stdout, stderr = await proc.communicate()
                if stdout:
                    await bot.editMessageText((msg['chat']['id'], sent['message_id']), f'Resultado:\n{stdout.decode()}')
                    sent = await bot.sendMessage(msg['chat']['id'], 'Reiniciando...')
                    db.set_restarted(sent['chat']['id'], sent['message_id'])
                    await asyncio.sleep(3)
                    os.execl(sys.executable, sys.executable, *sys.argv)
                elif stderr:
                    await bot.editMessageText((msg['chat']['id'], sent['message_id']),
                                              f'Ocorreu um erro:\n{stderr.decode()}')


            elif msg['text'].startswith('!leave') or msg['text'].startswith('leave'):
                print('Usuario {} solicitou /leave'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /leave  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                if len(msg['text'].split()) == 2:
                    chat_id = msg['text'].split()[1]
                else:
                    chat_id = msg['chat']['id']
                try:
                    await bot.sendMessage(chat_id, 'Tou saindo daqui flws')
                except TelegramError:
                    pass
                await bot.leaveChat(chat_id)
                return True


            elif msg['text'].startswith('!chat') or msg['text'].startswith('chat'):
                print('Usuario {} solicitou /chat'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /chat  --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                if ' ' in msg['text']:
                    chat = msg['text'].split()[1]
                else:
                    chat = msg['chat']['id']
                sent = (await bot.sendMessage(msg['chat']['id'], '⏰ Obtendo informações do chat...',
                                              reply_to_message_id=msg['message_id']
                                              ))['message_id']
                try:
                    res_chat = await bot.getChat(chat)
                except TelegramError:
                    return await bot.editMessageText((msg['chat']['id'], sent), 'Chat não encontrado')
                if res_chat['type'] != 'private':
                    try:
                        link = await bot.exportChatInviteLink(chat)
                    except TelegramError:
                        link = 'Não disponível'
                    try:
                        members = await bot.getChatMembersCount(chat)
                    except TelegramError:
                        members = 'erro'
                    try:
                        username = '@' + res_chat['username']
                    except KeyError:
                        username = 'nenhum'
                    await bot.editMessageText((msg['chat']['id'], sent), f'''<b>Informações do chat:</b>

<b>Título:</b> {html.escape(res_chat["title"])}
<b>Username:</b> {username}
<b>ID:</b> {res_chat["id"]}
<b>Link:</b> {link}
<b>Membros:</b> {members}
''',
                                              parse_mode='HTML',
                                              disable_web_page_preview=True)
                else:
                    try:
                        username = '@' + res_chat['username']
                    except KeyError:
                        username = 'nenhum'
                    await bot.editMessageText((msg['chat']['id'], sent),
                                              '''<b>Informações do chat:</b>

<b>Nome:</b> {}
<b>Username:</b> {}
<b>ID:</b> {}
'''.format(html.escape(res_chat['first_name']), username, res_chat['id']),
                                              parse_mode='HTML',
                                              disable_web_page_preview=True)
                return True


            elif msg['text'] == '!promote' or msg['text'] == 'promovido' or msg['text'] == 'promover':
                print('Usuario {} solicitou /promote'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /promote --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                if 'reply_to_message' in msg:
                    reply_id = msg['reply_to_message']['from']['id']
                else:
                    return
                for perms in await bot.getChatAdministrators(msg['chat']['id']):
                    if perms['user']['id'] == bot_id:
                        await bot.promoteChatMember(
                            chat_id=msg['chat']['id'],
                            user_id=reply_id,
                            can_change_info=perms['can_change_info'],
                            can_delete_messages=perms['can_delete_messages'],
                            can_invite_users=perms['can_invite_users'],
                            can_restrict_members=perms['can_restrict_members'],
                            can_pin_messages=perms['can_pin_messages'],
                            can_promote_members=True)
                return True


             


            elif msg['text'].split()[0] == '!backup' or msg['text'] == 'backup' or msg['text'] == '/backup' or msg['text'] == '/backup@gorpo_bot':
                print('Usuario {} solicitou /backup'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou /backup --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                sent = await bot.sendMessage(msg['chat']['id'], '⏰ Fazendo backup...',
                                             reply_to_message_id=msg['message_id'])

                if 'pv' in msg['text'].lower() or 'privado' in msg['text'].lower():
                    msg['chat']['id'] = msg['from']['id']

                cstrftime = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')

                fname = backup_sources()

                if not os.path.getsize(fname) > 52428800:
                    await bot.sendDocument(msg['chat']['id'], open(fname, 'rb'), caption="📅 " + cstrftime)
                    await bot.editMessageText((sent['chat']['id'], sent['message_id']), '✅ Backup concluído!')
                    os.remove(fname)
                else:
                    await bot.editMessageText((sent['chat']['id'], sent['message_id']),
                                              f'Ei, o tamanho do backup passa de 50 MB, então não posso enviá-lo aqui.\n\nNome do arquivo: `{fname}`',
                                              parse_mode='Markdown')

                return True

            elif '|' in msg['text']:
                print('Usuario {} solicitou desligamento temporario do bot definindo uma hora'.format(msg['from']['first_name']))
                log = '\nUsuario {} solicitou desligamento temporario do bot definindo uma hora --> Grupo: {} --> Data/hora:{}'.format(msg['from']['first_name'],msg['chat']['title'],time.ctime())
                arquivo = open('logs/grupos.txt','a')
                arquivo.write(log)
                arquivo.close()
                h = msg['text'].split('|')[0]
                m = msg['text'].split('|')[1]
                hm = (int(h),int(m))
                await bot.sendMessage(msg['chat']['id'],emojize(':alarm_clock:  Beleza {} você definou o horário para eu ficar offline até {}:{}, aviso quando voltar! :alarm_clock: '.format(msg['from']['first_name'],h,m)),'markdown',reply_to_message_id=msg['message_id'])
                                   
                while True:
                    if time.localtime()[3:5] == hm:
                        await bot.sendMessage(msg['chat']['id'],emojize(':bell:  {} ja são {}:{}, voltei como vc tinha pedido. :bell: '.format(msg['from']['first_name'],h,m)) ,'markdown',reply_to_message_id=msg['message_id'])
                        break   