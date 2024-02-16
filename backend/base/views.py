from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models




# Create your views here.

class Ac_appViewSet(viewsets.ModelViewSet):
    queryset = models.Ac_app.objects.all()
    serializer_class = serializers.Ac_appSerializier