from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('send_feedback/', send_feedback, name='feedback'),
    path('create/', CreateNews.as_view(), name='add_news'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', CategoryNews.as_view(extra_context={'title': 'Тайтл'}), name='category'),
    path('<int:pk>/', ViewNews.as_view(), name='view_news'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)