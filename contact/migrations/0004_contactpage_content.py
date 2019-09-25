# Generated by Django 2.2.5 on 2019-09-25 20:05

from django.db import migrations
import streamfs.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_stackimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', streamfs.blocks.RichTextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=250, null=True, required=False))]))], blank=True, null=True),
        ),
    ]
