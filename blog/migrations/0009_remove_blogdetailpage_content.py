# Generated by Django 2.2.4 on 2019-09-04 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190904_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='content',
        ),
    ]