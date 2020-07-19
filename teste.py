import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

# inicia o modulo colorama - corzinha no terminal
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET

# inicializa o set de links (links unicos)
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

#inicializa o código------------>
if __name__ == "__main__":
    url = 'https://willpsx.blogspot.com/'
    max_urls = 10
    #faz o crawler------------->
    crawler(url, max_urls=max_urls)
    #tras os resultados------------>
    print("[+] Total de links internos:", len(urls_internas))
    print("[+] Total de links externos:", len(urls_externas))
    print("[+] Total de URLs:", len(urls_externas) + len(urls_internas))

    nome_dominio = urlparse(url).netloc

    # salva os links internos em um arquivo
    with open(f"{nome_dominio}_internal_links.txt", "w") as f:
        for internal_link in urls_internas:
            print(internal_link.strip(), file=f)

    # salva os links externos em um arquivo
    with open(f"{nome_dominio}_external_links.txt", "w") as f:
        for external_link in urls_externas:
            print(external_link.strip(), file=f)