from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    # owner is the user posting the book
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='book_images', blank=True)
    image_url = models.CharField(blank=True, max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    liked = models.CharField(default=' ', max_length=200)

    class Meta:
        ordering = ('created',)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.pk

# The standard Django User model has only a few fields. Here we expand said model
# to include country, city and zip code.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    # some zip codes, such as UK's, are alpha-numerical, so we need this to be char field
    zipcode = models.CharField(max_length=20)
    # Latitude and Longitude are stored in the UserProfile model so they're calculated
    # only once, and then fetched whenever required
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username