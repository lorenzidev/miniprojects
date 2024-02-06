import pandas as pd

arquivo_excel = 'C:/Users/Victor/Desktop/python/data_for_january.xlsx'
df = pd.read_excel(arquivo_excel)

# Agrupa pelo nome da campanha primeiro e depois itera sobre cada grupo
for nome_campanha, grupo_campanha in df.groupby('CAMPAIGN'):
    print(f"CAMPAIGN: {nome_campanha}")
    
    # Calcula a porcentagem para 'Confirmed' e 'Failed' dentro do grupo atual
    porcentagens = grupo_campanha['General.Authenticated'].value_counts(normalize=True) * 100
    contagem_real = grupo_campanha['General.Authenticated'].value_counts()

    # Imprime as porcentagens formatadas
    for resultado, porcentagem in porcentagens.items():
        print(f"{resultado}: {porcentagem:.2f}%    ({contagem_real[resultado]})")

    # Espaço extra para separar as campanhas na saída
    print()