from django.shortcuts import render
from django.views.generic import TemplateView
from resume.models import Skill,SkillCategory,Experience,MainProfile
from portfolio.models import Portfolio, Category
from blog.models import Post
from django.conf import settings
from django.http import JsonResponse
from django.core.mail import send_mail


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
        context["portfolio"] = Portfolio.objects.filter(is_featured=True).order_by('-creation_date')[:6]
        context["posts"] = posts.order_by('-created')[:3]
        context["profile"] = MainProfile.objects.get(pk=settings.MAIN_PROFILE_ID)

        return context

def ajax_posting(request):
    if request.is_ajax():
        firstname = request.POST.get('firstname', None) # getting data from input first_name id
        lastname = request.POST.get('lastname', None) # getting data from input first_name id
        email = request.POST.get('email', None) # getting data from input first_name id
        subject = request.POST.get('subject', None) # getting data from input first_name id
        message = request.POST.get('message', None) # getting data from input first_name id
        to = "eric@erictragoustis.com"
        if firstname and lastname and email and subject and message: 
            message = "From: " + firstname + " " + lastname + " | Email: " + email + " | Message: " + message 
            
            response = {'msg':'The message has been sent' }
            send_mail(subject, message, to, ['eric@erictragoustis.com'], fail_silently=False)
        else:
            response = {
                         'msg':'Please before sending the message enter correct data' # response message
            }
        return JsonResponse(response) 
