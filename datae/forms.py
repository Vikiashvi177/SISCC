from django import forms 
from .models import crudst, RFIDInfo

class stform(forms.ModelForm):
    class Meta:
        model = crudst
        fields = "__all__"

class RFIDInfoForm(forms.ModelForm):
    class Meta:
        model = RFIDInfo
        fields = "__all__"