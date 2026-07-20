from django.utils import timezone
from django.views.generic import TemplateView

from .models import Notice


def _current_notice():
    """
    Return the single most relevant notice to display: the newest
    active notice whose date window includes right now.
    """
    now = timezone.now()
    return (
        Notice.objects.filter(is_active=True, start_date__lte=now)
        .exclude(end_date__lt=now)
        .first()
    )


class HomeView(TemplateView):
    """Landing page: hero, what we offer, current notice, find us."""

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["notice"] = _current_notice()
        return ctx


class AboutView(TemplateView):
    """About page: the Shato Sports Bar story."""

    template_name = "core/about.html"


class LatestNoticeView(TemplateView):
    """
    Returns just the notice partial. Polled by HTMX from the Home
    page (see templates/core/home.html) so the notice band can
    refresh itself without a full page reload.
    """

    template_name = "core/partials/notice.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["notice"] = _current_notice()
        return ctx
