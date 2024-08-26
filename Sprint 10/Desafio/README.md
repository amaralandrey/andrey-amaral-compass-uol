## Desafio

Nesta sprint, tivemos o desafio de construir um dashboard com os dados da camada Refined utilizando AWS Quicksight como ferramenta de visualização de dados. 

### Etapa 0

Após receber a dica da monitora de ser melhor usar um tema específico do que um genérico para a nossa análise, decidi refinar meu tema. Dessa vez decidi focar nos filmes da franquia Batman, de 1989 a 2022, pois crime é um dos temas principais das estórias da personagem. Assim, decidi trazer as minhas perguntas definidas anteriormente para a franquia Batman:

	Qual o filme do Batman, entre 1989 e 1997, com a maior popularidade? e com a menor popularidade?  

	Qual o filme do Batman, entre 2004 e 2012, com a maior popularidade? e com a menor popularidade?  

	Qual o filme do Batman, entre 1989 e 2022, com a maior popularidade? e com a menor popularidade?  

	Quais os gêneros mais frequentemente combinados nos filmes do Batman entre 1989 e 2022? quais os menos combinados?  

	Filmes do Batman que combinam com gêneros específicos tendem a ter popularidades mais altas ou mais baixas?  

	Qual o total de bilheteria dos filmes do Batman entre 1989? Qual o mais rentável? E o menos rentável?    

Em razão disso, precisei criar um novo data lake, construir as camadas e modelar o banco de dados. Modelagem dimensional do data lake definitivo:

![Modelagem dimensional do data lake da franquia Batman](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-2.png)

### Etapa 1

Decidi começar modelando uma visualização para exibir os títulos de filmes analisados e seus respectivos anos de lançamento, usando para isso um heat map. 

![heat map](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-3.png)


Em seguida utilizei KPIs para exibir os totais de orçamento investido, receitas domésticas (EUA e Canadá), receitas internacionais e total de bilheteria mundial com exibição do porcentual de lucro em relação ao total investido. 

![kpis](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-4.png)


Após, utilizei um campo calculado para descobrir a proporção de receita total pelo valor do orçamento de cada filme.

![barras-grafico](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-5.png)

A fórmula utilizada para o campo calculado foi:  
	
 	(sum({total_revenue}) - sum(budget)) / sum(budget)


Na segunda parte do dashboard analisei a popularidade de todos filmes usando um gráfico de barras horizontais.

![barras-grafico](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-6.png)


Em seguida, analisei a popularidade dos filmes lançados no anos 1990.

![barras-grafico](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-7.png)


Fechando a análise de popularidade, comparei a nota de popularidade com o número de votos de cada filme para concluir que o número de votos não está necessariamente ligado a maior popularidade.

![barras-grafico](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-8.png)


Por fim, utilizei a nuvem de palavras para visualizar os gêneros mais recorrentes e os menos recorrentes na franquia Batman.  

![barras-grafico](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2010/Evidencias/evidencia-9.png)
