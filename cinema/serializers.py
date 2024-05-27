from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(serializers.ModelSerializer):
    genres_name = serializers.SerializerMethodField()
    actors_full_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres_name", "actors_full_name"]

    def get_genres_name(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_actors_full_name(self, obj):
        return [actor.full_name for actor in obj.actors.all()]


class MovieSessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    show_time = serializers.DateTimeField()

    def create(self, validated_data: dict) -> MovieSession:
        return MovieSession.objects.create(**validated_data)

    def update(self,
               instance: MovieSession,
               validated_data: dict) -> MovieSession:
        instance.show_time = validated_data.get(
            "show_time", instance.show_time
        )
        instance.save()
        return instance
