# Generated by Django 5.1.4 on 2024-12-21 14:04

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_homepage_advertisement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='advertisement',
            field=wagtail.fields.StreamField([('Vertical_Adv', 1), ('Horizontal_Adv', 3), ('Poster_Adv', 5), ('Box_Adv', 7), ('Popup_Adv', 9)], blank=True, block_lookup={0: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 168x934', 'rendition_rules': {'original': 'fill-168x934-c0|format-webp', 'original_fallback': 'fill-168x934-c0'}, 'required': False}), 1: ('wagtail.blocks.StructBlock', [[('image', 0)]], {}), 2: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 1280x190', 'rendition_rules': {'original': 'fill-1280x190-c0|format-webp', 'original_fallback': 'fill-1280x190-c0'}, 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('image', 2)]], {}), 4: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 305x545', 'rendition_rules': {'original': 'fill-305x545-c0|format-webp', 'original_fallback': 'fill-305x545-c0'}, 'required': False}), 5: ('wagtail.blocks.StructBlock', [[('image', 4)]], {}), 6: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-420', 'rendition_rules': {'original': 'width-420|format-webp', 'original_fallback': 'width-420'}, 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 6)]], {}), 8: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('image', 8)]], {})}, null=True),
        ),
    ]
