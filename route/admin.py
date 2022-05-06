from django.contrib import admin

from route.models import Route, RouteAttractionMapping


class RouteAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'name', 'price', 'introduction', 'image')
    list_editable = ('name', 'price', 'introduction', 'image')
    search_fields = ('name',)
    fields = ('name', 'price', 'introduction', 'image')


class RouteAttractionAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'route', 'attraction')
    list_editable = ('route', 'attraction')
    fields = ('route', 'attraction')


admin.site.register(Route, RouteAdmin)
admin.site.register(RouteAttractionMapping, RouteAttractionAdmin)
