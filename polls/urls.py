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
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

# pre_process table view
urlpatterns += [
    path(r'table/<slug:slug>/', TableView.as_view(), name='table_url_parsing'),
]

# classification
urlpatterns += [
    path(r'CF/<slug:table_descprition>/', ClassificationView.as_view(), name='classification'),
    path(r'CF_result/<slug:table_descprition>/', CFViewResult.as_view(), name='CFresult')
]

# clustering
urlpatterns += [
    path('delete_all_local_cache/', views.delete_local_cache, name='del_local_cache')
]
