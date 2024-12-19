from wagtail import hooks
from .models import *
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register




"""
.##....##.########.##......##..######.
.###...##.##.......##..##..##.##....##
.####..##.##.......##..##..##.##......
.##.##.##.######...##..##..##..######.
.##..####.##.......##..##..##.......##
.##...###.##.......##..##..##.##....##
.##....##.########..###..###...######.
"""

class AmarBartaAdmin(ModelAdmin):
    model = AmarBarta
    menu_label = 'Amar Barta'  # ditch this to use verbose_name_plural from model
    menu_icon = 'form'
    menu_order = 200  
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
    menu_label = 'Missing Messages'  # Ditch this to use verbose_name_plural from model
    menu_icon = 'warning'  # Use an appropriate Wagtail icon (e.g., 'warning' for missing alerts)
    menu_order = 210  # Position in the menu
    list_display = ('name', 'age', 'skin_tone', 'missing_time_date', 'contact_number')
    search_fields = ('name', 'contact_number', 'skin_tone')
    list_filter = ('missing_time_date','published_date')

# Register the ModelAdmin class
modeladmin_register(MissingMessageAdmin)
