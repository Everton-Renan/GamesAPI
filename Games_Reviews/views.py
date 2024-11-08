from django.db.models import Q
from django.http import (Http404, HttpRequest, HttpResponse,
                         HttpResponseNotAllowed, JsonResponse)
from django.shortcuts import render

from Games_Reviews.models import GenerateKeys, Review, User


def return_data(request: HttpRequest, username: str, key: str):
    if request.method == 'POST':
        return HttpResponseNotAllowed(['GET'])
    user = User.objects.filter(username=username)
    _key = GenerateKeys.objects.filter(user_id=user.get().pk)
    if key != _key.get().key:
        return JsonResponse({'error': 'Incorrect key.'}, status=404)
    games = Review.objects.all().values(
        'title',
        'reviews',
        'image',
        'developer',
        'publisher',
        'series',
        'platforms',
        'release',
        'genre',
        'mode'
    )

    games_list = list(games)
    return JsonResponse(games_list, safe=False)


def home(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        search = request.POST.get('query')
        games = Review.objects.filter(
            Q(title__contains=search) |
            Q(platforms__contains=search) |
            Q(publisher__contains=search) |
            Q(reviews__contains=search) |
            Q(release__contains=search)
        )
        context = {
            'games': games
        }
        return render(request, 'index.html', context)

    games = Review.objects.all()
    context = {
        'games': games
    }
    return render(request, 'index.html', context)


def single_game(request: HttpRequest, _id: int) -> HttpResponse:
    game = Review.objects.filter(id=_id)
    context = {
        'game': game
    }
    return render(request, 'single_game.html', context)
