from dataclasses import fields
from django import forms
from .models import *

class TreaineesForms(forms.ModelForm):
    class Meta:
        model = Trainees
        fields = "__all__"
        