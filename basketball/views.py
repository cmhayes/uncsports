from basketball.models import Team, Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger		

# Create your views here.
def home(request):
	context = {
		'players_count': Players.objects.count(),
		'team_count': Team.objects.count(),
	}
	return render(request, "basketball/home.html", context)	

def team(request, pk):
	tempTeams = Team.objects.get(id=pk)
	tempTeams = tempTeams.players.all()
	team = get_object_or_404(Team, id=pk)
	context = {
		'teamList': tempTeams,
		'team': team,
	}
	return render(request, "basketball/team.html", context)

def player(request, pk):
	player = get_object_or_404(Player, id=pk)
	return render (request, "basketball/player.html", {'player': player})