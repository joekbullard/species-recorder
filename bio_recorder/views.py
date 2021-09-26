from django.views.generic.base import TemplateView


class RecorderMapView(TemplateView):
    """Markers map view."""

    template_name = "map.html"