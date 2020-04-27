from rest_framework import viewsets
from steam import WebAPI

from .models import Game
from .serializers import GameSerializer

api = WebAPI(key='1AD897533C698E617B4F351C640EC53E')
res = api.IPlayerService.GetOwnedGames(
    key='1AD897533C698E617B4F351C640EC53E',
    steamid='76561198080321262',
    include_appinfo=True,
    include_played_free_games=True,
    appids_filter=[])

games = res.get('response').get('games')

for game in games:
    if game.get('playtime_two_weeks'):
        print(game)
# Game.objects.update_or_create(name=game.get('name'), defaults={"name": game.get('name')})
#     serializer = GameSerializer(data=game)
#     if serializer.is_valid():
#         serializer.save()


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerializer
