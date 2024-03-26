from django.urls import path

from blog.apps import BlogConfig
from blog.views import PosterListView, PosterDetailView, PosterCreateView, PosterUpdateView, PosterDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('posts/', PosterListView.as_view(), name='main_page'),
    path('post/<int:pk>', PosterDetailView.as_view(), name='post'),
    path('create_post/', PosterCreateView.as_view(), name='create_post'),
    path('edit/<int:pk>', PosterUpdateView.as_view(), name='edit_post'),
    path('delete/<int:pk>', PosterDeleteView.as_view(), name='delete_post'),

]