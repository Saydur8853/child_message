from django.db import models
from django.utils import timezone

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
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
        
    ]
    
 ######  ##     ## ########  ########  ######## ##    ## ########    ##    ## ######## ##      ##  ######  
##    ## ##     ## ##     ## ##     ## ##       ###   ##    ##       ###   ## ##       ##  ##  ## ##    ## 
##       ##     ## ##     ## ##     ## ##       ####  ##    ##       ####  ## ##       ##  ##  ## ##       
##       ##     ## ########  ########  ######   ## ## ##    ##       ## ## ## ######   ##  ##  ##  ######  
##       ##     ## ##   ##   ##   ##   ##       ##  ####    ##       ##  #### ##       ##  ##  ##       ## 
##    ## ##     ## ##    ##  ##    ##  ##       ##   ###    ##       ##   ### ##       ##  ##  ## ##    ## 
 ######   #######  ##     ## ##     ## ######## ##    ##    ##       ##    ## ########  ###  ###   ######  
class CurrentNews(models.Model):
    news_bulletin = models.CharField(max_length=500, help_text="Enter news heading")
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.news_bulletin


   ###    ##     ##    ###    ########     ########     ###    ########  ########    ###    
  ## ##   ###   ###   ## ##   ##     ##    ##     ##   ## ##   ##     ##    ##      ## ##   
 ##   ##  #### ####  ##   ##  ##     ##    ##     ##  ##   ##  ##     ##    ##     ##   ##  
##     ## ## ### ## ##     ## ########     ########  ##     ## ########     ##    ##     ## 
######### ##     ## ######### ##   ##      ##     ## ######### ##   ##      ##    ######### 
##     ## ##     ## ##     ## ##    ##     ##     ## ##     ## ##    ##     ##    ##     ## 
##     ## ##     ## ##     ## ##     ##    ########  ##     ## ##     ##    ##    ##     ## 
                                                                                                                                                                          
class AmarBarta(models.Model, index.Indexed):
    main_heading = models.CharField(max_length=255, help_text="Main Heading of the News")
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
    

    def __str__(self):
        return self.main_heading
    
    class Meta:
        verbose_name = "Amar Barta"
        verbose_name_plural = "Amar Bartas"

    

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


    ##    ## ######## ##      ##  ######  
    ###   ## ##       ##  ##  ## ##    ## 
    ####  ## ##       ##  ##  ## ##       
    ## ## ## ######   ##  ##  ##  ######  
    ##  #### ##       ##  ##  ##       ## 
    ##   ### ##       ##  ##  ## ##    ## 
    ##    ## ########  ###  ###   ######  

class NewsCategory(models.Model):
    category = models.CharField(
        _("News Category"), max_length=50, blank=True, null=True
    )

    def __str__(self):
        return self.category
    
    
    # ---------------------------------------------------------------------
    #                             NewsIndexPage
    # ---------------------------------------------------------------------
class NewsIndexPage(MenuPage):
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
    parent_page_types = ["home.HomePage"]
    subpage_types = ["home.NewsDetailsPage"]
    
    
    # ---------------------------------------------------------------------
    #                             NewsDetailsPage
    # ---------------------------------------------------------------------
    
    
    
class NewsDetailsPage(MenuPage):
    news_category = models.ForeignKey(
        NewsCategory,
        verbose_name=_("Select a Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news_details_page",
    )
    main_heading = models.CharField(max_length=255, help_text="Main Heading of the News")
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
        
    ]
    parent_page_types = ["home.NewsIndexPage"]
    subpage_types = ["home.NewsDetailsPage"]

    def __str__(self):
        return self.main_heading
    
