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

Em razão disso, precisei criar um novo data lake, construir as camadas e modelar o banco de dados.

![Modelagem dimensional do data lake da franquia Batman](caminho/para/imagem.extensao)

### Etapa 1

Como forma de tentar gerar uma narrativa, eu decidi começar modelando visualizações sobre o desempenho de bilheteria da franquia.




