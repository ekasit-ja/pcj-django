from django.db import models
from django.template.defaultfilters import truncatechars, striptags
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import get_language

# Create your models here.
class Finance(models.Model):
    title_en    = RichTextField(config_name='small', verbose_name='title english')
    title_th    = RichTextField(default='', blank=True, config_name='small', verbose_name='title thai')
    content_en  = RichTextField(verbose_name='content english')
    content_th  = RichTextField(default='', blank=True, verbose_name='content thai')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

    @property
    def short_title_en(self):
        return truncatechars(striptags(self.title_en), 50)
    @property
    def short_content_en(self):
        return truncatechars(striptags(self.content_en), 100)

    @property
    def title(self):
        return self.title_th if get_language()=='th' and self.title_th else self.title_en

    @property
    def content(self):
        return self.content_th if get_language()=='th' and self.content_th else self.content_en

    class Meta:
        ordering = ('-order',)
        verbose_name_plural = "finance"

    def __str__(self):
        return truncatechars(self.title_en, 30)
