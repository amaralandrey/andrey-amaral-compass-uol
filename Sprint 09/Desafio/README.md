## Desafio

Nesta sprint, tivemos o desafio de construir, com os dados da camada Trusted, a camada Refined do nosso datalake referente ao desafio final, com a utilização do AWS Glue e Spark. O desafio era formado por duas etapas.


### Etapa 01

Na primeira etapa, precisavamos criar a modelagem dimensional (modelo de dados) da camada Refined, considerando nossas questões definidas e os dados ingeridos anteriormente.  

Inicialmente, considerando as minhas questões e as duas fontes de dados que nos foram dadas, além de adicionar questões novas por orientação do monitor, modelei o seguinte esqueme dimensional:  


Contudo, ao seguir para a etapa 02, eu não consegui realizar o processamento de dados de duas fontes diferentes, pois o Spark espera que todos os dados lidos em um script sejam consistentes em colunas, o que não ocorre com os dados que nos foram passados e os dados que são extraídos da API do TMDB. E eu não consegui solucionar esse problema a tempo.    

Colunas do CSV:  
id|tituloPincipal|tituloOriginal|anoLancamento|tempoMinutos|genero|notaMedia|numeroVotos|generoArtista|personagem|nomeArtista|anoNascimento|anoFalecimento|profissao|titulosMaisConhecidos  

Colunas do JSON extraído do TMDB:  
 {
        "adult": false,
        "backdrop_path": "/3jlYVxDpPZg7s8Vn61OfKzlBS8r.jpg",
        "genre_ids": [
            80,
            18
        ],
        "id": 15322,
        "original_language": "en",
        "original_title": "I.D.",
        "overview": "Four policemen go undercover and infiltrate a gang of football hooligans hoping to route out their leaders. For one of the four, the line between 'job' and 'yob' becomes more unclear as time passes . . .",
        "popularity": 15.965,
        "poster_path": "/hcDZx4VTA9QzquHvWOdoOSeSB2t.jpg",
        "release_date": "1995-05-05",
        "title": "I.D.",
        "video": false,
        "vote_average": 6.597,
        "vote_count": 88
    }
 
Assim, para conseguir realizar a entrega desta sprint, eu desconsiderei as questões novas criadas nesta sprint e trabalhei apenas com as questões criadas anteriormente. Então, cheguei ao seguinte modelo de dados:  


Após isso, criei o banco de dados e as tabelas no Glue Data Catalog.  

database_name = 'db_data-lake-andrey-amaral-1.1'

glue_cliente.create_database(
        DatabaseInput={
            'Name': database_name,
            'Description': 'Banco de dados para armazenar as tabelas refinadas do data lake.',
        }
    )

glue_cliente.create_table(
    DatabaseName=database_name,
    TableInput={
        'Name': 'fato_filme',
        'StorageDescriptor': {
            'Columns': [
                {'Name': 'id_filme', 'Type': 'int'},
                {'Name': 'titulo_original', 'Type': 'string'},
                {'Name': 'id_combinacao_generos', 'Type': 'int'},
                {'Name': 'popularidade', 'Type': 'float'},
                {'Name': 'lancamento', 'Type': 'string'}
            ],
            'InputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
            'OutputFormat': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
            'Compressed': False
        },
        'TableType': 'EXTERNAL_TABLE'
    }
)


### Etapa 02

Na etapa 02, era preciso processar os dados da Trusted para a Refined usando AWS Glue e Spark.  

Eu optei por utilizar um job para cada tabela.  

- Tabela 01 - fato_filme:  

df_fato_filme = df_movies.select(
    col("id").alias("id_filme"),
    col("original_title").alias("titulo_original"),
    col("genre_ids").alias("combinacao_generos"),
    col("popularity").alias("popularidade"),
    col("release_date").alias("lancamento")
).distinct()

- Tabela 02 - dim_genero:  

df_dim_genero = df_movies.select(
    col("genero_exploded").alias("id_genero")
).distinct()

- Tabela 03 - dim_combinacao_generos:  

df_dim_combinacao_generos = df_movies.select(
    col("id_combinacao_generos"),
    col("id_genero")
).distinct()

