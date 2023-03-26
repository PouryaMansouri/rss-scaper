from django.db import models


class Feed(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True, blank=False)
    url = models.URLField(null=False, blank=False)
    image_url = models.CharField(max_length=512, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    last_polled = models.DateTimeField(blank=True, null=True)
    live = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class FeedItem(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    body = models.TextField()
    created = models.DateTimeField(db_index=True)
    guid = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    image_url = models.CharField(max_length=512, blank=True, null=True)


class FeedSubscription(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, null=False, blank=False)
