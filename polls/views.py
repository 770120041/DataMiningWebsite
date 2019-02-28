from django.http import HttpResponse
from polls.csv_handler import *
from django.shortcuts import render, get_object_or_404
import os
from django.views import View
from polls.models import *


def home(request):
    return render(request, 'polls/index.html', {'table': "homepage"})


class TableView(View):
    TEMPLATE_NAME = 'polls/index.html'
    table_name = ""

    def get(self, request, slug):
        print(slug)
        dfmodel = get_object_or_404(DataFrameModel, data_frame_name=slug)
        context ={
            "table_name": self.table_name,
            "table": csv_to_html(dfmodel.data_frame_path)
        }
        return render(request, self.TEMPLATE_NAME, context=context)



def about(request):
    return render(request, 'polls/about.html')

