
import boto3
from datetime import datetime


cliente = boto3.client('s3',  
    aws_access_key_id='ASIAZQ3DQ2REDVPUNFUI',
    aws_secret_access_key='VdLFQniSgPGffukeMmQPXAu/AVgU+z13HjPFyc6z',
    aws_session_token = 'IQoJb3JpZ2luX2VjEKP//////////wEaCXVzLWVhc3QtMSJHMEUCID8EcWsWYFf/YyXJGL4J++IILV4CSAleTDt4hmNnUpGDAiEAjXkHdJWu5M7xlc7U8OQkx1nv55UgQ7Y9KprNy6VWkRwqoQMIXBAAGgw2NTQ2NTQzNjI2OTYiDFYN5cBTLvWEOIeSvCr+AhN6yXmK07/AX+rB6EKWiXaxPDKjjqUqBXYH+D19TmKM9lpzIXS1b668fr9zd2J3ZfEIx14BzSRMEpTS3oUgUwhwq8be7HhwfY0nWyUxgnzukcMHA57cdL5uf8su9DHkfC3Kg/wZmMAffYDgWDvBZO1928HiEYli9oueNr4PsTahrHyXhB/ZWB2nG49Uwa324oCsogQJ0vfoMAdjVuFAx9yfCGZBTQ7uB+5j1sRlcn7vqBNDePHY2iSJcD7C4fX2RBE5RwhKz371gEGGNljaBTlOpwbw+72nxL1L995BZdZEyO9LEex/hNBW814hsn6bBW6ncdkxSiz1uUhnyJ2XhjFW78bCD0KcYartUi1IMfXGDxPAdvD8VNiaMJaftd0KDBNyJUz7ghEP8PhbDoJQOVG1zKT9iMjJHQl9NTd1gv+/VK2I8jOZtWH40AqNPWKMq8r6fRBqWVF/d4/Jxm9hapkiGMDHs/qZJ7rLuUEdOmmqWjLZxU3UlZSPFEKEXYgw+JaKtAY6pgGf64iAfojk+65Z9bumE8h1LEzYnZeM8yrQXSOC+AMN1ys5iIVhrmuG85MDpd+DdrXGBm297vmNmd1XMc2BpvUr9BusJEL3wDkUIILdXitI+BkgVrwI63ALpxAdv2hBmTOxDvy8A03jX/rDtQDz60rznqoqc2cRqf6kM8VNPhgpJzbycn2KGAjXwkf5wWos6akaYmmkqT7DExcpymfo5+/wA6JxCwy8')

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


