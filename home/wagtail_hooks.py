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