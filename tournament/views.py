from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.template import loader


# Create your views here.
def index(request):
     template = loader.get_template('tournament/index.html')
     context = {}
     return HttpResponse(template.render(context, request))
 
def teams(request):
    template = loader.get_template('tournament/teams.html')
    context = {
        'teams' : Team.objects.order_by('team_wins'),
    }
    return HttpResponse(template.render(context,request))

def details_tournament(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    template = loader.get_template('tournament/tournament_details.html')
    context = {
        'tournament' : tournament,
        'matches' : Match.objects.filter(tournament_id=tournament.id)
    }
    return HttpResponse(template.render(context,request))

def matches_tournament(request, tournament_id):
    tournament = Tournament.objects.get(pk=tournament_id)
    return HttpResponse("All the Matches of the tournament %s" % tournament.name)

def tournaments(request):
    all_tournament = Tournament.objects.order_by('-date_start')
    template = loader.get_template('tournament/tournaments.html')
    context = {
        'tournaments' : all_tournament,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    return HttpResponse("Something in here")
    

def get_tournament(request, tournament_id):
    try:
        tournament = Tournament.objects.get(pk=tournament_id)
    except Tournament.DoesNotExist:
        return JsonResponse({'error': 'Tournament not found'}, status=404)
    
    # Serialize tournament data to JSON
    tournament_data = {
        'tournament_type': tournament.type,
        # add other fields as needed
    }
    
    # Return JSON response
    return JsonResponse(tournament_data, content_type='application/json')