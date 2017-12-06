from django.db import models

# Create your models here.
class TwitchUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(default="No bio available")
    game = models.CharField(max_length=50, default="No game available")
    followers = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    profile_link = models.URLField(default='not')

    def __str__(self):
        return self.name