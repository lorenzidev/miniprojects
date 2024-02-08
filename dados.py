import pandas as pd

# Importar o arquivo de leitura em csv

copel_df = pd.read_csv('CPLE6.csv')

copel_resumo = copel_df[['DATA','FECHAMENTO']].copy()

copel_resumo.columns = ['Data', 'Fechamento']

copel_resumo['Fechamento'] = copel_resumo['Fechamento'].str.replace(',', '.').astype(float)

print(copel_resumo)

# Exportar para um novo arquivo

copel_resumo.to_csv('COPEL.csv', index=False)

preco_medio = copel_resumo['Fechamento'].mean()

print(f'O valor medio da acao da COPEL eh de: R$ {preco_medio:.2f}')