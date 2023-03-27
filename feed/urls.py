from django.urls import path
from .views import (FeedList, FeedDetail)


urlpatterns = [
    path('feeds/<int:pk>/', FeedDetail.as_view(), name='feed-detail'),
    path('feeds/', FeedList.as_view(), name='feed-list'),
]

