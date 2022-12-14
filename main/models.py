from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BloggerList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bloggerlist", null=True)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    time_post = models.CharField(max_length=50)

    def __str__(self):
        return self.title
