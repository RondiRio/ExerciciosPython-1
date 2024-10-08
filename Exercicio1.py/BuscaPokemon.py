import pandas as pd

# Carregar o arquivo CSV
dataframe = pd.read_csv("C:\\xampp\\htdocs\\cursoBradescoPython\\Exercicio1.py\\Pokemon.csv")

# Verificar a contagem de valores nulos por coluna
nulos_por_coluna = dataframe.isnull().sum()
print("Valores nulos por coluna:")
print(nulos_por_coluna)

# Verificar se há algum valor nulo em todo o DataFrame
tem_nulos = dataframe.isnull().values.any()
print(f"Existem valores nulos no DataFrame? {'Sim' if tem_nulos else 'Não'}")

# Verificar a contagem de linhas duplicadas
linhas_duplicadas = dataframe[dataframe.duplicated()]

# Verificar e exibir as linhas duplicadas, se existirem
if not linhas_duplicadas.empty:
    print("Linhas duplicadas encontradas:")
    print(linhas_duplicadas)
else:
    print("Não há linhas duplicadas.")

#### Analisando quais tipos

contagem_type1 = dataframe['Type 1'].value_counts()
contagem_type2 = dataframe['Type 2'].value_counts()
contagem = contagem_type1
print(contagem)
contagem_total = contagem_type1.add(contagem_type2, fill_value=0)
#mais_comum = contagem_total.idxmax()
mais_comum = contagem_total.max()
print("O tipo de pokemon mais comum é: ", mais_comum)
# print(dataframe)''''''''''''''''  '''''