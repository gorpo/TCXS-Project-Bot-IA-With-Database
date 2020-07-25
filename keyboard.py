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

from amanobot.namedtuple import InlineKeyboardMarkup




voltar_store_free = InlineKeyboardMarkup(inline_keyboard=[[dict(text='« Voltar', callback_data='store_free')]])
store_free = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='📦 TCXS Store PKG', callback_data='download_store_free')] +
            [dict(text="🗳️ FIX TCXS Store ", callback_data='download_fix')],
            [dict(text='📺 Tutorial Segundo Plano', callback_data='tutorial_segundo_plano')] +
            [dict(text="🎧 Fone Bluetooth ", callback_data='fone_bluetooth')],
            [dict(text='📲 Uso de Proxy', callback_data='proxy_usuarios')] +
            [dict(text='« Voltar', callback_data='inicio_menu')],])




voltar_store_doadores = InlineKeyboardMarkup(inline_keyboard=[[dict(text='« Voltar', callback_data='store_doadores')]])
store_doadores = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='⚠️ Como Participar,leia é importante ⚠️', callback_data='como_participar')] ,
            [dict(text="🤑 Doar Agora", callback_data='mercado_pago')]+
            [dict(text='📦 TCXS Store PKG', callback_data='download_store_doadores')],
            [dict(text="🗳️ FIX HAN PKG ", callback_data='download_fix_han_doadores')]+
            [dict(text="🗳️ FIX HEN PKG ", callback_data='download_fix_hen_doadores')],
            [dict(text="🗳️ FIX CFW XML ", callback_data='download_fix_cfw_doadores')]+
            [dict(text="🗳️ FIX HEN XML ", callback_data='download_fix_hen_xml_doadores')],
            [dict(text="📺 INSTALAÇÃO HAN/HEN!! ", callback_data='tutorial_loja')],
            [dict(text="📺 TUTORIAL INSTALAÇÃO CFW ", callback_data='tutorial_cfw')],
            [dict(text='📺 TUTORIAL SEGUNDO PLANO', callback_data='tutorial_segundo_plano_doadores')]+
            [dict(text="🎧 FONE BLUETOOTH", callback_data='fone_bluetooth_doadores')],
            [dict(text='📲 PROXY NO PS3', callback_data='proxy_usuarios_doadores')] +
            [dict(text='« Voltar', callback_data='inicio_menu')]])




voltar_comandos_usuarios = InlineKeyboardMarkup(inline_keyboard=[[dict(text='« Voltar', callback_data='comandos_usuarios')]])
comandos_usuarios = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='🦸 Comandos', callback_data='comandos_users')] +
            [dict(text="🦸 Sites", callback_data='sites_users')],
            [dict(text='🦸 Criar XML', callback_data='cria_xml_users')]+
            [dict(text='« Voltar', callback_data='inicio_menu')]])




voltar_comandos_admins = InlineKeyboardMarkup(inline_keyboard=[[dict(text='« Voltar', callback_data='comandos_admins')]])
comandos_admins = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text="🤖 Lojas/Fix IA", callback_data='cadastrar_lojas')]+
            [dict(text="🤖 Doadores IA", callback_data='restringir_doadores')],
            [dict(text='🤖 Grupos IA', callback_data='gerenciar_grupos')]+
            [dict(text="🤖 Comandos IA", callback_data='cadastrar_comandos')],
            [dict(text="🤖 Perguntas IA", callback_data='perguntas_admins')]+
            [dict(text="🤖 Proibições IA", callback_data='admin_proibicoes')],
            [dict(text='🤖 Frequencia IA', callback_data='admin_frequencia')]+
            [dict(text='🤖 Inteligência IA', callback_data='admin_inteligencia')],
            [dict(text='🤖 Desenvolvedor', callback_data='area_dev')]+
            [dict(text='« Voltar', callback_data='inicio_menu')]])




voltar_ferramentas_gerais = InlineKeyboardMarkup(inline_keyboard=[[dict(text='« Voltar', callback_data='ferramentas_gerais')]])
ferramentas_gerais = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='🧰 Ferramentas', callback_data='ferramenta_comandos')]+
            [dict(text='🤖 Frequencia IA', callback_data='ferramenta_frequencia')],
            [dict(text='🤖 Inteligência IA', callback_data='ferramenta_inteligencia')]+
            [dict(text='🤖 Perguntas IA', callback_data='ferramenta_perguntas')],
            [dict(text='🤖 Proibições IA', callback_data='ferramenta_proibicoes')]+
            [dict(text='« Voltar', callback_data='inicio_menu')]])




voltar_info_extras = InlineKeyboardMarkup(inline_keyboard=[[dict(text='« Voltar', callback_data='infos_extras')]])
info_extras = InlineKeyboardMarkup(inline_keyboard=[
            [dict(text='🗳️ Como adquirir Store PKG', callback_data='info_adquirir')],
            [dict(text='🤑 Sobre Doar', callback_data='info_doacao')]+
            [dict(text='🎮 Pré-requisitos', callback_data='info_requisitos')],
            [dict(text='🚧 Suporte', callback_data='info_suporte')]+
            [dict(text='« Voltar', callback_data='inicio_menu')]])















all_cmds = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='👮 Admins', callback_data='admin_cmds')] +
    [dict(text='👤 Usuários', callback_data='user_cmds')],
    [dict(text='🔧 Ferramentas', callback_data='tools_cmds')] +
    [dict(text='🔎 Modo inline', switch_inline_query_current_chat='')],
    [dict(text='« Voltar', callback_data='start_back')]
])

cmds_back = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='« Voltar', callback_data='all_cmds')]
])

del_msg = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='🗑 Deletar mensagem', callback_data='del_msg')]
])

ia_question = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='✅ Aceitar', callback_data='ia_yes')] +
    [dict(text='❌ Recusar', callback_data='ia_no')]
])
