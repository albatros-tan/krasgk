from django.contrib import admin

from .models import ServiceTable, Pages, Articles, Images, Files

# Register your models here.

admin.site.register(Pages)
admin.site.register(ServiceTable)
admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(Files)
