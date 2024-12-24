# Generated by Django 5.1.4 on 2024-12-24 12:06

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_newsdetailspage_main_heading'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheifVoicePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('advertisement', wagtail.fields.StreamField([('Vertical_Adv', 1), ('Horizontal_Adv', 3), ('Poster_Adv', 5), ('Box_Adv', 7), ('Popup_Adv', 9)], blank=True, block_lookup={0: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 168x934', 'rendition_rules': {'original': 'fill-168x934-c0|format-webp', 'original_fallback': 'fill-168x934-c0'}, 'required': False}), 1: ('wagtail.blocks.StructBlock', [[('image', 0)]], {}), 2: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 1280x190', 'rendition_rules': {'original': 'fill-1280x190-c0|format-webp', 'original_fallback': 'fill-1280x190-c0'}, 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('image', 2)]], {}), 4: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 305x545', 'rendition_rules': {'original': 'fill-305x545-c0|format-webp', 'original_fallback': 'fill-305x545-c0'}, 'required': False}), 5: ('wagtail.blocks.StructBlock', [[('image', 4)]], {}), 6: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-420', 'rendition_rules': {'original': 'width-420|format-webp', 'original_fallback': 'width-420'}, 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 6)]], {}), 8: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('image', 8)]], {})}, null=True)),
                ('body', wagtail.fields.StreamField([('Chief_voice', 3)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'required': False}), 1: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 2: ('wagtailutils.blocks.RichTextBlock', (), {'required': False}), 3: ('wagtail.blocks.StructBlock', [[('title', 0), ('name', 0), ('designation', 0), ('image', 1), ('text', 2)]], {})}, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]