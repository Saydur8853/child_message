   ###    ########  ##     ## ######## ########  ######## ####  ######  ######## ##     ## ######## ##    ## ######## 
  ## ##   ##     ## ##     ## ##       ##     ##    ##     ##  ##    ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##     ## ##     ## ##       ##     ##    ##     ##  ##       ##       #### #### ##       ####  ##    ##    
##     ## ##     ## ##     ## ######   ########     ##     ##   ######  ######   ## ### ## ######   ## ## ##    ##    
######### ##     ##  ##   ##  ##       ##   ##      ##     ##        ## ##       ##     ## ##       ##  ####    ##    
##     ## ##     ##   ## ##   ##       ##    ##     ##     ##  ##    ## ##       ##     ## ##       ##   ###    ##    
##     ## ########     ###    ######## ##     ##    ##    ####  ######  ######## ##     ## ######## ##    ##    ##    


from django.shortcuts import render
from .models import *

from .views import current_news_view, live_streaming_view,focus_video_view
from django.shortcuts import render, get_object_or_404

# Fetch the popup advertisement
def popup_advertisement_view(request):
    try:
        missingnewspage = get_object_or_404(MissingNewsPage)
        popup_adv_url = None
        
        # Iterate through the advertisement blocks
        for block in missingnewspage.advertisement:
            if block.block_type == "Popup_Adv":
                image = block.value.get("image")
                # print(f"Image found: {image}")  # Debugging line
                if image:  # Ensure the image exists
                    # Generate the rendition
                    rendition = image.get_rendition("width-500")
                    popup_adv_url = rendition.url  # Get the URL of the rendition
                    # print(f"Popup Image URL: {popup_adv_url}")  # Debugging line
                break
    except MissingNewsPage.DoesNotExist:
        popup_adv_url = None

    return popup_adv_url

# Fetch the vertical advertisement
def vertical_advertisement_view(request):
    try:
        missingnewspage = get_object_or_404(MissingNewsPage)
        vertical_adv_urls = []
        
        for block in missingnewspage.advertisement:
            if block.block_type == "Vertical_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-168x934-c0")
                    vertical_adv_urls.append(rendition.url)
                    
                if len(vertical_adv_urls) >= 2:  # Limit to two images
                    break
    except MissingNewsPage.DoesNotExist:
        vertical_adv_urls = [None, None]

    # Ensure two entries for left and right ads
    while len(vertical_adv_urls) < 2:
        vertical_adv_urls.append(None)

    return vertical_adv_urls

# Fetch the horizontal advertisement
def horizontal_advertisement_view(request):
    try:
        missingnewspage = get_object_or_404(MissingNewsPage)
        horizontal_adv_urls = []

        for block in missingnewspage.advertisement:
            if block.block_type == "Horizontal_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("height-135")
                    horizontal_adv_urls.append(rendition.url)

                if len(horizontal_adv_urls) >= 7:  # Limit to one image
                    break
    except MissingNewsPage.DoesNotExist:
        horizontal_adv_urls = [None]

    # Ensure at least one entry for horizontal ad
    while len(horizontal_adv_urls) < 7:
        horizontal_adv_urls.append(None)

    return horizontal_adv_urls


# Fetch the poster advertisement
def poster_advertisement_view(request):
    try:
        missingnewspage = get_object_or_404(MissingNewsPage)
        poster_adv_url = None
        
        for block in missingnewspage.advertisement:
            if block.block_type == "Poster_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-305x545-c0")
                    poster_adv_url = rendition.url
                break
    except MissingNewsPage.DoesNotExist:
        poster_adv_url = None

    return poster_adv_url

# Fetch the box advertisement
def box_advertisement_view(request):
    try:
        missingnewspage = get_object_or_404(MissingNewsPage)
        box_adv_url = None
        
        for block in missingnewspage.advertisement:
            if block.block_type == "Box_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("width-420")
                    box_adv_url = rendition.url
                break
    except MissingNewsPage.DoesNotExist:
        box_adv_url = None

    return box_adv_url




def missing_news_view(request):
    vertical_adv_urls = vertical_advertisement_view(request)
    horizontal_adv_urls = horizontal_advertisement_view(request)
    poster_adv_url = poster_advertisement_view(request)
    box_adv_url = box_advertisement_view(request)
    popup_adv_url = popup_advertisement_view(request)

    current_news = current_news_view(request)  
    live_streaming = live_streaming_view(request)
    focus_video = focus_video_view(request)
    site_associate = Site_associate.objects.first()
    missing_person = MissingMessage.objects.last() 
    # Check if missing_person exists
    if missing_person:
        other_missing_messages = MissingMessage.objects.exclude(id=missing_person.id).order_by('-published_date')[:4]
    else:
        other_missing_messages = MissingMessage.objects.order_by('-published_date')[:4]

    # Create the context
    context = {
        "vertical_adv_left_url": vertical_adv_urls[0],
        "vertical_adv_right_url": vertical_adv_urls[1],
        "horizontal_adv_url_1": horizontal_adv_urls[0],
        "horizontal_adv_url_2": horizontal_adv_urls[1],
        "horizontal_adv_url_3": horizontal_adv_urls[2],
        "horizontal_adv_url_4": horizontal_adv_urls[3],
        "horizontal_adv_url_5": horizontal_adv_urls[4],
        "horizontal_adv_url_6": horizontal_adv_urls[5],
        "horizontal_adv_url_7": horizontal_adv_urls[6],
        "poster_adv_url": poster_adv_url,
        "box_adv_url": box_adv_url,
        "popup_adv_url": popup_adv_url,
        "current_news": current_news,
        "live_streaming": live_streaming,
        "focus_video": focus_video,
        "site_associate": site_associate,
        "missing_person": missing_person,
        "other_missing_messages": other_missing_messages,

    }

    # Render the template
    return render(request, 'home/missing_news_page.html', context)
