from typing import List

import aiohttp

from feed.models import Feed


def get_feeds_from_db() -> List[Feed]:
    return Feed.objects.all()


async def get_fetch_feeds_items_from_feed_url(feed: Feed):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(feed.url) as resp:
            resp = await resp.json()
            return resp
