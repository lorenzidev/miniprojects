import pandas as pd

# Substitua 'caminho/para/seu/arquivo.xlsx' pelo caminho real do seu arquivo Excel
arquivo_excel = 'C:/Users/Victor/Desktop/python/mobile_app_python.xlsx'
#pd.set_option('display.max_columns', None)
df = pd.read_excel(arquivo_excel)
print(df)

# Contagem de valores únicos na coluna 'NomeDaColuna'
contagem = df['DISPOSITION'].value_counts()
print(contagem)
