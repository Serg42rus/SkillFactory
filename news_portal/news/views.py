from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from accounts.forms import *
from .models import *
from .filters import PostFilter
from news.forms import PostForm, SubscribeForm
from django.core.cache import cache


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
    paginate_by = 1
    # raise_exception = True


class PostDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'
    # raise_exception = True


class SearchPost(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'post'
    paginate_by = 1

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ArticleCreate(CreateView):
    """ Представление для создания статьи. """
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить статью"
        return context



class ArticleUpdate(UpdateView):
    """ Представление для редактирования статьи. """
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать статью"
        return context


class ArticleDelete(DeleteView):
    """ Представление для удаления статьи. """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить статью"
        context['previous_page_url'] = reverse_lazy('news')
        return context


class NewsCreate(CreateView):
    """ Представление для создания новости. """
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить новость"
        return context


class NewsUpdate(UpdateView):
    """ Представление для редактирования новости. """
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать новость"
        return context


class NewsDelete(DeleteView):
    """ Представление для удаления новости. """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить новость"
        context['previous_page_url'] = reverse_lazy('news')
        return context


class SubscribersView(LoginRequiredMixin, CreateView):
    template_name = 'subscribers.html'
    form_class = SubscribeForm
    model = Subscribers
    context_object_name = 'subscribers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self,form):
        user = self.request.user
        form.instance.user = User.objects.get(pk=user.id)
        self.object = form.save()
        return redirect('/')