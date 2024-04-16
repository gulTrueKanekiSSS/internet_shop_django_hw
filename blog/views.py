from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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


class PosterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_poster'
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


class PosterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    model = Poster
    form_class = PosterForm
    success_url = reverse_lazy('blog:main_page')
    permission_required = 'blog.add_poster'

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.title)
            prod.save()
            form.instance.creator = self.request.user
        return super().form_valid(form)


class PosterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    login_url = reverse_lazy('users:login')
    redirect_field_name = 'next'

    model = Poster
    success_url = reverse_lazy('blog:main_page')
    permission_required = 'blog.delete_poster'


class UserPostsListView(LoginRequiredMixin, PosterListView):
    model = Poster

    def get_queryset(self):
        user = self.request.user
        return Poster.objects.filter(creator=user)