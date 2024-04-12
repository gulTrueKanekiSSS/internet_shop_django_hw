from django.contrib import admin

from catalog.models import Products, Categories, Contacts, VersionProduct


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_for_unit', 'category', 'creator',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message',)
    search_fields = ('name', 'phone',)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(VersionProduct)
class VersionProductAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_num')

