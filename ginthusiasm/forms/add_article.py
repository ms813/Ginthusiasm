from django import forms
from ginthusiasm.models import Article

class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'shortDesc',
            'content',
            'date',
            'slug',
            'author',
            'image',
            'month',
        )
