from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls'), name='users'),
    path('admin/', admin.site.urls),
    # path('', include('events.urls')),
]
