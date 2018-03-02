# -*- encoding: utf-8 -*-
from django import forms
from .models import BarCodeModel


class BarCodeModelForm(forms.ModelForm):
    class Meta:
        model = BarCodeModel
        exclude = ['id']


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=200)
    file = forms.FileField(required=False)



