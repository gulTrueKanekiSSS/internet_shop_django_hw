from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.mail import EmailMultiAlternatives

from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify
from catalog.forms import ProductForm, ContactForm
from catalog.models import Products, Categories, Contacts, VersionProduct


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



class ProductUpdateView(PermissionRequiredMixin ,LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Products
    form_class = ProductForm
    # permission_required = ('catalog.change_products',)

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

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.creator

    def get_success_url(self):
        return reverse('catalog:product_page', args=[self.kwargs.get('pk')])

class ProductDeleteView(PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Products
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:ProductsList')
    # permission_required = ('catalog.delete_products',)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.creator


class ProductCreateView(LoginRequiredMixin, CreateView):

    redirect_field_name = 'next'

    model = Products
    form_class = ProductForm
    success_url = reverse_lazy('catalog:ProductsList')
    # permission_required = ('catalog.add_products',)

    def form_valid(self, form):
        if form.is_valid():
            prod = form.save()
            prod.slug = slugify(prod.name)
            prod.save()
            VersionProduct.objects.create(product=prod, version_name='Initial Version')
            form.instance.creator = self.request.user
        return super().form_valid(form)


class VersionDetailView(DetailView):
    model = VersionProduct


class UserProductsListView(ListView):
    model = Products

    def get_queryset(self):
        user = self.request.user
        return Products.objects.filter(creator=user)



