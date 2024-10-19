from django.urls import path
from django.views.decorators.cache import cache_page

from addinfo.apps import AddinfoConfig
from addinfo.views import (ComTextCreateView, ComTextDeleteView,
                           ComTextDetailView, ComTextListView,
                           ComTextUpdateView, FeedbackListView, FeedbackDetailView, FeedbackCreateView,
                           FeedbackUpdateView, FeedbackDeleteView)
from meddata.views import home

app_name = AddinfoConfig.name
urlpatterns = [
    path("", home, name="home"),
    path("comtext_list/", ComTextListView.as_view(), name="comtext_list"),
    path(
        "comtext/<int:pk>/", cache_page(60)(ComTextDetailView.as_view()), name="comtext"
    ),
    path("comtext/create/", ComTextCreateView.as_view(), name="comtext_create"),
    path(
        "comtext/<int:pk>/update/", ComTextUpdateView.as_view(), name="comtext_update"
    ),
    path(
        "comtext/<int:pk>/delete/", ComTextDeleteView.as_view(), name="comtext_delete"
    ),

    path("feedback_list/", FeedbackListView.as_view(), name="feedback_list"),
    path(
        "feedback/<int:pk>/", cache_page(60)(FeedbackDetailView.as_view()), name="feedback"
    ),
    path("feedback/create/", FeedbackCreateView.as_view(), name="feedback_create"),
    path(
        "feedback/<int:pk>/update/", FeedbackUpdateView.as_view(), name="feedback_update"
    ),
    path(
        "feedback/<int:pk>/delete/", FeedbackDeleteView.as_view(), name="feedback_delete"
    ),
]
