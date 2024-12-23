# Generated by Django 5.1.4 on 2024-12-22 19:06

import django.db.models.deletion
import django.utils.timezone
import wagtail.fields
import wagtail.search.index
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_bulletin', models.CharField(help_text='Enter news heading', max_length=500)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True, verbose_name='News Category')),
            ],
        ),
        migrations.CreateModel(
            name='NewsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('repeat_in_subnav', models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation')),
                ('repeated_item_text', models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text')),
                ('advertisement', wagtail.fields.StreamField([('Vertical_Adv', 1), ('Horizontal_Adv', 3), ('Poster_Adv', 5), ('Box_Adv', 7), ('Popup_Adv', 9)], blank=True, block_lookup={0: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 168x934', 'rendition_rules': {'original': 'fill-168x934-c0|format-webp', 'original_fallback': 'fill-168x934-c0'}, 'required': False}), 1: ('wagtail.blocks.StructBlock', [[('image', 0)]], {}), 2: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 1280x190', 'rendition_rules': {'original': 'fill-1280x190-c0|format-webp', 'original_fallback': 'fill-1280x190-c0'}, 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('image', 2)]], {}), 4: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 305x545', 'rendition_rules': {'original': 'fill-305x545-c0|format-webp', 'original_fallback': 'fill-305x545-c0'}, 'required': False}), 5: ('wagtail.blocks.StructBlock', [[('image', 4)]], {}), 6: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-420', 'rendition_rules': {'original': 'width-420|format-webp', 'original_fallback': 'width-420'}, 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 6)]], {}), 8: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('image', 8)]], {})}, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AddField(
            model_name='homepage',
            name='advertisement',
            field=wagtail.fields.StreamField([('Vertical_Adv', 1), ('Horizontal_Adv', 3), ('Poster_Adv', 5), ('Box_Adv', 7), ('Popup_Adv', 9)], blank=True, block_lookup={0: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 168x934', 'rendition_rules': {'original': 'fill-168x934-c0|format-webp', 'original_fallback': 'fill-168x934-c0'}, 'required': False}), 1: ('wagtail.blocks.StructBlock', [[('image', 0)]], {}), 2: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 1280x190', 'rendition_rules': {'original': 'fill-1280x190-c0|format-webp', 'original_fallback': 'fill-1280x190-c0'}, 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('image', 2)]], {}), 4: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 305x545', 'rendition_rules': {'original': 'fill-305x545-c0|format-webp', 'original_fallback': 'fill-305x545-c0'}, 'required': False}), 5: ('wagtail.blocks.StructBlock', [[('image', 4)]], {}), 6: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-420', 'rendition_rules': {'original': 'width-420|format-webp', 'original_fallback': 'width-420'}, 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 6)]], {}), 8: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('image', 8)]], {})}, null=True),
        ),
        migrations.CreateModel(
            name='AmarBarta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(help_text='Main Heading of the News', max_length=255)),
                ('subtitle', models.CharField(blank=True, help_text='Subtitle of the News', max_length=255, null=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Publish Date and Time')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Updated Date and Time')),
                ('details', wagtail.fields.RichTextField(blank=True, help_text='Details of the news')),
                ('image', models.ForeignKey(blank=True, help_text='Optimal_Dimension : 520x365', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Amar Barta',
                'verbose_name_plural': 'Amar Bartas',
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='MissingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the missing person', max_length=255)),
                ('age', models.PositiveIntegerField(help_text='Age of the missing person')),
                ('skin_tone', models.CharField(help_text='Skin tone of the missing person', max_length=100)),
                ('dress', models.CharField(help_text='Description of the dress the missing person was wearing', max_length=255)),
                ('missing_time_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Time and date when the person went missing')),
                ('published_date', models.DateTimeField(auto_now=True, help_text='Updated Date and Time')),
                ('contact_number', models.CharField(help_text='Contact number to reach out for information', max_length=15)),
                ('detail_story', models.TextField(help_text='Detailed story of the missing incident')),
                ('image', models.ForeignKey(blank=True, help_text='Optimal_Dimension : 520x365', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Missing Message',
                'verbose_name_plural': 'Missing Messages',
            },
        ),
        migrations.CreateModel(
            name='NewsDetailsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('repeat_in_subnav', models.BooleanField(default=False, help_text="If checked, a link to this page will be repeated alongside it's direct children when displaying a sub-navigation for this page.", verbose_name='repeat in sub-navigation')),
                ('repeated_item_text', models.CharField(blank=True, help_text="e.g. 'Section home' or 'Overview'. If left blank, the page title will be used.", max_length=255, verbose_name='repeated item link text')),
                ('main_heading', models.CharField(help_text='Main Heading of the News', max_length=255)),
                ('subtitle', models.CharField(blank=True, help_text='Subtitle of the News', max_length=255, null=True)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Publish Date and Time')),
                ('updated_date', models.DateTimeField(auto_now=True, help_text='Updated Date and Time')),
                ('details', wagtail.fields.RichTextField(blank=True, help_text='Details of the news')),
                ('make_featured_news', models.BooleanField(blank=True, default=False, verbose_name='Make it featured?')),
                ('advertisement', wagtail.fields.StreamField([('Vertical_Adv', 1), ('Horizontal_Adv', 3), ('Poster_Adv', 5), ('Box_Adv', 7), ('Popup_Adv', 9)], blank=True, block_lookup={0: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 168x934', 'rendition_rules': {'original': 'fill-168x934-c0|format-webp', 'original_fallback': 'fill-168x934-c0'}, 'required': False}), 1: ('wagtail.blocks.StructBlock', [[('image', 0)]], {}), 2: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 1280x190', 'rendition_rules': {'original': 'fill-1280x190-c0|format-webp', 'original_fallback': 'fill-1280x190-c0'}, 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('image', 2)]], {}), 4: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : 305x545', 'rendition_rules': {'original': 'fill-305x545-c0|format-webp', 'original_fallback': 'fill-305x545-c0'}, 'required': False}), 5: ('wagtail.blocks.StructBlock', [[('image', 4)]], {}), 6: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-420', 'rendition_rules': {'original': 'width-420|format-webp', 'original_fallback': 'width-420'}, 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('image', 6)]], {}), 8: ('wagtailutils.blocks.ImageChooserBlock', (), {'help_text': 'Optimal Dimension : width max-500', 'rendition_rules': {'original': 'width-500|format-webp', 'original_fallback': 'width-500'}, 'required': False}), 9: ('wagtail.blocks.StructBlock', [[('image', 8)]], {})}, null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Optimal_Dimension : 520x365', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('news_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_details_page', to='home.newscategory', verbose_name='Select a Category')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]