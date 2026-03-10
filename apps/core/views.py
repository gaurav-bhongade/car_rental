from django.shortcuts import render
from apps.cars.models import Car
from .models import Service  # wait, services is in core, Service
from apps.testimonials.models import Testimonial
from apps.team.models import TeamMember
from apps.blog.models import BlogPost

def index(request):
    featured_cars = Car.objects.filter(availability=True)[:6]  # limit to 6
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    team_members = TeamMember.objects.all()[:4]  # preview
    blog_posts = BlogPost.objects.all()[:3]  # preview
    context = {
        'featured_cars': featured_cars,
        'services': services,
        'testimonials': testimonials,
        'team_members': team_members,
        'blog_posts': blog_posts,
    }
    return render(request, 'index.html', context)

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def team(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def about(request):
    return render(request, 'about.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')
