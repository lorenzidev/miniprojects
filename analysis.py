import pandas as pd

# Substitua 'caminho/para/seu/arquivo.xlsx' pelo caminho real do seu arquivo Excel
arquivo_excel = 'C:/Users/Victor/Desktop/python/data for january.xlsx'

df = pd.read_excel(arquivo_excel)

# Descomente se quiser ver o DataFrame completo no console
# pd.set_option('display.max_columns', None)

# Calcula a porcentagem de cada valor único na coluna 'General.Authenticated' e multiplica por 100 para obter a porcentagem
general_authenticated = df['General.Authenticated'].value_counts(normalize=True) * 100
#general_process = df['General.Process'].value_counts(normalize=True) * 100

# Itera sobre a série de porcentagens para imprimir cada valor único e sua porcentagem correspondente
for resultado, porcentagem in general_authenticated.items():
    print(f"{resultado}: {porcentagem:.2f}%")