from django.urls import path

from events.views import index

urlpatterns = [
    path('', index, name='index')
]
