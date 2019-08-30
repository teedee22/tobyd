from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class FooterSettings(BaseSetting):
    """Footer settings for social media and other bits"""

    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")
    github = models.URLField(blank=True, null=True, help_text="Github URL")
    reddit = models.URLField(blank=True, null=True, help_text="Reddit URL")
    twitter = models.URLField(blank=True, null=True, help_text="twitter URL")

    footertext = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        help_text="Copyright logo precedes this"
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("linkedin"),
                FieldPanel("github"),
                FieldPanel("reddit"),
                FieldPanel("twitter"),
            ],
            heading="Social Media Settings",
        ),
        FieldPanel("footertext"),
    ]
