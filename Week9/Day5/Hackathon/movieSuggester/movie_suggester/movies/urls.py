from django.urls import path
from . import views

urlpatterns = [
    path('api/<category>/<int:page>', views.GetMovies.as_view(), name='movies'),
    path('api/discover/<category>/<int:page>', views.Discover.as_view(), name='discover'),
    path('api/search/<category>/<query>/<int:page>', views.Search.as_view(), name='search'),
    path('api/favorites/', views.Favorites.as_view(), name='favorites'),
    path('api/watched/', views.Watched.as_view(), name='watched'),
    path('api/watchlist/', views.Watchlist.as_view(), name='watchlist'),
    path('movie-check/<int:movie_id>', views.MovieCheck.as_view(), name='movie_check'),
]
