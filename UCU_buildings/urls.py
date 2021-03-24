from django.conf.urls import url, include
from django.urls import path
from UCU_buildings.views import BuildingsView

urlpatterns = [
    url(r'^buildings', BuildingsView.as_view())
]
