
call heroku login
call heroku create --region us manicomio 
call it init
call git add *
call git commit -m "Primeiro commit!"
call heroku git:remote -a manicomio
call git push heroku master 
call heroku config:set TELEGRAM_TOKEN=1186597860:AAGVtPY-1nHFdufqXDe06lI66UG9ttlwbVM
call heroku ps:scale bot=1 
call heroku logs --tail 
