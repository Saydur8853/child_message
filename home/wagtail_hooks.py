from .models import *
from wagtail_modeladmin.options import ModelAdmin,ModelAdminGroup, modeladmin_register


class LiveStreamingAdmin(ModelAdmin):
    model = LiveStreaming
    menu_label = "Live Streaming"
    menu_icon = "view"  # Choose a Wagtail icon (e.g., 'link', 'media')
    list_display = ("link", "published_date")
    search_fields = ("link",)


class FocusVideoAdmin(ModelAdmin):
    model = FocusVideo
    menu_label = "Focus Videos"
    menu_icon = "media"  # Choose a Wagtail icon
    list_display = ("video", "link", "published_date")
    search_fields = ("video", "link")


modeladmin_register(LiveStreamingAdmin)
modeladmin_register(FocusVideoAdmin)

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
    model = NewsDetails
    menu_label = "Newsroom"
    menu_icon = "form"
    menu_order = 210
    list_display = (
        "main_heading",
        "page_choice",
        "news_category",
        "published_date",
        "make_featured_news",
    )
    search_fields = ("news_category__name",)
    list_filter = ("page_choice","news_category","published_date","make_featured_news",)
    
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

 ######  ##     ## #### ##       ########  ########  ######## ##    ##    ##     ##    ###    ##    ##    ###     ######   ######## ##     ## ######## ##    ## ######## 
##    ## ##     ##  ##  ##       ##     ## ##     ## ##       ###   ##    ###   ###   ## ##   ###   ##   ## ##   ##    ##  ##       ###   ### ##       ###   ##    ##    
##       ##     ##  ##  ##       ##     ## ##     ## ##       ####  ##    #### ####  ##   ##  ####  ##  ##   ##  ##        ##       #### #### ##       ####  ##    ##    
##       #########  ##  ##       ##     ## ########  ######   ## ## ##    ## ### ## ##     ## ## ## ## ##     ## ##   #### ######   ## ### ## ######   ## ## ##    ##    
##       ##     ##  ##  ##       ##     ## ##   ##   ##       ##  ####    ##     ## ######### ##  #### ######### ##    ##  ##       ##     ## ##       ##  ####    ##    
##    ## ##     ##  ##  ##       ##     ## ##    ##  ##       ##   ###    ##     ## ##     ## ##   ### ##     ## ##    ##  ##       ##     ## ##       ##   ###    ##    
 ######  ##     ## #### ######## ########  ##     ## ######## ##    ##    ##     ## ##     ## ##    ## ##     ##  ######   ######## ##     ## ######## ##    ##    ##    

# Admin for StudentClass
class StudentClassAdmin(ModelAdmin):
    model = StudentClass
    menu_label = "Student Classes"
    menu_icon = "list-ul"  # Choose an icon from Wagtail's icon set
    list_display = ("name",)
    search_fields = ("name",)
   
class ChildGeneralistAdmin(ModelAdmin):
    model = ChildGeneralist
    menu_label = "Child Generalists" 
    menu_icon = "user"  
    list_display = ("name", "father_name", "mother_name", "student_class", "district", "phone_no")
    search_fields = ("name", "father_name", "mother_name", "district", "phone_no")
    list_filter = ('student_class','district')


class ChildPresenterAdmin(ModelAdmin):
    model = ChildPresenter
    menu_label = "Child Presenters"
    menu_icon = "user"  
    list_display = ("name", "father_name", "mother_name", "student_class", "district", "phone_no")
    search_fields = ("name", "father_name", "mother_name", "district", "phone_no")
    list_filter = ('student_class','district')

class ChildAdminGroup(ModelAdminGroup):
    menu_label = "Children Management"
    menu_icon = "group"
    items = (StudentClassAdmin,ChildGeneralistAdmin, ChildPresenterAdmin)

modeladmin_register(ChildAdminGroup)


class SiteAssociateAdmin(ModelAdmin):
    model = Site_associate
    menu_label = "Site Associate"  
    menu_icon = "cogs"
    menu_order = 500  
    add_to_settings_menu = True  
    exclude_from_explorer = False  
    list_display = ("hotline_number", "child_helpline_number", "copyright_line")
    search_fields = ("hotline_number", "child_helpline_number", "copyright_line")

# Register the model admin class
modeladmin_register(SiteAssociateAdmin)