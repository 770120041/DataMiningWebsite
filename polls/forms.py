from django import forms

class Preprocess(forms.Form):
    Classification = 'CF'
    Clustering = 'CR'
    AssociationRules = 'AS'
    CHOICES = ((Classification, "Classification"),
               (Clustering, 'Clustering'),
               (AssociationRules, "AssociationRules"))

    drop_missing = forms.BooleanField(required=False)
    digit_to_char = forms.BooleanField(required=False)
    method_selection = forms.ChoiceField(choices=CHOICES)
    # pre = forms.CharField(label="what to do", max_length=100)