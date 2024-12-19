from wagtail import blocks
from wagtailutils import blocks as util_blocks


class CallToActionBlock(blocks.StructBlock):
    link = util_blocks.PageOrLinkBlock(required=False)
    anchor = blocks.CharBlock(required=False)

    class Meta:
        icon = "link"


class LabeledCallToActionBlock(CallToActionBlock):
    label = blocks.CharBlock(required=False, default="Read More")

    class Meta:
        icon = "link"



   ###    ########  ##     ## ######## ########  ######## ####  ######  ######## ##     ## ######## ##    ## ######## 
  ## ##   ##     ## ##     ## ##       ##     ##    ##     ##  ##    ## ##       ###   ### ##       ###   ##    ##    
 ##   ##  ##     ## ##     ## ##       ##     ##    ##     ##  ##       ##       #### #### ##       ####  ##    ##    
##     ## ##     ## ##     ## ######   ########     ##     ##   ######  ######   ## ### ## ######   ## ## ##    ##    
######### ##     ##  ##   ##  ##       ##   ##      ##     ##        ## ##       ##     ## ##       ##  ####    ##    
##     ## ##     ##   ## ##   ##       ##    ##     ##     ##  ##    ## ##       ##     ## ##       ##   ###    ##    
##     ## ########     ###    ######## ##     ##    ##    ####  ######  ######## ##     ## ######## ##    ##    ##    



class VerticalAddBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : 165x625",
        rendition_rules={
            "original": "fill-165x625-c0|format-webp",
            "original_fallback": "fill-165x625-c0",
        },
    )

class HorizontalAddBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : 1280x190",
        rendition_rules={
            "original": "fill-1280x190-c0|format-webp",
            "original_fallback": "fill-1280x190-c0",
        },
    )

class PosterAddBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : 305x545",
        rendition_rules={
            "original": "fill-305x545-c0|format-webp",
            "original_fallback": "fill-305x545-c0",
        },
    )

class BoxAddBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : width max-420",
        rendition_rules={
            "original": "width-420|format-webp",
            "original_fallback": "width-420",
        },
    )

class PopupAddBlock(blocks.StructBlock):
    image = util_blocks.ImageChooserBlock(
        required=False,
        help_text="Optimal Dimension : width max-500",
        rendition_rules={
            "original": "width-500|format-webp",
            "original_fallback": "width-500",
        },
    )
