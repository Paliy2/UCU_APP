from django.conf.urls import url
from events.views import EventRetrieveUpdateDestroyAPIView, EventListView, EventFavoritesView
from django.urls import path

urlpatterns = [
    # url(r'^events/(\d+)/$', EventRetrieveUpdateDestroyAPIView.as_view()),
    url(r'^events/', EventListView.as_view()),
    path('events/v1/<int:id>/', EventRetrieveUpdateDestroyAPIView.as_view()),

]