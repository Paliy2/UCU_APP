from django.conf.urls import url
from organizations.views import OrganizationListView, OrganizationDetailView
from django.urls import path

urlpatterns = [
    path('organizations/<int:pk>', OrganizationDetailView.as_view()),
    url(r'^organizations/', OrganizationListView.as_view()),
]