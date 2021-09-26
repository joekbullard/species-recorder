"""Markers urls."""

from django.urls import path

from .views import RecorderMapView

app_name = "bio_recorder"

urlpatterns = [
    path("map/", RecorderMapView.as_view()),
]