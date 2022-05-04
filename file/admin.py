from django.contrib import admin

from file.models import AttractionImage


class AttractionImageAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'name', 'image')
    list_editable = ('name', 'image')
    search_fields = ('name',)
    fields = ('name', 'image', 'attraction')


admin.site.register(AttractionImage, AttractionImageAdmin)
