from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django import forms
from .models import Tasting

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class TastinFormDatePicker(forms.ModelForm):
    tasting_date = DateField(widget=AdminDateWidget)

    class Meta:
        model = Tasting
        fields = ['tasting_date']
