from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)

from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)
from streamfs import blocks


class StackImages(Orderable):
    page = ParentalKey("contact.ContactPage", related_name="stack_images")
    stack_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    stack_url = models.URLField(blank=True, null=True)
    panels = [ImageChooserPanel("stack_image"), FieldPanel("stack_url")]


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactPage", on_delete=models.CASCADE, related_name="form_fields"
    )


class ContactPage(WagtailCaptchaEmailForm):

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )

    template = "contact/contact_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("single_image_block", blocks.SingleImageBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content"),
        InlinePanel('form_fields', label="Form Fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6")
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
        MultiFieldPanel(
            [
                InlinePanel(
                    "stack_images", max_num=10, min_num=1, label="stack images"
                )
            ],
            heading="Images of tech stack used",),
    ]
