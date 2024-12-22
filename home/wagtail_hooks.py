from .models import *
from wagtail_modeladmin.options import ModelAdmin,ModelAdminGroup, modeladmin_register





"""
.##....##.########.##......##..######.
.###...##.##.......##..##..##.##....##
.####..##.##.......##..##..##.##......
.##.##.##.######...##..##..##..######.
.##..####.##.......##..##..##.......##
.##...###.##.......##..##..##.##....##
.##....##.########..###..###...######.
"""

class NewsCategoryAdmin(ModelAdmin):
    model = NewsCategory
    menu_order = 200
    menu_label = "News Category"
    menu_icon = "view"
    add_to_settings_menu = False
    list_display = ("category",)
    search_fields = ("category",)
    
class NewsDetailsAdmin(ModelAdmin):
    model = NewsDetailsPage
    menu_label = "Newsroom"
    menu_icon = "form"
    menu_order = 210
    list_display = (
        "main_heading",
        "news_category",
        "published_date",
        "make_featured_news",
    )
    list_display = ("news_category",)
    search_fields = ("news_category",)
    
class Newsroom(ModelAdminGroup):
    menu_label = "Newsroom"
    menu_icon = "glasses"
    menu_order = 300
    items = (NewsCategoryAdmin, NewsDetailsAdmin)


modeladmin_register(Newsroom) 
 
  
class CurrentNewsAdmin(ModelAdmin):
    model = CurrentNews
    menu_label = 'Current News'  # ditch this to use verbose_name_plural from model
    menu_icon = 'crosshairs'
    menu_order = 210  
    list_display = ('news_bulletin', 'published_date')
    search_fields = ('news_bulletin',)
    list_filter = ('published_date',)
modeladmin_register(CurrentNewsAdmin)


class AmarBartaAdmin(ModelAdmin):
    model = AmarBarta
    menu_label = 'Amar Barta News'  # ditch this to use verbose_name_plural from model
    menu_icon = 'form'
    menu_order = 220
    list_display = ('main_heading', 'published_date', 'updated_date')
    search_fields = ('main_heading', 'subtitle')
    list_filter = ('published_date',)

modeladmin_register(AmarBartaAdmin)



##     ## ####  ######   ######  #### ##    ##  ######      ##     ## ########  ######   ######     ###     ######   ######## 
###   ###  ##  ##    ## ##    ##  ##  ###   ## ##    ##     ###   ### ##       ##    ## ##    ##   ## ##   ##    ##  ##       
#### ####  ##  ##       ##        ##  ####  ## ##           #### #### ##       ##       ##        ##   ##  ##        ##       
## ### ##  ##   ######   ######   ##  ## ## ## ##   ####    ## ### ## ######    ######   ######  ##     ## ##   #### ######   
##     ##  ##        ##       ##  ##  ##  #### ##    ##     ##     ## ##             ##       ## ######### ##    ##  ##       
##     ##  ##  ##    ## ##    ##  ##  ##   ### ##    ##     ##     ## ##       ##    ## ##    ## ##     ## ##    ##  ##       
##     ## ####  ######   ######  #### ##    ##  ######      ##     ## ########  ######   ######  ##     ##  ######   ######## 

class MissingMessageAdmin(ModelAdmin):
    model = MissingMessage
    menu_label = 'Missing News'  # Ditch this to use verbose_name_plural from model
    menu_icon = 'warning'  # Use an appropriate Wagtail icon (e.g., 'warning' for missing alerts)
    menu_order = 230  # Position in the menu
    list_display = ('name', 'age', 'skin_tone', 'missing_time_date', 'contact_number')
    search_fields = ('name', 'contact_number', 'skin_tone')
    list_filter = ('missing_time_date','published_date')

# Register the ModelAdmin class
modeladmin_register(MissingMessageAdmin)
