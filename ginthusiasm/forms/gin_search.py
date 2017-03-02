from django import forms
from ginthusiasm.models import Gin, TasteTag

class GinSearchForm(forms.Form):
    RELEVANCE = 'relevance'
    NAME_AZ = 'name'
    NAME_ZA = '-name'
    PRICE_LO = 'price'
    PRICE_HI = '-price'
    RATING_LO = 'average_rating'
    RATING_HI = '-average_rating'

    ORDER_BY_CHOICES = (
        (RELEVANCE, 'Relevance'),
        (NAME_AZ, 'Gin Name - A to Z'),
        (NAME_ZA, 'Gin Name - Z to A'),
        (PRICE_LO, 'Price - Low to High'),
        (PRICE_HI, 'Price - High to Low'),
        (RATING_LO, 'Average Rating - Low to High'),
        (RATING_HI, 'Average Rating - High to Low'),
    )

    keywords = forms.CharField(max_length=128, required=False)
    min_price = forms.FloatField(min_value=0.0, required=False)
    max_price = forms.FloatField(min_value=0.0, required=False)
    min_rating = forms.FloatField(min_value=0.0, max_value=5.0, required=False)
    max_rating = forms.FloatField(min_value=0.0, max_value=5.0, required=False)
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES)

    # Add more fields to filter be groups of distilleries e.g. All Scottish distilleries
    # Add more fields to filter by location of reviews?
