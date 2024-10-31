from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from Games_Reviews.models import NewUser, Review


def return_data(request: HttpRequest, username: str, key: str):
    if request.method == 'POST':
        return HttpResponse('POST method is not accepted.')
    user = NewUser.objects.filter(username=username)
    if key != user.get().key:
        return HttpResponse("Key errada.")
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
    games = Review.objects.all()
    context = {
        'games': games
    }
    return render(request, 'index.html', context)
