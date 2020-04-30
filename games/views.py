from rest_framework import viewsets
from steam import WebAPI

from .models import Game
from .serializers import GameSerializer

# TODO move variable to env
api = WebAPI(key='1AD897533C698E617B4F351C640EC53E')
res = api.IPlayerService.GetOwnedGames(
    key='1AD897533C698E617B4F351C640EC53E',
    steamid='76561198080321262',
    include_appinfo=True,
    include_free_sub=False,
    include_played_free_games=True,
    appids_filter=[])

games = res.get('response').get('games')

for game in games:
    print(game)

    appid = game.get('appid')
    defaults = {
        'name': game.get('name'),
        'appid': appid,
        'playtime_forever': game.get('playtime_forever'),
        'icon_url': f'http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{game.get("img_icon_url")}.jpg',
        'logo_url': f'http://media.steampowered.com/steamcommunity/public/images/apps/{appid}/{game.get("img_logo_url")}.jpg'
    }

    if game.get('playtime_2weeks'):
        defaults['playtime_two_weeks'] = game.get('playtime_2weeks')

    Game.objects.update_or_create(pk=appid, defaults=defaults)


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('-id')
    serializer_class = GameSerializer
