from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from pytils.translit import slugify

from blog.forms import PosterForm
from blog.models import Poster


# Create your views here.

class PosterListView(ListView):
    model = Poster

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class PosterDetailView(DetailView):
    model = Poster

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class PosterUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    model = Poster
    form_class = PosterForm

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.title)
            prod.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', args=[self.kwargs.get('pk')])


class PosterCreateView(LoginRequiredMixin, CreateView):

    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    model = Poster
    form_class = PosterForm
    success_url = reverse_lazy('blog:main_page')

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.title)
            prod.save()
        return super().form_valid(form)


class PosterDeleteView(LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    model = Poster
    success_url = reverse_lazy('blog:main_page')