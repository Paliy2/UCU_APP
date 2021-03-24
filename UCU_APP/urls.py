from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    # url(r'^', include('api.urls')),
    path('api/', include('user.urls')),
    path('api/', include('trapezna.urls')),
    path('api/', include('UCU_buildings.urls')),
    path('api/', include('profile.urls')),
]
