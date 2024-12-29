from django.db import models
from django.utils import timezone

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index
from child_message.blocks import *
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from django.core.exceptions import ValidationError
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images import get_image_model_string

##     ##    ###    #### ##    ##    ##     ## ######## ##    ## ##     ## 
###   ###   ## ##    ##  ###   ##    ###   ### ##       ###   ## ##     ## 
#### ####  ##   ##   ##  ####  ##    #### #### ##       ####  ## ##     ## 
## ### ## ##     ##  ##  ## ## ##    ## ### ## ######   ## ## ## ##     ## 
##     ## #########  ##  ##  ####    ##     ## ##       ##  #### ##     ## 
##     ## ##     ##  ##  ##   ###    ##     ## ##       ##   ### ##     ## 
##     ## ##     ## #### ##    ##    ##     ## ######## ##    ##  #######  
@register_setting
class MainMenu(BaseSiteSetting, ClusterableModel):
    """Main menu settings."""
    panels = [
        InlinePanel('menu_items', label="Menu Items"),
    ]


class MenuItem(models.Model):
    """Menu item for the main menu."""
    menu = ParentalKey(MainMenu, related_name='menu_items', on_delete=models.CASCADE)
    page = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Link to a Wagtail page (required)."
    )
    order = models.PositiveIntegerField(default=0)

    panels = [
        PageChooserPanel('page'),
        FieldPanel('order'),
    ]

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.page.title if self.page else 'No Title'

    def get_url(self):
        """Return the URL for the menu item from the linked page."""
        if self.page:
            return self.page.url
        return '#'

    
    
    
 
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





class FocusVideo(models.Model):
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    link = models.URLField(blank=True, null=True, help_text="External link.")
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.video) if self.video else self.link

    def clean(self):
        super().clean()  # Call the parent class's clean method
        if self.video and self.link:
            raise ValidationError("You can provide either a video or a link, but not both.")
        if not self.video and not self.link:
            raise ValidationError("You must provide either a video or a link.")
        
class Hotline(models.Model):
    hotline_name = models.CharField(max_length=255, help_text="Name of the hotline")
    number = models.CharField(max_length=20, help_text="Contact number")

    def __str__(self):
        return f"{self.hotline_name} ({self.number})"

    class Meta:
        verbose_name = "Hotline"
        verbose_name_plural = "Hotlines"
    
    
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
    
    

 ######  ##     ## #### ##       ########     ########     ###     ######  ######## 
##    ## ##     ##  ##  ##       ##     ##    ##     ##   ## ##   ##    ## ##       
##       ##     ##  ##  ##       ##     ##    ##     ##  ##   ##  ##       ##       
##       #########  ##  ##       ##     ##    ########  ##     ##  ######  ######   
##       ##     ##  ##  ##       ##     ##    ##     ## #########       ## ##       
##    ## ##     ##  ##  ##       ##     ##    ##     ## ##     ## ##    ## ##       
 ######  ##     ## #### ######## ########     ########  ##     ##  ######  ######## 
class StudentClass(models.Model):
    name = models.CharField(_("Class Name"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student Class"
        verbose_name_plural = "Student Classes"

 ######  ##     ## #### ##       ########      ######   ######## ##    ## ######## ########     ###    ##       ####  ######  ######## 
##    ## ##     ##  ##  ##       ##     ##    ##    ##  ##       ###   ## ##       ##     ##   ## ##   ##        ##  ##    ##    ##    
##       ##     ##  ##  ##       ##     ##    ##        ##       ####  ## ##       ##     ##  ##   ##  ##        ##  ##          ##    
##       #########  ##  ##       ##     ##    ##   #### ######   ## ## ## ######   ########  ##     ## ##        ##   ######     ##    
##       ##     ##  ##  ##       ##     ##    ##    ##  ##       ##  #### ##       ##   ##   ######### ##        ##        ##    ##    
##    ## ##     ##  ##  ##       ##     ##    ##    ##  ##       ##   ### ##       ##    ##  ##     ## ##        ##  ##    ##    ##    
 ######  ##     ## #### ######## ########      ######   ######## ##    ## ######## ##     ## ##     ## ######## ####  ######     ##    

class ChildGeneralist(models.Model):
    DISTRICT_CHOICES = [
            (1, "কুমিল্লা"),
            (2, "ফেনী"),
            (3, "ব্রাহ্মণবাড়িয়া"),
            (4, "রাঙ্গামাটি"),
            (5, "নোয়াখালী"),
            (6, "চাঁদপুর"),
            (7, "লক্ষ্মীপুর"),
            (8, "চট্টগ্রাম"),
            (9, "কক্সবাজার"),
            (10, "খাগড়াছড়ি"),
            (11, "বান্দরবান"),
            (12, "সিরাজগঞ্জ"),
            (13, "পাবনা"),
            (14, "বগুড়া"),
            (15, "রাজশাহী"),
            (16, "নাটোর"),
            (17, "জয়পুরহাট"),
            (18, "চাঁপাইনবাবগঞ্জ"),
            (19, "নওগাঁ"),
            (20, "যশোর"),
            (21, "সাতক্ষীরা"),
            (22, "মেহেরপুর"),
            (23, "নড়াইল"),
            (24, "চুয়াডাঙ্গা"),
            (25, "কুষ্টিয়া"),
            (26, "মাগুরা"),
            (27, "খুলনা"),
            (28, "বাগেরহাট"),
            (29, "ঝিনাইদহ"),
            (30, "ঝালকাঠি"),
            (31, "পটুয়াখালী"),
            (32, "পিরোজপুর"),
            (33, "বরিশাল"),
            (34, "ভোলা"),
            (35, "বরগুনা"),
            (36, "সিলেট"),
            (37, "মৌলভীবাজার"),
            (38, "হবিগঞ্জ"),
            (39, "সুনামগঞ্জ"),
            (40, "নরসিংদী"),
            (41, "গাজীপুর"),
            (42, "শরীয়তপুর"),
            (43, "নারায়ণগঞ্জ"),
            (44, "টাঙ্গাইল"),
            (45, "কিশোরগঞ্জ"),
            (46, "মানিকগঞ্জ"),
            (47, "ঢাকা"),
            (48, "মুন্সিগঞ্জ"),
            (49, "রাজবাড়ী"),
            (50, "মাদারীপুর"),
            (51, "গোপালগঞ্জ"),
            (52, "ফরিদপুর"),
            (53, "পঞ্চগড়"),
            (54, "দিনাজপুর"),
            (55, "লালমনিরহাট"),
            (56, "নীলফামারী"),
            (57, "গাইবান্ধা"),
            (58, "ঠাকুরগাঁও"),
            (59, "রংপুর"),
            (60, "কুড়িগ্রাম"),
            (61, "শেরপুর"),
            (62, "ময়মনসিংহ"),
            (63, "জামালপুর"),
            (64, "নেত্রকোণা")
]
    name = models.CharField(_("Name"), max_length=50, blank=True, null=True)
    father_name = models.CharField(_("Father's Name"), max_length=50, blank=True, null=True)
    mother_name = models.CharField(_("Mother's Name"), max_length=50, blank=True, null=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Class"))
    district = models.CharField(_("District Name"), max_length=50, choices=DISTRICT_CHOICES)
    phone_no = models.CharField(_("Phone Number"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Child"

    class Meta:
        verbose_name = "Child Generalist Form"
        verbose_name_plural = "Child Generalist Forms"  
        
        
 ######  ##     ## #### ##       ########     ########  ########  ########  ######  ######## ##    ## ######## ######## ########     
##    ## ##     ##  ##  ##       ##     ##    ##     ## ##     ## ##       ##    ## ##       ###   ##    ##    ##       ##     ##    
##       ##     ##  ##  ##       ##     ##    ##     ## ##     ## ##       ##       ##       ####  ##    ##    ##       ##     ##    
##       #########  ##  ##       ##     ##    ########  ########  ######    ######  ######   ## ## ##    ##    ######   ########     
##       ##     ##  ##  ##       ##     ##    ##        ##   ##   ##             ## ##       ##  ####    ##    ##       ##   ##      
##    ## ##     ##  ##  ##       ##     ##    ##        ##    ##  ##       ##    ## ##       ##   ###    ##    ##       ##    ##     
 ######  ##     ## #### ######## ########     ##        ##     ## ########  ######  ######## ##    ##    ##    ######## ##     ##    

class ChildPresenter(models.Model):
    DISTRICT_CHOICES = [
            (1, "কুমিল্লা"),
            (2, "ফেনী"),
            (3, "ব্রাহ্মণবাড়িয়া"),
            (4, "রাঙ্গামাটি"),
            (5, "নোয়াখালী"),
            (6, "চাঁদপুর"),
            (7, "লক্ষ্মীপুর"),
            (8, "চট্টগ্রাম"),
            (9, "কক্সবাজার"),
            (10, "খাগড়াছড়ি"),
            (11, "বান্দরবান"),
            (12, "সিরাজগঞ্জ"),
            (13, "পাবনা"),
            (14, "বগুড়া"),
            (15, "রাজশাহী"),
            (16, "নাটোর"),
            (17, "জয়পুরহাট"),
            (18, "চাঁপাইনবাবগঞ্জ"),
            (19, "নওগাঁ"),
            (20, "যশোর"),
            (21, "সাতক্ষীরা"),
            (22, "মেহেরপুর"),
            (23, "নড়াইল"),
            (24, "চুয়াডাঙ্গা"),
            (25, "কুষ্টিয়া"),
            (26, "মাগুরা"),
            (27, "খুলনা"),
            (28, "বাগেরহাট"),
            (29, "ঝিনাইদহ"),
            (30, "ঝালকাঠি"),
            (31, "পটুয়াখালী"),
            (32, "পিরোজপুর"),
            (33, "বরিশাল"),
            (34, "ভোলা"),
            (35, "বরগুনা"),
            (36, "সিলেট"),
            (37, "মৌলভীবাজার"),
            (38, "হবিগঞ্জ"),
            (39, "সুনামগঞ্জ"),
            (40, "নরসিংদী"),
            (41, "গাজীপুর"),
            (42, "শরীয়তপুর"),
            (43, "নারায়ণগঞ্জ"),
            (44, "টাঙ্গাইল"),
            (45, "কিশোরগঞ্জ"),
            (46, "মানিকগঞ্জ"),
            (47, "ঢাকা"),
            (48, "মুন্সিগঞ্জ"),
            (49, "রাজবাড়ী"),
            (50, "মাদারীপুর"),
            (51, "গোপালগঞ্জ"),
            (52, "ফরিদপুর"),
            (53, "পঞ্চগড়"),
            (54, "দিনাজপুর"),
            (55, "লালমনিরহাট"),
            (56, "নীলফামারী"),
            (57, "গাইবান্ধা"),
            (58, "ঠাকুরগাঁও"),
            (59, "রংপুর"),
            (60, "কুড়িগ্রাম"),
            (61, "শেরপুর"),
            (62, "ময়মনসিংহ"),
            (63, "জামালপুর"),
            (64, "নেত্রকোণা")
]
    name = models.CharField(_("Name"), max_length=50, blank=True, null=True)
    father_name = models.CharField(_("Father's Name"), max_length=50, blank=True, null=True)
    mother_name = models.CharField(_("Mother's Name"), max_length=50, blank=True, null=True)
    student_class = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Class"))
    district = models.CharField(_("District Name"), max_length=50, choices=DISTRICT_CHOICES)
    phone_no = models.CharField(_("Phone Number"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Unnamed Child"

    class Meta:
        verbose_name = "Child Presenter Form"
        verbose_name_plural = "Child Presenter Forms"  


########  #######   #######  ######## ######## ########  
##       ##     ## ##     ##    ##    ##       ##     ## 
##       ##     ## ##     ##    ##    ##       ##     ## 
######   ##     ## ##     ##    ##    ######   ########  
##       ##     ## ##     ##    ##    ##       ##   ##   
##       ##     ## ##     ##    ##    ##       ##    ##  
##        #######   #######     ##    ######## ##     ## 



IMAGE_MODEL = get_image_model_string()
@register_setting
class FooterSettings(BaseSiteSetting):
    
    logo = models.ForeignKey(
        IMAGE_MODEL,
        verbose_name=_("Footer logo"),
        on_delete=models.SET_NULL,
        help_text="Optimal_Dimension : max width 190px",
        null=True,
        blank=True,
    )
    
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
                FieldPanel("logo"),
            ],
            heading="Organization logo",
        ),
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