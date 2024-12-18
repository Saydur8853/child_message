from django.db import models
from django.utils import timezone

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail.search import index
from wagtailutils import blocks as util_blocks



class HomePage(Page):
    news_bulletin = RichTextField(features=["bold", "italic"],blank=True, help_text="The News Bulletin.")

    content_panels = Page.content_panels + [
        FieldPanel('news_bulletin'),
    ]



"""
.##....##.########.##......##..######.
.###...##.##.......##..##..##.##....##
.####..##.##.......##..##..##.##......
.##.##.##.######...##..##..##..######.
.##..####.##.......##..##..##.......##
.##...###.##.......##..##..##.##....##
.##....##.########..###..###...######.
"""


class AmarBarta(models.Model, index.Indexed):
    main_heading = models.CharField(max_length=255, help_text="Main Heading of the News")
    subtitle = models.CharField(max_length=255, blank=True, null=True, help_text="Subtitle of the News")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Optimal_Dimension : 485x320",
        related_name="+",
    )
    published_date = models.DateTimeField(default=timezone.now, help_text="Publish Date and Time")
    updated_date = models.DateTimeField(auto_now=True, help_text="Updated Date and Time")
    # image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="amar_barta_images", help_text="News Image")
    details = RichTextField(blank=True, help_text="Details of the news")
    

    def __str__(self):
        return self.main_heading
    
    class Meta:
        verbose_name = "Amar Barta"
        verbose_name_plural = "Amar Bartas"

    
    