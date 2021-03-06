from rest_framework import viewsets

from . import models
from . import serializers


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
