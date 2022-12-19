from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import cars
from .serializers import carsSerializer
from .permissions import OwnerOnly

class carsListCreateView(ListCreateAPIView):
    
    queryset=cars.objects.all()
    serializer_class=carsSerializer


class carsDetailView(RetrieveUpdateDestroyAPIView):
    queryset=cars.objects.all()
    serializer_class=carsSerializer
    permission_classes=[OwnerOnly]
