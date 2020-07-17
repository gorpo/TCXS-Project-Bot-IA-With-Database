# Copyright (C) 2018-2019 Amano Team <contact@amanoteam.ml>
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


import os
import time
import schedule
from datetime import datetime
from utils import backup_sources
from multiprocessing import Process
from config import backups_chat, backup_hours, na_bot

#função que faz os backups com base em hora
def backup_func():
    cstrftime = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
    file = backup_sources()
    na_bot.sendDocument(backups_chat, open(file, 'rb'), caption="📅 " + cstrftime + "\n_Gerado automaticamente pelo horario agendado por você._", parse_mode='Markdown')
    os.remove(file)


def backup_scheduler(target):
    for hour in backup_hours:
        schedule.every().day.at(hour).do(target)

    while True:
        schedule.run_pending()
        time.sleep(5)


def backup_service():
    p = Process(target=backup_scheduler, args=(backup_func,))
    p.start()
