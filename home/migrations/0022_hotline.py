# Generated by Django 5.1.4 on 2024-12-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_focusvideo_livestreaming'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotline_name', models.CharField(help_text='Name of the hotline', max_length=255)),
                ('number', models.CharField(help_text='Contact number', max_length=20)),
            ],
            options={
                'verbose_name': 'Hotline',
                'verbose_name_plural': 'Hotlines',
            },
        ),
    ]
