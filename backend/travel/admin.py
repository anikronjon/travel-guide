from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from .models import (
    Category,
    Location,
    Place,
    Media
)


# Register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'places']
    prepopulated_fields = {'slug': ('name',)}

    def places(self, category):
        url = (reverse('admin:travel_place_changelist')
               + '?'
               + urlencode({
                    'category__id__exact': str(category.id)
                }))
        return format_html('<a href="{}">{}</a>', url, category.place_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(place_count=Count('places'))


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('division', 'district', 'places')

    def places(self, location):
        url = (reverse('admin:travel_place_changelist')
               + '?'
               + urlencode({'location__id__exact': str(location.id)}))
        return format_html(f'<a href="{url}">{location.place_count}</a>')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(place_count=Count('places'))


class MediaInline(admin.TabularInline):
    model = Media


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'category')
    list_filter = ('location', 'category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [MediaInline]

