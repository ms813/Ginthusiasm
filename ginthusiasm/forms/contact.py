from django import forms
from ginthusiasm.models import Contact
from datetime import datetime, date

class ContactForm(forms.ModelForm):

    name = forms.CharField()
    email = forms.EmailInput()
    message = forms.CharField(widget=forms.Textarea)

    date = forms.DateField(widget=forms.HiddenInput(), initial = date.today)

    class Meta:
        model = Contact
        fields = ('date','name', 'email', 'message',)
