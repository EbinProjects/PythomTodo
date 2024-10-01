from .models import TODO1
from django import forms


class TodoForms(forms.ModelForm):
    class Meta:
        model = TODO1
        fields = ['name', 'priority', 'datefield']
