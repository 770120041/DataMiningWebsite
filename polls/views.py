from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


from polls.forms import  *
from polls.models import *

from polls.logic import *

TMPDIRPATH = "\\polls\\tmp\\"
DATADIRPATH = "\\polls\\data\\"


class TableView(View):
    """
        This class is used for pre-processing and method selection of table
        Datas are precopied data here
    """
    TEMPLATE_NAME = 'polls/preprocess.html'
    form_inital = {"drop_missing": True, "digit_to_char": True, "method_selection": "CF"}
    root_path = get_root_path()

    def get(self, request, slug):
        dfmodel = get_object_or_404(DataFrameModel, df_description=slug)
        df = read_csv_file(self.root_path + DATADIRPATH + dfmodel.df_stroed_name)
        form = PreprocessForm(initial=self.form_inital)
        context ={
            "form": form,
            "tableName": slug,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    def post(self, request, slug):

        dfmodel = get_object_or_404(DataFrameModel, df_description=slug)
        form = PreprocessForm(request.POST)
        df = read_csv_file(self.root_path + DATADIRPATH + dfmodel.df_stroed_name)
        if form.is_valid():
            if form.cleaned_data['drop_missing']:
                df = drop_na(df)
            if form.cleaned_data['digit_to_char']:
                df = char_to_digit(df)

            # save new df
            new_csv_description = dfmodel.df_description + "-after-preprocessing"
            new_csv_store_name = dfmodel.df_stroed_name.replace(".csv", "_pre.csv")

            save_csv_file(df, self.root_path + TMPDIRPATH + new_csv_store_name)

            # save this model to database
            save_csv_model(new_csv_description, new_csv_store_name)

            print(form.cleaned_data['method_selection'])

             # redirect to classification method
            return redirect("/polls/"+form.cleaned_data['method_selection']+"/"+new_csv_description+"/")

        # in case form not valid
        context = {
            "form": form,
            "tableName": slug,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


class ClassificationVIew(View):
    TEMPLATE_NAME = 'polls/logic/classification.html'
    root_path = get_root_path()
    form_inital = {"method_selection": "LG", "classification_parameters": ""}

    def get(self, request, table_descprition):
        dfmodel = get_object_or_404(DataFrameModel, df_description=table_descprition)
        df = read_csv_file(self.root_path + TMPDIRPATH + dfmodel.df_stroed_name)
        form = ClassificationForm(initial=self.form_inital)
        context ={
            "form": form,
            "tableName": table_descprition,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    def post(self, request):
        pass


class ClusteringView(View):
    TEMPLATE_NAME = 'polls/logic/clustering.html'

    def get(self, request, table_descprition):
        return HttpResponse(table_descprition)

    def post(self, request):
        pass


def home(request):
    return render(request, 'polls/home.html')


def about(request):
    return render(request, 'polls/about.html')

def delete_local_cache(request):
    print("in deleted local cache funciton")
    return redirect("/polls/about/")


