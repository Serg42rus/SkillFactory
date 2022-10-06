from django.urls import path
from .views import *


urlpatterns = [
    path('news/', PostList.as_view(), name='news'),
    path('news/<int:pk>/', PostDetail.as_view()),
]