from django.db import models

DEFAULT_STEAM_STORE_ID = 1


class Game(models.Model):
    appid = models.IntegerField(primary_key=True, editable=True)
    price = models.IntegerField(default=0)

    name = models.CharField(max_length=200)
    store = models.ForeignKey("games.Store", default=DEFAULT_STEAM_STORE_ID, on_delete=models.DO_NOTHING)

    playtime_forever = models.IntegerField(default=0)
    playtime_two_weeks = models.IntegerField(default=0)

    icon_url = models.CharField(blank=True, max_length=200)
    logo_url = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return f'{self.name}'


class Store(models.Model):
    name = models.CharField(max_length=200)
    key = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'