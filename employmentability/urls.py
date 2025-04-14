

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('employability-online-admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('core', include('core.urls')),
    path('secondarystudents', include('secondarystudents.urls')),
    path('tertiarystudents', include('tertiarystudents.urls')),
    path('adults', include('adults.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'accounts.views.handler404'