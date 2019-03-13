from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.validators import FileExtensionValidator


from polls.forms import  *
from polls.models import *

from polls.logic import *

TMPDIRPATH = "\\polls\\tmp\\"
DATADIRPATH = "\\polls\\data\\"
ROOTPATH = get_root_path()

class TableView(View):
    """
        This class is used for pre-processing and method selection of table
        After choosing pre-processing options and methods, redirect to specific
        method diplaying
    """
    TEMPLATE_NAME = 'polls/preprocess.html'
    form_inital = {"drop_missing": True, "digit_to_char": True, "Classifier": "CF"}
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
            return redirect("/polls/" + form.cleaned_data['method_selection'] + "/" + new_csv_description + "/")

        # in case form not valid
        context = {
            "form": form,
            "tableName": slug,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


class ClassificationView(View):
    """
        This view is used for classification parameters seting
    """
    TEMPLATE_NAME = 'polls/logic/classification.html'
    root_path = get_root_path()
    form_inital = {"Classifier": "LG", "train_ratio" : "0.7"}


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

    # rendering post and redirect to showing result
    def post(self, request, table_descprition):
        dfmodel = get_object_or_404(DataFrameModel, df_description=table_descprition)
        df = read_csv_file(self.root_path + TMPDIRPATH + dfmodel.df_stroed_name)
        form = ClassificationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["classification_parameters"])
            # param = form.cleaned_data
            new_csv, train_stat = MyClassification(df, form.cleaned_data["label_name"], form.cleaned_data["Classifier"],form.cleaned_data["train_ratio"], param=form.cleaned_data["classification_parameters"])
            new_csv_description = dfmodel.df_description + "-result"
            new_csv_store_name = dfmodel.df_stroed_name.replace("_pre.csv", "_result.csv")
            save_csv_file(new_csv, self.root_path + TMPDIRPATH + new_csv_store_name)
            # save this model to database
            save_csv_model(new_csv_description, new_csv_store_name)
            request.session['cfstat'] = train_stat
            return redirect('/polls/CF_result/'+new_csv_description+"/")

        # if in this, means that form is invalid
        context = {
            "form": form,
            "tableName": table_descprition,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


class CFViewResult(View):

    TEMPLATE_NAME = 'polls/logic/classfication_result.html'
    def get(self, request,table_descprition):
        train_stat = request.session['cfstat']

        dfmodel = get_object_or_404(DataFrameModel, df_description=table_descprition)
        df = read_csv_file(ROOTPATH + TMPDIRPATH + dfmodel.df_stroed_name)
        context = {
            "tableName": table_descprition,
            "table": df_to_html(df),
            "stat" : train_stat
        }
        return render(request, self.TEMPLATE_NAME, context=context)




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

def success_url(request):
    return HttpResponse("success page")

def fail_upload(request):
    return HttpResponse("fail page")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            if form.cleaned_data['title'].lower().endswith('.csv') is not True:
                return redirect('/polls/fail_upload/')

            print("file name is " + form.cleaned_data['title'])
            save_upload_file(file, ROOTPATH + TMPDIRPATH + form.cleaned_data["title"])
            return redirect('/polls/success/')
    else:
        form = UploadFileForm()
    return render(request, 'polls/upload.html', {'form': form})

def delete_local_cache(request):
    print("in deleted local cache funciton")
    return redirect("/polls/about/")


