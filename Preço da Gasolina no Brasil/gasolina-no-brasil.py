#################### Preço da Gasolina no Brasil (2004-2021) ####################

# %%
#################### Importando Bibliotecas ####################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
#################### Carregando o Dataset ####################
df = pd.read_csv('Dataset/gasolina.csv')

print(df.info())


# %%
#################### Transformando as Datas ####################

# As datas estão em formato de string, é conveniente transfomá-las em Timestamp / Datetime 
df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])


# %%
#################### Limpando a Base de Dados ####################

# Eliminando coluna "Unnamed: 0", ela não é necessária
df.drop('Unnamed: 0', axis=1, inplace=True)
df.info()

# %%
# Verificando os tipos de produtos que temos na base de dados
df['PRODUTO'].value_counts()

# %%
# Filtrando os dados para a coluna 'PRODUTO' conter só 'GASOLINA COMUM'
gasolina = df[df['PRODUTO'] == 'GASOLINA COMUM']
gasolina['PRODUTO'].value_counts()


# %%
# A Média do Preço Médio de Revenda da Gasolina na década de 2000
print('A Média do Preço Médio de Revenda da Gasolina na década de 2000: R${:.2f}' .format(gasolina[(gasolina['DATA INICIAL'].dt.year < 2009)]['PREÇO MÉDIO REVENDA'].mean()))

# %%
# A Média do Preço Máximo de Revenda da Gasolina na década de 2000
print('A Média do Preço Máximo de Revenda da Gasolina na década de 2000: R$ {:.2f}' .format(gasolina[(gasolina['DATA INICIAL'].dt.year < 2009)]['PREÇO MÁXIMO REVENDA'].mean()))

# %%
# A Média do Preço Médio de Revenda da Gasolina na década de 2010
print('A Média do Preço Médio de Revenda da Gasolina na década de 2010: R${:.2f}' .format(gasolina[(gasolina['DATA INICIAL'].dt.year >= 2010)]['PREÇO MÉDIO REVENDA'].mean()))

# %%
# A Média do Preço Máximo de Revenda da Gasolina na década de 2010
print('A Média do Preço Máximo de Revenda da Gasolina na década de 2010: R${:.2f}' .format(gasolina[(gasolina['DATA INICIAL'].dt.year >= 2010)]['PREÇO MÁXIMO REVENDA'].mean()))

# %%
# Média do Preço de Revenda da Gasolina nos Estados na Década de 2000
media_revenda2000 = gasolina[gasolina['DATA FINAL'].dt.year < 2009].groupby(['ESTADO'])['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=False)

# %%
# Média do Preço de Revenda da Gasolina nos Estados na Década de 2010
media_revenda2010 = gasolina[gasolina['DATA FINAL'].dt.year >= 2010].groupby(['ESTADO'])['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=False)


# %%
# Maior valor do preço médio de revenda
max_revenda = gasolina[['ESTADO', 'REGIÃO', 'DATA INICIAL', 'DATA FINAL', 'PREÇO MÉDIO REVENDA']].sort_values(by='PREÇO MÉDIO REVENDA', ascending=False).iloc[0]


# %%
# Preço médio de revenda nas regiões na década de 2010
regioes = gasolina[(gasolina['DATA INICIAL'].dt.year >= 2012) & (gasolina['DATA FINAL'].dt.year < 2020)].groupby('REGIÃO')['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=False)
