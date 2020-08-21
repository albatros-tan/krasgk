from django.utils.deprecation import MiddlewareMixin

from .models import Topic, Pages


class ButtonsMenu(MiddlewareMixin):

    def process_template_response(self, request, response):
        # Process the response
        menu = {}
        for topic in Topic.objects.all().prefetch_related():
            menu[topic.name] = Pages.objects.filter(topic=topic).only(
                'name_in_menu', 'slug')
        response.context_data["menu"] = menu
        return response
