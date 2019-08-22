from django.db import models
from django.utils.translation import get_language

# Create your models here.
class Project(models.Model):
    title_en    = models.CharField(max_length=255, verbose_name='title english')
    title_th    = models.CharField(max_length=255, blank=True, verbose_name='title thai')
    country     = models.CharField(max_length=255)
    area        = models.CharField(max_length=255)
    year        = models.CharField(max_length=10)
    company     = models.CharField(max_length=255)
    image       = models.ImageField(upload_to='project')
    order       = models.PositiveIntegerField(default=0, blank=False, null=False)

    @property
    def title(self):
        return self.title_th if get_language()=='th' and self.title_th else self.title_en

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title_en
