from django.contrib import admin
from django.contrib.admin import ModelAdmin

from polls.models import DataFrameModel
# Register your models here.

class DataFrameModelAdmin(ModelAdmin):
    list_display = ('data_frame_name', 'df_path')


admin.site.register(DataFrameModel, DataFrameModelAdmin)

