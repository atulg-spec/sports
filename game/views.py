from django.shortcuts import render, get_object_or_404
from .models import Game

def game_view(request):
    query = request.GET.get('search', '')  # Get the search query from the GET parameters
    if query:
        # Filter games based on the search query
        all_games = Game.objects.filter(name__icontains=query).order_by('?')[:80]
    else:
        # If no search query, retrieve all games
        all_games = Game.objects.order_by('?')[:80]

    return render(request, 'game/game.html', {'all_games': all_games, 'search_query': query})

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    top_5_games = Game.objects.order_by('?')[:12]
    return render(request, 'game/game_detail.html', {'game': game,'top_5_games':top_5_games})
