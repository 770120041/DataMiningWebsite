from polls.logic.csv_handler import *
from django.shortcuts import render, get_object_or_404
from django.views import View
from polls.models import *
from polls.forms import *
from polls.logic import *

TMPDIRPATH = "\\polls\\tmp\\"
DATADIRPATH = "\\polls\\data\\"


class TableView(View):

    TEMPLATE_NAME = 'polls/preprocess_form.html'
    table_name = ""
    form_inital = {"drop_missing": True, "digit_to_char": True, "method_selection": "CF"}
    root_path = get_root_path()

    def get(self, request, slug):
        dfmodel = get_object_or_404(DataFrameModel, df_description=slug)
        df = read_csv_file(self.root_path + DATADIRPATH + dfmodel.df_stroed_name)
        # if post: submit a form, else, display blank form
        form = Preprocess(initial=self.form_inital)
        context ={
            "form": form,
            "tableName": slug,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    def post(self, request, slug):
        print("root path is :" + self.root_path)

        dfmodel = get_object_or_404(DataFrameModel, df_description=slug)
        # if post: submit a form, else, display blank form
        form = Preprocess(request.POST)
        df = read_csv_file(self.root_path + DATADIRPATH + dfmodel.df_stroed_name)
        if form.is_valid():
            if form.cleaned_data['drop_missing']:
                df = drop_na(df)
            if print(form.cleaned_data['digit_to_char']):
                df = char_to_digit(df)
            # save new df
            new_csv_description = dfmodel.df_description + " after preprocessing"
            new_csv_store_name = dfmodel.df_stroed_name.replace(".csv", "_pre.csv")

            save_csv_file(df, self.root_path + TMPDIRPATH + new_csv_store_name)

            preprocessed_csv = DataFrameModel()
            preprocessed_csv.df_description = new_csv_description
            preprocessed_csv.df_stroed_name = new_csv_store_name

            print(form.cleaned_data['method_selection'])

        context = {
            "form": form,
            "tableName": slug,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


def home(request):
    return render(request, 'polls/home.html')


def about(request):
    return render(request, 'polls/about.html')

