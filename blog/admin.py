from django.contrib import admin

from blog.models import Poster


@admin.register(Poster)
class PostersAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'view_count',)
    list_filter = ('is_published',)
    search_fields = ('title',)
