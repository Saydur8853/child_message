# Generated by Django 5.1.4 on 2024-12-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_rename_hotline_name_site_associate_hotline_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_associate',
            name='child_helpline_number',
            field=models.CharField(blank=True, help_text='Child helpline number', max_length=20),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='hotline_number',
            field=models.CharField(blank=True, help_text='Hotline number', max_length=25),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='quick_link_1_name',
            field=models.CharField(blank=True, help_text='Quick link 1 name', max_length=255),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='quick_link_2_name',
            field=models.CharField(blank=True, help_text='Quick link 2 name', max_length=255),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='quick_link_3_name',
            field=models.CharField(blank=True, help_text='Quick link 3 name', max_length=255),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='quick_link_4_name',
            field=models.CharField(blank=True, help_text='Quick link 4 name', max_length=255),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='quick_link_5_name',
            field=models.CharField(blank=True, help_text='Quick link 5 name', max_length=255),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='quick_link_6_name',
            field=models.CharField(blank=True, help_text='Quick link 6 name', max_length=255),
        ),
        migrations.AlterField(
            model_name='site_associate',
            name='short_message',
            field=models.CharField(blank=True, help_text='Short message', max_length=255),
        ),
    ]
