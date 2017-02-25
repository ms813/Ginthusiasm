from django import forms
from ginthusiasm.models import Gin, TasteTag

class GinSearchForm(forms.Form):
    NAME = 'name'
    PRICE = 'price'
    RATING = 'average_rating'
    #DISTILLERY = 'distillery'
    ORDER_BY_CHOICES = (
        (NAME, 'Gin Name'),
        (PRICE, 'Price'),
        (RATING, 'Average Rating'),
    #    (DISTILLERY, 'Distillery Name'),
    )

    ASCENDING = 'ASC'
    DESCENDING = 'DESC'
    ORDER_ORDER_CHOICES = (
        (ASCENDING, 'Ascending'),
        (DESCENDING, 'Descending'),
    )

    keywords = forms.CharField(max_length=128, required=False)
    min_price = forms.FloatField(min_value=0.0, required=False)
    max_price = forms.FloatField(min_value=0.0, required=False)
    min_rating = forms.FloatField(min_value=0.0, max_value=5.0, required=False)
    max_rating = forms.FloatField(min_value=0.0, max_value=5.0, required=False)
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES)
    order = forms.ChoiceField(choices=ORDER_ORDER_CHOICES)
    # taste_tags = forms.MultipleChoiceField(choices=TasteTag.objects.all, required=False)
    # distillery = forms.CharField(max_length=128, required=False)

    # Add more fields to filter be groups of distilleries e.g. All Scottish distilleries
    # Add more fields to filter by location of reviews?
