from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add-new-gif/', views.add_new_gif, name='add_new_gif'),
    path('add-new-category/', views.add_new_category, name='add_new_category'),
    path('category/<int:pk>/', views.category, name='category'),
    path('gif/<int:pk>/', views.gif, name='gif'),
    path('categories/', views.categories, name='categories'),
    path('liked-gifs/', views.liked_gifs, name='liked_gifs'),
]
