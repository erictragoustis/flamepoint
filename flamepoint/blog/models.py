from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from image_optimizer.fields import OptimizedImageField
from ckeditor_uploader.fields import RichTextUploadingField

# Category
class Category (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Category Title", unique=True, always_update=False, populate_from="title")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,related_name='blog_category', blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title
# Post

class Post (TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = AutoSlugField("Post Title", unique=True, always_update=False, populate_from="title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = RichTextUploadingField()
    is_featured = models.BooleanField(default=False)
    feat_image = OptimizedImageField(upload_to='blog/images')
    thumbnail = models.ImageField(upload_to='blog/images/')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    thumbnail = ImageSpecField(source='feat_image',
                                      processors=[ResizeToFill(800, 533)],
                                      format='JPEG',
                                      options={'quality': 60})
    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('blog:dashPosts_detail', args=[str(self.slug)])