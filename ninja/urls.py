from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('start_game', views.start_game),
    path('process_money', views.process_money, name='process_money'),
    path('reset', views.reset),
]
