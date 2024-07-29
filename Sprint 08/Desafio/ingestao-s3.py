import boto3
import os
from datetime import datetime


s3_bucket_nome = 'data-lake-andrey-amaral'
s3_caminho = 'Raw/TMDB/JSON/'  # Camada para a ingestão dos dados coletados

s3_cliente = boto3.client('s3',
    aws_access_key_id='key',
    aws_secret_access_key='key',
    aws_session_token='token'
)

# Parâmetros de data para a formação das camadas conforme o momento da execução
data_atual = datetime.now()
ano = data_atual.year
mes = data_atual.month
dia = data_atual.day

# Diretório local onde os arquivos JSON estão armazenados
diretorio_local = f'/home/nome/Documents/Compass-UOL'


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
           
       print(f'Arquivo {filename} enviado para {s3_key}')



