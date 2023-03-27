from abc import ABC
import feedparser

from django.utils import timezone
import celery
from celery import shared_task

from feed.models import Feed, FeedItem
from feed.utils import get_live_feeds_ids_from_db, update_feed_attributes, update_feed_items

MAX_RETRIES = 5


class BaseTaskWithFailure(celery.Task, ABC):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)


@shared_task(base=BaseTaskWithFailure, bind=True, max_retries=MAX_RETRIES)
def update_feed(feed_id):
    """
    Task to update the feed attributes and fetch and update feed items.

    Args:
        feed_id (int): The ID of the Feed object to be updated.

    """
    feed = Feed.objects.get(id=feed_id)
    update_feed_attributes(feed)
    update_feed_items(feed)


@shared_task(base=BaseTaskWithFailure, bind=True, max_retries=MAX_RETRIES)
def update_feeds():
    """
    Task to update all the feeds that are live.
    """
    lives_feeds_ids = get_live_feeds_ids_from_db()
    list(map(update_feed.delay, lives_feeds_ids))
