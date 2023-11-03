from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Films, English, Series, UserProfile, WatchlistItem, Kids


def all_movies(request):
    all_movies = Films.objects.filter(Type='movie')
    return render(request, 'movies.html', {'movies': all_movies})


def all_series(request):
    all_series = Series.objects.all()
    return render(request, 'series.html', {'all_series': all_series})


def all_kids(request):
    all_kids = Kids.objects.all()
    return render(request, 'kids.html', {'kids': all_kids})


def HomePage(request):
    return render(request, 'filmlist.html')


@login_required
def movie_detail(request, movie_id):
    film = Films.objects.get(pk=movie_id)
    related_movies = Films.objects.filter(genre=film.genre).exclude(pk=movie_id)[:6]
    return render(request, 'details.html', {'object': film, 'related_movies': related_movies})


@login_required
def series_detail(request, series_id):
    series = Series.objects.get(pk=series_id)
    return render(request, 'series_details.html', {'object': series})


@login_required
def add_to_watchlist(request, movie_id):
    film = Films.objects.get(pk=movie_id)

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    watchlist_item, created = WatchlistItem.objects.get_or_create(user=user_profile, film=film)
    if created:
        watchlist_item.save()

    return redirect('my_watchlist')


@login_required
def my_watchlist(request):
    # Assuming you have a user profile associated with the logged-in user
    user_profile = request.user.userprofile
    watchlist = WatchlistItem.objects.filter(user=user_profile)
    return render(request, 'watchlist.html', {'watchlist': watchlist})


def malayalam_view(request):
    return render(request, 'malayalam.html')


def tamil_view(request):
    return render(request, 'tamil.html')


def languages_view(request):
    return render(request, 'languages.html')


def malayalam_romantic_movies(request):
    malayalam_romantic_movies = Films.objects.filter(language='Malayalam', genre='Romance')
    return render(request, 'malayalamromantic.html', {'movies': malayalam_romantic_movies})


def en_action_movies(request):
    english_action_movies = Films.objects.filter(language='English', genre='Action')
    return render(request, 'eng_action_movies.html', {'movies': english_action_movies})


def en_romance_movies(request):
    english_romance_movies = Films.objects.filter(language='English', genre='Romance')
    return render(request, 'english_romane.html', {'movies': english_romance_movies})


def high_rated_movies(request):
    high_rated_movies = Films.objects.filter(Type='movie', rating__gt=8)
    return render(request, 'high_rated_movies.html', {'movies': high_rated_movies})


def movies_2023(request):
    movies_2023 = Films.objects.filter(year=2023)
    return render(request, 'movie_2023.html', {'movies_2023': movies_2023})


def popular_media(request):
    popular_movies = Films.objects.filter(populor=True, Type='Movie')[:10]
    popular_series = Films.objects.filter(populor=True, Type='Web series')[:10]
    return render(request, 'popular_media.html', {'popular_movies': popular_movies, 'popular_series': popular_series})


def english_list(request):
    english_entries = English.objects.all()
    return render(request, 'english.html', {'english_entries': english_entries})


def en_thriller_view(request):
    english_entries_thriller = English.objects.filter(genre='thriller')
    return render(request, 'thriller_template.html', {'english_entries': english_entries_thriller})


def en_comedy_view(request):
    english_entries_comedy = English.objects.filter(genre='comedy')
    return render(request, 'comedy_template.html', {'english_entries': english_entries_comedy})


class SearchResultsView(ListView):
    template_name = 'searchview.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            movies_results = Films.objects.filter(
                Q(title__icontains=query) |
                Q(year__icontains=query) |
                Q(language__icontains=query) |
                Q(genre__icontains=query)
            )
            series_results = Series.objects.filter(
                Q(title__icontains=query) |
                Q(language__icontains=query) |
                Q(genre__icontains=query)
            )
            search_results = list(movies_results) + list(series_results)
            return search_results
            return []

