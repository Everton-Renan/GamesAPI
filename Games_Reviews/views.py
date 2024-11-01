from django.db.models import Q
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
