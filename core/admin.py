from django.contrib import admin

from .models import ServiceTable, Pages, Articles, Images, Files, Albums


class ImageInline(admin.TabularInline):
    model = Images


class AlbumAdmin(admin.ModelAdmin):
	inlines = [
		ImageInline
	]

# Register your models here.

admin.site.register(Pages)
admin.site.register(ServiceTable)
admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(Albums, AlbumAdmin)
admin.site.register(Files)
