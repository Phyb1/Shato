from django.urls import path

from .views import AboutView, HomeView, LatestNoticeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("htmx/latest-notice/", LatestNoticeView.as_view(), name="latest-notice"),
]
