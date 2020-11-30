from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from easy_select2 import select2_modelform
import requests

@admin.register(Resource)
class ResourceAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('uploader'),
                ('name'),
                ('batch','branch'),
                ('course'),
                ('date')

            ]
        }),
        ('Resource Details',{
            'fields': [
                ('resource_type','pdf'),
                ('url'),
                ('tags'),
                ('details')
            ]
        }),
    ]
    list_display = ('course','branch')
    list_filter = ('resource_type', 'tags')
    select2 = select2_modelform(Resource, attrs={'width': '250px'})
    form = select2

@admin.register(Resource_Type)
class ResourceTypeAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('name', 'author'),
            ]
        }),
    ]

@admin.register(Resource_Tag)
class ResourceTagAdmin(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('name', 'author'),
            ]
        }),
    ]

@admin.register(Branch)
class Branch(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('name', 'author'),
            ]
        }),
    ]

@admin.register(Courses)
class Courses(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('name', 'author'),
                ('course_code')
            ]
        }),
    ]

@admin.register(Batch)
class Batch(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    fieldsets = [
        ('Basic Details', {
            'fields': [
                ('year', 'author'),
            ]
        }),
    ]
