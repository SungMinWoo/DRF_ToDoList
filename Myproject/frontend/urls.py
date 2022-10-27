from django.urls import path, include
from .views import list

app_name = 'frontend'


urlpatterns = [
    path('', list, name='list'),
]