from django import forms

class select_method(forms.Form):
    renewal_date = forms.ChoiceField()