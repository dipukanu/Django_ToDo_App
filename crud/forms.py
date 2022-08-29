from django import forms
from .models import mytask

class task_form(forms.ModelForm):
    class Meta:
        model=mytask
        fields="__all__"
    
        labels={
            'task':'Task:'
        }

        widgets={
            'task':forms.TextInput(attrs={'placeholder':'Enter your task'})
        }