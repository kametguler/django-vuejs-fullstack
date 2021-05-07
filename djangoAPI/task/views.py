from rest_framework import viewsets
from .serializer import *
from .models import *


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

