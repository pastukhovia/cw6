from django.conf import settings
from django.db import models
from users.models import User


class Ad(models.Model):
    class Meta:
        ordering = ['-created_at']

    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='ad_images', null=True)


class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
