from django.contrib import admin
from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    fields = ('title', 'image')

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            thumbnail_url = get_thumbnailer(obj.image)['admin_preview'].url
            return format_html('<img src="{}" style="width: 100px; height: auto;"/>', thumbnail_url)
        return "Нет изображения"
    image_preview.short_description = "Превью"