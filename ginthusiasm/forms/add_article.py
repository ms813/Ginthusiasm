from django import forms
from ginthusiasm.models import Article
import datetime

class AddArticleForm(forms.ModelForm):

    date = forms.DateField(widget=forms.HiddenInput(), initial=datetime.date.today())
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    #image = forms.ImageField(widget=forms.HiddenInput(), required=False, initial="articles/jan_gin.jpg")

    class Meta:
        model = Article
        fields = (
            'title',
            'shortDesc',
            'content',
            'author',
            'month',
        )
