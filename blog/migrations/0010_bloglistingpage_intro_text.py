# Generated by Django 2.2.5 on 2019-09-18 20:27

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_blogdetailpage_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloglistingpage',
            name='intro_text',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]