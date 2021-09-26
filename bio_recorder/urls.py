"""Markers urls."""

from django.urls import path

from .views import RecorderMapView, HomePageView, AboutPageView

app_name = "bio_recorder"

urlpatterns = [
    path('map/', RecorderMapView.as_view(), name='map'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]