from django.urls import path

from catalog.views import ProductListView, ProductDetailView, registration, ProductCreateView, ContactCreateView, \
    VersionDetailView, ProductUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='ProductsList'),
    path('contacts/', ContactCreateView.as_view(), name='create_contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_page'),
    path('register/', registration),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('version_product/<int:pk>', VersionDetailView.as_view(), name='get_version'),
]