from wagtail import hooks
from .models import AmarBarta
from wagtail_modeladmin.options import ModelAdmin, modeladmin_register



class AmarBartaAdmin(ModelAdmin):
    model = AmarBarta
    menu_label = 'Amar Barta'  # ditch this to use verbose_name_plural from model
    menu_icon = 'form'
    menu_order = 200  
    list_display = ('main_heading', 'published_date', 'updated_date')
    search_fields = ('main_heading', 'subtitle')
    list_filter = ('published_date',)

modeladmin_register(AmarBartaAdmin)