from django.db import models
from filer.fields.image import FilerImageField

class SliderImage(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    image = FilerImageField(related_name="slider_images", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение для слайдера"
        verbose_name_plural = "Изображения для слайдера"
        ordering = ['id']