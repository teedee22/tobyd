from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page

from blog.models import BlogDetailPage


class HomePage(Page):
    """Home page model/ landing page"""

    template = "home/home_page.html"
    max_count = 1
    banner_title = models.CharField(max_length=50, blank=True, null=True)
    banner_subtitle = models.CharField(max_length=200, blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),
            ],
            heading="Banner Options",
        )
    ]

    def get_context(self, request, *args, **kwargs):
        """Getting blog posts into context"""

        context = super().get_context(request)

        posts = (
            BlogDetailPage.objects.live()
            .public()
            .order_by("-first_published_at")
        )

        context["posts"] = posts
        return context
