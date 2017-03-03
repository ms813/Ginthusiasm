from django import forms
from ginthusiasm.models import Review
from datetime import datetime, date

class ReviewForm(forms.ModelForm):

    date = forms.DateField(widget=forms.HiddenInput(), initial = date.today)

    rating = forms.IntegerField(initial =0, help_text="Rating: ")
    summary = forms.CharField(help_text="Summary: ")
    content = forms.CharField(help_text="Content: ")
    lat = forms.FloatField(help_text="Lat: ")
    long = forms.FloatField(help_text="Long: ")
    #gin = forms.FloatField(help_text="Gin: ")
    #user = forms.FloatField(help_text="User")

    class Meta:
        model = Review
        fields = ('date','rating', 'summary', 'content', 'lat', 'long',)
