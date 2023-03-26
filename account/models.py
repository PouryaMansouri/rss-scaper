from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(null=False, blank=False)
    feeds = models.ManyToManyField('feed.Feed', through='feed.FeedSubscription')
