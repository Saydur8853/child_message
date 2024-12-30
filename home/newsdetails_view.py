   ###    ########  ##     ## ######## ########  ######## ####  ######  ######## ##     ## ######## ##    ## ######## 
  ## ##   ##     ## ##     ## ##       ##     ##    ##     ##  ##    ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##     ## ##     ## ##       ##     ##    ##     ##  ##       ##       #### #### ##       ####  ##    ##    
##     ## ##     ## ##     ## ######   ########     ##     ##   ######  ######   ## ### ## ######   ## ## ##    ##    
######### ##     ##  ##   ##  ##       ##   ##      ##     ##        ## ##       ##     ## ##       ##  ####    ##    
##     ## ##     ##   ## ##   ##       ##    ##     ##     ##  ##    ## ##       ##     ## ##       ##   ###    ##    
##     ## ########     ###    ######## ##     ##    ##    ####  ######  ######## ##     ## ######## ##    ##    ##    


from django.shortcuts import render
from .models import *

from .views import current_news_view,live_streaming_view,focus_video_view
from django.shortcuts import render, get_object_or_404


# Fetch the popup advertisement
def popup_advertisement_view(request, news_slug):
    try:
        newsdetailspage = get_object_or_404(NewsDetailsPage, slug=news_slug)
        popup_adv_url = None
        
        # Iterate through the advertisement blocks
        for block in newsdetailspage.advertisement:
            if block.block_type == "Popup_Adv":
                image = block.value.get("image")
                # print(f"Image found: {image}")  # Debugging line
                if image:  # Ensure the image exists
                    # Generate the rendition
                    rendition = image.get_rendition("width-500")
                    popup_adv_url = rendition.url  # Get the URL of the rendition
                    # print(f"Popup Image URL: {popup_adv_url}")  # Debugging line
                break
    except NewsDetailsPage.DoesNotExist:
        popup_adv_url = None

    return popup_adv_url

# Fetch the vertical advertisement
def vertical_advertisement_view(request, news_slug):
    try:
        newsdetailspage = get_object_or_404(NewsDetailsPage, slug=news_slug)
        vertical_adv_urls = []
        
        for block in newsdetailspage.advertisement:
            if block.block_type == "Vertical_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-168x934-c0")
                    vertical_adv_urls.append(rendition.url)
                    
                if len(vertical_adv_urls) >= 2:  # Limit to two images
                    break
    except NewsDetailsPage.DoesNotExist:
        vertical_adv_urls = [None, None]

    # Ensure two entries for left and right ads
    while len(vertical_adv_urls) < 2:
        vertical_adv_urls.append(None)

    return vertical_adv_urls

# Fetch the horizontal advertisement
def horizontal_advertisement_view(request, news_slug):
    try:
        newsdetailspage = get_object_or_404(NewsDetailsPage, slug=news_slug)
        horizontal_adv_urls = []

        for block in newsdetailspage.advertisement:
            if block.block_type == "Horizontal_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("height-135")
                    horizontal_adv_urls.append(rendition.url)

                if len(horizontal_adv_urls) >= 7:  # Limit to one image
                    break
    except NewsDetailsPage.DoesNotExist:
        horizontal_adv_urls = [None]

    # Ensure at least one entry for horizontal ad
    while len(horizontal_adv_urls) < 7:
        horizontal_adv_urls.append(None)

    return horizontal_adv_urls


# Fetch the poster advertisement
def poster_advertisement_view(request, news_slug):
    try:
        newsdetailspage = get_object_or_404(NewsDetailsPage, slug=news_slug)
        poster_adv_url = None
        
        for block in newsdetailspage.advertisement:
            if block.block_type == "Poster_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-305x545-c0")
                    poster_adv_url = rendition.url
                break
    except NewsDetailsPage.DoesNotExist:
        poster_adv_url = None

    return poster_adv_url

# Fetch the box advertisement
def box_advertisement_view(request, news_slug):
    try:
        newsdetailspage = get_object_or_404(NewsDetailsPage, slug=news_slug)
        box_adv_url = None
        
        for block in newsdetailspage.advertisement:
            if block.block_type == "Box_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("width-420")
                    box_adv_url = rendition.url
                break
    except NewsDetailsPage.DoesNotExist:
        box_adv_url = None

    return box_adv_url




def newsdetails_combined_view(request,category_slug,news_slug):
    vertical_adv_urls = vertical_advertisement_view(request,news_slug)
    horizontal_adv_urls = horizontal_advertisement_view(request,news_slug)
    poster_adv_url = poster_advertisement_view(request,news_slug)
    box_adv_url = box_advertisement_view(request,news_slug)
    popup_adv_url = popup_advertisement_view(request,news_slug)

    current_news = current_news_view(request)  
    live_streaming = live_streaming_view(request)
    focus_video = focus_video_view(request)


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
    }

    # Render the template
    return render(request, 'home/news_details_page.html', context)
