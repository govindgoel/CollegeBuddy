from django.contrib import admin
from events.models import *
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from easy_select2 import select2_modelform
import requests

@admin.register(Event)
class EventAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('creator','pinned'),
                ('name', 'slug'),
                ('date', 'event_type','location'),
                'tags',
                ('details')
            ]
        }),
    ]
    list_display = ('name', 'event_type', 'pinned')
    list_filter = ('event_type', 'pinned', 'tags')

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('name', 'author'),
            ]
        }),
    ]

@admin.register(Event_Type)
class CategoryAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('name', 'author'),
            ]
        }),
    ]
