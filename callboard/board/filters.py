from django_filters import FilterSet

from .models import Advert

class AdvertFilter(FilterSet):
   class Meta:
       model = Advert
       fields = {
           'CategoryType': ['icontains'],
       }