from django.conf.urls import url
from organizations.views import OrganizationListView, OrganizationDetailView
from organizations.views import DepartmentListView, DepartmentDetailView
from django.urls import path

urlpatterns = [
    path('organizations/<int:pk>', OrganizationDetailView.as_view()),
    url(r'^organizations/', OrganizationListView.as_view()),
    url(r'^departments/', DepartmentListView.as_view()),
    url(r'^departments/<int:pk>', DepartmentDetailView.as_view()),
]