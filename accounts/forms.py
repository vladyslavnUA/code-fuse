from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import django.contrib.auth.forms as auth_forms
from .models import Developer

class SignUpForm(UserCreationForm):
    '''A form that handles registering new users.'''
    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name', 'last_name',
                  'password1', 'password2'
                  ]

    def save(self, commit=True):
        '''Initializes fields of the new User instance.'''
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit is True:
            user.save()

        return user


class StatusForm(forms.ModelForm):
    '''A form for users confirming status as a developer.'''
    class Meta:
        model = Developer
        fields = ['developer']