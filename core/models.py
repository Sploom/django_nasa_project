from django.db import models
from filer.fields.image import FilerImageField

class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    image = FilerImageField(related_name="slider_images", on_delete=models.CASCADE)
    order = models.IntegerField(default=0, verbose_name="Порядок")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "изображение для слайдера"
        verbose_name_plural = "Изображения для слайдера"
        ordering = ['order']
