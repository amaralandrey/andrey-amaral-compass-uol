## Desafio

Nesta sprint, o desafio teve como objetivo a ingestão de dados da API do TMDB em um bucket S3 da AWS, utilizando uma função AWS Lambda. O desafio tinha quatro requisitos principais.  

### Requisito 01 - Criar no AWS Lambda as camadas para as bibliotecas necessárias.

Para o desafio, decidi utilizar a biblioteca requests, pois ela é melhor documentada que a biblioteca do TMDB e geram os mesmos resultados.  
Assim, criei uma pasta local chamada python e fiz a instalação da biblioteca nela com o comando:

    pip install -t requests .

Em seguida zipei a pasta com o comando:

     zip python.zip python

A pasta original e a pasta zipada no subdiretório 'layer-utilizada'.  

Por fim, fiz a adição da camada pelo console da AWS.  
![evidencia-1](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2007/Evidencias/evidencia-01.png)

### Requisitos 02, 03 e 04 - Implementar o código Python para o consumo dos dados da API TMDB, buscar dados e agrupar e persistir os dados no S3.

O código utiliza as bibliotecas requests, json, boto3 e datetime.  

Criei um dicionário de parâmetros para serem referenciados nas chamadas da API. 

      parametros = {
          'api_key': api_key,
          'with_genres': '80',  # id do gênero Crime.
          'sort_by': 'popularity.desc',  # para essa etapa do desafio final, busquei os filmes de crime mais populares.
          'page': 1  
      }

Para criar as camadas do data lake, utilizei uma variável com o caminho a ser criado para os dados retornados.

     s3_caminho = 'Raw/TMDB/JSON/'

Com uso dos métodos de datetime, salvei a data de execução em variáveis de ano, mês e dia para criar as camadas do data lake.

      data_atual = datetime.now()
      ano = data_atual.year
      mes = data_atual.month
      dia = data_atual.day

Por último, utilizei uma função recursiva para requisitar os dados, salvar em jsons com 20 registros e persistir os arquivos no S3.

    def ingestao_api_tmdb_to_s3(movies, page):
      
       ...
    
        for page in range(1, 6):
            parametros['page'] = page
            response = requests.get(base_url, params=parametros)
            
            if response.status_code == 200:
                data = response.json()
                movies = data['results']
                ingestao_api_tmdb_to_s3(movies, page)
            else:
                print(f'Erro na requisição da página {page}: {response.status_code}')


Criação do script da função lambda:

![evidencia-2](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2007/Evidencias/evidencia-02.png)


Resultado da execução da função lambda:

![evidencia-3](https://github.com/amaralandrey/andrey-amaral-compass-uol/blob/main/Sprint%2007/Evidencias/evidencia-03.png)
