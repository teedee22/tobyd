# Generated by Django 2.2.4 on 2019-08-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footersettings',
            name='footertext',
            field=models.CharField(blank=True, help_text='Copyright logo precedes this', max_length=255, null=True),
        ),
    ]
