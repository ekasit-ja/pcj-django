from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    product_type = models.CharField(
        max_length=3,
        choices=settings.CONSTANTS['product_choices'],
        default=settings.CONSTANTS['product_choices'][0][0],
    )
    title_en    = models.CharField(max_length=255, verbose_name='title english')
    title_th    = models.CharField(max_length=255, blank=True, verbose_name='title thai')
    desc_en     = RichTextField(default='', blank=True, verbose_name='description english')
    desc_th     = RichTextField(default='', blank=True, verbose_name='description thai')
    image       = models.ImageField(upload_to='product')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

    @property
    def title(self):
        return self.title_th if get_language()=='th' and self.title_th else self.title_en

    @property
    def desc(self):
        return self.desc_th if get_language()=='th' and self.desc_th else self.desc_en

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title_en
