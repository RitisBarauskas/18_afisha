from django.urls import path

from events.views import index, cities, places_by_city

urlpatterns = [
    path('cities/<int:city_id>/', places_by_city, name='places_by_city'),
    path('cities/', cities, name='cities'),
    path('', index, name='index')
]
