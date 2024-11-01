from django.urls import path

from Games_Reviews.views import home, return_data, single_game

app_name = 'Games_Reviews'

urlpatterns = [
    path('api/<str:username>/<str:key>', return_data, name='return_data'),
    path('game/<int:_id>', single_game, name='single_game'),
    path('', home, name='home')
]
