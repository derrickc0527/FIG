from django.contrib import admin
from .models import Products
# from import_export.admin import ImportExportModelAdmin

admin.site.register(Products)

# @admin.register(Products)
# class ViewAdmin(ImportExportModelAdmin):
#     pass
