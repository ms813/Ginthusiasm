from django import forms
from ginthusiasm.models import Distillery

class DistillerySearchForm(forms.Form):
    NAME = 'name'

    distillery_name = forms.CharField(max_length=225, required=True)
