from django.conf.urls import url, include
from django.urls import path
from api import views

urlpatterns = [
    # url(r'^', include('api.urls')),
    path('api/', include('user.urls')),
    path('api/', include('profile.urls')),
]
