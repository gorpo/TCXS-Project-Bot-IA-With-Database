#mudei tudo para pt aqui pq ingles nao pegava as linhas originais para linux estao comentadas

import json
from glob import glob
from sys import platform
from db_handler import cursor

strings = {}
if platform == 'linux' or platform == 'linux2':
    langs = [x.split('/')[1] for x in glob('langs/pt/main.json')]
if platform == 'win32':
    langs = [x.split('/')[1] for x in glob('langs/pt/main.json')]

for lang in langs:
    strings[lang] = {}
    if platform == 'linux' or platform == 'linux2':
        for file in glob('langs/{}/*.json'.format('pt')):
            strings[lang].update(json.load(open(file, encoding="utf8")))
    if platform == 'win32':
        for file in glob('langs/{}/*.json'.format('pt')):
            strings[lang].update(json.load(open(file, encoding="utf8")))


class Strings:
    def __init__(self, chat_id):
        # Supergoup and group IDs are negative.
        if chat_id < 0:
            cursor.execute('SELECT chat_lang FROM chats WHERE chat_id = ?', (chat_id,))
            try:
                self.language = cursor.fetchone()[0]
            except (IndexError, TypeError):
                if platform == 'linux' or platform == 'linux2':
                    self.language = 'pt'
                if platform == 'win32':
                    self.language = 'pt'
        else:
            cursor.execute('SELECT chat_lang FROM users WHERE user_id = ?', (chat_id,))
            try:
                self.language = cursor.fetchone()[0]
            except (IndexError, TypeError):
                if platform == 'linux' or platform == 'linux2':
                    self.language = 'pt'
                if platform == 'win32':
                    self.language = 'pt'
        if self.language not in langs:
            if platform == 'linux' or platform == 'linux2':
                self.language = 'pt'
            if platform == 'win32':
                self.language = 'pt'

        self.strings = strings[self.language]

    def get(self, string_key):
        if strings[self.language].get(string_key):
            return strings[self.language][string_key]
        elif platform == 'linux' or platform == 'linux2' and strings['pt'].get(string_key):
            return strings['pt'][string_key]
        elif platform == 'win32' and strings['pt'].get(string_key):
            return strings['pt'][string_key]
        else:
            return string_key
