from django import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models
from django_extensions.db.fields import AutoSlugField

from modelcluster.fields import ParentalManyToManyField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

from streamfs import blocks


@register_snippet
class BlogCategory(models.Model):
    """Register categories for blog"""

    name = models.CharField(max_length=255, blank=False, null=False)
    slug = AutoSlugField(
        populate_from="name",
        editable=True,
        allow_unicode=True,
        help_text="This is the url of the category",
    )

    panels = [FieldPanel("name"), FieldPanel("slug")]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog category"
        verbose_name_plural = "Blog categories"
        ordering = ["name"]


class BlogListingPage(Page):
    """Lists all the blog posts"""

    max_count = 1
    template = "blog/blog_listing_page.html"
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        related_name="+",
        on_delete="models.SET_NULL",
    )
    custom_title = models.CharField(max_length=120, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("banner_image"),
    ]

    def get_context(self, request):
        """get all blog posts to list"""
        context = super().get_context(request)
        all_posts = (
            BlogDetailPage.objects.live()
            .public()
            .order_by("-first_published_at")
        )
        # Adding paginator to blog listing page:
        paginator = Paginator(all_posts, 5)
        page = request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['posts'] = posts

        # Filters posts if request is category using GET
        filtered_posts = (
            BlogDetailPage.objects.live()
            .public()
            .filter(category__slug__in=[request.GET.get("category")])
        )
        if filtered_posts:
            context["posts"] = filtered_posts
            context["category"] = request.GET.get("category").capitalize()
        return context

    @property
    def display_title(self):
        return title_method(self)


class BlogDetailPage(Page):
    """Blog detail page"""

    template = "blog/blog_detail_page.html"

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

    streams = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("code_block", blocks.CodeBlock()),
            ("single_image", blocks.SingleImageBlock()),
        ],
        null=True,
        blank=True,
    )

    category = ParentalManyToManyField("blog.BlogCategory", blank=True)

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
        FieldPanel("category", widget=forms.CheckboxSelectMultiple),
        StreamFieldPanel("streams"),
    ]

    @property
    def display_title(self):
        return title_method(self)


def title_method(self):
    """Method for logic of what title to display on blog detail and listing"""
    if self.custom_title:
        return self.custom_title
    elif self.title:
        return self.title
    return "Missing Title"
