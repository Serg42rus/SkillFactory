from django import template

register = template.Library()


CATEGORY_CHOICES = {
        'TANK': 'танк',
        'HILL': 'хиллы',
        'DD': 'ДД',
        'DILLER': 'торговец',
        'GILDMASTER': 'гилдмастер',
        'QUEST': 'Квестгивер',
        'SMITH': 'Кузнец',
        'SKINNER': 'Кожевник',
        'WITCH': 'Зельевар',
        'WIZARD': 'Мастер заклинаний',
}


@register.filter()
def category(value, code='DD'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
   postfix = CATEGORY_CHOICES[code]

   return f'{value}{postfix}'