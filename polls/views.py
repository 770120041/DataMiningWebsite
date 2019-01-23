from django.http import HttpResponse
from polls.csv_handler import *
from django.shortcuts import render
import os

def home(request):

    return render(request, 'polls/index.html',{'table':"homepage"})


def table1(request):
    return render(request, 'polls/index.html',{'table': csv_to_html("polls\\data\\1_3cweka.csv")})

def table2(request):
    return render(request, 'polls/index.html',{'table': csv_to_html("polls\\data\\2_chinese_stock.csv")})

def table3(request):
    return render(request, 'polls/index.html',{'table': csv_to_html("polls\\data\\3_license_plate.csv")})

def table4(request):
    return render(request, 'polls/index.html',{'table': csv_to_html("polls\\data\\4_hapiness.csv")})

def about(request):
    return render(request, 'polls/about.html')