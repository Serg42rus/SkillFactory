from django import forms
from django.core.exceptions import ValidationError
from .models import Post


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