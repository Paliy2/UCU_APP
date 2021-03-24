from django.conf.urls import url
from trapezna.views import MenuItemView


urlpatterns = [
    url(r'^view-menu/', MenuItemView.as_view()),
    # url(r'^login/', UserLoginView.as_view()),
    ]