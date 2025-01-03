# Generated by Django 5.1.4 on 2024-12-24 12:11

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_cheifvoicepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheifvoicepage',
            name='body',
            field=wagtail.fields.StreamField([('Chief_voice', 3)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': False}), 1: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 2: ('wagtailutils.blocks.RichTextBlock', (), {'required': False}), 3: ('wagtail.blocks.StructBlock', [[('title', 0), ('name', 0), ('designation', 0), ('image', 1), ('note', 2)]], {})}, null=True),
        ),
    ]
