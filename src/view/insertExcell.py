import pandas as pd
import re
import unidecode
from src.controller.relatorio import RelatorioController, Relatorio


def insert_from_excell(path):

    df = pd.read_excel(path)

    def clean_column_name(name):
        name = unidecode.unidecode(name)  # Remove acentos
        name = re.sub(r'\s+', '_', name)  # Substitui espaços por underlines
        name = re.sub(r'[^\w\s]', '', name)  # Remove caracteres especiais
        return name

    df.columns = [clean_column_name(col.lower()) for col in df.columns] # removendo espaço
    df = df.fillna("")
    rows = df.shape[0]
    relatories = []
    err = False
    for i in range(rows - 1):
        row = df.iloc[i]
        row_dict = row.to_dict()
        try:
            relatories.append(Relatorio.fill(row_dict))
        except Exception as e:
            print(f'erro na linha {i} : {str(e)}')
            print(row_dict)
            err = True
    if not err:
        RelatorioController.create_relatories(relatories)
