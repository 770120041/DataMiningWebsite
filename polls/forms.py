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
        "LG": 'LogisticREgression',
        "KN": "KNeighborsClassifier",
        "SV": "SVC",
        "GB": "GradientBoostingClassifier",
        "DT": "DecisionTreeClassifier",
        "RF": "RandomForestClassifier",
        "MP": "MLPClassifier",
        "NB": "GaussianNB",
    }
    Class_method_Choice = ((k, v) for k, v in method_dict.items())
    method_selection = forms.ChoiceField(choices=Class_method_Choice,
                                         widget=RadioSelect)


class DelCacheForm(forms.Form):
    delete_cache = forms.BooleanField(required=True)
