from django.urls import path
from .views import placement_stories, story_detail

urlpatterns = [
    path('', placement_stories, name='placement_stories'),
    path('placement-stories/<int:story_id>/', story_detail, name='story_detail'),
]
