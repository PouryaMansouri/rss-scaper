from rest_framework import generics
from rest_framework.permissions import AllowAny
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
