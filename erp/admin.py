from django.contrib import admin
from .models import Property
from django.utils.safestring import mark_safe
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count', 'price', 'adress', 'data', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'adress')
    # list_editable = ('is_published',)
    list_filter = ('title', 'adress')
    fields = ('title', 'count', 'price', 'adress', 'data', 'get_photo', )
    readonly_fields = ('get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'



admin.site.register(Property, PropertyAdmin)
