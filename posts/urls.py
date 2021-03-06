from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.create_post, name='create'),
    path('<int:post_id>/', views.detail_post, name='detail'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
    path('<int:post_id>/review/', views.create_review, name='review'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create', views.CategoryCreateView.as_view(), name='create-category'),
]