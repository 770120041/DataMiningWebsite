from decimal import Decimal

from django import forms
from django.forms import RadioSelect
from django.utils.safestring import mark_safe

"""
    if add new methods, need to update:
        urls.py
        add new template
        add new view
"""


class PreprocessForm(forms.Form):
    method_dict = {
        "CF": "Classification",
        "CR": "Clustering",
        "AS": "AssociationRules",
    }
    Method_CHOICES = ((k, v) for k, v in method_dict.items())

    drop_missing = forms.BooleanField(required=False, help_text="Drop rows if there are missing slots.")
    digit_to_char = forms.BooleanField(required=False, help_text="Map non-numeric columns to numeric")
    method_selection = forms.ChoiceField(choices=Method_CHOICES)


class ClassificationForm(forms.Form):
    method_dict = {
        "LG": 'LogisticRegression',
        "KN": "KNeighborsClassifier",
        "SV": "SVC",
        "GB": "GradientBoostingClassifier",
        "DT": "DecisionTreeClassifier",
        "RF": "RandomForestClassifier",
        "MP": "MLPClassifier",
        "NB": "GaussianNB",
    }
    dict_train_raito = {
        "0.1": "0.1",
        "0.2": "0.2",
        "0.3": "0.3",
        "0.4": "0.4",
        "0.5": "0.5",
        "0.6": "0.6",
        "0.7": "0.7",
        "0.8": "0.8",
        "0.9": "0.9"
    }
    Class_Train_Ratio = ((k,v) for k,v in dict_train_raito.items())
    Class_method_Choice = ((k, v) for k, v in method_dict.items())
    method_selection = forms.ChoiceField(choices=Class_method_Choice,
                                         widget=forms.Select(attrs={'onchange': 'ajax_class_change();'})
                                         )
    classification_parameters = forms.CharField(widget=forms.TextInput, required=False)
    label_name = forms.CharField()

    train_ratio = forms.ChoiceField(choices=Class_Train_Ratio)
    # def __init__(self, targetChoices, *args, **kwargs):
    #     super(ClassificationForm, self).__init__(*args, **kwargs)
    #     targetTuple = {x[:2]:x for x in targetChoices}
    #     print(targetTuple)
    #     self.target_column = forms.ChoiceField(choices=targetChoices)



    # target_column = forms.CharField(widget=forms.TextInput, required=True)

class DelCacheForm(forms.Form):
    delete_cache = forms.BooleanField(required=True)
