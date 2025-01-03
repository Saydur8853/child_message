# Generated by Django 5.1.4 on 2025-01-02 09:57

import home.models
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_alter_homepage_news_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='news_categories',
            field=wagtail.fields.StreamField([('News_Category', 1)], blank=True, block_lookup={0: ('wagtail.blocks.ChoiceBlock', [], {'choices': home.models.get_news_category_choices, 'label': 'News Category'}), 1: ('wagtail.blocks.StructBlock', [[('category', 0)]], {})}, null=True),
        ),
    ]
