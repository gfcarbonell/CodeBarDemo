from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import BarCodeModel

@admin.register(BarCodeModel)
class BarCodeModelAdmin(ImportExportModelAdmin):
    pass