from django.urls import path

from . import views
from polls.views import TableView


# name is used for a particular mapping(a line in urlpatterns)

"""
    TODO:
        passing more variables to url function  
        https://docs.djangoproject.com/en/1.11/topics/http/urls/#passing-extra-options-to-view-functions
"""

urlpatterns = [
    path('', views.home , name = 'home'),
    path('table1/', views.table1, name = 'table1'),
    path('table2/', views.table2, name = 'table2'),
    path('table3/', views.table3, name = 'table3'),
    path('table4/', views.table4, name = 'table4'),
    path('about/', views.about, name = 'about'),
]

urlpatterns += [
    path('class/', TableView.as_view(table_number = 2), name = 'table_class2_')
]
