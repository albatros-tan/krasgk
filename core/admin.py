from django.contrib import admin

from .models import ServiceTable, Pages, Articles, Images, Files, Albums, Topic


class ImageInline(admin.TabularInline):
    model = Images
    #extra = 2


class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


class PageInline(admin.StackedInline):
    model = Pages
    extra = 1
    fields = (
        'header', 'title', 'name_in_menu', 'slug',
    )


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        PageInline
    ]


class ArticlesInline(admin.StackedInline):
    model = Articles
    extra = 0


class AlbumsInline(admin.TabularInline):
    model = Albums
    extra = 3


class FilesInline(admin.TabularInline):
    model = Files
    extra = 3


class PageAdmin(admin.ModelAdmin):
    inlines = [
        ArticlesInline,
        AlbumsInline,
        FilesInline,
    ]


# Register your models here.

admin.site.register(Topic, TopicAdmin)
admin.site.register(Pages, PageAdmin)
admin.site.register(Albums, AlbumAdmin)

"""
admin.site.register(ServiceTable)
admin.site.register(Articles)
admin.site.register(Images)

admin.site.register(Files)
"""

