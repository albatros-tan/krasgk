from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView

from .models import Pages, Articles, Images, Files

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
        context["images"] = Images.objects.filter(page=obj)
        context["files"] = Files.objects.filter(page=obj)
        return context


def main_page(request):
    """Переход на главную страницу редиректится на страницу с
    общими сведениями

    """
    return redirect('/obshchie-svedeniia/', permanent=True)
