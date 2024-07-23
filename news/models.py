from django.db import models
from django.template.defaultfilters import truncatechars, striptags
from django.db.models import Max
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import get_language

# Create your models here.
class News(models.Model):
    title_en    = models.TextField(verbose_name='title english')
    title_th    = models.TextField(blank=True, verbose_name='title thai')
    content_en  = RichTextUploadingField(verbose_name='content english')
    content_th  = RichTextUploadingField(default='', blank=True, verbose_name='content thai')
    image       = models.ImageField(upload_to='news')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)
    publish     = models.BooleanField(default=False)

    class Meta:
        ordering = ('-order',)
        verbose_name_plural = "news"

    def __str__(self):
        return self.short_title_en

    @property
    def short_title_en(self):
        return truncatechars(self.title_en, 30)
    @property
    def short_content_en(self):
        return truncatechars(striptags(self.content_en), 50)

    @property
    def title(self):
        return self.title_th if get_language()=='th' and self.title_th else self.title_en

    @property
    def content(self):
        return self.content_th if get_language()=='th' and self.content_th else self.content_en

    @property
    def title_short(self):
        return truncatechars(self.title, 100)

    @property
    def content_short(self):
        return truncatechars(striptags(self.content), 220)
