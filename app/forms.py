from django import forms
from django.forms import fields
from app.models import Messagebox


class Form1(forms.ModelForm):
    class Meta:
       model = Messagebox
       fields = '__all__'


