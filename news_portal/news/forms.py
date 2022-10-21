from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Post, Subscribers


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = '__all__'

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get("заголовок")
       if title is not None and len(title) < 5:
           raise ValidationError({})
       name = cleaned_data.get("name")
       if name == title:
           raise ValidationError()
       return cleaned_data


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribers
        fields = ['category_subscribers']