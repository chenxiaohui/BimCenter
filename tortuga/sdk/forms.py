#!/usr/bin/python
#coding=
#Filename:forms.py
from django import forms
from django.forms import ModelForm,Form
from models import SRL

class ModelUploadForm(Form):
    file = forms.FileField(required=True)

class SRLUploadForm(ModelForm):
    """"""
    class Meta(object):
        """"""
        model = SRL

class SRLChooseForm(Form):
    """"""
    srl = forms.ChoiceField(choices=[ (o.id, o.name) for o in SRL.objects.all()]) 
