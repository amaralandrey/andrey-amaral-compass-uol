## Desafio

Nesta sprint, o desafio teve como objetivo a ingestão de dados em um bucket S3 da AWS, utilizando Boto3 e Docker. O desafio tinha três etapas.

### Etapa 01

Na primeira etapa, precisavamos construir um script python para ler dois arquivos CSV e realizar a carga desses dados em um bucket S3 da AWS.

Foi pedido pelo monitor para que o bucket fosse criado pelo script.

    cliente.create_bucket(Bucket='data-lake-andrey-amaral')

Para a leitura dos arquivos, foi preciso utilizar padrão do Docker para o caminho, já que a execução deveria ocorrer no container.

    caminho_movies = '/app/movies.csv'
    caminho_series = '/app/series.csv'
    
    
    with open(caminho_movies, 'rb') as arquivo_movies:
        conteudo_movies = arquivo_movies.read()
    
    with open(caminho_series, 'rb') as arquivo_series:
        conteudo_series = arquivo_series.read()

Para gravar o bucket a definição raw zone, foi utilizado a biblioteca datetime para pegar a data atual e formatar a key de cada objeto. 

    data_atual = datetime.now()
    ano = data_atual.year
    mes = data_atual.month
    dia = data_atual.day
    
    movies_key = f'Raw/Local/CSV/Movies/{ano}/{mes:02d}/{dia:02d}/movies.csv'
    series_key = f'Raw/Local/CSV/Series/{ano}/{mes:02d}/{dia:02d}/series.csv'

A carga dos dados foi feita com o método put_object().

    cliente.put_object(Bucket=nome_bucket, Key=movies_key, Body=conteudo_movies)
    cliente.put_object(Bucket=nome_bucket, Key=series_key, Body=conteudo_series)

### Etapa 02

Na etapa 02, era precisar criar um container Docker para executar o script criado anteriormente.

    FROM python:3.10
    
    WORKDIR /app
    
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    COPY movies.csv /app/movies.csv
    
    COPY series.csv /app/series.csv
    
    COPY ingestao_batch_s3.py .
    
    CMD ["python", "ingestao_batch_s3.py"]

A instalação do boto3 no container foi realizada com a utilização de um documento de requisitos (requirements.txt, no diretório Desafio).

### Etapa 03

A etapa 03 consistia na construção e execução local do container. 

![Texto alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2006/Evidencias/evidencia-1.png)

Bucket construído.

![Texto alternativo](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2006/Evidencias/evidencia-2.png)
