from django.contrib import admin
from .models import SkillCategory,Skill,Experience, Responsibilities,MainProfile



admin.site.register(MainProfile)

class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title','category','skill')


admin.site.register(Skill,SkillAdmin)
admin.site.register(SkillCategory,SkillCategoryAdmin)

class ResponsibilitiesAdmin(admin.TabularInline):
    model = Responsibilities

class ExperienceAdmin(admin.ModelAdmin):
   inlines = [ResponsibilitiesAdmin,]



admin.site.register(Experience,ExperienceAdmin)