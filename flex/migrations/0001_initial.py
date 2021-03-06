# Generated by Django 2.2.4 on 2019-08-31 18:49

from django.db import migrations, models
import django.db.models.deletion
import streamfs.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlexiblePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('custom_title', models.CharField(blank=True, max_length=100, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=250, null=True)),
                ('content', wagtail.core.fields.StreamField([('full_richtext', streamfs.blocks.RichTextBlock()), ('single_image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(max_length=250, null=True, required=False))]))], blank=True, null=True)),
                ('banner_image', models.ForeignKey(null=True, on_delete='models.SET_NULL', related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
