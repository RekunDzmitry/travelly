from django.urls import path
from . import views


urlpatterns = [
    path('cities', views.list_cities, name='list_cities'),
    path('', views.index, name='home'),
]