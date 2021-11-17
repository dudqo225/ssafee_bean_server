import requests, json

movie_list = []

for i in range(1, 11):

    URL = f'https://api.themoviedb.org/3/movie/popular?api_key=65bf23772658c6b898a2865e99430c95&language=ko-KR&page={i}'

    response = requests.get(URL)

    response_dict = response.json()

    # print(response_dict['results'])


    for res in response_dict['results']:
        # print(res.keys())
        movie = {
            'model': 'movies.movie',
        }
        movie['fields'] = {
            'title': res['title'],
            'story': res['overview'],
            'rank': round(res['vote_average'])//2,
            'release_date': res['release_date'],
            'poster_path': res['poster_path'],
            'genres': res['genre_ids'],
        }

        movie_list.append(movie)

print(movie_list)

file_path = './movie.json'

with open(file_path, 'w', encoding='UTF8') as outfile:
    json.dump(movie_list, outfile, ensure_ascii=False, indent=4)