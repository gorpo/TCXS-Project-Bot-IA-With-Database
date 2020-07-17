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


print(r'''
███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
╔╦╗╔═╗═╗ ╦╔═╗  ╔═╗╦═╗╔═╗ ╦╔═╗╔═╗╔╦╗  ╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗  ╔╦╗╔═╗╔═╗╔╦╗
 ║ ║  ╔╩╦╝╚═╗  ╠═╝╠╦╝║ ║ ║║╣ ║   ║   ╠═╣╠═╣║  ╠╩╗║╣ ╠╦╝   ║ ║╣ ╠═╣║║║
 ╩ ╚═╝╩ ╚═╚═╝  ╩  ╩╚═╚═╝╚╝╚═╝╚═╝ ╩   ╩ ╩╩ ╩╚═╝╩ ╩╚═╝╩╚═   ╩ ╚═╝╩ ╩╩ ╩
     [+] @GorpoOrko 2020 - Telegram Bot and Personal Assistant [+]
     |   TCXS Project Hacker Team - https://tcxsproject.com.br   |
     |   Telegram: @GorpoOrko Mail:gorpoorko@protonmail.com      |
     |        Github Gorpo Dev: https://github.com/gorpo         |
     [+]   Thanks: https://github.com/AmanoTeam/amanobot       [+]

Manicômio Telegram BOT - @GorpoOrko Developer 
Iniciando a hackeada na galera.
Iniciando o Manicômio Bot Manicômio.
''')

import asyncio
import json
import html
import traceback
import amanobot.aio
from amanobot.exception import TelegramError, TooManyRequestsError, NotEnoughRightsError
from amanobot.aio.loop import MessageLoop
from colorama import Fore
from urllib3.exceptions import ReadTimeoutError

import backups
import db_handler as db
from config import bot, na_bot, enabled_plugins, logs, version, backups_chat
from utils import send_to_dogbin

ep = []
n_ep = {}

for num, i in enumerate(enabled_plugins):
    try:
        print(Fore.RESET + 'Carregando plugins para hackear os cornos... [{}/{}]'.format(num + 1, len(enabled_plugins)), end='\r')
        exec('from plugins.{0} import {0}'.format(i))
        ep.append(i)
    except Exception as erro:
        n_ep[i] = traceback.format_exc()
        print('\n' + Fore.RED + 'Erro ao carregar o plugin {}:{}'.format(i, Fore.RESET), erro)


async def handle(msg):
    for plugin in ep:
        try:
            p = await globals()[plugin](msg)
            if p:
                break
        except (TooManyRequestsError, NotEnoughRightsError, ReadTimeoutError):
            break
        except Exception as e:
            formatted_update = json.dumps(msg, indent=3)
            formatted_exc = traceback.format_exc()
            exc_url = await send_to_dogbin('Update:\n' + formatted_update + '\n\n\n\nFull Traceback:\n' + formatted_exc)
            print(f"""Ocorreu um erro com plugin: {plugin}
Tipo do erro: {e.__class__.__name__}
Descrição: {html.escape(e.description if isinstance(e, TelegramError) else str(e))}
Erro completo: {exc_url}""")
#            await bot.sendMessage(logs, '''• <b>Erro:</b>
# » Plugin: <code>{plugin}</code>
# » Tipo do erro: <code>{exc_type}</code>
# » Descrição: <i>{exc_desc}</i>
#- <a href="{exc_url}">Erro completo</a>'''.format(plugin=plugin, exc_type=e.__class__.__name__,  exc_desc=html.escape(e.description if isinstance(e, TelegramError) else str(e)), exc_url=exc_url), parse_mode='html', disable_web_page_preview=True)



if __name__ == '__main__':

    answerer = amanobot.aio.helper.Answerer(bot)
    loop = asyncio.get_event_loop()

    print('\n\nBot Manicomio iniciado com sucesso, enviando dados para o Telegram! {}\n'.format(version))

    if backups_chat:
        backups.backup_service()

    loop.create_task(MessageLoop(bot, handle).run_forever())

    wr = db.get_restarted()

    if wr:
        try:
            na_bot.editMessageText(wr, 'Reiniciado com sucesso!')
        except TelegramError:
            pass
        db.del_restarted()
    else:
        #na_bot.sendMessage(logs, '''Manicômio bot iniciado com sucesso, 28 plugins foram carregados, digite /comandos@gorpo_bot para saber os comandos do bot.'''.format(version, len(ep), len(n_ep),': ' + (', '.join(n_ep)) if n_ep else ''))
        pass
    loop.run_forever()
