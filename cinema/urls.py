from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieViewSet,
)

app_name = "cinema"

router = routers.DefaultRouter()

router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("genres", GenreViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
