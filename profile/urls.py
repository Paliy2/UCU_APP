from django.conf.urls import url
# from profile.views import UserProfileView
from profile.views import ContactListView, PhoneNumberListView


urlpatterns = [
    # url(r'^profile', UserProfileView.as_view()),
    url(r'^search-phone', ContactListView.as_view()),
    url(r'^phone', PhoneNumberListView.as_view()),
    ]