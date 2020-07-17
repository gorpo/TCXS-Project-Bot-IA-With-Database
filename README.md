[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()
<h2 align="center">Manicomio Telegram Heroku Bot</h2>

<h2>Instruções:</h2><br>
1. Edite no arquivo config se quer rodar o bot local ou no heroku, comente e descomente as linhas.<br>
2. Edite requeriments.txt caso tenha adicionado novas libs.<br>
3. Especifique a versão do python no arquivo runtime, confira as versões de python disponiveis no heroku https://devcenter.heroku.com/articles/python-runtimes<br>
4. Crie um bot no Botfather e pegue o token do bot.<br>
5. insira este bot em um canal e pegue o id do canal, ele servirá para os logs.<br>
6. pegue sua id ela servirá para você ser adm master.<br>
<br>
<h2>Via linha de comando - CLI</h2><br>
<code>cd manicomio_bot_heroku</code><br>
<code>heroku login</code><br>
<code>heroku create --region us manicomio</code> seta us como regiao e nome_do_app defina o nome do  app no heroku<br>
<code>git init</code><br>
<code>git add *</code><br>
<code>git commit -m "Primeiro commit!"</code><br>
<code>heroku git:remote -a manicomio</code><br>


<code>git push heroku master</code>              deploy do programa no heroku<br>
<code>heroku config:set TELEGRAM_TOKEN=1186597860:AAHZTQT--xYhNHhkO8SbxlSxrdwVnkvi38s</code> seta as config vars, insira seu token<br>
<code>heroku config:set LOGS=-1001215401730</code> seta a id do canal de logs que o bot ja deve estar e ter admin<br>
<code>heroku config:set SUDOERS=522510051</code> seta o sudo ou seja adm master do bot<br>
<code>heroku ps:scale bot=1</code> start bot dyno - inicia seu bot<br>
<code>heroku logs --tail</code> tiva os logs no terminal ou cmd<br>
<code>heroku ps:stop bot</code> para o bot dyno  - para seu bot

<br><br>
<h2>links uteis</h2><br>
- https://devcenter.heroku.com/articles/dynos<br>
- https://devcenter.heroku.com/articles/config-vars<br>
- https://devcenter.heroku.com/articles/heroku-redis<br>
- https://devcenter.heroku.com/articles/error-codes<br>

<br>
<h2>Deploying via Heroku Dashboard</h2><br>
https://dashboard.heroku.com<br>
1. Fork este repositorio.<br>
3. Vá para https://dashboard.heroku.com, faça login, Pressione _Novo_ e escolha _Criar novo aplicativo._<br>
4. Preencha um _App Name_ e escolha _Runtime Region._<br>
5. Conecte seu repositório GitHub na página _Deploy_.<br>
6. Configuração ** Automatics deploys ** _ (Opcionalmente) ._<br>
7. _Implante uma filial do GitHub._<br>
8. Em seguida, vá para uma página _Settings_, clique em _Reveal Config Vars_ e adicione seus próprios, por exemplo:<br>
    8.1 TELEGRAM_TOKEN=118232260:AAHZTQT--xYhNHhkOsdfbxlSxrdwVnkvi38s <br>
    8.2 LOGS=-10012154123123 #id do canal do bot<br>
    8.3 SUDOERS=234234234234 #sua id<br>
9. ** Finalmente **, vá para a página _Resources_.<br>
    1. Instale o _Heroku Redis_ add-on _ (Opcionalmente) _<br>
    2. Pressione um botão pequeno da caneta, mova o controle deslizante e clique em _Confirmar_, que iniciará o bot dyno.<br>
    3. Simplesmente mova o controle deslizante para trás se precisar parar o bot dyno, lembre-se de clicar em _Confirmar_.<br>
    4. Se, por algum motivo, não estiver funcionando, verifique os logs.<br>
