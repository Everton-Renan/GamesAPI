from django.urls import path

from Games_Reviews.views import return_data

urlpatterns = [
    path('api/<str:username>/<str:key>', return_data, name='return_data')
]
