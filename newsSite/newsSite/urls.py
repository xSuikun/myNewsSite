from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('test/', include('testapp.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha', include('captcha.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

