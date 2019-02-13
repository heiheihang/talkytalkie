from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('test/', views.testing, name='test'),
    path('past_posts/', views.past_posts, name='past_posts')
]