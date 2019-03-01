from django import forms



"""
    if add new methods, need to update:
        urls.py
        add new template
        add new view
"""
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


class Classification(forms.Form):
    pass


class DelCacheForm(forms.Form):
    delete_cache = forms.BooleanField(required=True)
