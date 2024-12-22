# Generated by Django 5.1.4 on 2024-12-22 11:44

import django.db.models.deletion
import django.utils.timezone
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_newscategory_alter_currentnews_news_bulletin_and_more'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
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
                ('image', models.ForeignKey(blank=True, help_text='Optimal_Dimension : 520x365', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('news_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_details_page', to='home.newscategory', verbose_name='Select a Category')),
            ],
            options={
                'verbose_name': 'Amar Barta',
                'verbose_name_plural': 'Amar Bartas',
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]