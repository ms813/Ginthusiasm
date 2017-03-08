from django import forms
from ginthusiasm.models import Review
from datetime import datetime, date

class ReviewForm(forms.ModelForm):

    date = forms.DateField(widget=forms.HiddenInput(), initial = date.today)
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial =0,)
    #content = forms.CharField()
    lat = forms.FloatField(initial =4.5)
    long = forms.FloatField(initial =6.7)
    #gin = forms.FloatField(help_text="Gin: ")
    #user = forms.FloatField(help_text="User")

    class Meta:
        model = Review
        fields = ['date','rating', 'content', 'lat', 'long',]
        widgets = {
            'content': forms.TextInput(
                attrs={'id': 'review_content', 'required': True, 'placeholder': 'Say something...'}
            ),
        }
