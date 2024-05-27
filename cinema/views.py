from rest_framework import viewsets

from cinema.models import Actor, CinemaHall, Genre, Movie
from cinema.serializers import (
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    MovieListSerializer,
    MovieSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            super().get_queryset().prefetch_related('actors', 'genres')
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        return MovieSerializer
