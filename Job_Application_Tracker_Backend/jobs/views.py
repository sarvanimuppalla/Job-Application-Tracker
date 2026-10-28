from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import jobs
from .serializers import JobSerializer

# Create your views here.

class JobHandler(ModelViewSet):
    queryset = jobs.objects.all()
    serializer_class = JobSerializer
