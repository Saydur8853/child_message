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
    missing_person = missing_person_details_view(request)
    latest_news = latest_news_view(request)
    popup_adv_url = popup_advertisement_view(request)
    
    return render(
        request,
        'home/home_page.html',
        {
            'missing_person': missing_person, 
            'latest_news': latest_news,
            'popup_adv_url': popup_adv_url,
        }
    )