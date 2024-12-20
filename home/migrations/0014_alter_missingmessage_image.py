# Generated by Django 5.1.4 on 2024-12-19 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_missingmessage_image'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingmessage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Optimal_Dimension : 520x365', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
