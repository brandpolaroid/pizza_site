from django import forms
from django.forms import TextInput, NumberInput, ModelForm


class AddOrder(forms.Form):
    name = forms.CharField(max_length=20, label="Имя")
    phone = forms.CharField(max_length=20, label="Номер")
    address = forms.CharField(max_length=300, label="Адрес")
