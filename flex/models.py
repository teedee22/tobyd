"""Flexible page"""

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streamfs import blocks


class FlexiblePage(Page):
    template = "flex/flexible_page.html"

    custom_title = models.CharField(max_length=100, null=True, blank=True)
    subtitle = models.CharField(max_length=250, null=True, blank=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )

    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("single_image_block", blocks.SingleImageBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("subtitle"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content"),
    ]
