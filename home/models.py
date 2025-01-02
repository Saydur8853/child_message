from django.db import models
from django.utils import timezone

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel,MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.models import Image
from wagtail.search import index
from child_message.blocks import *
from wagtail.blocks import StructBlock, ChoiceBlock
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from django.core.exceptions import ValidationError
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.images import get_image_model_string
IMAGE_MODEL = get_image_model_string()


class NewsCategory(models.Model):
    category = models.CharField(_("News Category"), max_length=50, blank=True, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "News Category"
        verbose_name_plural = "News Categories" 
        
def get_news_category_choices():
    return [(cat.id, cat.category) for cat in NewsCategory.objects.all()]

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
    news_categories = StreamField(
        [
            ("News_Category", StructBlock([
                ("category", ChoiceBlock(
                    choices=get_news_category_choices,
                    label="News Category",
                ))
            ])),
        ],
        null=True,
        blank=True,
    )


    content_panels = Page.content_panels + [
        FieldPanel('advertisement'),
        FieldPanel('news_categories'),
    ]
    subpage_types = [
        "home.NewsIndexPage",
        "home.CheifVoicePage",
        "home.MissingNewsPage",
    ]

class LiveStreaming(models.Model):
    link = models.URLField(blank=True, null=True, help_text="External link.")
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.link


##     ## #### ########  ########  #######  
##     ##  ##  ##     ## ##       ##     ## 
##     ##  ##  ##     ## ##       ##     ## 
##     ##  ##  ##     ## ######   ##     ## 
 ##   ##   ##  ##     ## ##       ##     ## 
  ## ##    ##  ##     ## ##       ##     ## 
   ###    #### ########  ########  #######  
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
    # ---------------------------------------------------------------------
    #                             NewsDetailsPage
    # ---------------------------------------------------------------------
class NewsDetails(models.Model):
    page_choice = models.ForeignKey(
        NewsIndexPage,
        verbose_name=_("Associated page"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news_page",
    )
    news_category = models.ForeignKey(
        'NewsCategory',
        verbose_name=_("News Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news_category",
    )
    main_heading = models.CharField(
        max_length=255, 
        help_text="Main Heading of the News",
        blank=True,
    )
    subtitle = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Subtitle of the News",
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Optimal_Dimension : 520x365",
        related_name="+",
    )
    published_date = models.DateTimeField(
        default=timezone.now, 
        help_text="Publish Date and Time",
    )
    updated_date = models.DateTimeField(
        auto_now=True, 
        help_text="Updated Date and Time",
    )
    details = models.TextField(
        blank=True, 
        help_text="Details of the news",
    )
    make_featured_news = models.BooleanField(
        _("Make it featured?"), 
        default=False, 
        blank=True,
    )

    def __str__(self):
        return self.main_heading or "Untitled News"
    class Meta:
        verbose_name = "News detail"
        verbose_name_plural = "News details"
    
    
# class NewsDetailsPage(Page):
#     news_category = models.ForeignKey(
#         NewsCategory,
#         verbose_name=_("Select a Category"),
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="news_details_page",
#     )
#     main_heading = models.CharField(max_length=255, help_text="Main Heading of the News",blank=True,)
#     subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Subtitle of the News")
#     image = models.ForeignKey(
#         "wagtailimages.Image",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         help_text="Optimal_Dimension : 520x365",
#         related_name="+",
#     )
#     published_date = models.DateTimeField(default=timezone.now, help_text="Publish Date and Time")
#     updated_date = models.DateTimeField(auto_now=True, help_text="Updated Date and Time")
#     details = RichTextField(blank=True, help_text="Details of the news")
#     make_featured_news = models.BooleanField(
#         _("Make it featured?"), default=False, blank=True
#     )
#     advertisement = StreamField(
#         [
#             ("Vertical_Adv", VerticalAddBlock()),
#             ("Horizontal_Adv", HorizontalAddBlock()),
#             ("Poster_Adv", PosterAddBlock()),
#             ("Box_Adv", BoxAddBlock()),
#             ("Popup_Adv", PopupAddBlock()),
#         ],
#         null=True,
#         blank=True,
#     )
#     content_panels = Page.content_panels + [
#         FieldPanel('advertisement'),
#         FieldPanel('news_category'),
#         FieldPanel('main_heading'),
#         FieldPanel('subtitle'),
#         FieldPanel('image'),
#         FieldPanel('published_date'),
#         FieldPanel('details'),
#         FieldPanel('make_featured_news'),
        
#     ]


   
   
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
        ("কুমিল্লা", "কুমিল্লা"),
        ("ফেনী", "ফেনী"),
        ("ব্রাহ্মণবাড়িয়া", "ব্রাহ্মণবাড়িয়া"),
        ("রাঙ্গামাটি", "রাঙ্গামাটি"),
        ("নোয়াখালী", "নোয়াখালী"),
        ("চাঁদপুর", "চাঁদপুর"),
        ("লক্ষ্মীপুর", "লক্ষ্মীপুর"),
        ("চট্টগ্রাম", "চট্টগ্রাম"),
        ("কক্সবাজার", "কক্সবাজার"),
        ("খাগড়াছড়ি", "খাগড়াছড়ি"),
        ("বান্দরবান", "বান্দরবান"),
        ("সিরাজগঞ্জ", "সিরাজগঞ্জ"),
        ("পাবনা", "পাবনা"),
        ("বগুড়া", "বগুড়া"),
        ("রাজশাহী", "রাজশাহী"),
        ("নাটোর", "নাটোর"),
        ("জয়পুরহাট", "জয়পুরহাট"),
        ("চাঁপাইনবাবগঞ্জ", "চাঁপাইনবাবগঞ্জ"),
        ("নওগাঁ", "নওগাঁ"),
        ("যশোর", "যশোর"),
        ("সাতক্ষীরা", "সাতক্ষীরা"),
        ("মেহেরপুর", "মেহেরপুর"),
        ("নড়াইল", "নড়াইল"),
        ("চুয়াডাঙ্গা", "চুয়াডাঙ্গা"),
        ("কুষ্টিয়া", "কুষ্টিয়া"),
        ("মাগুরা", "মাগুরা"),
        ("খুলনা", "খুলনা"),
        ("বাগেরহাট", "বাগেরহাট"),
        ("ঝিনাইদহ", "ঝিনাইদহ"),
        ("ঝালকাঠি", "ঝালকাঠি"),
        ("পটুয়াখালী", "পটুয়াখালী"),
        ("পিরোজপুর", "পিরোজপুর"),
        ("বরিশাল", "বরিশাল"),
        ("ভোলা", "ভোলা"),
        ("বরগুনা", "বরগুনা"),
        ("সিলেট", "সিলেট"),
        ("মৌলভীবাজার", "মৌলভীবাজার"),
        ("হবিগঞ্জ", "হবিগঞ্জ"),
        ("সুনামগঞ্জ", "সুনামগঞ্জ"),
        ("নরসিংদী", "নরসিংদী"),
        ("গাজীপুর", "গাজীপুর"),
        ("শরীয়তপুর", "শরীয়তপুর"),
        ("নারায়ণগঞ্জ", "নারায়ণগঞ্জ"),
        ("টাঙ্গাইল", "টাঙ্গাইল"),
        ("কিশোরগঞ্জ", "কিশোরগঞ্জ"),
        ("মানিকগঞ্জ", "মানিকগঞ্জ"),
        ("ঢাকা", "ঢাকা"),
        ("মুন্সিগঞ্জ", "মুন্সিগঞ্জ"),
        ("রাজবাড়ী", "রাজবাড়ী"),
        ("মাদারীপুর", "মাদারীপুর"),
        ("গোপালগঞ্জ", "গোপালগঞ্জ"),
        ("ফরিদপুর", "ফরিদপুর"),
        ("পঞ্চগড়", "পঞ্চগড়"),
        ("দিনাজপুর", "দিনাজপুর"),
        ("লালমনিরহাট", "লালমনিরহাট"),
        ("নীলফামারী", "নীলফামারী"),
        ("গাইবান্ধা", "গাইবান্ধা"),
        ("ঠাকুরগাঁও", "ঠাকুরগাঁও"),
        ("রংপুর", "রংপুর"),
        ("কুড়িগ্রাম", "কুড়িগ্রাম"),
        ("শেরপুর", "শেরপুর"),
        ("ময়মনসিংহ", "ময়মনসিংহ"),
        ("জামালপুর", "জামালপুর"),
        ("নেত্রকোণা", "নেত্রকোণা"),
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
        ("কুমিল্লা", "কুমিল্লা"),
        ("ফেনী", "ফেনী"),
        ("ব্রাহ্মণবাড়িয়া", "ব্রাহ্মণবাড়িয়া"),
        ("রাঙ্গামাটি", "রাঙ্গামাটি"),
        ("নোয়াখালী", "নোয়াখালী"),
        ("চাঁদপুর", "চাঁদপুর"),
        ("লক্ষ্মীপুর", "লক্ষ্মীপুর"),
        ("চট্টগ্রাম", "চট্টগ্রাম"),
        ("কক্সবাজার", "কক্সবাজার"),
        ("খাগড়াছড়ি", "খাগড়াছড়ি"),
        ("বান্দরবান", "বান্দরবান"),
        ("সিরাজগঞ্জ", "সিরাজগঞ্জ"),
        ("পাবনা", "পাবনা"),
        ("বগুড়া", "বগুড়া"),
        ("রাজশাহী", "রাজশাহী"),
        ("নাটোর", "নাটোর"),
        ("জয়পুরহাট", "জয়পুরহাট"),
        ("চাঁপাইনবাবগঞ্জ", "চাঁপাইনবাবগঞ্জ"),
        ("নওগাঁ", "নওগাঁ"),
        ("যশোর", "যশোর"),
        ("সাতক্ষীরা", "সাতক্ষীরা"),
        ("মেহেরপুর", "মেহেরপুর"),
        ("নড়াইল", "নড়াইল"),
        ("চুয়াডাঙ্গা", "চুয়াডাঙ্গা"),
        ("কুষ্টিয়া", "কুষ্টিয়া"),
        ("মাগুরা", "মাগুরা"),
        ("খুলনা", "খুলনা"),
        ("বাগেরহাট", "বাগেরহাট"),
        ("ঝিনাইদহ", "ঝিনাইদহ"),
        ("ঝালকাঠি", "ঝালকাঠি"),
        ("পটুয়াখালী", "পটুয়াখালী"),
        ("পিরোজপুর", "পিরোজপুর"),
        ("বরিশাল", "বরিশাল"),
        ("ভোলা", "ভোলা"),
        ("বরগুনা", "বরগুনা"),
        ("সিলেট", "সিলেট"),
        ("মৌলভীবাজার", "মৌলভীবাজার"),
        ("হবিগঞ্জ", "হবিগঞ্জ"),
        ("সুনামগঞ্জ", "সুনামগঞ্জ"),
        ("নরসিংদী", "নরসিংদী"),
        ("গাজীপুর", "গাজীপুর"),
        ("শরীয়তপুর", "শরীয়তপুর"),
        ("নারায়ণগঞ্জ", "নারায়ণগঞ্জ"),
        ("টাঙ্গাইল", "টাঙ্গাইল"),
        ("কিশোরগঞ্জ", "কিশোরগঞ্জ"),
        ("মানিকগঞ্জ", "মানিকগঞ্জ"),
        ("ঢাকা", "ঢাকা"),
        ("মুন্সিগঞ্জ", "মুন্সিগঞ্জ"),
        ("রাজবাড়ী", "রাজবাড়ী"),
        ("মাদারীপুর", "মাদারীপুর"),
        ("গোপালগঞ্জ", "গোপালগঞ্জ"),
        ("ফরিদপুর", "ফরিদপুর"),
        ("পঞ্চগড়", "পঞ্চগড়"),
        ("দিনাজপুর", "দিনাজপুর"),
        ("লালমনিরহাট", "লালমনিরহাট"),
        ("নীলফামারী", "নীলফামারী"),
        ("গাইবান্ধা", "গাইবান্ধা"),
        ("ঠাকুরগাঁও", "ঠাকুরগাঁও"),
        ("রংপুর", "রংপুর"),
        ("কুড়িগ্রাম", "কুড়িগ্রাম"),
        ("শেরপুর", "শেরপুর"),
        ("ময়মনসিংহ", "ময়মনসিংহ"),
        ("জামালপুর", "জামালপুর"),
        ("নেত্রকোণা", "নেত্রকোণা"),
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

 ######  #### ######## ########       ###     ######   ######   #######   ######  ####    ###    ######## ######## 
##    ##  ##     ##    ##            ## ##   ##    ## ##    ## ##     ## ##    ##  ##    ## ##      ##    ##       
##        ##     ##    ##           ##   ##  ##       ##       ##     ## ##        ##   ##   ##     ##    ##       
 ######   ##     ##    ######      ##     ##  ######   ######  ##     ## ##        ##  ##     ##    ##    ######   
      ##  ##     ##    ##          #########       ##       ## ##     ## ##        ##  #########    ##    ##       
##    ##  ##     ##    ##          ##     ## ##    ## ##    ## ##     ## ##    ##  ##  ##     ##    ##    ##       
 ######  ####    ##    ########    ##     ##  ######   ######   #######   ######  #### ##     ##    ##    ######## 

class Site_associate(models.Model):
    logo = models.ForeignKey(
        IMAGE_MODEL,
        verbose_name=_("Site logo"),
        on_delete=models.SET_NULL,
        help_text="Optimal Dimension: max width 190px",
        null=True,
        blank=True,
    )
    facebook = models.URLField(_("Facebook"), max_length=255, blank=True)
    twitter = models.URLField(_("Twitter"), max_length=255, blank=True)
    instagram = models.URLField(_("Instagram"), max_length=255, blank=True)
    youtube = models.URLField(_("Youtube"), max_length=255, blank=True)

    hotline_number = models.CharField(max_length=25, help_text="Hotline number", blank=True)
    child_helpline_number = models.CharField(max_length=20, help_text="Child helpline number", blank=True)
    
    short_message = models.CharField(max_length=255, help_text="Short message", blank=True)

    quick_link_1_name = models.CharField(max_length=255, help_text="Quick link 1 name", blank=True)
    quick_link_1_url = models.URLField(_("Quick link 1 URL"), max_length=255, blank=True)

    quick_link_2_name = models.CharField(max_length=255, help_text="Quick link 2 name", blank=True)
    quick_link_2_url = models.URLField(_("Quick link 2 URL"), max_length=255, blank=True)

    quick_link_3_name = models.CharField(max_length=255, help_text="Quick link 3 name", blank=True)
    quick_link_3_url = models.URLField(_("Quick link 3 URL"), max_length=255, blank=True)

    quick_link_4_page = models.ForeignKey(
        Page,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Link to a Wagtail page (required)."
    )

    quick_link_5_name = models.CharField(max_length=255, help_text="Quick link 5 name", blank=True)
    quick_link_5_url = models.URLField(_("Quick link 5 URL"), max_length=255, blank=True)

    quick_link_6_name = models.CharField(max_length=255, help_text="Quick link 6 name", blank=True)
    quick_link_6_url = models.URLField(_("Quick link 6 URL"), max_length=255, blank=True)
    
    copyright_line = models.CharField(
        _("copyright"),
        max_length=255,
        blank=True,
        default="Copyright © 2024 Child Message. All rights reserved.",
    )


    def __str__(self):
        return f"{self.hotline_number} ({self.child_helpline_number})"

    class Meta:
        verbose_name = "Site associate"
