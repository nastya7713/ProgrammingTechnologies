from django import forms
from django.core import validators
from .models import *
from django.core.exceptions import ValidationError
from .admin import *

class RegisterListForm(forms.ModelForm):

    def __init__(self, faculty=None, register_enrollees=None, **kwargs):
        super(RegisterListForm, self).__init__(**kwargs)
        self.fields['faculty'].required = True

    def has_changed(self):
        super(RegisterListForm, self).has_changed()
        print("changed")

    class Meta:
        model = RegisterList
        fields =('faculty', 'register_enrollees')

    def clean(self):
        register_enrollees = self.cleaned_data.get('register_enrollees')
        limit = self.cleaned_data.get('faculty').faculty_limit
        if register_enrollees and register_enrollees.count() > limit:
            raise ValidationError('Faculty limit error')
        return self.cleaned_data
