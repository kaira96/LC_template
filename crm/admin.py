from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Student
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'course', 'tariff', 'payment', 'data', 'finished', 'get_photo', 'accept')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'phone_number', 'course', 'tariff', 'payment',)
    list_editable = ('accept',)
    list_filter = ('name', 'phone_number', 'course', 'tariff',)
    fields = ('name', 'phone_number', 'course', 'tariff', 'payment', 'finished', 'certificate', 'accept')
    readonly_fields = ('get_photo',)
    save_on_top = True

    def get_photo(self, obj):
        if obj.certificate:
            return mark_safe(f'<img src="{obj.certificate.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'

admin.site.register(Student, StudentAdmin)
admin.site.site_title = 'Управление студентами'
admin.site.site_header = 'Управление студентами'