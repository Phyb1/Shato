from django.contrib import admin

from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    """
    Admin screen for posting notices (e.g. 'Weekly Pool Tournament')
    without touching code. See templates/admin/base_site.html for the
    Shato-branded admin header/colours.
    """

    list_display = ("title", "start_date", "end_date", "is_active", "is_current")
    list_filter = ("is_active", "start_date")
    search_fields = ("title", "body")
    list_editable = ("is_active",)
    date_hierarchy = "start_date"
    fieldsets = (
        (None, {"fields": ("title", "body", "flyer")}),
        ("Scheduling", {"fields": ("is_active", "start_date", "end_date")}),
    )

    @admin.display(boolean=True, description="Currently showing?")
    def is_current(self, obj):
        return obj.is_current
