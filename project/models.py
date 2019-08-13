from django.db import models

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

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title_en
