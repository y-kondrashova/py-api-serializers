from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data: dict) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance: CinemaHall, validated_data: dict) -> CinemaHall:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_rows = validated_data.get(
            "seats_in_rows", instance.seats_in_rows
        )
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Genre.objects.all())]
    )

    def create(self, validated_data: dict) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data: dict) -> Genre:
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(style={"type": "textarea"})
    duration = serializers.IntegerField()

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)

    def update(self, instance: Movie, validated_data: dict) -> Movie:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get(
            "description", instance.description
        )
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance


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
