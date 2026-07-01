from banco_dados.banco_dados import BancoDados

db = BancoDados()

classe = db.carregar_tabela("Classes")

print(classe)