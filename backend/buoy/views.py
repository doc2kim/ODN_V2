from rest_framework import generics
from .serializers import BuoyDataSerializer
from .models import Data


class BuoyDataView(generics.ListCreateAPIView):
    serializer_class = BuoyDataSerializer
    queryset = Data.objects.all()
