from django.shortcuts import render
from django.views.generic import TemplateView
from resume.models import Skill,SkillCategory,Experience,MainProfile
from portfolio.models import Portfolio, Category
from blog.models import Post
from django.conf import settings


# Create your views here.
class HomePage(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        skills = Skill.objects.all()
        posts = Post.objects.all()
        work = Experience.objects.all()

        #allskills = Skill.objects.values('category__parent__title').values('category__title', 'title').order_by('category__parent')
        allskills = Skill.objects.order_by('sort').values('category__parent__title','category__title', 'title')
        context["allskills"] = allskills
        context["skills"] = skills.order_by('category__parent__sort','category__parent','category')
        context["work"] = work
        context["portfolio_categories"] = Category.objects.all()
        context["portfolio"] = Portfolio.objects.order_by('-is_featured','created')[:6]
        context["posts"] = posts.order_by('-created')[:3]
        context["profile"] = MainProfile.objects.get(pk=settings.MAIN_PROFILE_ID)

        return context
