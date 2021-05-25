from django.conf.urls import url, include
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':
                           'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
    path('openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),

    # url(r'^', include('api.urls')),
    path('api/', include('user.urls')),
    path('api/', include('events.urls')),
    path('api/', include('profile.urls')),
    path('api/', include('organizations.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
