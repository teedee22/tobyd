"""Streamfields find their home in this file"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class RichTextBlock(blocks.RichTextBlock):
    """Richtext with all the features"""

    class Meta:
        template = "streamfs/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class CodeBlock(blocks.RichTextBlock):
    """Richtext block to show code"""

    class Meta:
        template = "streamfs/code_block.html"
        icon = "code"
        label = "Code Format"


class SingleImageBlock(blocks.StructBlock):
    """Block to show a single image and optional caption"""

    image = ImageChooserBlock(required=True)
    caption = blocks.CharBlock(required=False, null=True, max_length=250)

    class Meta:
        template = "streamfs/single_image_block.html"
        icon = "image"
        label = "Single Image"
