from django import forms
from .models import Tasting

from django.contrib.admin import widgets

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class TastinFormDatePicker(forms.ModelForm):
    tasting_date = forms.DateField(widget=forms.DateInput(attrs={"format":"mm/dd/YYYY", 'placeholder':"Formato 12/12/2018"}))
    class Meta:
        model = Tasting
        fields = ['tasting_date']
        help_texts = {'tasting_date': "Data no formato YYYY-MM-DD"}
