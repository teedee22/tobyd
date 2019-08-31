from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from streamfs import blocks


class BlogDetailPage(Page):
    """Blog detail page"""

    custom_title = models.CharField(
        max_length=120,
        blank=False,
        null=False,
        help_text="Overwrites the default title",
    )
    description = models.CharField(
        max_length=300,
        blank=False,
        null=False,
        help_text="Description which will appear in the listing",
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )
    author = models.CharField(max_length=100, blank=True, null=True)
    content = RichTextField(blank=False)

    streams = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("code_block", blocks.CodeBlock()),
            ("single_image", blocks.SingleImageBlock())
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("custom_title"),
                FieldPanel("description"),
                FieldPanel("author"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Blog page information",
        ),
        FieldPanel("content"),
        StreamFieldPanel("streams"),
    ]
