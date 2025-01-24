from django.urls import path

from events.views import index, cities, places_by_city, event_detail

app_name = 'events'

urlpatterns = [
    path('cities/<int:city_id>/', places_by_city, name='places_by_city'),
    path('cities/', cities, name='cities'),
    path('events/<int:event_id>/', event_detail, name='event_detail'),
    path('', index, name='index')
]
