from django.urls import path, include
from rest_framework import routers

from cinema.views import ActorViewSet, CinemaHallViewSet

app_name = "cinema"

router = routers.DefaultRouter()

router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
