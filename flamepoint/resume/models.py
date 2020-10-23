from django.urls import reverse
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField

# Category
class SkillCategory (TimeStampedModel):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200,blank=True, null=True )
    slug = AutoSlugField("Skill Category Title", unique=True, always_update=False, populate_from="title")
    sort = models.IntegerField(default="",null=True, blank=True,)
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "skill categories"

    def __str__(self):
        return self.title

# Skill
class Skill (TimeStampedModel):
    title = models.CharField(max_length=200)    
    slug = AutoSlugField("Skill Title", unique=True, always_update=False, populate_from="title")
    category = models.ForeignKey(SkillCategory , on_delete=models.CASCADE)
    skill = models.IntegerField(default=10)
    sort = models.IntegerField(default=1)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

#Work Experience

class Experience (TimeStampedModel):
    title = models.CharField(max_length=200) 
    duties = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    sort = models.IntegerField(default=1)
    from_date = models.DateField(null=True, blank=True,)
    to_date = models.DateField(null=True, blank=True,)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

