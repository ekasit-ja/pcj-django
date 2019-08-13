from django.db import models
from django.template.defaultfilters import truncatechars, striptags
from django.db.models import Max
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class News(models.Model):
    title_en    = models.TextField(verbose_name='title english')
    title_th    = models.TextField(blank=True, verbose_name='title thai')
    content_en  = RichTextUploadingField(verbose_name='content english')
    content_th  = RichTextUploadingField(default='', blank=True, verbose_name='content thai')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

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

class NewsImage(models.Model):
    news        = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='news')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.image.url

    def news_id(self):
        return self.news.id
