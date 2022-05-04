from django.contrib import admin

from route.models import Route


class RouteAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ('id', 'name', 'price', 'introduction', 'image')
    list_editable = ('name', 'price', 'introduction', 'image')
    search_fields = ('name',)
    fields = ('name', 'price', 'introduction', 'image')


admin.site.register(Route, RouteAdmin)
