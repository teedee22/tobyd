"""Flexible page"""

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Orderable, Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from streamfs import blocks


class StackImages(Orderable):
    page = ParentalKey("flex.FlexiblePage", related_name="stack_images")
    stack_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    stack_url = models.URLField(blank=True, null=True)
    panels = [ImageChooserPanel("stack_image"), FieldPanel("stack_url")]


class FlexiblePage(Page):
    template = "flex/flexible_page.html"

    banner_title = models.CharField(max_length=100, null=True, blank=True)
    banner_subtitle = models.CharField(max_length=250, null=True, blank=True)
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
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        MultiFieldPanel(
            [
                InlinePanel(
                    "stack_images", max_num=10, min_num=1, label="stack images"
                )
            ],
            heading="Images of tech stack used",
        ),
        StreamFieldPanel("content"),
    ]
