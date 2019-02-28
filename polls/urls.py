from django.urls import path

from . import views
from polls.views import *


# name is used for a particular mapping(a line in urlpatterns)


CSV_PATH = {
        "cweka": "polls\\data\\1_3cweka.csv",
        "chinese_stock": "polls\\data\\2_chinese_stock.csv",
        "license_plate": "polls\\data\\3_license_plate.csv",
        "hapiness": "polls\\data\\4_hapiness.csv"
    }

urlpatterns = [
    path('', views.home , name = 'home'),
    path('about/', views.about, name='about'),

]

# adding table parser here
urlpatterns += [
    path(r'table/<slug:slug>/', TableView.as_view(), name='table_url_parsing'),
]
# urlpatterns += [
#     path(r'table/<slug:slug>/functions/', FunctionTableView.as_view(), name='function_table_view'),
# ]

# path('table1/', TableView.as_view(table_name="weka"), name='table1'),
# path('table2/', TableView.as_view(table_name="chinese_stock"), name='table2'),
# path('table3/', TableView.as_view(table_name="license_plate"), name='table3'),
# path('table4/', TableView.as_view(table_name="hapiness"), name='table4'),
