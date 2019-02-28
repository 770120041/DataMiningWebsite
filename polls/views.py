from django.http import HttpResponse
from polls.csv_handler import *
from django.shortcuts import render, get_object_or_404
import os
from django.views import View
from polls.models import *


def home(request):
    return render(request, 'polls/index.html', {'table':"homepage"})


class TableView(View):
    TABLE_PATH = {
        1: "polls\\data\\1_3cweka.csv",
        2: "polls\\data\\2_chinese_stock.csv",
        3: "polls\\data\\3_license_plate.csv",
        4: "polls\\data\\4_hapiness.csv"
    }
    TEMPLATE_NAME =  'polls/index.html'
    table_name = ""

    def get(self, request):
        dfmodel = get_object_or_404(DataFrameModel, data_frame_name=self.table_name )
        context ={
            "table_name": self.table_name,
            "table": csv_to_html(dfmodel.data_frame_path)
        }
        return render(request, self.TEMPLATE_NAME, context=context)



def about(request):
    return render(request, 'polls/about.html')

