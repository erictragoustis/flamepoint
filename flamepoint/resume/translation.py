from modeltranslation.translator import register, TranslationOptions
from .models import MainProfile


@register(MainProfile)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name','surname','story','catchphrase')

