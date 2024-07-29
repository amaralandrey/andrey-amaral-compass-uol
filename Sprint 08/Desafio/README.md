
## Desafio

Nesta sprint, tivemos o desafio de construir, com os dados da camada raw, a camada trusted do nosso datalake referente ao desafio final, com a utilização do AWS Glue.  

### Etapa 0

Na sprint 07, não consegui realizar o desafio completamente, pois eu buscava dados de bilheteria/receita, os quais a API do TMDB não disponibiliza para todos os filmes, especialmente para os filmes mais recentes. Assim, naquele momento fiz a ingestão dos 100 filmes de crime mais populares.  
 
Em razão disso, iniciei o desafio da sprint 08 redefinindo as minhas questões norteadoras para o desafio final. Agora, trabalharei com as seguintes perguntas:

"Considerando que um filme comumente se encaixa em mais de um gênero, quais os gêneros mais comumente combinados com o gênero crime? e os menos combinados? quais são as combinações com o gênero crime que tem filmes com maior popularidade? e com a menor popularidade?".  

Após, refiz a ingestão de API, utilizando a seguinte função:  

	def requisitar_filmes_tmdb(movies, page):

	    filename = f'movies_page_{page}.json'
	    
	    with open(filename, 'w', encoding='utf-8') as file:
		json.dump(movies, file, ensure_ascii=False, indent=4)
        
Utilizei um laço "for" para chamar a função por 500 vezes e assim conseguir 10.000 registros de filmes que pertençam ao gênero crime, a partir dos quais construirei minha análise. 

O código completo está no script "requisicao-tmdb.py".  

Fiz a ingestão dos dados salvos localmente para o datalake no AWS S3 em um script separado, utilizando a biblioteca OS. 

	for filename in os.listdir(diretorio_local):
	   if filename.endswith('.json'):
	       caminho_local = os.path.join(diretorio_local, filename)
		  
	       s3_key = f'{s3_caminho}{ano}/{mes}/{dia}/{filename}'
		    
	       with open(caminho_local, 'rb') as f:
		   s3_cliente.put_object(
		   Bucket=s3_bucket_nome,
		   Key=s3_key,
		   Body=f,
		   ContentType='application/json'
		   )

O código completo está no script "ingestao-s3.py".  

### Etapa 1
        
Na etapa 01, era preciso criar um job que fizesse o processamento dos dados oriundos da ingestão batch.

- Definição dos caminhos de entrada e saída:

	input_path = "s3://data-lake-andrey-amaral/Raw/Local/CSV/"
	output_path = "s3://data-lake-andrey-amaral/Trusted/"

- Extração dos dados:

	datasource0 = glueContext.create_dynamic_frame.from_options(
	    format_options={"withHeader": True},
	    connection_type="s3",
	    format="csv",
	    connection_options={"paths": [input_path]},
	    transformation_ctx="datasource0"
	)
	
- Transformação dos dados:
	applymapping1 = ApplyMapping.apply(
	    frame=datasource0, 
	    mappings=[("col1", "string", "col1", "string"), ("col2", "int", "col2", "int")],
	    transformation_ctx="applymapping1"
	)

	df = applymapping1.toDF()

	df.write.mode("append").parquet(output_path)

