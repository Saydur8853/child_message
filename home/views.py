from django.shortcuts import render
from .models import *




   ###    ########  ##     ## ######## ########  ######## ####  ######  ######## ##     ## ######## ##    ## ######## 
  ## ##   ##     ## ##     ## ##       ##     ##    ##     ##  ##    ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##     ## ##     ## ##       ##     ##    ##     ##  ##       ##       #### #### ##       ####  ##    ##    
##     ## ##     ## ##     ## ######   ########     ##     ##   ######  ######   ## ### ## ######   ## ## ##    ##    
######### ##     ##  ##   ##  ##       ##   ##      ##     ##        ## ##       ##     ## ##       ##  ####    ##    
##     ## ##     ##   ## ##   ##       ##    ##     ##     ##  ##    ## ##       ##     ## ##       ##   ###    ##    
##     ## ########     ###    ######## ##     ##    ##    ####  ######  ######## ##     ## ######## ##    ##    ##    

# Fetch the popup advertisement
def popup_advertisement_view(request):
    try:
        homepage = HomePage.objects.live().first()
        popup_adv_url = None
        
        # Iterate through the advertisement blocks
        for block in homepage.advertisement:
            if block.block_type == "Popup_Adv":
                image = block.value.get("image")
                # print(f"Image found: {image}")  # Debugging line
                if image:  # Ensure the image exists
                    # Generate the rendition
                    rendition = image.get_rendition("width-500")
                    popup_adv_url = rendition.url  # Get the URL of the rendition
                    # print(f"Popup Image URL: {popup_adv_url}")  # Debugging line
                break
    except HomePage.DoesNotExist:
        popup_adv_url = None

    return popup_adv_url

# Fetch the vertical advertisement
def vertical_advertisement_view(request):
    try:
        homepage = HomePage.objects.live().first()
        vertical_adv_urls = []
        
        for block in homepage.advertisement:
            if block.block_type == "Vertical_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-168x934-c0")
                    vertical_adv_urls.append(rendition.url)
                    
                if len(vertical_adv_urls) >= 2:  # Limit to two images
                    break
    except HomePage.DoesNotExist:
        vertical_adv_urls = [None, None]

    # Ensure two entries for left and right ads
    while len(vertical_adv_urls) < 2:
        vertical_adv_urls.append(None)

    return vertical_adv_urls

# Fetch the horizontal advertisement
def horizontal_advertisement_view(request):
    try:
        homepage = HomePage.objects.live().first()
        horizontal_adv_urls = []

        for block in homepage.advertisement:
            if block.block_type == "Horizontal_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("height-135")
                    horizontal_adv_urls.append(rendition.url)

                if len(horizontal_adv_urls) >= 7:  # Limit to one image
                    break
    except HomePage.DoesNotExist:
        horizontal_adv_urls = [None]

    # Ensure at least one entry for horizontal ad
    while len(horizontal_adv_urls) < 7:
        horizontal_adv_urls.append(None)

    return horizontal_adv_urls


# Fetch the poster advertisement
def poster_advertisement_view(request):
    try:
        homepage = HomePage.objects.live().first()
        poster_adv_url = None
        
        for block in homepage.advertisement:
            if block.block_type == "Poster_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("fill-305x545-c0")
                    poster_adv_url = rendition.url
                break
    except HomePage.DoesNotExist:
        poster_adv_url = None

    return poster_adv_url

# Fetch the box advertisement
def box_advertisement_view(request):
    try:
        homepage = HomePage.objects.live().first()
        box_adv_url = None
        
        for block in homepage.advertisement:
            if block.block_type == "Box_Adv":
                image = block.value.get("image")
                if image:
                    rendition = image.get_rendition("width-420")
                    box_adv_url = rendition.url
                break
    except HomePage.DoesNotExist:
        box_adv_url = None

    return box_adv_url



"""
.##....##.########.##......##..######.
.###...##.##.......##..##..##.##....##
.####..##.##.......##..##..##.##......
.##.##.##.######...##..##..##..######.
.##..####.##.......##..##..##.......##
.##...###.##.......##..##..##.##....##
.##....##.########..###..###...######.
"""
def latest_news_view(request):
    try:
        latest_news = AmarBarta.objects.latest('published_date')  # Get the most recent news item
    except AmarBarta.DoesNotExist:
        latest_news = None  # Or you can set a default value here, such as an empty string or a placeholder
    
    return latest_news


##     ## ####  ######   ######  #### ##    ##  ######      ##     ## ########  ######   ######     ###     ######   ######## 
###   ###  ##  ##    ## ##    ##  ##  ###   ## ##    ##     ###   ### ##       ##    ## ##    ##   ## ##   ##    ##  ##       
#### ####  ##  ##       ##        ##  ####  ## ##           #### #### ##       ##       ##        ##   ##  ##        ##       
## ### ##  ##   ######   ######   ##  ## ## ## ##   ####    ## ### ## ######    ######   ######  ##     ## ##   #### ######   
##     ##  ##        ##       ##  ##  ##  #### ##    ##     ##     ## ##             ##       ## ######### ##    ##  ##       
##     ##  ##  ##    ## ##    ##  ##  ##   ### ##    ##     ##     ## ##       ##    ## ##    ## ##     ## ##    ##  ##       
##     ## ####  ######   ######  #### ##    ##  ######      ##     ## ########  ######   ######  ##     ##  ######   ######## 

def missing_person_details_view(request):
    try:
        missing_person = MissingMessage.objects.latest('published_date')  # Use published_date to get the latest
    except MissingMessage.DoesNotExist:
        missing_person = None

    return missing_person

 ######   #######  ##     ## ########  #### ##    ## ######## 
##    ## ##     ## ###   ### ##     ##  ##  ###   ## ##       
##       ##     ## #### #### ##     ##  ##  ####  ## ##       
##       ##     ## ## ### ## ########   ##  ## ## ## ######   
##       ##     ## ##     ## ##     ##  ##  ##  #### ##       
##    ## ##     ## ##     ## ##     ##  ##  ##   ### ##       
 ######   #######  ##     ## ########  #### ##    ## ########  
def combined_view(request):
    vertical_adv_urls = vertical_advertisement_view(request)
    horizontal_adv_urls = horizontal_advertisement_view(request)
    poster_adv_url = poster_advertisement_view(request)
    box_adv_url = box_advertisement_view(request)
    popup_adv_url = popup_advertisement_view(request)

    missing_person = missing_person_details_view(request)
    latest_news = latest_news_view(request)
    return render(
        request,
        'home/home_page.html',
        {
            'vertical_adv_left_url': vertical_adv_urls[0],
            'vertical_adv_right_url': vertical_adv_urls[1],

            'horizontal_adv_url_1': horizontal_adv_urls[0],
            'horizontal_adv_url_2': horizontal_adv_urls[1],
            'horizontal_adv_url_3': horizontal_adv_urls[2],
            'horizontal_adv_url_4': horizontal_adv_urls[3],
            'horizontal_adv_url_5': horizontal_adv_urls[4],
            'horizontal_adv_url_6': horizontal_adv_urls[5],
            'horizontal_adv_url_7': horizontal_adv_urls[6],


            # 'horizontal_adv_url': horizontal_adv_url,
            'poster_adv_url': poster_adv_url,
            'box_adv_url': box_adv_url,
            'popup_adv_url': popup_adv_url,
            'missing_person': missing_person, 
            'latest_news': latest_news,
        }
    )