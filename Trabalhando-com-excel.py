import pandas as pd

# FIXME: Leitura dos arquivos

df1 = pd.read_excel('./datasets/Aracaju2.xlsx')
df2 = pd.read_excel('./datasets/Fortaleza.xlsx')
df3 = pd.read_excel('./datasets/Natal.xlsx')
df4 = pd.read_excel('./datasets/Recife.xlsx')
df5 = pd.read_excel('./datasets/Salvador.xlsx')

# FIXME: Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# FIXME: Retorna uma amostra do conjunto de dados
print(df.sample(5))

# FIXME: Retorna os tipos de dados de cada coluna
print('\n\tTipos de cada coluna\n')
print(df.dtypes)

# FIXME: Mudando o tipo de uma coluna
df['LojaID'] = df['LojaID'].astype('object')
print('\n\tTipo da coluna LojaID alterado de int64 para object\n')
print(df.dtypes)

# FIXME: Verificando se existe valores faltando/nulos
print('\n\tVerificando valores faltantes ou nulos\n')
print(df.isnull().sum())

# FIXME: Substituindo os valores nulos por 0
df["Vendas"].fillna(0, inplace=True)

# FIXME: Apagando as linhas que estão com o valor nulo
# df.dropna(inplace=True)

# FIXME: Busca os dados que foram substituidos por 0
print('\n\tBusca os dados que tiveram o valor alterado por 0\n')
print(df.loc[df["Vendas"] == 0])

# FIXME: Verificando se existe valores faltando/nulos
print('\n\tVerificando valores faltantes ou nulos\n')
print(df.isnull().sum())

# FIXME: Apagando as linhas com valores nulos na coluna especifica
df.dropna(subset=['Vendas'], inplace=True)

# FIXME: Removendo linhas com valores faltantes em todas as colunas
df.dropna(how='all', inplace=True)

# FIXME: Somando todas as vendas de cada cidade
print('\n\tSomando todas as vendas de cada cidade\n')
print(df.groupby('Cidade')['Vendas'].sum())

## TODO: Criando novas colunas

# FIXME: Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])

# FIXME: Retorna as linhas iniciais com a coluna receita adicionada
print('\n\tRetorna as linhas iniciais com a coluna receita adicionada\n')
print(df.head())

# FIXME: Criando uma coluna para pegar a quantidade de produtos da venda
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# FIXME: Retorna as linhas iniciais com a coluna receita/vendas adicionada
print('\n\tRetorna as linhas iniciais com a coluna receita/vendas adicionada\n')
print(df.head())

# FIXME: Retornando a maior receita
print("\n\tRetornando a maior receita\n")
print(df["Receita"].max())

# FIXME: Retornando a menor receita
print("\n\tRetornando a menor receita\n")
print(df["Receita"].min())

# FIXME: nlargest
print('\n\tRetorna as 3 maiores receitas da base de dados\n')
print(df.nlargest(3, "Receita"))

# FIXME: nsamllest
print('\n\tRetorna as 3 menores receitas da base de dados\n')
print(df.nsmallest(3, "Receita"))

# FIXME: Agrupamento por cidade
print('\n\tRetorna o valor da soma de todas as receitas de cada cidade\n')
print(df.groupby("Cidade")["Receita"].sum())

# FIXME: Ordenando o conjunto de dados
print('\n\tRetorna as 10 primeiras vendas com as receitas ordenadas da maior para a menor\n')
print(df.sort_values("Receita", ascending=False).head(10))


## TODO: Trabalhando com datas

# FIXME: Transformando a coluna de data em tipo inteiro
df['Data'] = df['Data'].astype('int64')

# FIXME: Verificando o tipo de dado de cada coluna
print('\n\tVerificando o tipo de dado de cada coluna\n')
print(df.dtypes)

# FIXME: Transformando a colunda de data em data
df['Data'] = pd.to_datetime(df['Data'])

# FIXME: Verificando o tipo de dado de cada coluna
print('\n\tVerificando o tipo de dado de cada coluna\n')
print(df.dtypes)

# FIXME: Agrupamento por ano
print('\n\tAgrupamento por ano\n')
print(df.groupby(df['Data'].dt.year)['Receita'].sum())

# FIXME: Criando uma nova coluna com o ano
print('\n\tCriando uma nova coluna com o ano\n')
df['Ano_Venda'] = df["Data"].dt.year

# FIXME: Retorna 5 amostras
print('\n\tRetorna 5 amostras\n')
print(df.sample(5))

# FIXME: Extraindo o mês e o dia
print('\n\tExtraindo o mês e o dia\n')
df['Mes_Venda'], df['Dia_Venda'] = (df['Data'].dt.month, df['Data'].dt.day)

# FIXME: Retorna 5 amostras
print('\n\tRetorna 5 amostras\n')
print(df.sample(5))

# FIXME: Retornando a data mais antiga
print('\n\tRetornando a data mais antiga\n')
print(df['Data'].min())

# FIXME: Calculando a diferença de dia
print('\n\tCalculando a diferença de dia\n')
df['Diferenca_Dias'] = df['Data'] - df['Data'].min()

# FIXME: Retorna 5 amostras
print('\n\tRetorna 5 amostras\n')
print(df.sample(5))

# FIXME: Criando a coluna de trimestre
df['Trimestre_Venda'] = df['Data'].dt.quarter

# FIXME: Retorna 5 amostras
print('\n\tRetorna 5 amostras\n')
print(df.sample(5))

# FIXME: Filtrando as vendas de 2019 do mês de março
print('\n\tFiltrando as vendas de 2019 do mês de março\n')
vendas_marco_2019 = df.loc[(df['Data'].dt.year == 2019) & (df['Data'].dt.month == 3)]

# FIXME: Retornando as vendas em março de 2019
print('\n\tRetornando as vendas em março de 2019\n')
print(vendas_marco_2019)





