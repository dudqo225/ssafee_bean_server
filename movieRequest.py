import requests, json

movie_list = []

for i in range(1, 11):
    URL2 = f'https://api.themoviedb.org/3/movie/now_playing?api_key=65bf23772658c6b898a2865e99430c95&language=ko-KR&page={i}'

    response2 = requests.get(URL2)
    response_dict2 = response2.json()

    for res in response_dict2['results']:
        movie = {
            'model': 'movies.movie',
        }
        movie['fields'] = {
            'id': res['id'],
            'title': res['title'],
            'story': res['overview'],
            'rank': round(res['vote_average'])//2,
            'original_title': res['original_title'],
            # 'user_rank': 0,
            'release_date': res['release_date'],
            'poster_path': res['poster_path'],
            'genres': res['genre_ids'],
            'popularity': res['popularity'],
        }

        movie_list.append(movie)

for i in range(11, 35):
    URL1 = f'https://api.themoviedb.org/3/movie/popular?api_key=65bf23772658c6b898a2865e99430c95&language=ko-KR&page={i}'
    response1 = requests.get(URL1)
    response_dict1 = response1.json()

    for res in response_dict2['results']:
        movie = {
            'model': 'movies.movie',
        }
        movie['fields'] = {
            'id': res['id'],
            'title': res['title'],
            'story': res['overview'],
            'rank': round(res['vote_average'])//2,
            'original_title': res['original_title'],
            # 'user_rank': 0,
            'release_date': res['release_date'],
            'poster_path': res['poster_path'],
            'genres': res['genre_ids'],
            'popularity': res['popularity'],
        }

        movie_list.append(movie)


file_path = './movie.json'

with open(file_path, 'w', encoding='UTF8') as outfile:
    json.dump(movie_list, outfile, ensure_ascii=False, indent=4)

