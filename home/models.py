from django.db import models
from django.utils import timezone

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel
from wagtail.images.models import Image
from wagtail.search import index
from child_message.blocks import *
from django.utils.translation import gettext_lazy as _
from wagtailmenus.models import MenuPage

class HomePage(Page):
    advertisement = StreamField(
        [
            ("Vertical_Adv", VerticalAddBlock()),
            ("Horizontal_Adv", HorizontalAddBlock()),
            ("Poster_Adv", PosterAddBlock()),
            ("Box_Adv", BoxAddBlock()),
            ("Popup_Adv", PopupAddBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel('advertisement'),
    ]
    subpage_types = [
        "home.NewsIndexPage",
        "home.CheifVoicePage",
        "home.MissingNewsPage",
    ]
    
    
##    ## ######## ##      ##  ######     ########  ##     ## ##       ##       ######## ######## #### ##    ## 
###   ## ##       ##  ##  ## ##    ##    ##     ## ##     ## ##       ##       ##          ##     ##  ###   ## 
####  ## ##       ##  ##  ## ##          ##     ## ##     ## ##       ##       ##          ##     ##  ####  ## 
## ## ## ######   ##  ##  ##  ######     ########  ##     ## ##       ##       ######      ##     ##  ## ## ## 
##  #### ##       ##  ##  ##       ##    ##     ## ##     ## ##       ##       ##          ##     ##  ##  #### 
##   ### ##       ##  ##  ## ##    ##    ##     ## ##     ## ##       ##       ##          ##     ##  ##   ### 
##    ## ########  ###  ###   ######     ########   #######  ######## ######## ########    ##    #### ##    ## 

class CurrentNews(models.Model):
    news_bulletin = models.CharField(max_length=500, help_text="Enter news heading")
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.news_bulletin


    

##     ## ####  ######   ######  #### ##    ##  ######      ##     ## ########  ######   ######     ###     ######   ######## 
###   ###  ##  ##    ## ##    ##  ##  ###   ## ##    ##     ###   ### ##       ##    ## ##    ##   ## ##   ##    ##  ##       
#### ####  ##  ##       ##        ##  ####  ## ##           #### #### ##       ##       ##        ##   ##  ##        ##       
## ### ##  ##   ######   ######   ##  ## ## ## ##   ####    ## ### ## ######    ######   ######  ##     ## ##   #### ######   
##     ##  ##        ##       ##  ##  ##  #### ##    ##     ##     ## ##             ##       ## ######### ##    ##  ##       
##     ##  ##  ##    ## ##    ##  ##  ##   ### ##    ##     ##     ## ##       ##    ## ##    ## ##     ## ##    ##  ##       
##     ## ####  ######   ######  #### ##    ##  ######      ##     ## ########  ######   ######  ##     ##  ######   ######## 


class MissingMessage(models.Model):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Optimal_Dimension : 520x365",
        related_name="+",
    )
    name = models.CharField(max_length=255, help_text="Name of the missing person")
    age = models.PositiveIntegerField(help_text="Age of the missing person")
    skin_tone = models.CharField(max_length=100, help_text="Skin tone of the missing person")
    dress = models.CharField(max_length=255, help_text="Description of the dress the missing person was wearing")
    missing_time_date = models.DateTimeField(default=timezone.now, help_text="Time and date when the person went missing")
    published_date = models.DateTimeField(auto_now=True, help_text="Updated Date and Time")
    contact_number = models.CharField(max_length=15, help_text="Contact number to reach out for information")
    detail_story = models.TextField(help_text="Detailed story of the missing incident")

    def __str__(self):
        return f"{self.name} ({self.age} years old) - Missing"

    class Meta:
        verbose_name = "Missing Message"
        verbose_name_plural = "Missing Messages"

    # ---------------------------------------------------------------------
    #                             Missing message Page
    # ---------------------------------------------------------------------
class MissingNewsPage(Page):
    advertisement = StreamField(
        [
            ("Vertical_Adv", VerticalAddBlock()),
            ("Horizontal_Adv", HorizontalAddBlock()),
            ("Poster_Adv", PosterAddBlock()),
            ("Box_Adv", BoxAddBlock()),
            ("Popup_Adv", PopupAddBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel('advertisement'),
    ]
   
   


    ##    ## ######## ##      ##  ######  
    ###   ## ##       ##  ##  ## ##    ## 
    ####  ## ##       ##  ##  ## ##       
    ## ## ## ######   ##  ##  ##  ######  
    ##  #### ##       ##  ##  ##       ## 
    ##   ### ##       ##  ##  ## ##    ## 
    ##    ## ########  ###  ###   ######  

class NewsCategory(models.Model):
    category = models.CharField(_("News Category"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = "News Categories"   
    
    
    # ---------------------------------------------------------------------
    #                             NewsIndexPage
    # ---------------------------------------------------------------------
# from functools import cached_property
class NewsIndexPage(Page):
    advertisement = StreamField(
        [
            ("Vertical_Adv", VerticalAddBlock()),
            ("Horizontal_Adv", HorizontalAddBlock()),
            ("Poster_Adv", PosterAddBlock()),
            ("Box_Adv", BoxAddBlock()),
            ("Popup_Adv", PopupAddBlock()),
        ],
        null=True,
        blank=True,
    )
    def additional_menu_data(self, context={}):
        return {
            "use_initial_child": self.use_initial_child,
        }
    def get_template(self, request, *args, **kwargs):
        return "home/news_index_page.html"
    
    def get_context(self, request, *args, **kwargs):
        context = super(NewsIndexPage,self).get_context(request, *args, **kwargs)
        return context

        
    
    content_panels = Page.content_panels + [
        FieldPanel('advertisement'),
        
    ]
    subpage_types = ["home.NewsDetailsPage",]
    
    # @cached_property
    # def parent_page(self):
    #     return self.get_parent().specific
    
    
    
    # ---------------------------------------------------------------------
    #                             NewsDetailsPage
    # ---------------------------------------------------------------------
    
    
    
class NewsDetailsPage(Page):
    news_category = models.ForeignKey(
        NewsCategory,
        verbose_name=_("Select a Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news_details_page",
    )
    main_heading = models.CharField(max_length=255, help_text="Main Heading of the News",blank=True,)
    subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Subtitle of the News")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Optimal_Dimension : 520x365",
        related_name="+",
    )
    published_date = models.DateTimeField(default=timezone.now, help_text="Publish Date and Time")
    updated_date = models.DateTimeField(auto_now=True, help_text="Updated Date and Time")
    details = RichTextField(blank=True, help_text="Details of the news")
    make_featured_news = models.BooleanField(
        _("Make it featured?"), default=False, blank=True
    )
    advertisement = StreamField(
        [
            ("Vertical_Adv", VerticalAddBlock()),
            ("Horizontal_Adv", HorizontalAddBlock()),
            ("Poster_Adv", PosterAddBlock()),
            ("Box_Adv", BoxAddBlock()),
            ("Popup_Adv", PopupAddBlock()),
        ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [
        FieldPanel('advertisement'),
        FieldPanel('news_category'),
        FieldPanel('main_heading'),
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('published_date'),
        FieldPanel('details'),
        FieldPanel('make_featured_news'),
        
    ]
   
   
 ######  ##     ## ######## #### ########    ##     ##  #######  ####  ######  ######## 
##    ## ##     ## ##        ##  ##          ##     ## ##     ##  ##  ##    ## ##       
##       ##     ## ##        ##  ##          ##     ## ##     ##  ##  ##       ##       
##       ######### ######    ##  ######      ##     ## ##     ##  ##  ##       ######   
##       ##     ## ##        ##  ##           ##   ##  ##     ##  ##  ##       ##       
##    ## ##     ## ##        ##  ##            ## ##   ##     ##  ##  ##    ## ##       
 ######  ##     ## ######## #### ##             ###     #######  ####  ######  ######## 
 
 
class CheifVoicePage(Page):
    advertisement = StreamField(
        [
            ("Vertical_Adv", VerticalAddBlock()),
            ("Horizontal_Adv", HorizontalAddBlock()),
            ("Poster_Adv", PosterAddBlock()),
            ("Box_Adv", BoxAddBlock()),
            ("Popup_Adv", PopupAddBlock()),
        ],
        null=True,
        blank=True,
    )
    body = StreamField(
        [
            ("Chief_voice", ChiefBlock()),
        ],
        null=True,
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('advertisement'),
        FieldPanel('body'),
    ]
   


########  #######   #######  ######## ######## ########  
##       ##     ## ##     ##    ##    ##       ##     ## 
##       ##     ## ##     ##    ##    ##       ##     ## 
######   ##     ## ##     ##    ##    ######   ########  
##       ##     ## ##     ##    ##    ##       ##   ##   
##       ##     ## ##     ##    ##    ##       ##    ##  
##        #######   #######     ##    ######## ##     ## 

from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images import get_image_model_string

IMAGE_MODEL = get_image_model_string()
@register_setting
class FooterSettings(BaseSiteSetting):

    menu_title_1 = models.CharField(
        _("Menu Title 1"),
        max_length=200,
        null=True,
        blank=True,
    )

    text = models.CharField(
        _("Text"),
        max_length=200,
        null=True,
        blank=True,
    )

    facebook = models.URLField(_("Facebook"), max_length=255, blank=True)
    twitter = models.URLField(_("Twitter"), max_length=255, blank=True)
    instagram = models.URLField(_("Instagram"), max_length=255, blank=True)
    youtube = models.URLField(_("Youtube"), max_length=255, blank=True)


    menu_column_title_1 = models.CharField(
        _("Menu Column Title 1"),
        max_length=200,
        null=True,
        blank=True,
    )

    menu_column_1 = models.ForeignKey(
        "wagtailmenus.FlatMenu",
        verbose_name=_("Menu Column 1"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    menu_column_title_2 = models.CharField(
        _("Menu Column Title 2"),
        max_length=200,
        null=True,
        blank=True,
    )
    menu_column_2 = models.ForeignKey(
        "wagtailmenus.FlatMenu",
        verbose_name=_("Menu Column 2"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    copyright_line = models.CharField(
        _("copyright"),
        max_length=255,
        blank=True,
        default="Copyright © 2024 Child Message. All right reserved.",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("menu_title_1"),
                FieldPanel("text"),
                FieldPanel("menu_column_title_1"),
                FieldPanel("menu_column_1"),
                FieldPanel("menu_column_title_2"),
                FieldPanel("menu_column_2"),
            ],
            heading="Menus",
        ),
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("instagram"),
                FieldPanel("youtube"),
            ],
            heading="Social Links",
        ),
        FieldPanel("copyright_line"),
    ]

    class Meta:
        verbose_name = "Footer Settings"