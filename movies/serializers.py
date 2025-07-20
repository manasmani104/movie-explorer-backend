from rest_framework import serializers
from .models import Movie, Actor, Director, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_year', 'genres', 'actors', 'director']

    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        actors_data = validated_data.pop('actors')
        director_data = validated_data.pop('director')

        director, _ = Director.objects.get_or_create(**director_data)
        movie = Movie.objects.create(director=director, **validated_data)

        for genre in genres_data:
            g, _ = Genre.objects.get_or_create(**genre)
            movie.genres.add(g)

        for actor in actors_data:
            a, _ = Actor.objects.get_or_create(**actor)
            movie.actors.add(a)

        return movie
