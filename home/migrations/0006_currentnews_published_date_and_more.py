from django.db import migrations, models
import datetime

def set_default_published_date(apps, schema_editor):
    CurrentNews = apps.get_model('home', 'CurrentNews')
    for news_item in CurrentNews.objects.all():
        if not news_item.published_date:
            news_item.published_date = datetime.datetime.now()
            news_item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_currentnews_news_bulletin'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentnews',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.RunPython(set_default_published_date),
    ]
