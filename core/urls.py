from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from .views import SimplePage, AlbumPage, MainPage


urlpatterns = [
    path('album/<int:pk>/', AlbumPage.as_view(), name='album-page'),
    path('<slug:slug>/', SimplePage.as_view(), name='simple-page'),
    path('', MainPage.as_view(), name='main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
if settings.DEBUG:
    urlpatterns = [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        re_path(r'', include('django.contrib.staticfiles.urls')),


    ] + urlpatterns
"""
