from django.urls import path

from catalog.views import ProductListView, ProductDetailView, registration, ProductCreateView, ContactCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='ProductsList'),
    path('contacts/', ContactCreateView.as_view(), name='create_contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_page'),
    path('register/', registration),
    path('create_product/', ProductCreateView.as_view(), name='create_product')
]