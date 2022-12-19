from django.urls import path
from .views import carsListCreateView,carsDetailView
urlpatterns = [
    path('',carsListCreateView.as_view(),name='car_list_create'),
    path('<int:pk>',carsDetailView.as_view(),name='cars_detail'),

    
]