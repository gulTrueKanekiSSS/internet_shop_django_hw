from django.urls import path

from catalog.views import home, contacts, product_page, go_to_product, registration, make_product

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('product/<int:product_id>/', product_page, name='product_page'),
    path('go_to_product/', go_to_product, name='go_to_product'),
    path('register/', registration),
    path('create_product/', make_product)
]