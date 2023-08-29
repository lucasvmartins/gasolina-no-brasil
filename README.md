# Preço da Gasolina no Brasil de 2004 - 2020

Link para Download do _Dataset:_ https://www.kaggle.com/datasets/matheusfreitag/gas-prices-in-brazil

Este é um código Python que demonstra a análise do preço da gasolina no Brasil entre os anos de 2004 e 2021. O código utiliza a biblioteca Pandas para manipulação de dados e a biblioteca Matplotlib para visualizações gráficas. Considere no projeto em que, toda vez que falado na década de 2000 ela é iniciada na análise no ano de 2004.
##
O código está dividido em várias seções, cada uma realizando uma etapa específica da análise:

1. **Importando Bibliotecas:** Nesta seção, são importadas as bibliotecas necessárias: Pandas para manipulação de dados e Matplotlib para visualizações gráficas.
2. **Carregando o Dataset:** Aqui, o código lê um arquivo CSV contendo os dados do preço da gasolina no Brasil. O método .info() é usado para mostrar informações sobre o DataFrame carregado.
3. **Transformando as Datas:** As colunas de datas são convertidas do formato _string_ para o formato de data usando a função pd.to_datetime().
4. **Limpando a Base de Dados:** A coluna "Unnamed: 0" é eliminada do DataFrame usando o método .drop().
5. **Filtrando os Dados:** Os dados são filtrados para incluir apenas o item "GASOLINA COMUM" na coluna "PRODUTO".
6. **Análise dos Preços na Década de 2000:** O código calcula a média dos preços médios e máximos de revenda da gasolina na década de 2000.
7. **Análise dos Preços na Década de 2010:** O código calcula a média dos preços médios e máximos de revenda da gasolina na década de 2010.
8. **Agrupamento por Estados:** O código cria um dicionário para mapear estados para suas siglas, depois analisa as maiores e menores médias de preço de revenda nos estados durante as décadas de 2000 e 2010.
9. **Maior Valor do Preço de Revenda:** O código identifica o registro com o maior preço médio de revenda de gasolina.
10. **Análise por Regiões:** O código calcula a média dos preços médios de revenda da gasolina por região na década de 2010 e cria um gráfico de barras para visualização.
11. **Preço Médio da Gasolina no Brasil:** O código calcula o preço médio mensal da gasolina no Brasil na década de 2010 e cria um gráfico de linha para visualização.
##
Este é um exemplo de análise de dados exploratória usando Python, Pandas e Matplotlib para examinar o preço da gasolina no Brasil ao longo de um período de tempo específico.
