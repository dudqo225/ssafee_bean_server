from django.db import models

class Genre(models.Model):
    NO_GENRE = 'No_Genre'
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    ANIMATION = 'Animation'
    COMEDY = 'Comedy'
    CRIME = 'Crime'
    DOCUMENTARY = 'Documentary'
    DRAMA = 'Drama'
    FAMILY = 'Family'
    FANTASY = 'Fantasy'
    HISTORY = 'History'
    HORROR = 'Horror'
    MUSIC = 'Music'
    MYSTERY = 'Mystery'
    ROMANCE = 'Romance'
    SCIENCE_FICTION = 'Science_Fiction'
    TV_MOVIE = 'TV_Movie'
    THRILLER = 'Thriller'
    WAR = 'War'
    WESTERN = 'Western'
    GENRE_CHOICES = [
        (NO_GENRE, '없음'),
        (ACTION, '액션'),
        (ADVENTURE, '모험'),
        (ANIMATION, '애니메이션'),
        (COMEDY, '코미디'),
        (CRIME, '범죄'),
        (DOCUMENTARY, '다큐멘터리'),
        (DRAMA, '드라마'),
        (FAMILY, '가족'),
        (FANTASY, '판타지'),
        (HISTORY, '역사'),
        (HORROR, '공포'),
        (MUSIC, '음악'),
        (MYSTERY, '미스터리'),
        (ROMANCE, '로맨스'),
        (SCIENCE_FICTION, 'SF'),
        (TV_MOVIE, 'TV 영화'),
        (THRILLER, '스릴러'),
        (WAR, '전쟁'),
        (WESTERN, '서부'),
    ]
    name = models.CharField(max_length=50, choices=GENRE_CHOICES, default=NO_GENRE)
    # genre_pk = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField()
    rank = models.IntegerField()
    # actor = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.id}: {self.title}'