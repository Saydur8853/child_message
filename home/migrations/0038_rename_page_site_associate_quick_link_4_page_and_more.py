# Generated by Django 5.1.4 on 2025-01-02 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_site_associate_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_associate',
            old_name='page',
            new_name='quick_link_4_page',
        ),
        migrations.RemoveField(
            model_name='site_associate',
            name='quick_link_4_name',
        ),
        migrations.RemoveField(
            model_name='site_associate',
            name='quick_link_4_url',
        ),
    ]