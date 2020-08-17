from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.conf import settings

from .models import Pages, Articles, Images, Files, Albums

# Create your views here.

class SimplePage(DetailView):
    """Представление для обычной страницы"""

    model = Pages
    template_name = 'simple_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context.get('object', None)
        if obj is None:
            return HttpResponse('', status_code=500)
        context["articles"] = Articles.objects.filter(page=obj)
        albums = []
        temp = []
        counter = 0
        for image in Albums.objects.filter(page=obj):
            counter += 1
            temp.append(image)
            if counter == settings.COUNT_ALBUIMS_IN_ROWS:
                albums.append(temp)
                temp = []
                counter = 0
        if len(temp) > 0:
            albums.append(temp)

        context["albums"] = albums
        context["files"] = Files.objects.filter(page=obj)
        return context


class AlbumPage(DetailView):
    """Представление для отображения контента альбома"""

    model = Albums
    template_name = 'album_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = context.get('object', None)
        images = []
        temp = []
        counter = 0
        for image in Images.objects.filter(album=obj):
            counter += 1
            temp.append(image)
            if counter == settings.COUNT_IMAGES_IN_ROWS:
                images.append(temp)
                temp = []
                counter = 0
        if len(temp) > 0:
            images.append(temp)
            
        context["images"] = images
        return context


def main_page(request):
    """Переход на главную страницу редиректится на страницу с
    общими сведениями

    """
    return redirect('/obshchie-svedeniia/', permanent=True)
