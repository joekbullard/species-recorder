from django.views.generic.base import TemplateView


class RecorderMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'