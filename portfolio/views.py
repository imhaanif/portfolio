from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views import generic
from portfolio.models import(OwnerDetails,
                             Service,
                             FeaturedProjects,
                             CliantTestimonails,
                             TechnicalSkills,
                             ProfessonalSkills,
                             Education,
                             Expirence,
                             Pricing,
                             Services,
                             CliantMessage,
                             AboutSection,
                             ClientReview,
                             Teammates)




# Create your views here.


#home view

class HomeView(generic.TemplateView):
    model = OwnerDetails
    template_name = 'home-two-w.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        details = OwnerDetails.objects.all().order_by('-id')[:1]
        about = AboutSection.objects.all().order_by('-id')[:1]
        services = Service.objects.all()
        projects = FeaturedProjects.objects.all().order_by('-id')
        testimonials = CliantTestimonails.objects.all
        technical_skills = TechnicalSkills.objects.all().order_by('id')
        professonal_skills = ProfessonalSkills.objects.all().order_by('id')
        educations = Education.objects.all().order_by('-id')
        expirences = Expirence.objects.all().order_by('-id')
        pricing = Pricing.objects.all().order_by('id')
        priceService = Services.objects.all().order_by('-id')
        reviews = ClientReview.objects.all().order_by('-id')
        teammates = Teammates.objects.all().order_by('-id')
        context['details'] = details
        context['services'] = services
        context['projects'] = projects
        context['testimonials'] = testimonials
        context['technical_skills'] = technical_skills
        context['professonal_skills'] = professonal_skills
        context['educations'] = educations
        context['expirences'] = expirences
        context['pricing'] = pricing
        context['priceService'] = priceService
        context['aboutme'] = about
        context['reviews'] = reviews
        context['teammates'] = teammates
        
        
        return context

class ContactForm(generic.TemplateView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            data = CliantMessage(first_name=first_name,last_name=last_name, email=email, message=message)
            data.save()

            return redirect('home')
        