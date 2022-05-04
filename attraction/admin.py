from django.contrib import admin

from attraction.models import Attraction


class AttractionAdmin(admin.ModelAdmin):
    fields = ('name', 'introduction')


admin.site.register(Attraction, AttractionAdmin)
