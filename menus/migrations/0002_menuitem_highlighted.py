# Generated by Django 2.2.5 on 2019-09-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='highlighted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
