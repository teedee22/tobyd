# Generated by Django 2.2.5 on 2019-09-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190914_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
