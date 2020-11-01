from django.contrib import admin
from .models import SkillCategory,Skill,Experience, Responsibilities,MainProfile


admin.site.register(Skill)
admin.site.register(MainProfile)

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')



admin.site.register(SkillCategory,SkillCategoryAdmin)

class ResponsibilitiesAdmin(admin.TabularInline):
    model = Responsibilities

class ExperienceAdmin(admin.ModelAdmin):
   inlines = [ResponsibilitiesAdmin,]



admin.site.register(Experience,ExperienceAdmin)