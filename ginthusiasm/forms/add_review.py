from django import forms
from ginthusiasm.models import Review
from datetime import datetime, date

class ReviewForm(forms.ModelForm):

    date = forms.DateField(widget=forms.HiddenInput(), initial = date.today,required=False)
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial =0)
    content = forms.TextInput()
    lat = forms.FloatField(widget=forms.HiddenInput(),required=False)
    lng = forms.FloatField(widget=forms.HiddenInput(),required=False)
    postcode = forms.CharField(required=False)
    #gin = forms.FloatField(help_text="Gin: ")
    #user = forms.FloatField(help_text="User")

    class Meta:
        model = Review
        fields = ['date','rating', 'content', 'lat', 'lng', 'postcode']
