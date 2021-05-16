from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    # url(r'^', include('api.urls')),
    path('api/', include('user.urls')),
    path('api/', include('events.urls')),
    path('api/', include('profile.urls')),
    path('api/', include('organizations.urls')),
]
