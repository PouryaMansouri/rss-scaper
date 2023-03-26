from django.contrib import admin
from django.contrib.admin.decorators import register

from feed.models import Feed, FeedItem, FeedSubscription


@register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created')


@register(FeedSubscription)
class FeedSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('feed', 'user')
