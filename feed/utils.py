from datetime import datetime
from typing import List

import feedparser

from feed.exceptions import FetchFeedException
from feed.models import Feed, FeedItem


def get_live_feeds_ids_from_db() -> List[int]:
    """
    Get the ids of the feeds that are live
    """
    return Feed.objects.filter(live=True).values_list("id", flat=True)


def fetch_feed(url):
    """
    Fetch a RSS feed using feedparser.
    """
    try:
        parsed_feed = feedparser.parse(url)
        return parsed_feed
    except Exception:
        raise FetchFeedException("Error while fetching feed")


def update_feed_attributes(feed):
    """
    Update the feed attributes (name, description, last_update) in the database.

    Args:
        feed (Feed): The Feed object to be updated.

    """
    parsed_feed = fetch_feed(feed.url)

    # Update attributes of the feed object
    feed.name = parsed_feed.feed.title
    feed.description = parsed_feed.feed.subtitle
    feed.last_update = datetime.now()
    feed.save()


def update_feed_items(feed):
    """
    Fetch and update feed items in the database.

    Args:
        feed (Feed): The Feed object whose items need to be updated.

    """
    parsed_feed = fetch_feed(feed.url)

    # Create or update feed items in the database
    # for entry in parsed_feed.entries:
    #     feed_item, created = FeedItem.objects.get_or_create(
    #         feed=feed,
    #         guid=entry.guid,
    #     )
    #
    #     # If the feed item already exists, update it
    #     if not created:
    #         feed_item.title = entry.title
    #         feed_item.body = entry.description
    #         feed_item.save()
    print('*'*100)
    print('update_feed_items')
