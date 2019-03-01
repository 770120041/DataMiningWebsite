from django.contrib import admin
from django.contrib.admin import ModelAdmin

from polls.models import DataFrameModel
# Register your models here.

class DataFrameModelAdmin(ModelAdmin):
    list_display = ('df_description', 'df_stroed_name')


admin.site.register(DataFrameModel, DataFrameModelAdmin)

