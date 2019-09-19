# Generated by Django 2.2.5 on 2019-09-19 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0007_homepage_about_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_cta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
