from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .filters import AdvertFilter
from .forms import AdvertForm, RespondForm
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from django.dispatch import receiver


@receiver(post_save, sender=Respond)
def notify_managers_respond(sender, instance, created, **kwargs):
    subject = f'{instance.text}'

    mail_managers(
        subject=subject,
        message=instance.text,
    )
post_save.connect(notify_managers_respond, sender=Respond)


class AdvertList(ListView):
    model = Advert
    ordering = 'dateCreation'
    template_name = 'advert.html'
    context_object_name = 'advert'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdvertFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AdvertDetail(DetailView):
    model = Advert
    template_name = 'advert_detail.html'
    context_object_name = 'advert'
    pk_url_kwarg = 'pk'


class RespondList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Respond
    template_name = 'respond.html'
    context_object_name = 'respond'


class AdvertCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AdvertForm
    model = Advert
    template_name = 'advert_edit.html'


class AdvertUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = AdvertForm
    model = Advert
    template_name = 'advert_edit.html'


class AdvertDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Advert
    template_name = 'advert_delete.html'
    success_url = reverse_lazy('advert')


class RespondCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = RespondForm
    model = Respond
    template_name = 'respond_edit.html'


class RespondUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = RespondForm
    model = Respond
    template_name = 'respond_edit.html'


class RespondDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Respond
    template_name = 'respond_delete.html'
    success_url = reverse_lazy('advert')