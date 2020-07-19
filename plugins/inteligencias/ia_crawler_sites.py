import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama
from config import bot
import os

# inicia o modulo colorama - corzinha no terminal
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET

# armazena todas as urls internas e externas em um set
urls_internas = set()
urls_externas = set()

total_url_visitadas = 0

#Checka se a url é válida------------------>
def url_valida(url):
    url_analisada = urlparse(url)
    return bool(url_analisada.netloc) and bool(url_analisada.scheme)


#Retorna todos os URLs encontrados em `url 'nos quais pertence ao mesmo site------>
def todosLinks(url):
    # todos os URLs de `url`
    urls = set()
    # nome de domínio da URL sem o protocolo
    dominio_site = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        # href vazia----
        if href == "" or href is None:
            continue
        #adiciona a URL se for relativo e não o link absoluto
        href = urljoin(url, href)
        href_analisada = urlparse(href)
        #remova parâmetros de URL GET, fragmentos de URL etc.
        href = href_analisada.scheme + "://" + href_analisada.netloc + href_analisada.path
        # não é uma url valida
        if not url_valida(href):
            continue
        # já está no set
        if href in urls_internas:
            continue
        # capta links externos e internos do site
        if dominio_site not in href:
            if href not in urls_externas:
                print(f"{GRAY}[!] Link Externo: {href}{RESET}")
                urls_externas.add(href)
            continue
        print(f"{GREEN}[*] Link Interno: {href}{RESET}")
        urls.add(href)
        urls_internas.add(href)
    return urls


def crawler(url, max_urls=50):
    """
    Crawler - Rastreia uma página da web e extrai todos os links.
    Você encontrará todos os links nas variáveis​de conjunto global `urls_internas` e` urls_internas`.
    params:
        max_urls (int): número de URLs máximos a serem rastreados, o padrão é 30.
    """
    global total_url_visitadas
    total_url_visitadas += 1
    links = todosLinks(url)
    for link in links:
        if total_url_visitadas > max_urls:
            break
        crawler(link, max_urls=max_urls)
        #pega o nome de dominio do site
        nome_dominio = urlparse(url).netloc
        # salva os links internos em um arquivo
        with open(f"images/links_internos.txt", "w") as f:
            for internal_link in urls_internas:
                   f.write(internal_link)
                   print(internal_link.strip(), file=f)
            f.close()
        # salva os links externos em um arquivo
        with open(f"images/links_externos.txt", "w") as f:
            for external_link in urls_externas:
                f.write(external_link)
                print(external_link.strip(), file=f)
            f.close()





async def crawling(msg):
    try:#verifica se o usuario é um admin de grupo ou canal
        id_usuario = msg['from']['id']
        chat_type = msg['chat']['type']
        chat_id = msg['chat']['id']
        if chat_type == 'supergroup':
            if msg['text'].split()[0] == 'crawler':
                url = msg['text'].split()[1]
                try:
                    amax_urls = msg['text'].split()[2]
                    max_urls = amax_urls
                except:
                    max_urls = 2
                nome_dominio = urlparse(url).netloc
                await bot.sendMessage(chat_id,f'🤖 `Crawler no site {nome_dominio} iniciado aguarde...`','markdown', reply_to_message_id=msg['message_id'])
                a = crawler(url,max_urls)
                await bot.sendMessage(chat_id,f'🤖 `Crawler do site {nome_dominio} concluído, aqui estão os arquivos com os links:`','markdown', reply_to_message_id=msg['message_id'])
                await bot.sendDocument(chat_id,document=open('images/links_internos.txt','rb'),caption=f'Links internos que consegui captar no site {nome_dominio}',reply_to_message_id=msg['message_id'])
                await bot.sendDocument(chat_id, document=open('images/links_externos.txt', 'rb'),caption=f'Links externos que consegui captar no site {nome_dominio}',reply_to_message_id=msg['message_id'])
                os.remove('images/links_internos.txt')
                os.remove('images/links_externos.txt')






    except Exception as e:
        print(e)


#inicializa o código------------>
#if __name__ == "__main__":
    #url = 'https://archive.org/details/armchaircommando'
    #max_urls = 10
    #faz o crawler------------->
#    crawler(url, max_urls=max_urls)


    #tras os resultados------------>
#    print("[+] Total de links internos:", len(urls_internas))
#    print("[+] Total de links externos:", len(urls_externas))
#    print("[+] Total de URLs:", len(urls_externas) + len(urls_internas))

