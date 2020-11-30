from django.contrib import admin
from info.models import *
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from easy_select2 import select2_modelform
import requests

@admin.register(Notice)
class NoticeAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('title','pinned'),
                ('date'),
                ('url','pdf'),
                ('details')
            ]
        }),
    ]
    list_display = ('title','pinned')
    list_filter = ('date', 'pinned' )