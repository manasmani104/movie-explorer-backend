import pytest
from movies.models import Movie, Actor, Director, Genre


@pytest.mark.django_db
def test_create_movie():
    genre = Genre.objects.create(name="Thriller")
    director = Director.objects.create(name="Test Director")
    actor = Actor.objects.create(name="Test Actor")

    movie = Movie.objects.create(title="Sample Movie", release_year=2024, director=director)
    movie.genres.add(genre)
    movie.actors.add(actor)

    assert movie.title == "Sample Movie"
    assert movie.genres.count() == 1
    assert movie.actors.count() == 1
