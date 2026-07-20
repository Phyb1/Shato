from django.db import models
from django.utils import timezone


class Notice(models.Model):
    """
    A short announcement posted from the admin, e.g. 'Weekly Pool
    Tournament'. The most recent *currently active* notice is shown
    on the Home page and refreshed periodically via HTMX.
    """

    title = models.CharField(
        max_length=100,
        help_text="Short headline, e.g. 'Weekly Pool Tournament'.",
    )
    body = models.TextField(help_text="What's happening at Shato.")
    flyer = models.ImageField(
        upload_to="notices/",
        blank=True,
        null=True,
        help_text="Optional flyer/poster image for this notice.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Untick to hide this notice without deleting it.",
    )
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Leave blank for a notice with no fixed end date.",
    )

    class Meta:
        ordering = ["-start_date"]
        verbose_name_plural = "Notices"

    def __str__(self):
        return self.title

    @property
    def is_current(self):
        """True if the notice is active and within its date window."""
        now = timezone.now()
        if not self.is_active or self.start_date > now:
            return False
        if self.end_date and now > self.end_date:
            return False
        return True
