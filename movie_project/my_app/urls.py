from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import all_movies, all_series, movie_detail, add_to_watchlist, my_watchlist, series_detail, \
    SearchResultsView

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('all-movies/', views.all_movies, name='all_movies'),
    path('series/', views.all_series, name='all_series'),
    path('kids/', views.all_kids, name='all_kids'),
    path('malayalam/', views.malayalam_view, name='malayalam'),
    path('tamil/', views.tamil_view, name='tamil'),
    path('languages/', views.languages_view, name='languages'),
    path('malayalam-romantic/', views.malayalam_romantic_movies, name='malayalam_romantic'),
    path('english-action/', views.en_action_movies, name='english_action'),
    path('romance-romance/', views.en_romance_movies, name='eng_romance'),
    path('high_rated_movies/', views.high_rated_movies, name='high_rated_movies'),
    path('movies_2023/', views.movies_2023, name='movies_2023'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('popular-media/', views.popular_media, name='popular_media'),
    path('english/', views.english_list, name='english_genre'),
    path('thriller/', views.en_thriller_view, name='eng_thriller'),
    path('comedy/', views.en_comedy_view, name='eng_comedy'),
    path('film/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('series/<int:series_id>/', series_detail, name='series_detail'),
    path('film/<int:movie_id>/add_to_watchlist/', add_to_watchlist, name='add_to_watchlist'),
    path('mywatchlist/', my_watchlist, name='my_watchlist'),
    path('search/',SearchResultsView.as_view(),name='search'),


]

