import requests
import json

api_key = 'key'
base_url = 'https://api.themoviedb.org/3/discover/movie'

# dicionário com parâmetros a serem referenciados na requisição da API
parametros = {
    'api_key': api_key,
    'with_genres': '80',  # id do genêro de filmes Crime
    'page': 1  # página de resultados retornados
}

# função para requisitar e salvar os filmes
def requisitar_filmes_tmdb(movies, page):

    filename = f'movies_page_{page}.json'
    
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(movies, file, ensure_ascii=False, indent=4)

# loop para requisitar 10000 registros, 20 por página
for page in range(1, 501):

    parametros['page'] = page
    
    response = requests.get(base_url, params=parametros)
    
    if response.status_code == 200:
        data = response.json()
        movies = data['results']
        requisitar_filmes_tmdb(movies, page)
        
    else:
        print(f'Erro na requisição da página {page}: {response.status_code}')

