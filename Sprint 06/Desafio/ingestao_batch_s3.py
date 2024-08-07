
import boto3
from datetime import datetime


cliente = boto3.client('s3',  
    aws_access_key_id='key',
    aws_secret_access_key='key',
    aws_session_token = 'token')

cliente.create_bucket(Bucket='data-lake-andrey-amaral')

nome_bucket = 'data-lake-andrey-amaral'

caminho_movies = '/app/movies.csv'
caminho_series = '/app/series.csv'


with open(caminho_movies, 'rb') as arquivo_movies:
    conteudo_movies = arquivo_movies.read()

with open(caminho_series, 'rb') as arquivo_series:
    conteudo_series = arquivo_series.read()


data_atual = datetime.now()
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

movies_key = f'Raw/Local/CSV/Movies/{ano}/{mes:02d}/{dia:02d}/movies.csv'
series_key = f'Raw/Local/CSV/Series/{ano}/{mes:02d}/{dia:02d}/series.csv'

cliente.put_object(Bucket=nome_bucket, Key=movies_key, Body=conteudo_movies)
cliente.put_object(Bucket=nome_bucket, Key=series_key, Body=conteudo_series)


