from pathlib import Path
import pandas as pd


class BancoDados:
    def __init__(self):
        #Caminho do arquivo Excel
        self.arquivo = Path(__file__).parent / "banco_dados.xlsx"
        
    #Retorna uma aba do Excel como DataFrame(tabela)
    def carregar_tabela(self, nome_tabela):
        
        try:
            
            return pd.read_excel(
                self.arquivo,
                sheet_name=nome_tabela
            )
            
        except Exception as erro:
             print(f"Erro ao abrir a aba '{nome_tabela}'")
             print(erro)
             
             return None
             
    def listar_tabela(self):
        
        planilha = pd.ExcelFile(self.file)
        
        return planilha.sheet_names
    
    def tem_tabela(self, sheet_name):

        return sheet_name in self.listar_tabela()
    
    def get_by_id(self, sheet_name, id):
        
        tabela = self.get_table(sheet_name)
        
        resultado = tabela.loc[tabela["ID"] == id]
        
        if resultado.empty:
            return None
        
        return resultado.iloc[0]