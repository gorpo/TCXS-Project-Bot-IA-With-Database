import csv
import sqlite3


conexao_sqlite = sqlite3.connect('bot.db')
#conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()

id_grupo = '-1001367782383'

cursor_sqlite.execute(f"select * from frequencia  ")
freq = cursor_sqlite.fetchall()


lista = list(freq)
#print(lista)
for i, id_grupo in enumerate(lista):
        #print(i, id_grupo)
        if id_grupo[0] ==  -1001367782383:
                id_grupo_db = id_grupo[0]
                frequencia_db = id_grupo[2]
                print(id_grupo_db, frequencia_db)



