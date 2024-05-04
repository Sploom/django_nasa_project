from django.contrib import admin
from .models import SliderImage
from adminsortable2.admin import SortableAdminMixin

@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    fields = ('title', 'image')

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 150px; height: auto;"/>', obj.image.url)
        return "No Image"
    image_preview.short_description = "Предварительный просмотр изображения"





