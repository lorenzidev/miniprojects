import pandas as pd

# Substitua pelo caminho real do seu arquivo Excel
arquivo_excel = 'C:/Users/Victor/Desktop/python/data_for_january_sample.xlsx'
df = pd.read_excel(arquivo_excel)

# Agrupa pelo nome da campanha primeiro e depois itera sobre cada grupo
for reason, general_reason in df.groupby('General.Reason'):
    print(f" {reason}")

    contagens_reais = general_reason['SKILL'].value_counts()

    # Calcula a porcentagem para 'Confirmed' e 'Failed' dentro do grupo atual
    porcentagens = general_reason['SKILL'].value_counts(normalize=True) * 100
    
    # Imprime as porcentagens formatadas
    for resultado, porcentagem in porcentagens.items():
        # Certifique-se de que 'resultado' exista em 'contagens_reais' antes de tentar acessá-lo
        contagem_real = contagens_reais.get(resultado, 0)  # Usa 0 como valor padrão se 'resultado' não existir
        print(f"{resultado}: {porcentagem:.2f}%    ({contagem_real})")
    
    # Espaço extra para separar as campanhas na saída
    print(" ")
