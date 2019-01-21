from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('table1/', views.table1, name = 'table1'),
    path('table2/', views.table2, name = 'table2'),
    path('table3/', views.table3, name = 'table3'),
    path('table4/', views.table4, name = 'table4'),
    path('about/', views.about, name = 'about'),

]