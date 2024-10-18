from django.urls import path
from django.views.decorators.cache import cache_page

from addinfo.apps import AddinfoConfig
from addinfo.views import (ComTextCreateView, ComTextDeleteView,
                           ComTextDetailView, ComTextListView,
                           ComTextUpdateView)
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
]
