# # blog/urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),
#     path('category/<str:category_name>/', views.posts_by_category, name='posts_by_category'),
# ]

# blog/urls.py
from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView # NEW

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<str:category_name>/', views.posts_by_category, name='posts_by_category'),
    # --- NEW URLS for CRUD ---
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
