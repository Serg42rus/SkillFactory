from django.urls import path, include
from .views import *


urlpatterns = [
    path('news/', PostList.as_view(), name='news'),
    path('news/<int:pk>/', PostDetail.as_view()),
    path('news/search/', SearchPost.as_view(), name='news'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscribers/', SubscribersView.as_view(), name='Subscribers'),

]