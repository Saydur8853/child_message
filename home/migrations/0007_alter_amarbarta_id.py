# Generated by Django 5.1.4 on 2024-12-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_amarbarta_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amarbarta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
