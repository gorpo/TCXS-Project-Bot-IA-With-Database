[![Build](https://img.shields.io/badge/dev-gorpo-brightgreen.svg)]()
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Build](https://img.shields.io/badge/python-v3.7-blue.svg)]()
[![Build](https://img.shields.io/badge/windows-7%208%2010-blue.svg)]()
[![Build](https://img.shields.io/badge/Linux-Ubuntu%20Debian-orange.svg)]()
[![Build](https://img.shields.io/badge/arquiterura-64bits-blue.svg)]()
<h2 align="center">Manicomio Telegram Heroku Bot</h2>
## Instruções:
1. Edite no arquivo config se quer rodar o bot local ou no heroku, comente e descomente as linhas.
2. Edite requeriments.txt caso tenha adicionado novas libs.
3. Especifique a versão do python no arquivo runtime, confira as versões de python disponiveis no heroku [aqui](https://devcenter.heroku.com/articles/python-runtimes)
4. Crie um bot no Botfather e pegue o token do bot.
5. insira este bot em um canal e pegue o id do canal, ele servirá para os logs.
6. pegue sua id ela servirá para você ser adm master.

### Via linha de comando - CLI
```
cd manicomio_bot_heroku
heroku login
heroku create --region us manicomio       #seta us como regiao e nome_do_app defina o nome do  app no heroku
heroku buildpacks:set heroku/python       #seta o python
git push heroku master                    #deploy do programa no heroku

heroku config:set TELEGRAM_TOKEN=1186597860:AAHZTQT--xYhNHhkO8SbxlSxrdwVnkvi38s #seta as config vars, insira seu token
heroku config:set LOGS=-1001215401730    #seta a id do canal de logs que o bot ja deve estar e ter admin
heroku config:set SUDOERS=522510051      #seta o sudo ou seja adm master do bot

heroku ps:scale bot=1 # start bot dyno - inicia seu bot
heroku logs --tail # Ativa os logs no terminal ou cmd
heroku ps:stop bot #para o bot dyno  - para seu bot
```

## Deploying via [Heroku Dashboard](https://dashboard.heroku.com) (GUI)
1. [Fork](https://github.com/Kylmakalle/heroku-telegram-bot/fork) this repo to your account. 
2. [Edit files](https://github.com/Kylmakalle/heroku-telegram-bot#edit-files)
3. Go to [Dashboard](https://dashboard.heroku.com), login, Press _New_ and choose _Create new app._
4. Fill in an _App Name_ and choose _Runtime Region._
5. Connect your GitHub repo at _Deploy_ page.
6. Setup **Automatics deploys** _(Optionaly)._
7. _Deploy a GitHub branch._
8. Then go to a _Settings_ page, click _Reveal Config Vars_ and then add your own, for example:
![Config Vars](http://i.imgur.com/C3cmphh.png)
9. **Finally**, go to the _Resources_ page.
    1. Install _Heroku Redis_ add-on _(Optionaly)_
    2. Press on a small pen button, move slider and then click _Confirm_, that will start bot dyno.
    3. Simply move slider back if you need to stop bot dyno, remember to click _Confirm_.
    4. If for some reason it’s not working, check the logs here     
    ![Logs](http://i.imgur.com/rIHU6zF.png)

### More about
- https://devcenter.heroku.com/articles/dynos
- https://devcenter.heroku.com/articles/config-vars
- https://devcenter.heroku.com/articles/heroku-redis
- https://devcenter.heroku.com/articles/error-codes


