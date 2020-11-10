from modeltranslation.translator import register, TranslationOptions
from .models import MainProfile, Experience, Responsibilities


@register(MainProfile)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','surname','story','catchphrase',)

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('title','duties','description',)

@register(Responsibilities)
class ResponsibilitiesTranslationOptions(TranslationOptions):
    fields = ('title',)

