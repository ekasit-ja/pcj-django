from django.db import models
from django.conf import settings
from django.utils.translation import get_language

# Create your models here.
class Document(models.Model):
    product_type = models.CharField(
        max_length=6,
        choices=settings.CONSTANTS['product_choices'],
        default=settings.CONSTANTS['product_choices'][0][0],
    )

    document_type = models.CharField(
        max_length=5,
        choices=settings.CONSTANTS['document_choices'],
        default=settings.CONSTANTS['document_choices'][0][0],
    )

    title_en    = models.CharField(max_length=255, verbose_name='title english')
    title_th    = models.CharField(max_length=255, blank=True, verbose_name='title thai')
    image       = models.ImageField(upload_to='document', blank=True)
    doc_en      = models.FileField(upload_to='document', verbose_name='document english')
    doc_th      = models.FileField(upload_to='document', blank=True, verbose_name='document thai')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

    @property
    def title(self):
        return self.title_th if get_language()=='th' and self.title_th else self.title_en

    @property
    def doc(self):
        return self.doc_th if get_language()=='th' and self.doc_th else self.doc_en

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title_en
