from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from pytils.translit import slugify
from catalog.forms import ProductForm, ContactForm
from catalog.models import Users, Products, Categories, Contacts, VersionProduct


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
    # fields = ('name', 'phone', 'message',)
    form_class = ContactForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        version_product = product.versionproduct_set.first()
        if version_product:
            context['version'] = version_product.version_num
        return context


def registration(request):
    categories = list(Categories.objects.all())
    context = {'categories': categories}
    return render(request, 'catalog/registartion.html', context)


class ProductUpdateView(UpdateView):

    model = Products
    form_class = ProductForm

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save(commit=False)
            prod.slug = slugify(prod.name)
            version_product = VersionProduct.objects.get(product=prod)

            major, minor, patch = version_product.version_num.split('.')
            patch = int(patch) + 1
            if patch > 9:
                patch = 0
                minor = int(minor) + 1
                if minor > 9:
                    minor = 0
                    major = int(major) + 1

            version_product.version_num = f"{major}.{minor}.{patch}"
            version_product.save()

            prod.save()


        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product_page', args=[self.kwargs.get('pk')])


class ProductCreateView(CreateView):
    model = Products
    # fields = ('name', 'description', 'price_for_unit', 'image',)
    form_class = ProductForm
    success_url = reverse_lazy('catalog:ProductsList')

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.name)
            prod.save()
            VersionProduct.objects.create(product=prod, version_name='Initial Version')
        return super().form_valid(form)


class VersionDetailView(DetailView):
    model = VersionProduct

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     version =

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     version = self.object.version_num
    #     major, minor, patch = version.split('.')
    #     patch = int(patch) + 1
    #     if patch > 9:
    #         patch = 0
    #         minor = int(minor) + 1
    #         if minor > 9:
    #             minor = 0
    #             major = int(major) + 1
    #     version = f"{major}.{minor}.{patch}"
    #     self.object.version_num = version
    #     self.object.save()
    #
    #     return self.object



