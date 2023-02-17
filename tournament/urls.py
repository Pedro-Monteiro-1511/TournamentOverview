from django import urls
from django.urls import path
from . import views
from tournament.views import get_tournament

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/tournament/get_tournament/<int:tournament_id>/', get_tournament, name='get_tournament'),
    path('<int:tournament_id>/details', views.details_tournament, name="details_tournament"),
    path('<int:tournament_id>/matches', views.matches_tournament, name="matches_tournament"),
    path('about', views.about, name="about"),
    path('tournaments', views.tournaments, name="tournaments"),
    path('details_tournament', views.details_tournament, name="details_tournament"),
    path('teams', views.teams, name="teams"),
]
