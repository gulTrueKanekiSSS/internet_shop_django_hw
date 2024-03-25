from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from pytils.translit import slugify

from catalog.models import Users, Products, Categories, Contacts



# Create your views here.
class ProductListView(ListView):
    model = Products

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class CategoriesListView(ListView):
    model = Categories


class ContactCreateView(CreateView):
    model = Contacts
    fields = ('name', 'phone', 'message',)
    success_url = reverse_lazy('catalog:ProductsList')

    def form_valid(self, form):
        print(form.cleaned_data["name"])
        print(form.cleaned_data["phone"])
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Products

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        if self.object.views_counter == 100:
            subject = f'Товар {self.object.name}'
            text_content = f'Поздравляем, товар {self.object.name} собрал 100 просмотров!!'
            html_content = '<p>HTML версия сообщения</p>'
            from_email = 'zds.vip1221@gmail.com'
            to_email = ['dmitry.zahar201@yandex.ru']

            msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        return self.object


def registration(request):
    categories = list(Categories.objects.all())
    context = {'categories': categories}
    return render(request, 'catalog/registartion.html', context)


class ProductUpdateView(UpdateView):

    model = Products
    fields = ('name', 'description', 'price_for_unit', 'image',)

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.name)
            prod.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_page', args=[self.kwargs.get('pk')])


class ProductCreateView(CreateView):
    model = Products
    fields = ('name', 'description', 'price_for_unit', 'image',)
    success_url = reverse_lazy('catalog:ProductsList')

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.name)
            prod.save()
        return super().form_valid(form)





