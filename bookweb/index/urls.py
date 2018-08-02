from django.conf.urls import url

from .views import index_views, story_views, chapter_views
from .models import *
urlpatterns = [
    url(r'^index/$',index_views),
    url(r'^index/story/', story_views),
    url(r'^index/chapter/',chapter_views)
]