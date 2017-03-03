from django import forms
from ginthusiasm.models import Article
from datetime import datetime, date

class AddArticleForm(forms.ModelForm):

    date = forms.DateField(widget=forms.HiddenInput(), initial = date.today)
    content = forms.Textarea()

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
