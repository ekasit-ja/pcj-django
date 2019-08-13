from django.db import models
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Finance(models.Model):
    title_en    = RichTextField(config_name='small', verbose_name='title english')
    title_th    = RichTextField(default='', blank=True, config_name='small', verbose_name='title thai')
    content_en  = RichTextUploadingField(verbose_name='content english')
    content_th  = RichTextUploadingField(default='', blank=True, verbose_name='content thai')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('-order',)
        verbose_name_plural = "finance"

    def __str__(self):
        return truncatechars(self.title_en, 30)
