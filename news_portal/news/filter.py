import django_filters
from .models import *
import django.forms
import re
from django import template
from pathlib import Path


class PostFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        field_name='title', label='Заголовок содержит', lookup_expr='icontains')


    Category = django_filters.ModelMultipleChoiceFilter(
        field_name='category', label='Искать в категориях', lookup_expr='exact', queryset=Category.objects.all())


    DateCreation__gt = django_filters.DateFilter(
        field_name="date_time", label="От даты", lookup_expr='gt')

    DateCreation__lt = django_filters.DateFilter(
        field_name="date_time", label="До даты", lookup_expr='lt'),


register = template.Library()


@register.filter()
def censor(post_text):

    key_words = Path(__file__).resolve().parent.joinpath('censored_words.txt').read_text(encoding='utf-8')
    key_words = [word.strip() for word in key_words.split()]
    for word in key_words:
        pattern = f'\\b{word}\\b'
        post_text = re.sub(pattern, f"{word[0]}{(len(word)-2) * '*'}{word[-1]}", post_text, flags=re.I)
    return post_text