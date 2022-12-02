from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'data', 'accept')
    list_display_links = ('id', 'name', 'phone_number')
    list_filter = ('name', 'phone_number', 'accept')
    search_fields = ('name', 'phone_number')


admin.site.register(Lead, LeadAdmin)

admin.site.site_title = 'Управление Лидами'
admin.site.site_header = 'Управление Лидами'