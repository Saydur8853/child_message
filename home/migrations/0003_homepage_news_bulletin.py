# Generated by Django 5.1.4 on 2024-12-17 06:30

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='news_bulletin',
            field=wagtail.fields.RichTextField(blank=True, help_text='The News Bulletin.'),
        ),
    ]