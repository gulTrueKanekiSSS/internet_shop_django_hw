from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactCreateView, \
    VersionDetailView, ProductUpdateView, ProductDeleteView, UserProductsListView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='ProductsList'),
    path('contacts/', ContactCreateView.as_view(), name='create_contact'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_page'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product_page'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('edit_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('version_product/<int:pk>', VersionDetailView.as_view(), name='get_version'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('user_products/', UserProductsListView.as_view(), name='user_products'),

]
