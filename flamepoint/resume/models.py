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

# Profile

class MainProfile (TimeStampedModel):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='portfolio/images/',null=True, blank=True)
    cv = models.FileField(upload_to='porfolio/uploads/')
    worktitle = models.CharField(max_length=200)
    story = RichTextUploadingField(null=True, blank=True)
    catchphrase = RichTextUploadingField(null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    messenger = models.URLField(max_length=200, null=True, blank=True)


    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)
    thumbnail = ImageSpecField(source='main_image',
                                    processors=[ResizeToFill(800, 533)],
                                    format='JPEG',
                                    options={'quality': 60})

    def __str__(self):
        return self.name + self.surname

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


class Responsibilities (TimeStampedModel):
    title = models.CharField(max_length=200) 
    sort = models.IntegerField(default=1)
    work = models.ForeignKey(Experience , on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

