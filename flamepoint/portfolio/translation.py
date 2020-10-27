from modeltranslation.translator import register, TranslationOptions
from .models import Category, Technology, Portfolio


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Technology)
class TechnologyTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Portfolio)
class TPorfolioTranslationOptions(TranslationOptions):
    fields = ('title','description','section')