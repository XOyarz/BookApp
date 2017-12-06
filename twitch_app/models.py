from django.db import models

# Create your models here.
class TwitchUser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name