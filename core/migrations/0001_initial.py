import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(help_text="Short headline, e.g. 'Weekly Pool Tournament'.", max_length=100)),
                ("body", models.TextField(help_text="What's happening at Shato.")),
                ("flyer", models.ImageField(blank=True, help_text="Optional flyer/poster image for this notice.", null=True, upload_to="notices/")),
                ("is_active", models.BooleanField(default=True, help_text="Untick to hide this notice without deleting it.")),
                ("start_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("end_date", models.DateTimeField(blank=True, help_text="Leave blank for a notice with no fixed end date.", null=True)),
            ],
            options={
                "verbose_name_plural": "Notices",
                "ordering": ["-start_date"],
            },
        ),
    ]
