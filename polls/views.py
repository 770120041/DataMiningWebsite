from polls.csv_handler import *
from django.shortcuts import render, get_object_or_404
from django.views import View
from polls.models import *


class TableView(View):
    TEMPLATE_NAME = 'polls/show_table.html'
    table_name = ""

    def get(self, request, slug):
        print(slug)
        dfmodel = get_object_or_404(DataFrameModel, data_frame_name=slug)
        context ={
            "tableName": slug,
            "table": csv_to_html(dfmodel.data_frame_path)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


def home(request):
    return render(request, 'polls/home.html')


def about(request):
    return render(request, 'polls/about.html')

