from rest_framework import viewsets

from cinema.models import Actor
from cinema.serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
