from django.urls import path

from . import views
from polls.views import *


# name is used for a particular mapping(a line in urlpatterns)

# data
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
    path(r'table/<slug:df_description>/', TableView.as_view(), name='table_url_parsing'),
]

# classification
urlpatterns += [
    path(r'CF/<slug:new_csv_store_name>/', ClassificationView.as_view(), name='classification'),
    path(r'CF_result/<slug:new_csv_store_name>/', CFViewResult.as_view(), name='CFresult')
]
# clustering
urlpatterns += [
    path(r'CR/<slug:new_csv_store_name>/', ClusteringView.as_view(), name='classification'),
    path(r'CR_result/<slug:new_csv_store_name>/', CR_result.as_view(), name='CFresult')
]
urlpatterns += [
    path(r'AR/<slug:new_csv_store_name>/', AssociationRuleView.as_view(), name='classification'),
    # path(r'CR_result/<slug:new_csv_store_name>/', CR_result.as_view(), name='CFresult')
]

urlpatterns += [
    path('delete_all_local_cache/', views.delete_local_cache, name='del_local_cache')
]


# upload csv file
urlpatterns += [
    path('upload/', views.upload_file, name='upload_url'),
    path('download/<slug:new_csv_store_name>/', views.download_file, name='download_url')
]

# urlpatterns += [
#     path('upload/success/',views.success_url, name='op_success'),
#     path('upload/fail_upload/', views.fail_upload, name = 'fail_uload')
# ]


# docs
urlpatterns += [
    path('docs/<slug:method>/<slug:doc_name>/',DocsView.as_view(),name='view_docs')
]
