from django.http import HttpResponse
from polls.csv_handler import *
from django.shortcuts import render, get_object_or_404
import os
from django.views import View
from polls.models import *

class TableView(View):
    TABLE_PATH = {
        1:"polls\\data\\1_3cweka.csv",
        2:"polls\\data\\2_chinese_stock.csv",
        3:"polls\\data\\3_license_plate.csv",
        4:"polls\\data\\4_hapiness.csv"
    }
    TEMPLATE_NAME =  'polls/index.html'
    table_number = 1

    def get(self, request):
        return render(request, self.TEMPLATE_NAME, {'table': csv_to_html(self.TABLE_PATH[self.table_number])})


def home(request):
    return render(request, 'polls/index.html', {'table':"homepage"})


def table1(request):
    return render(request, 'polls/index.html', {'table': csv_to_html("polls\\data\\1_3cweka.csv")})

def table2(request):
    return render(request, 'polls/index.html', {'table': csv_to_html("polls\\data\\2_chinese_stock.csv")})

def table3(request):
    return render(request, 'polls/index.html', {'table': csv_to_html("polls\\data\\3_license_plate.csv")})

def table4(request):
    return render(request, 'polls/index.html',{'table': csv_to_html("polls\\data\\4_hapiness.csv")})

# def renew_book_librarian(request, pk):
#     book_instance = get_object_or_404(BookInstance, pk=pk)
#
#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#
#         # Create a form instance and populate it with data from the request (binding):
#         form = RenewBookForm(request.POST)
#
#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             book_instance.due_back = form.cleaned_data['renewal_date']
#             book_instance.save()
#
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('all-borrowed') )
#
#     # If this is a GET (or any other method) create the default form.
#     else:
#         proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
#         form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
#
#     context = {
#         'form': form,
#         'book_instance': book_instance,
#     }
#
#     return render(request, 'catalog/book_renew_librarian.html', context)
#
# def select_mode():
#     pass

def about(request):
    return render(request, 'polls/about.html')


def index(request):
    num_dataFrame = DataFrameModel.objects.all().count()
    context = {
        'num_books': num_dataFrame
    }
    return render(request, 'index.html', context=context)
