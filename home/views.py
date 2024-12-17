from django.shortcuts import render
from .models import AmarBarta

def latest_news_view(request):
    latest_news = AmarBarta.objects.latest('published_date')  # Get the most recent news item
    return render(request, 'home/welcome_page.html', {'latest_news': latest_news})
