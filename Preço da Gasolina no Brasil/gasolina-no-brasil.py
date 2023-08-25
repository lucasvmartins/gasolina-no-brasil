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
# Criando um dicionário de cada estado com suas respectivas siglas
mapa_estados = {
    'ACRE': 'AC', 'ALAGOAS': 'AL', 'AMAPA': 'AP', 'AMAZONAS': 'AM',
    'BAHIA': 'BA', 'CEARA': 'CE', 'DISTRITO FEDERAL': 'DF',
    'ESPIRITO SANTO': 'ES', 'GOIAS': 'GO', 'MARANHAO': 'MA',
    'MATO GROSSO': 'MT', 'MATO GROSSO DO SUL': 'MS',
    'MINAS GERAIS': 'MG', 'PARA': 'PA', 'PARAIBA': 'PB',
    'PARANA': 'PR', 'PERNAMBUCO': 'PE', 'PIAUI': 'PI',
    'RIO DE JANEIRO': 'RJ', 'RIO GRANDE DO NORTE': 'RN',
    'RIO GRANDE DO SUL': 'RS', 'RONDONIA': 'RO', 'RORAIMA': 'RR',
    'SANTA CATARINA': 'SC', 'SAO PAULO': 'SP', 'SERGIPE': 'SE',
    'TOCANTINS': 'TO'
}

# %%
# Maiores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2000
maiormedia_revenda2000 = gasolina[gasolina['DATA FINAL'].dt.year < 2010].groupby(['ESTADO'])['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=False).head(10).to_frame().reset_index()

maiormedia_revenda2000['ESTADO'] = maiormedia_revenda2000['ESTADO'].map(mapa_estados)

plt.bar(maiormedia_revenda2000['ESTADO'], maiormedia_revenda2000['PREÇO MÉDIO REVENDA'])

plt.ylim(2.5, 2.9)
plt.xlabel('Estados')
plt.ylabel('Preço Médio de Revenda')
plt.title('Maiores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2000')


# %%
# Maiores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2010
maiormedia_revenda2010 = gasolina[gasolina['DATA INICIAL'].dt.year >= 2010].groupby(['ESTADO'])['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=False).head(10).to_frame().reset_index()

maiormedia_revenda2010['ESTADO'] = maiormedia_revenda2010['ESTADO'].map(mapa_estados)

plt.bar(maiormedia_revenda2010['ESTADO'], maiormedia_revenda2010['PREÇO MÉDIO REVENDA'])

plt.ylim(3.5, 4)
plt.xlabel('Estados')
plt.ylabel('Preço Médio de Revenda')
plt.title('Maiores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2010')


# %%
# Menores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2000
menormedia_revenda2000 = gasolina[gasolina['DATA FINAL'].dt.year < 2010].groupby(['ESTADO'])['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=True).head(10).to_frame().reset_index()

menormedia_revenda2000['ESTADO'] = menormedia_revenda2000['ESTADO'].map(mapa_estados)

plt.bar(menormedia_revenda2000['ESTADO'], menormedia_revenda2000['PREÇO MÉDIO REVENDA'])

plt.ylim(2.3, 2.55)
plt.xlabel('Estados')
plt.ylabel('Preço Médio de Revenda')
plt.title('Menores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2000')


# %%
# Menores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2010
menormedia_revenda2010 = gasolina[gasolina['DATA FINAL'].dt.year >= 2010].groupby(['ESTADO'])['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=True).head(10).to_frame().reset_index()

menormedia_revenda2010['ESTADO'] = menormedia_revenda2010['ESTADO'].map(mapa_estados)

plt.bar(menormedia_revenda2010['ESTADO'], menormedia_revenda2010['PREÇO MÉDIO REVENDA'])

plt.ylim(3.25, 3.5)
plt.xlabel('Estados')
plt.ylabel('Preço Médio de Revenda')
plt.title('Menores Médias do Preço de Revenda da Gasolina nos Estados na Década de 2010')


# %%
# Maior valor do preço médio de revenda
max_revenda = gasolina[['ESTADO', 'REGIÃO', 'DATA INICIAL', 'DATA FINAL', 'PREÇO MÉDIO REVENDA']].sort_values(by='PREÇO MÉDIO REVENDA', ascending=False).iloc[0]

print(max_revenda)

# %%
# Preço médio de revenda nas regiões na década de 2010
regioes = gasolina[(gasolina['DATA INICIAL'].dt.year >= 2012) & (gasolina['DATA FINAL'].dt.year < 2020)].groupby('REGIÃO')['PREÇO MÉDIO REVENDA'].mean().sort_values(ascending=False).to_frame().reset_index()

plt.bar(regioes['REGIÃO'], regioes['PREÇO MÉDIO REVENDA'])

plt.ylim(3.2, 3.8)
plt.xlabel('Regiões')
plt.ylabel('Preço Médio de Revenda')
plt.title('Preço médio de revenda nas regiões na década de 2010')

# %%
# Preço Médio da Gasolina no Brasil na década de 2010 (Gráfico de Linha)

 
