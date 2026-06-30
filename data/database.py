from pathlib import Path
import pandas as pd


class Database:
    def __init__(self):
        self.file = Path(__file__).parent / "database.xlsx"
        
    #Retorna uma aba do Excel como DataFrame(tabela)
    def get_table(self, sheet_name: str) -> pd.DataFrame:
        
        try:
            
            return pd.read_excel(
                self.file,
                sheet_name=sheet_name
            )
            
        except Exception as erro:
             print(f"Erro ao abrir a aba '{sheet_name}'")
             print(erro)
             
             return None
         
    def get_table(self, sheet_name: str):

        try:

            return pd.read_excel(
                self.file,
                sheet_name=sheet_name
            )

        except Exception as erro:

            print(f"Erro ao abrir a aba '{sheet_name}'")

            print(erro)

            return None     
        
    def list_tables(self):
        
        excel = pd.ExcelFile(self.file)
        
        return excel.sheet_names
    
    def has_table(self, sheet_name):

        return sheet_name in self.list_tables()
    
    def get_by_id(self, sheet_name, id):
        
        tabela = self.get_table(sheet_name)
        
        resultado = tabela.loc[tabela["ID"] == id]
        
        if resultado.empty:
            return None
        
        return resultado.iloc[0]