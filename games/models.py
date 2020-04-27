from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100, blank=True)

    # appid = models.IntegerField()
    # playtime_forever = models.IntegerField()
    # img_icon_url = models.CharField(max_length=100, blank=True)
    # img_logo_url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'