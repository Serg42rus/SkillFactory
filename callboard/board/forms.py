from django import forms
from .models import Advert, Respond


class AdvertForm(forms.ModelForm):
   class Meta:
       model = Advert
       fields =[
           'CategoryType',
           'title',
           'text',
           'author',
    ]


class RespondForm(forms.ModelForm):
   class Meta:
       model = Respond
       fields =[
           'respondAdvert',
           'text',
           'respondAuthor',
    ]