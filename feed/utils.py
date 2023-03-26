from feed.models import Feed


def get_feeds_from_db():
    return Feed.objects.all()