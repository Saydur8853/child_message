# Generated by Django 5.1.4 on 2025-01-01 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_newsdetails_delete_newsdetailspage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsdetails',
            options={'verbose_name': 'News detail', 'verbose_name_plural': 'News details'},
        ),
        migrations.AddField(
            model_name='newsdetails',
            name='page_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_details', to='home.newsindexpage', verbose_name='Choose a page'),
        ),
    ]
