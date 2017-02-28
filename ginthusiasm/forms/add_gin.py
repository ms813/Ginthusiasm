from django import forms
from ginthusiasm.models import Gin, TasteTag

class AddGinForm(forms.ModelForm):
    class Meta:
        model = Gin
        fields = (
            'name',
            'price',
            'short_description',
            'long_description',
            'abv',
            'taste_tags',
            'image',
        )
