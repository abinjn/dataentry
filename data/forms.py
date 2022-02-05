from django import forms
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.forms import fields, widgets
from .models import Profile


class DateInput(forms.DateInput):
    input_type = 'date'

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields =    ['name', 'grade', 'school', 'email', 'parent_name',
         'contact_number', 'alternate_contact_number', 'enquiry_source', 'enquiry_date', 'remark']
        widgets = {
            'enquiry_date': DateInput(),
        }
        
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length = 100, required=False)