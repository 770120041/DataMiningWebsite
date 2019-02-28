from polls.csv_handler import *
from django.shortcuts import render, get_object_or_404
from django.views import View
from polls.models import *
from polls.forms import *
import pandas as pd

class TableView(View):
    TEMPLATE_NAME = 'polls/preprocess_form.html'
    table_name = ""
    form_inital = {"drop_missing": True, "digit_to_char": True, "method_selection": "CF"}
    def get(self, request, slug):
        dfmodel = get_object_or_404(DataFrameModel, data_frame_name=slug)

        # if post: submit a form, else, display blank form

        form = Preprocess(initial=self.form_inital)

        context ={
            "form": form,
            "tableName": slug,
            "table": csv_to_html(dfmodel.data_frame_path)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    def post(self, request, slug):
        dfmodel = get_object_or_404(DataFrameModel, data_frame_name=slug)

        # if post: submit a form, else, display blank form
        form = Preprocess(request.POST)
        if form.is_valid():
            print(form.cleaned_data['drop_missing'])
            print(form.cleaned_data['digit_to_char'])
            print(form.cleaned_data['method_selection'])
        context = {
            "form": form,
            "tableName": slug,
            "table": csv_to_html(dfmodel.data_frame_path)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


def home(request):
    return render(request, 'polls/home.html')


def about(request):
    return render(request, 'polls/about.html')

