from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('add-film/', views.FilmCreateView.as_view(), name='add_film'),
    path('add-director/', views.DirectorCreateView.as_view(), name='add_director'),
    path('add-review/', views.ReviewCreateView.as_view(), name='add_review'),
    path('update-film/<pk>', views.FilmUpdateView.as_view(), name='update_film'),
    path('update-director/<pk>', views.DirectorUpdateView.as_view(), name='update_director'),
    path('delete-film/<pk>', views.FilmDeleteView.as_view(), name='delete_film'),
    path('favorite-film/<pk>', views.FavoriteFilmView.as_view(), name='favorite_film'),
    path('film-detail/<pk>', views.FilmDetailView.as_view(), name='film_detail'),
]
