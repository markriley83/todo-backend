from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register('todo', viewsets.TodoViewset, basename='todo')
