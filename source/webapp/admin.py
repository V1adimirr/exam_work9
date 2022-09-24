from django.contrib import admin

from webapp.models import ImagesModel, AlbumModel


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['photo', 'signature', 'author', 'album']
    list_filter = ['created_at']
    search_fields = ['author']
    readonly_fields = ['created_at']
    fields = ['photo', 'signature', 'created_at', 'author', 'album']


admin.site.register(ImagesModel, ImagesAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['image_name', 'description', 'album_author']
    list_filter = ['created_at_album']
    readonly_fields = ['created_at_album']
    fields = ['image_name', 'description', 'album_author', 'created_at_album']


admin.site.register(AlbumModel, AlbumAdmin)
