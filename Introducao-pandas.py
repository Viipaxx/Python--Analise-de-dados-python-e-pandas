
import pandas as pd

# FIXME: Pega o arquivo
df = pd.read_csv("./datasets/Gapminder.csv", on_bad_lines="skip", sep=";")

print(df.head())

# FIXME: Renomeia as colunas
df = df.rename(columns={"country": "Pais", "continent": "Continente", "year": "Ano", "lifeExp": "Expectativa de vida", "pop": "Pop total", "gdpPercap": "PIB"})

# FIXME:  Retorna as primeiras linhas
print('\n\tPrimeiras linhas:\n')
print(df.head(10))

# FIXME: Total de linhas e colunas
print('\n\tTotal de linhas e colunas:\n')
print(df.shape)

# FIXME: Total de colunas
print('\n\tTotal de colunas:\n')
print(df.columns)

# FIXME: Tipo de dados em cada coluna
print('\n\tTotal de linhas:\n')
print(df.dtypes)

# FIXME: Retorna as últimas linhas
print('\n\tÚltimas linhas:\n')
print(df.tail(15))

# FIXME: Retorna informações estatísticas do conjunto de dados
print('\n\tInformações estatísticas:\n')
print(df.describe())

# FIXME: Retorna todos os continentes do conjunto de dados
print('\n\tRetorna todos os continentes:\n')
print(df['Continente'].unique())

# FIXME: Pega todos os dados em que o continente é Oceania e adiciona a variavel oceania
print('\n\tPega todos os dados do continente especifico:\n')
oceania = df.loc[df['Continente'] == 'Oceania']

# FIXME: Retorna as primeiras linhas do continente
print(oceania.head())

# FIXME: Agrupamento de dados
print('\n\tRetorna os valores diferentes da coluna continente:\n')
print(df.groupby('Continente')['Pais'].nunique())

# FIXME: Agrupa a media de expectativa de vida por ano
print('\n\tRetorna a média da expectativa de vida agrupando por ano:\n')
print(df.groupby('Ano')['Expectativa de vida'].mean())

# FIXME: Pega a média da coluna PIB
print('\n\tRetorna a média da coluna:\n')
print(df["PIB"].mean())

# FIXME: Soma todos os valores da coluna PIB
print('\n\tSoma todos os valores da coluna:\n')
print(df["PIB"].sum())