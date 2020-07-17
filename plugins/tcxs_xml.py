
import html
import re
import random
import amanobot
import aiohttp
from amanobot.exception import TelegramError
import time
from config import bot, sudoers, logs, bot_username
from utils import send_to_dogbin, send_to_hastebin
import os
from utils import send_to_dogbin, send_to_hastebin



async def tcxs_xml(msg):
    if msg.get('text'):
        if '/ps1' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link = msg['text'].split()[4]
                #string armazena o xml a ser gravado e printado
                arq = (f'''
<XMBML version="1.0">
<View id="ps1_items_link">
<Attributes>
    <Table key="ps1_item_link">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PS1/download.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} </String></Pair>
    <Pair key="info"><String>TCXS - {descricao} </String></Pair>
    <Pair key="module_name"><String>webrender_plugin</String></Pair>
    <Pair key="module_action"><String>{link}</String></Pair>
</Table>
</Attributes>
<Items>
    <Query class="type:x-xmb/module-action" key="ps1_item_link" attr="ps1_item_link"/>
</Items>
</View>
</XMBML>''')
                #bot envia mensagem
                
                await bot.sendMessage(msg['chat']['id'], (f'Seu xml de PlaysTation1 meu mestre ```{arq}```'), 'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
    `Abaixo de <Attributes> cole:`
    ```
<Table key="ps1_{nome_xml}">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PS1/{nome_xml}.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
    <Pair key="info"><String> {descricao}- TCXS</String></Pair>
</Table>```
    `Abaixo de <Items> cole:`
    ```
<Query class="type:x-xmb/folder-pixmap" key="ps1_{nome_xml}" attr="ps1_{nome_xml}" src="xmb://localhost/dev_hdd0/game/HENBSTORE/USRDIR/XMLS/PS1/{nome_xml}.xml#ps1_items_link" />```''')

                jon = open("xml/PS1/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('','')
                    jon.writelines(j)
                jon.close()

                await bot.sendMessage(msg['chat']['id'],arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'], document=open("xml/PS1/{}.xml".format(nome_xml),'rb'), reply_to_message_id=msg['message_id'])

            except:
                instrucao = '''Instruções: 
```
1 - meu comando sempre começa com /xml
2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
`Copie de dentro das aspas o caractere invisivel:`"⠀"

**VAMOS AO COMANDO EM SI**
`Exemplo com caractere invisivel:`
``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
`Exemplo sem caractere visivel:`
``` /ps1 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
**Onde cada campo:**
`/ps1` ```- chama comando```
`gow` ```- nome do xml```
`god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
`descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
`www.linkdropbox.com` ```- Link do Dropbox```

'''
                await bot.sendMessage(msg['chat']['id'], instrucao,'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

        if '/ps2' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link = msg['text'].split()[4]
                # string armazena o xml a ser gravado e printado
                arq = (f'''
<XMBML version="1.0">
<View id="ps2_items_link">
<Attributes>
    <Table key="ps2_item_link">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PS2/download.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} </String></Pair>
    <Pair key="info"><String>TCXS - {descricao} </String></Pair>
    <Pair key="module_name"><String>webrender_plugin</String></Pair>
    <Pair key="module_action"><String>{link}</String></Pair>
</Table>
</Attributes>
<Items>
    <Query class="type:x-xmb/module-action" key="ps2_item_link" attr="ps2_item_link"/>
</Items>
</View>
</XMBML>''')
                # bot envia mensagem
                
                await bot.sendMessage(msg['chat']['id'], (f'Seu xml de PlaysTation2 meu mestre ```{arq}```'), 'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
            `Abaixo de <Attributes> cole:`
            ```
<Table key="ps2_{nome_xml}">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PS2/{nome_xml}.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
    <Pair key="info"><String> {descricao}- TCXS</String></Pair>
</Table>```
            `Abaixo de <Items> cole:`
            ```
<Query class="type:x-xmb/folder-pixmap" key="ps2_{nome_xml}" attr="ps2_{nome_xml}" src="xmb://localhost/dev_hdd0/game/HENBSTORE/USRDIR/XMLS/PS2/{nome_xml}.xml#ps2_items_link" />```''')

                jon = open("xml/PS2/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'], document= open("xml/PS2/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])

            except:
                instrucao = '''Instruções: 
        ```
        1 - meu comando sempre começa com /xml
        2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
        3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
        `Copie de dentro das aspas o caractere invisivel:`"⠀"
        
        **VAMOS AO COMANDO EM SI**
        `Exemplo com caractere invisivel:`
        ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
        `Exemplo sem caractere visivel:`
        ``` /ps2 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
        **Onde cada campo:**
        `/ps2` ```- chama comando```
        `gow` ```- nome do xml```
        `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
        `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
        `www.linkdropbox.com` ```- Link do Dropbox```

        '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

        if '/psp' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link = msg['text'].split()[4]
                # string armazena o xml a ser gravado e printado
                arq = (f'''
<XMBML version="1.0">
<View id="psp_items_link">
<Attributes>
<Table key="psp_item_link">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PSP/download.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} </String></Pair>
    <Pair key="info"><String>TCXS - {descricao} </String></Pair>
    <Pair key="module_name"><String>webrender_plugin</String></Pair>
    <Pair key="module_action"><String>{link}</String></Pair>
</Table>
</Attributes>
<Items>
    <Query class="type:x-xmb/module-action" key="psp_item_link" attr="psp_item_link"/>
</Items>
</View>
</XMBML>''')
                # bot envia mensagem
                
                await bot.sendMessage(msg['chat']['id'], (f'Seu xml meu mestre ```{arq}```'), 'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
            `Abaixo de <Attributes> cole:`
            ```
<Table key="psp_{nome_xml}">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PSP/{nome_xml}.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
    <Pair key="info"><String> {descricao}- TCXS</String></Pair>
</Table>```
            `Abaixo de <Items> cole:`
            ```
<Query class="type:x-xmb/folder-pixmap" key="psp_{nome_xml}" attr="psp_{nome_xml}" src="xmb://localhost/dev_hdd0/game/HENBSTORE/USRDIR/XMLS/PSP/{nome_xml}.xml#psp_items_link" />```''')

                jon = open("xml/PSP/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                    #print(i)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'], document=open("xml/PSP/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])

            except:
                instrucao = '''Instruções: 
        ```
        1 - meu comando sempre começa com /xml
        2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
        3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!``` 
        `Copie de dentro das aspas o caractere invisivel:`"⠀"
        
        **VAMOS AO COMANDO EM SI**
        `Exemplo com caractere invisivel:`
        ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com```
        `Exemplo sem caractere visivel:`
        ``` /psp gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com```
        **Onde cada campo:**
        `/psp` ```- chama comando```
        `gow` ```- nome do xml```
        `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
        `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
        `www.linkdropbox.com` ```- Link do Dropbox```

        '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True

        if '/ps3' in msg['text']:
            try:
                nome_xml = msg['text'].split()[1]
                nome = msg['text'].split()[2]
                descricao = msg['text'].split()[3]
                link1 = msg['text'].split()[4]
                link2 = msg['text'].split()[5]
                link3 = msg['text'].split()[6]

                # string armazena o xml a ser gravado e printado
                arq = (f'''<XMBML version="1.0">
<View id="ps3_items_link">
<Attributes>
     <Table key="ps3_item_0">
        <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/DLCS/download.png</String></Pair>
        <Pair key="title"><String>TCXS Parte1 GAME- {nome}</String></Pair>
        <Pair key="info"><String>TCXS - {descricao}</String></Pair>
        <Pair key="module_name"><String>webrender_plugin</String></Pair>
        <Pair key="module_action"><String>{link1}</String></Pair>
    </Table>
    <Table key="ps3_item_1">
        <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/DLCS/download.png</String></Pair>
        <Pair key="title"><String>TCXS Parte GAME+LIC- {nome}</String></Pair>
        <Pair key="info"><String>TCXS - {descricao}</String></Pair>
        <Pair key="module_name"><String>webrender_plugin</String></Pair>
        <Pair key="module_action"><String>{link2}</String></Pair>
    </Table>
    <Table key="ps3_item_2">
        <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/DLCS/download.png</String></Pair>
        <Pair key="title"><String>TCXS Parte GAME+LIC- {nome}</String></Pair>
        <Pair key="info"><String>TCXS - {descricao}</String></Pair>
        <Pair key="module_name"><String>webrender_plugin</String></Pair>
        <Pair key="module_action"><String>{link3}</String></Pair>
    </Table>
</Attributes>
<Items>
    <Query class="type:x-xmb/module-action" key="ps3_item_0" attr="ps3_item_0"/>
    <Query class="type:x-xmb/module-action" key="ps3_item_1" attr="ps3_item_1"/>
    <Query class="type:x-xmb/module-action" key="ps3_item_2" attr="ps3_item_2"/>
</Items>
</View>
</XMBML>''')
                # bot envia mensagem
                
                await bot.sendMessage(msg['chat']['id'], (f'Seu xml meu mestre ```{arq}```'), 'markdown',
                                      reply_to_message_id=msg['message_id'])

                arq2 = (f'''Seu XML esta pronto, insira estas linhas no seu XML Pai:
         `Abaixo de <Attributes> cole:`
         ```
<Table key="ps3_{nome_xml}">
    <Pair key="icon"><String>/dev_hdd0/game/HENBSTORE/USRDIR/IMAGES/PS3/{nome_xml}.jpg</String></Pair>
    <Pair key="title"><String>TCXS - {nome} - TCXS</String></Pair>
    <Pair key="info"><String>{descricao} - TCXS</String></Pair>
</Table>```
         `Abaixo de <Items> cole:`
         ```
<Query class="type:x-xmb/folder-pixmap" key="ps3_{nome_xml}" attr="ps3_{nome_xml}" src="xmb://localhost/dev_hdd0/game/HENBSTORE/USRDIR/XMLS/PS3/{nome_xml}.xml#ps3_items_link" />```''')

                jon = open("xml/PS3/{}.xml".format(nome_xml), "w")
                for i in arq:
                    j = i.replace('', '')
                    jon.writelines(j)
                    #print(i)
                jon.close()

                await bot.sendMessage(msg['chat']['id'], arq2, 'markdown',
                                      reply_to_message_id=msg['message_id'])

                await bot.sendDocument(msg['chat']['id'], document=open ("xml/PS3/{}.xml".format(nome_xml), 'rb'),
                                       reply_to_message_id=msg['message_id'])

            except:
                instrucao = '''Instruções: 
     ```
     1 - meu comando sempre começa com /xml
     2 - eu não aceito espaços no nome de arquivo, nome de jogo e nem na descrição!
     3 - você pode copiar o caractere especial invisivel dentro das aspas abaixo para usar onde precisar de espaço!
     4 - meu sistema para por jogos de PS3 aceitam apenas 3 links preciso deles como exemplos.``` 
     `Copie de dentro das aspas o caractere invisivel:`"⠀"
     
     **VAMOS AO COMANDO EM SI**
     `Exemplo com caractere invisivel:`
     ``` gow god⠀of⠀war descriçao⠀usando⠀caractere⠀invisivel     www.linkdropbox.com  www.linkdropbox.com  www.linkdropbox.com```
     `Exemplo sem caractere visivel:`
     ``` /ps3 gow god_of_war descrição_sem_caractere_visivel   www.linkdropbox.com www.linkdropbox.com www.linkdropbox.com```
     **Onde cada campo:**
     `/ps3` ```- chama comando```
     `gow` ```- nome do xml```
     `god_of_war` ```- nome do jogo, se quiser tirar os _ usar caractere especial no lugar```
     `descrição_do_jogo` ```- descrição, se quiser tirar os _ usar caractere especial no lugar``` 
     `www.linkdropbox.com` ```- Link do Dropbox, preciso de 3 links separados por espaço```

     '''
                await bot.sendMessage(msg['chat']['id'], instrucao, 'markdown',
                                      reply_to_message_id=msg['message_id'])
            return True