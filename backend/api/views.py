from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Opendata


class OpendataView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Opendata.objects.all()
# Create your views here.
