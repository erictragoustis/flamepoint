from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
from image_optimizer.fields import OptimizedImageField

# Category
class Category (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Skill Category Title", unique=True, always_update=False, populate_from="title")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

# Tag
class Tag (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Skill Category Title", unique=True, always_update=False, populate_from="title")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#Technologies
class Technology (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Skill Category Title", unique=True, always_update=False, populate_from="title")
    icon = models.CharField(max_length=200,blank=True, null=True )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Work

class Portfolio (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Portfolio Title", unique=True, always_update=False, populate_from="title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags  = models.ManyToManyField(Tag, blank=True)
    technologies  = models.ManyToManyField(Technology, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    creation_date = models.DateField(null=True, blank=True,)
    section = models.CharField(max_length=200,null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    is_video = models.BooleanField(default=False)
    video_id = models.CharField(max_length=200,null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    social_url = models.URLField(max_length=200, null=True, blank=True)
    feat_image = OptimizedImageField(upload_to='portfolio/images/',null=True, blank=True)
    front_image = OptimizedImageField(upload_to='portfolio/images/',null=True, blank=True)

    thumbnail = ImageSpecField(source='feat_image',
                                    processors=[ResizeToFill(800, 533)],
                                    format='JPEG',
                                    options={'quality': 60})
    thumbnail_front = ImageSpecField(source='front_image',
                                processors=[ResizeToFill(800, 533)],
                                format='JPEG',
                                options={'quality': 60})

    def __str__(self):
        return self.title

