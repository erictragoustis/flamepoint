from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

# Category
class Category (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Skill Category Title", unique=True, always_update=False, populate_from="title")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

# Category
class Tag (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Skill Category Title", unique=True, always_update=False, populate_from="title")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Work

class Portfolio (TimeStampedModel):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags  = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200, null=True, blank=True)
    feat_image = models.ImageField(upload_to='portfolio/images/')

    thumbnail = ImageSpecField(source='feat_image',
                                    processors=[ResizeToFill(800, 533)],
                                    format='JPEG',
                                    options={'quality': 60})

    def __str__(self):
        return self.title