from wagtail.images.blocks import ImageChooserBlock as DefaultImageChooserBlock


class ImageChooserBlock(DefaultImageChooserBlock):
    def to_python(self, value):
        if value is None:
            return value
        else:
            try:
                return self.target_model.objects.filter(pk=value).prefetch_related('renditions').first()
            except self.target_model.DoesNotExist:
                return None

    def get_api_representation(self, value, context=None):
        if value:
            data = {
                "id": value.id,
                "title": value.title,
                "original": value.get_rendition("original").attrs_dict,
            }
            rules = getattr(self.meta, "rendition_rules", False)
            if rules:
                for name, rule in rules.items():
                    data[name] = value.get_rendition(rule).attrs_dict
            return data
