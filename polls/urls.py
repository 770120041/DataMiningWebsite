from django.urls import path

from . import views
from polls.views import TableView


# name is used for a particular mapping(a line in urlpatterns)

"""
    TODO:
        passing more variables to url function  
        https://docs.djangoproject.com/en/1.11/topics/http/urls/#passing-extra-options-to-view-functions
"""

CSV_PATH = {
        "weka": "polls\\data\\1_3cweka.csv",
        "chinese_stock": "polls\\data\\2_chinese_stock.csv",
        "license_plate": "polls\\data\\3_license_plate.csv",
        "hapiness": "polls\\data\\4_hapiness.csv"
    }

urlpatterns = [
    path('', views.home , name = 'home'),
    path('about/', views.about, name='about'),

]

# adding base tables here
urlpatterns += [
    path('table1/', TableView.as_view(table_name="weka"), name='table1'),
    path('table2/', TableView.as_view(table_name="chinese_stock"), name='table2'),
    path('table3/', TableView.as_view(table_name="license_plate"), name='table3'),
    path('table4/', TableView.as_view(table_name="hapiness"), name='table4'),
]
