from django import forms
from ginthusiasm.models import Article
import datetime

class AddArticleForm(forms.ModelForm):
    #image = forms.ImageField(widget=forms.HiddenInput(), required=False, initial="articles/jan_gin.jpg")

    class Meta:
        model = Article
        fields = (
            'title',
            'shortDesc',
            'content',
            'author',
            'month',
            'date',
            'slug',
            'image',
        )
