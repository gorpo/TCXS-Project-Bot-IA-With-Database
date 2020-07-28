from telegraph import Telegraph
"""
#EDITOR DE PAGINAS NO TELEGRAPH
#cria uma conta e uma pagina retornando o token
telegraph = Telegraph()
a = telegraph.create_account(short_name='1337')
print(a)
response = telegraph.create_page('Nome da página', html_content='<p>conteudo em html</p>')
print('https://telegra.ph/{}'.format(response['path']))



#metodo de ediçao com requests

import requests
params = {
    'access_token': "adefb3eef080f888af21d3b81f225f54fbaf86b423cc7c66897554a25366",
    'path': '/Hey-07-25-30',
    'title': 'Manicômio',
    'content':[ {"tag":"p","children":["A link to gooererererergle",{"tag":"a","attrs":{"href":"http://google.com/","target":"_blank"},"children":["http://google.com"]}]} ],
    'author_name': '1337',
    'author_url': None,
    'return_content': 'true'
}

url = 'https://api.telegra.ph/editPage'

r = requests.post(url, json=params)
r.raise_for_status()
response = r.json()
print(response)
"""
telegraph = Telegraph()
a = telegraph.create_account(short_name='manicomio')
print(a)


#lista = []
#separador = ' '
#for i in range(3):
#    lista.append('<p>asdasdasd</p><img src="https://miro.medium.com/max/1200/1*ciLg4-fezXdbaunhk1E6gQ.jpeg">')
conteudo_html = separador.join(map(str, lista))

response = telegraph.create_page('Manicomio', html_content=str(conteudo_html))
print('https://telegra.ph/{}'.format(response['path']))

#<img src="https://miro.medium.com/max/1200/1*ciLg4-fezXdbaunhk1E6gQ.jpeg">
