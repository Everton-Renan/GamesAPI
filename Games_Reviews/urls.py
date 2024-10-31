from django.urls import path

from Games_Reviews.views import home, return_data

urlpatterns = [
    path('api/<str:username>/<str:key>', return_data, name='return_data'),
    path('', home, name='home')
]
