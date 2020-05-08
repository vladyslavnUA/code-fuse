from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    '''A form to handle creating and updating Codes.'''
    class Meta:
        model = Project
        exclude = [
            'slug',
            'date_posted',
            'last_revised',
            'posted_by',
        ]