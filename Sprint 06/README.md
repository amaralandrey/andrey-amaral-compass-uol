
## Desafio

Nesta sprint, o desafio teve como objetivo a ingestão de dados em um bucket S3 da AWS, utilizando Boto3 e Docker. O desafio tinha três etapas, que estão documentadas no diretório Desafio.

## Evidências 

- Evidência 01: construção da imagem e execução do container localmente.
![Texto alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2006/Evidencias/evidencia-1.png)

- Evidência 02 a 08: estrutura do bucket com a definição RAW zone.
  
  ## Exercícios
  
  - Lab 01: configuração do bucket para hospedagem de site estático.
  ![Texto alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2006/Exercicios/Lab01/etapa-6.png)
  
  - Lab 02: consulta SQL em objeto no S3 AWS utilizando Athena.
  
      WITH rank_nomes AS (
      	SELECT
          	nome,
          	ano,
          	ROW_NUMBER() OVER(PARTITION BY ano / 10 ORDER BY total DESC) as rank
      	FROM
          	meubanco.minhatabela
      	WHERE
          	ano >= 1950
      )
      
      SELECT
      	ano / 10 * 10 AS decada,
      	nome,
      	rank
      FROM
      	rank_nomes
      WHERE
      	rank <= 3
      ORDER BY
      	decada ASC,
      	rank ASC;

![Texto alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2006/Exercicios/Lab02/etapa-5.png)

## Certificados

Foram realizados nove cursos na plataforma Skill Builder, todos os certificados estão no diretório Certificados. 


