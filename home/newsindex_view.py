   ###    ########  ##     ## ######## ########  ######## ####  ######  ######## ##     ## ######## ##    ## ######## 
  ## ##   ##     ## ##     ## ##       ##     ##    ##     ##  ##    ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##     ## ##     ## ##       ##     ##    ##     ##  ##       ##       #### #### ##       ####  ##    ##    
##     ## ##     ## ##     ## ######   ########     ##     ##   ######  ######   ## ### ## ######   ## ## ##    ##    
######### ##     ##  ##   ##  ##       ##   ##      ##     ##        ## ##       ##     ## ##       ##  ####    ##    
##     ## ##     ##   ## ##   ##       ##    ##     ##     ##  ##    ## ##       ##     ## ##       ##   ###    ##    
##     ## ########     ###    ######## ##     ##    ##    ####  ######  ######## ##     ## ######## ##    ##    ##    


from django.shortcuts import render, get_object_or_404
from .models import *
from .views import current_news_view, live_streaming_view, focus_video_view
from django.utils import timezone
from django.utils.html import format_html
from django.http import JsonResponse
from django.core.paginator import Paginator
# Fetch the popup advertisement
def popup_advertisement_view(request, slug):
    try:
        newsindexpage = get_object_or_404(NewsIndexPage, slug=slug)
        popup_adv_url = None
        
        # Iterate through the advertisement blocks
        for block in newsindexpage.advertisement:
            if block.block_type == "Popup_Adv":
                image = block.value.get("image")
                # print(f"Image found: {image}")  # Debugging line
                if image:  # Ensure the image exists
                    # Generate the rendition
                    rendition = image.get_rendition("width-500")
                    popup_adv_url = rendition.url  # Get the URL of the rendition
                    # print(f"Popup Image URL: {popup_adv_url}")  # Debugging line
                break
    except NewsIndexPage.DoesNotExist:
        popup_adv_url = None

    return popup_adv_url

# Fetch the vertical advertisement
def vertical_advertisement_view(request, slug):
    try:
        newsindexpage = get_object_or_404(NewsIndexPage, slug=slug)
        vertical_adv_urls = []
        
        for block in newsindexpage.advertisement:
            if block.block_type == "Vertical_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-168x934-c0")
                    vertical_adv_urls.append(rendition.url)
                    
                if len(vertical_adv_urls) >= 2:  # Limit to two images
                    break
    except NewsIndexPage.DoesNotExist:
        vertical_adv_urls = [None, None]

    # Ensure two entries for left and right ads
    while len(vertical_adv_urls) < 2:
        vertical_adv_urls.append(None)

    return vertical_adv_urls

# Fetch the horizontal advertisement
def horizontal_advertisement_view(request, slug):
    try:
        newsindexpage = get_object_or_404(NewsIndexPage, slug=slug)
        horizontal_adv_urls = []

        for block in newsindexpage.advertisement:
            if block.block_type == "Horizontal_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("height-135")
                    horizontal_adv_urls.append(rendition.url)

                if len(horizontal_adv_urls) >= 7:  # Limit to one image
                    break
    except NewsIndexPage.DoesNotExist:
        horizontal_adv_urls = [None]

    # Ensure at least one entry for horizontal ad
    while len(horizontal_adv_urls) < 7:
        horizontal_adv_urls.append(None)

    return horizontal_adv_urls


# Fetch the poster advertisement
def poster_advertisement_view(request, slug):
    try:
        newsindexpage = get_object_or_404(NewsIndexPage, slug=slug)
        poster_adv_url = None
        
        for block in newsindexpage.advertisement:
            if block.block_type == "Poster_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-305x545-c0")
                    poster_adv_url = rendition.url
                break
    except NewsIndexPage.DoesNotExist:
        poster_adv_url = None

    return poster_adv_url

# Fetch the box advertisement
def box_advertisement_view(request, slug):
    try:
        newsindexpage = get_object_or_404(NewsIndexPage, slug=slug)
        box_adv_url = None
        
        for block in newsindexpage.advertisement:
            if block.block_type == "Box_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("width-420")
                    box_adv_url = rendition.url
                break
    except NewsIndexPage.DoesNotExist:
        box_adv_url = None

    return box_adv_url




def get_localized_time(time_field):
    """Helper function to convert time to the local timezone."""
    if time_field:
        return time_field.astimezone(timezone.get_current_timezone()).strftime("%d %b %Y, %I:%M %p")
    return None

def get_latest_news(news_index_page):
    """Helper function to get the latest news details."""
    return NewsDetails.objects.filter(page_choice=news_index_page).order_by('-published_date').first()

def get_second_latest_news(news_index_page):
    """Helper function to get the second latest news details."""
    return NewsDetails.objects.filter(page_choice=news_index_page).order_by('-published_date')[1:2].first()
def insert_advertisements(details_text, box_adv_url):
    """Inserts advertisements within the details text based on word count."""
    if not details_text or not box_adv_url:
        return details_text

    words = details_text.split()
    word_limit = 200
    ad_markup = f'<img src="{box_adv_url}" class="mx-auto" alt="add" />'

    if len(words) <= word_limit:
        # If text is less than or equal to 200 words, add the ad at the end
        return details_text + ad_markup

    # Insert ads every 200 words
    parts = []
    for i in range(0, len(words), word_limit):
        part = " ".join(words[i:i + word_limit])
        parts.append(part)
        if i + word_limit < len(words):  # Don't add ad after the last chunk
            parts.append(ad_markup)

    return " ".join(parts)

def get_latest_news_range(news_index_page, start, end):
    """Helper function to get a range of latest news details."""
    return NewsDetails.objects.filter(page_choice=news_index_page).order_by('-published_date')[start:end]


def news_combined_view(request, slug):
    # Advertisement URLs
    vertical_adv_urls = vertical_advertisement_view(request, slug)
    horizontal_adv_urls = horizontal_advertisement_view(request, slug)
    poster_adv_url = poster_advertisement_view(request, slug)
    box_adv_url = box_advertisement_view(request, slug)
    popup_adv_url = popup_advertisement_view(request, slug)

    # Other dynamic content
    current_news = current_news_view(request)
    live_streaming = live_streaming_view(request)
    focus_video = focus_video_view(request)
    site_associate = Site_associate.objects.first()

    # Get the news index page and related news details
    news_index_page = NewsIndexPage.objects.get(slug=slug)
    news_details = get_latest_news(news_index_page)
    
    news_range = get_latest_news_range(news_index_page, 2, 5)
    
    additional_news = []
    for news in news_range:
        additional_news.append({
            "image_url": news.image.file.url if news.image else "./assets/default_news.png",  # Default image fallback
            "main_heading": news.main_heading,
        })

    if news_details:
        # Convert times to local timezone
        local_published_date = get_localized_time(news_details.published_date)
        local_updated_date = get_localized_time(news_details.updated_date)
        
        # Retrieve the details and insert advertisements dynamically
        news_details_text = insert_advertisements(news_details.details, box_adv_url)
    else:
        local_published_date = None
        local_updated_date = None
        news_details_text = "No details available"

    # Second latest news details
    second_latest_news = get_second_latest_news(news_index_page)
    if second_latest_news:
        local_second_latest_published_date = get_localized_time(second_latest_news.published_date)
        second_latest_news_image_url = second_latest_news.image.file.url if second_latest_news.image else None
        second_latest_main_heading = second_latest_news.main_heading
        second_latest_updated_date = local_second_latest_published_date
        second_latest_subtitle = second_latest_news.subtitle
    else:
        second_latest_news_image_url = None
        second_latest_main_heading = "No second latest news available"
        second_latest_updated_date = None
        second_latest_subtitle = "No subtitle available"

    # Create context for template rendering
    context = {
        "vertical_adv_left_url": vertical_adv_urls[0],
        "vertical_adv_right_url": vertical_adv_urls[1],
        "horizontal_adv_urls": horizontal_adv_urls,
        "poster_adv_url": poster_adv_url,
        "box_adv_url": box_adv_url,
        "popup_adv_url": popup_adv_url,
        "current_news": current_news,
        "live_streaming": live_streaming,
        "focus_video": focus_video,
        "site_associate": site_associate,
        
        "page_choice_name": news_index_page.title,
        "main_heading": news_details.main_heading if news_details else "No news available",  # Latest main heading
        "subtitle": news_details.subtitle if news_details else "No subtitle available",  # Latest subtitle
        "details": format_html(news_details_text),  # Render the processed details as safe HTML
        "image_url": news_details.image.file.url if news_details and news_details.image else None,  # Image URL
        "published_date": local_published_date,  # Published date in local timezone
        "updated_date": local_updated_date,  # Updated date in local timezone

        "second_latest_news_image_url": second_latest_news_image_url,
        "second_latest_main_heading": second_latest_main_heading,
        "second_latest_updated_date": second_latest_updated_date,
        "second_latest_subtitle": second_latest_subtitle,
        "additional_news": additional_news,
    }

    # Render the template
    return render(request, 'home/news_index_page.html', context)

