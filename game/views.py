from django.shortcuts import render, get_object_or_404
from .models import Game

def game_view(request):
    all_games = Game.objects.all()
    return render(request, 'game/game.html', {'all_games': all_games})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    top_5_games = Game.objects.all().order_by('-created_at')[:12]
    return render(request, 'game/game_detail.html', {'game': game,'top_5_games':top_5_games})
