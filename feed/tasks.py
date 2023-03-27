from abc import ABC

import asyncio
import celery
from celery import shared_task

from feed.utils import get_feeds_from_db, fetch_feeds_items_from_feed_url

MAX_RETRIES = 5


class FeedTask(celery.Task, ABC):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('{0!r} failed: {1!r}'.format(task_id, exc))
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)


@shared_task(base=FeedTask, max_retries=MAX_RETRIES)
def fetch_one_feed(url):
    asyncio.run(fetch_feeds_items_from_feed_url(url))


@shared_task()
def fetch_feeds():
    """
    get all feeds from db
    create FeedTask for each feed in celery
    """
    all_live_feeds = get_feeds_from_db()
    list(map(lambda feed: fetch_one_feed.delay(feed.url), all_live_feeds))
