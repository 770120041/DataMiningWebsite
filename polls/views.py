from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.validators import FileExtensionValidator

from django.contrib import messages

from polls.forms import *
from polls.logic.AR import do_association_rule
from polls.logic.CR import MyClustering
from polls.models import *

from polls.logic import *
import os

if os.name == 'nt':
    TMPDIRPATH = "\\polls\\tmp\\"
    DATADIRPATH = "\\polls\\data\\"
else:
    TMPDIRPATH = "/polls/tmp/"
    DATADIRPATH = "/polls/data/"
ROOTPATH = get_root_path()

"""
    Section:    
        Preprocess data and model selection
"""

class TableView(View):
    """
        This class is used for pre-processing and method selection of table
        After choosing pre-processing options and methods, redirect to specific
        method diplaying
    """
    TEMPLATE_NAME = 'polls/preprocess.html'
    form_inital = {"drop_missing": True, "char_to_digit": True, "Classifier": "CF"}
    root_path = get_root_path()

    # param is table name
    def get(self, request, df_description):
        csv_name = df_description +".csv"
        print(csv_name)
        # dfmodel = get_object_or_404(DataFrameModel, df_description=slug)
        df = read_csv_file(self.root_path + DATADIRPATH + csv_name)
        form = PreprocessForm(initial=self.form_inital)
        context ={
            "form": form,
            "tableName": df_description,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    # submit form
    def post(self, request, df_description):
        csv_name = df_description + ".csv"
        # dfmodel = get_object_or_404(DataFrameModel, df_description=slug)
        form = PreprocessForm(request.POST)
        df = read_csv_file(self.root_path + DATADIRPATH + csv_name)
        if form.is_valid():
            if form.cleaned_data['drop_missing']:
                df = drop_na(df)
            if form.cleaned_data['char_to_digit']:
                df = char_to_digit(df)

            # save new df
            new_csv_description = df_description + "-after-preprocessing"
            new_csv_store_name =csv_name.replace(".csv", "_pre.csv")

            save_csv_file(df, self.root_path + TMPDIRPATH + new_csv_store_name)

            # save this model to database
            # save_csv_model(new_csv_description, new_csv_store_name)

            print(form.cleaned_data['method_selection'])

             # redirect to specific method
            return redirect("/polls/" + form.cleaned_data['method_selection'] + "/" + new_csv_store_name.replace(".csv","") + "/")

        # in case form not valid
        context = {
            "form": form,
            "tableName": df_description,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

"""
    End Section
"""


"""
    Section:
        Classification and showing its result
"""
class ClassificationView(View):
    """
        This view is used for classification parameters seting
    """
    TEMPLATE_NAME = 'polls/logic/classification.html'
    root_path = get_root_path()
    form_inital = {"Classifier": "LG", "train_ratio" : "0.7"}


    def get(self, request, new_csv_store_name):
        # dfmodel = get_object_or_404(DataFrameModel, df_description=new_csv_store_name)
        df = read_csv_file(self.root_path + TMPDIRPATH + new_csv_store_name+".csv")

        form = ClassificationForm(initial=self.form_inital)
        context ={
            "form": form,
            "tableName": new_csv_store_name,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)

    # rendering post and redirect to showing result
    def post(self, request, new_csv_store_name):
        # dfmodel = get_object_or_404(DataFrameModel, df_description=new_csv_store_name)
        df = read_csv_file(self.root_path + TMPDIRPATH + new_csv_store_name+".csv")
        form = ClassificationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["classification_parameters"])
            # param = form.cleaned_data
            new_csv, train_stat = MyClassification(df, form.cleaned_data["label_name"], form.cleaned_data["Classifier"],form.cleaned_data["train_ratio"], param=form.cleaned_data["classification_parameters"])
            new_csv_description = new_csv_store_name.replace("_pre", "_result") + "-result"
            new_csv_store_name = new_csv_store_name.replace("_pre", "_result.csv")
            save_csv_file(new_csv, self.root_path + TMPDIRPATH + new_csv_store_name)
            # save this model to database
            # save_csv_model(new_csv_description, new_csv_store_name)
            request.session['cfstat'] = train_stat
            return redirect('/polls/CF_result/'+new_csv_store_name.replace(".csv","")+"/")

        # if in this, means that form is invalid
        context = {
            "form": form,
            "tableName": new_csv_store_name,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


class CFViewResult(View):
    """
        This view is used to show classification result
    """
    TEMPLATE_NAME = 'polls/logic/classfication_result.html'
    def get(self, request,new_csv_store_name):
        train_stat = request.session['cfstat']

        # dfmodel = get_object_or_404(DataFrameModel, df_description=new_csv_store_name)
        df = read_csv_file(ROOTPATH + TMPDIRPATH + new_csv_store_name+".csv")
        context = {
            "tableName": new_csv_store_name,
            "table": df_to_html(df),
            "stat" : train_stat
        }
        return render(request, self.TEMPLATE_NAME, context=context)

"""
    End Section
"""


"""
    Section:
        Clustering and show its result
"""


class ClusteringView(View):
    TEMPLATE_NAME = 'polls/logic/clustering.html'
    root_path = get_root_path()
    form_inital = {"ClusterAlgo": "KMeans"}


    def get(self, request, new_csv_store_name):
        df = read_csv_file(self.root_path + TMPDIRPATH + new_csv_store_name + ".csv")

        form = ClusteringForm(initial=self.form_inital)
        context = {
            "form": form,
            "tableName": new_csv_store_name,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)
        # rendering post and redirect to showing result

    # rendering post and redirect to showing result
    def post(self, request, new_csv_store_name):
        df = read_csv_file(self.root_path + TMPDIRPATH + new_csv_store_name + ".csv")
        form = ClusteringForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["Cluster_Algo"])
            # param = form.cleaned_data
            new_csv, train_stat = MyClustering(df, form.cleaned_data["Cluster_Algo"],
                                                   param=form.cleaned_data["Clustering_Parameters"])
            new_csv_description = new_csv_store_name.replace("_pre", "_result") + "-result"
            new_csv_store_name = new_csv_store_name.replace("_pre", "_result.csv")
            save_csv_file(new_csv, self.root_path + TMPDIRPATH + new_csv_store_name)
            # save this model to database
            # save_csv_model(new_csv_description, new_csv_store_name)
            request.session['clustering_stat'] = train_stat
            return redirect('/polls/CR_result/' + new_csv_store_name.replace(".csv", "") + "/")

        # if in this, means that form is invalid
        context = {
            "form": form,
            "tableName": new_csv_store_name,
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)


class CR_result(View):
    """
        This view is used to show clustering result
    """
    TEMPLATE_NAME = 'polls/logic/clustering_result.html'
    def get(self, request,new_csv_store_name):
        train_stat = request.session['clustering_stat']

        df = read_csv_file(ROOTPATH + TMPDIRPATH + new_csv_store_name+".csv")
        context = {
            "tableName": new_csv_store_name,
            "table": df_to_html(df),
            "stat" : train_stat
        }
        return render(request, self.TEMPLATE_NAME, context=context)

"""
    End Section
"""


"""
    Section: Association Rules
"""
class AssociationRuleView(View):
    TEMPLATE_NAME = 'polls/logic/association_rules.html'
    root_path = get_root_path()


    def get(self, request, new_csv_store_name):
        df = read_csv_file(self.root_path + TMPDIRPATH + new_csv_store_name + ".csv")
        frequent_itemsets,rules = do_association_rule(df)
        print(type(frequent_itemsets))
        print(type(rules))
        context = {
            "frequent_itemsets": df_to_html(frequent_itemsets),
            "rules": df_to_html(rules),
            "table": df_to_html(df)
        }
        return render(request, self.TEMPLATE_NAME, context=context)
"""
    Section: showing a specific doc
"""
class DocsView(View):
    """
    class for showing docs
    """
    TEMPLATE_ROOT = 'polls/docs/'
    def get(self,request,method,doc_name):
        if method == "CF":
            return render(request,self.TEMPLATE_ROOT+"classification/"+doc_name+".html")
        elif method == "CR":
            return render(request,self.TEMPLATE_ROOT+"cluster/"+doc_name+".html")

"""
    End Section
"""


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            if form.cleaned_data['title'].lower().endswith('.csv') is not True:
                messages.add_message(request, messages.INFO, 'Must be ending with CSV')
                return redirect('/polls/upload/')

            print("file name is " + form.cleaned_data['title'])
            save_upload_file(file, ROOTPATH + DATADIRPATH + form.cleaned_data["title"].lower())
            return redirect('/polls/table/'+form.cleaned_data['title'].lower().replace(".csv", ""))
    else:
        form = UploadFileForm()
    return render(request, 'polls/upload.html', {'form': form})

def delete_local_cache(request):
    print("in deleted local cache funciton")
    return redirect("/polls/about/")

def download_file(request,new_csv_store_name):
    root_path = get_root_path()
    file_path = root_path + TMPDIRPATH + new_csv_store_name + ".csv"
    print(file_path)
    CSV_file = open(file_path,'r').read()
    resp = HttpResponse(CSV_file, content_type='application/x-download')
    result_name = 'attachment;filename='+new_csv_store_name+".csv"
    resp['Content-Disposition'] = result_name
    return resp

def home(request):
    return render(request, 'polls/home.html')


def about(request):
    return render(request, 'polls/about.html')


