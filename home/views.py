from django.http import JsonResponse
from .forms import ChildGeneralistForm, ChildPresenterForm
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
from django.shortcuts import render
from .models import *
from wagtail.models import Site


# @csrf_exempt
# def submit_child_form(request):
#     if request.method == 'POST':
#         form_type = request.POST.get('form_type')  # Form type (Child Generalist or Presenter)

#         if form_type == 'শিশু সাংবাদিকের তথ্য':
#             form = ChildGeneralistForm(request.POST)
#         else:
#             form = ChildPresenterForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             return JsonResponse({'success': False, 'error': form.errors})

#     return JsonResponse({'success': False, 'error': 'Invalid request'})


def menu_items(request):
    # Find the site based on the request
    site = Site.find_for_request(request)
    
    # If no site is found, return an empty menu list
    if not site:
        return {'menu_items': []}
    
    # Try to get the MainMenu for the site
    try:
        menu = MainMenu.for_site(site)
        # Return the menu items if available, else return an empty list
        return {'menu_items': menu.menu_items.all() if menu else []}
    except MainMenu.DoesNotExist:
        # In case MainMenu does not exist for the site, return an empty list
        return {'menu_items': []}


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
# Fetch the current news (for the scrolling marquee)
def current_news_view(request):
    # Fetch current news published in the last week, or None if none are available
    current_news = CurrentNews.objects.filter(published_date__gte=timezone.now() - timedelta(weeks=1)).order_by('-published_date') if CurrentNews.objects.exists() else None
    return current_news



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

##       #### ##     ## ######## 
##        ##  ##     ## ##       
##        ##  ##     ## ##       
##        ##  ##     ## ######   
##        ##   ##   ##  ##       
##        ##    ## ##   ##       
######## ####    ###    ########  
def live_streaming_view(request):
    try:
        livestreaming  = LiveStreaming.objects.last()
    except LiveStreaming.DoesNotExist:
        livestreaming  = None

    return livestreaming 

########  #######   ######  ##     ##  ######     ##     ## #### ########  ########  #######  
##       ##     ## ##    ## ##     ## ##    ##    ##     ##  ##  ##     ## ##       ##     ## 
##       ##     ## ##       ##     ## ##          ##     ##  ##  ##     ## ##       ##     ## 
######   ##     ## ##       ##     ##  ######     ##     ##  ##  ##     ## ######   ##     ## 
##       ##     ## ##       ##     ##       ##     ##   ##   ##  ##     ## ##       ##     ## 
##       ##     ## ##    ## ##     ## ##    ##      ## ##    ##  ##     ## ##       ##     ## 
##        #######   ######   #######   ######        ###    #### ########  ########  #######  

def focus_video_view(request):
    try:
        focus_video = FocusVideo.objects.first()  # Get the latest video or link
    except FocusVideo.DoesNotExist:
        focus_video = None

    return focus_video

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
    current_news = current_news_view(request)
    live_streaming = live_streaming_view(request)
    focus_video = focus_video_view(request)
    site_associate = Site_associate.objects.first()

    # Determine which form to use
    form_type = request.GET.get('form_type', 'generalist')  # Default to 'generalist'
    form = None

    if form_type == 'presenter':
        form = ChildPresenterForm(request.POST or None)
    else:
        form = ChildGeneralistForm(request.POST or None)

    # Handle form submission
    if request.method == 'POST':
        if form.is_valid():
            form.save()  # Save the form if it's valid
            return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

    return render(
        request,
        'home/home_page.html',
        {
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
            "missing_person": missing_person, 
            "current_news": current_news,
            "live_streaming": live_streaming,
            "focus_video": focus_video,
            "site_associate": site_associate,
            "form": form, 
        }
    )

