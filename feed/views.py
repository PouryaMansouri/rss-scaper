from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Feed
from .serializers import FeedSerializer


class FeedList(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [AllowAny]


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [AllowAny]


class UpdateFeeds(generics.GenericAPIView):

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        from .tasks import update_feeds
        update_feeds.delay()
        message = "Feeds are being updated"
        return Response(message, status=status.HTTP_200_OK)
