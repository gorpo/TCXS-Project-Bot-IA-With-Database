





import sqlite3

conexao_sqlite = sqlite3.connect('bot_database.db')
conexao_sqlite.row_factory = sqlite3.Row
cursor_sqlite = conexao_sqlite.cursor()

cursor_sqlite.execute("""SELECT * FROM permanencia; """)
resultados = cursor_sqlite.fetchall()
# for resutado in resultados:
grupo_restrito = list(resultados)
print(grupo_restrito)