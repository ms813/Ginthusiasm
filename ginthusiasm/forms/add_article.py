from django import forms
from ginthusiasm.models import Article
from datetime import datetime, date

class AddArticleForm(forms.ModelForm):

    title= forms.CharField(label='Article title')
    shortDesc = forms.CharField(widget=forms.Textarea, label='Enter a short description')
    content = forms.CharField(widget=forms.Textarea, label='Main content')
    date = forms.DateField(widget=forms.HiddenInput(), initial = date.today)
    image = forms.ImageField(label='Upload image')
    month = forms.BooleanField(label='Gin of the month?')

    class Meta:
        model = Article
        fields = (
            'title',
            'shortDesc',
            'content',
            'month',
            'date',
            'image',
        )
