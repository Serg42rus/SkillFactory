from django.urls import path
from .views import *


urlpatterns = [
    path('advert/', AdvertList.as_view(), name='advert'),
    path('advert/<int:pk>/', AdvertDetail.as_view(), name='advert_detail'),
    path('advert/create/', AdvertCreate.as_view(), name='advert_create'),
    path('advert/<int:pk>/update/', AdvertUpdate.as_view(), name='advert_update'),
    path('advert/<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    path('respond/', RespondList.as_view(), name='respond'),
    path('respond/create/', RespondCreate.as_view(), name='respond_create'),
    path('respond/<int:pk>/update/', RespondUpdate.as_view(), name='respond_update'),
    path('respond/<int:pk>/delete/', RespondDelete.as_view(), name='respond_delete'),
]
