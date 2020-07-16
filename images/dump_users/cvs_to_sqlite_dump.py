import csv
import sqlite3

#LE O ARQUIVO CSV BAIXADO-------------------------------------------->
arquivo = open('images/dump_users/members.csv','r', encoding='utf-8')
leitor = csv.reader(arquivo,delimiter=',')
for coluna in leitor:
    print(coluna)
    admin = 'foi feito dump usuários'
    if coluna[0] == '':
        doador = f"@{coluna[1]} ({coluna[3]})"
    else:
        doador = f"@{coluna[0]}"
    id_doador = coluna[1]
    dias = 30
    data_inicial =  '01/07/2020 22:08:15'
    data_final =    '01/08/2020 22:08:15'
    data_aviso =         '23/07/2020 22:08:15'

    #GRAVA OS DADOS NA DATABASE------------->
    conexao_sqlite = sqlite3.connect('bot.db')
    conexao_sqlite.row_factory = sqlite3.Row
    cursor_sqlite = conexao_sqlite.cursor()
    cursor_sqlite.execute(f"""INSERT INTO permanencia(int_id,admin, doador, id_doador, dias, data_inicial, data_final,data_aviso)VALUES(null,'{admin}','{doador}','{id_doador}','{dias}','{data_inicial}','{data_final}','{data_aviso}')""")
    conexao_sqlite.commit()
    cursor_sqlite.close()