from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)
    Author = get_user_model()
# Create your models here.
