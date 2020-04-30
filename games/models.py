from django.db import models


class Game(models.Model):
    appid = models.IntegerField(primary_key=True, editable=True)
    price = models.IntegerField(default=0)

    name = models.TextField()

    playtime_forever = models.IntegerField(default=0)
    playtime_two_weeks = models.IntegerField(default=0)

    icon_url = models.TextField(blank=True)
    logo_url = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'