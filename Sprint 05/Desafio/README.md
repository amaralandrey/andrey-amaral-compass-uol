
## Desafio

O objetivo do desafio era a prática de consultas SQL no ambiente da AWS.  
Quanto ao problema a ser resolvido, era a realização de vários tipos de consultas em um objeto no S3.  
Ao todo, incluindo a entrega, o desafio tinha seis etapas.

#### Etapa 01

O governo brasileiro protege as áreas naturais por meio de Unidades de Conservação (UC) - estratégia extremamente eficaz para a manutenção dos recursos naturais em longo prazo. Para atingir esse objetivo de forma efetiva e eficiente, foi instituído o Sistema Nacional de Conservação da Natureza (SNUC), com a promulgação da Lei nº 9.985, de 18 de julho de 2000. A Lei do SNUC representou grandes avanços à criação e gestão das UC nas três esferas de governo (federal, estadual e municipal), pois ele possibilita uma visão de conjunto das áreas naturais a serem preservadas. Além disso, estabeleceu mecanismos que regulamentam a participação da sociedade na gestão das UC, potencializando a relação entre o Estado, os cidadãos e o meio ambiente.

O conjunto de dados que escolhi para o desafio foi a lista das UCs ativas no CNUC até o primeiro semestre de 2024, com respectivas categorias de manejo, área, esfera de governo e ano de criação.

#### Etapa 02

Iniciei a análise e tratamento da tabela removendo a coluna Informações Gerais, pois ela não continha nenhum valor.  

Em seguida coloquei em letras minúsculas todos identificadores das colunas, substituí os espaços por um sublinhado e removi os acentos para facilitar a referência nas consultas SQL, processo esse que fiz manualmente, pois o excesso de "bad lines" me impediu de usar a biblioteca Pandas no Python.  

Por fim, decidi remover colunas que não estavam descritas no dicionário de dados disponível junto com a tabela, pois eu não teria base para trabalhar aqueles dados, além de que essa remoção resolveria uma parte significativa das "bad lines" que encontrei anteriormente.  

Após todo esse tratamento, criei uma cópia da tabela original a qual sinalizei com a flag [tratada].  

#### Etapas 03 e 04

Nas etapas 03 e 04, subi a tabela tratada para um bucket chamado desafio-andrey e decidi realizar as consultas SQL diretamente no console AWS.  

#### Etapa 05  

Criei duas queries.  

Na primeira query, utilizei os operadores lógicos AND e OR para encontrar as unidades de conservação da categoria Parque que sejam localizados no estado do Pará ou no Maranhão. A consulta entrega os nomes desses parques.  

Cada unidade de conservação tem dois identificadores na tabela, um ID e um código, sendo que o código é um tipo textual no padrão 0000.00.0000. Eu utilizei a função SUBSTRING para extrair os quatro últimos números dessa string. OBS: o json com o resultado da consulta baixado direto do ambiente da AWS apresenta inconsistências no resultado dessa parte da query, mas no output do console o resultado aparece corretamente, conforme print na pasta evidências.  

Na tabela analisada, o campo categoria_iucn tem a palavra category seguido do número da categoria em números romanos, eu utilizei a SUBSTRING para exibir apenas os números. 

	SELECT  
		nome_da_uc, 
		CAST(SUBSTRING(codigo_uc, 9) AS FLOAT) AS cod_uc_normalizado,
		SUBSTRING(categoria_iucn, 10) AS categoria_normalizada 
		FROM s3object 
	WHERE categoria_de_manejo = 'Parque' AND (uf = 'PA' OR uf = 'MA')

	{"nome_da_uc":"PARQUE NACIONAL DA SERRA DO PARDO","cod_uc_normalizado":151e0,"categoria_normalizada":"II"}
	{"nome_da_uc":"PARQUE NACIONAL DOS LENÇÓIS MARANHENSES","cod_uc_normalizado":180e0,"categoria_normalizada":"II"}

Em resumo, nessa consulta consegui reunir dois operadores lógicos (AND e OR), uma função condicional (WHERE) e uma função de string (SUBSTRING).  

Na segunda query, utilizei SUM para contar o total de parques no estado do Pará e o total de parques no Maranhão, utilizando o CASE WHEN para verificar a condição.

	SELECT 
		SUM(CASE WHEN categoria_de_manejo = 'Parque' AND uf = 'PA' THEN 1 ELSE 0 END) 			 
		AS total_parques_pa, 
		SUM(CASE WHEN categoria_de_manejo = 'Parque' AND uf = 'MA' THEN 1 ELSE 0 END) 
		AS total_parques_ma
	FROM s3object; 
	
	{"total_parques_pa":13,"total_parques_ma":9}
	
Em resumo, consegui reunir nessa query uma função de agregação (SUM) e uma função condicional (CASE WHEN).  

Não consegui aplicar nenhuma função de data no meu conjunto, pois as funções são muito rígidas quanto aos dados que podem ser tratados com essas funções e na minha tabela não havia datas ou strings no padrão aceito pelas funções de data do S3 Select.  


