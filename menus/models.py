from django.db import models

from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.snippets.models import register_snippet


class MenuItem(Orderable):
    """For each menu item in the menu"""
    link_title = models.CharField(max_length=100, blank=True, null=True)
    link_url = models.URLField(max_length=500, blank=True, null=True)
    link_page = models.ForeignKey(
        "wagtailcore.page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)
    page = ParentalKey("Menu", related_name="menu_items")
    highlighted = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
        FieldPanel("highlighted"),
    ]

    @property
    def link(self):
        if self.link_url:
            return self.link_url
        elif self.link_page:
            return self.link_page.url
        return "missing page url"


@register_snippet
class Menu(ClusterableModel):
    """The main menu"""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True)

    panels = [
        MultiFieldPanel(
            [FieldPanel("title"), FieldPanel("slug")], heading="Menu"
        ),
        InlinePanel("menu_items", label="Menu Items")
    ]

    def __str__(self):
        return self.title
