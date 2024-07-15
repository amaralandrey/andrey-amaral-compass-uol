import requests
import json
import boto3
from datetime import datetime


api_key = 'key'
base_url = 'https://api.themoviedb.org/3/discover/movie'

parametros = {
    'api_key': api_key,
    'with_genres': '80',  
    'sort_by': 'popularity.desc',  
    'page': 1  
}


s3_bucket_nome = 'data-lake-andrey-amaral'
s3_caminho = 'Raw/TMDB/JSON/'


s3_cliente = boto3.client('s3',
    aws_access_key_id='key',
    aws_secret_access_key='key',
    aws_session_token = 'token'
)

data_atual = datetime.now()
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

def ingestao_api_tmdb_to_s3(movies, page):
    
    filename = f'movies_page_{page}.json'
    json_data = json.dumps(movies, ensure_ascii=False, indent=4)
    
    
    s3_key = f'{s3_caminho}{ano}/{mes}/{dia}/{filename}'
    
    s3_cliente.put_object(
        Bucket=s3_bucket_nome,
        Key=s3_key,
        Body=json_data,
        ContentType='application/json'
    )
    print(f'Salvo {len(movies)} filmes em {s3_key}')

for page in range(1, 6):
    parametros['page'] = page
    response = requests.get(base_url, params=parametros)
    
    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        ingestao_api_tmdb_to_s3(movies, page)
    else:
        print(f'Erro na requisição da página {page}: {response.status_code}')
