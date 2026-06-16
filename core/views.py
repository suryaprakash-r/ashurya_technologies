from django.shortcuts import render
from services.models import Service
from portfolio.models import Project
from blog.models import Blog
from core.models import Testimonial


def home(request):

    services = Service.objects.filter(
        is_active=True
    )[:6]

    projects = Project.objects.filter(
        featured=True
    )[:3]

    blogs = Blog.objects.filter(
        is_published=True
    )[:3]

    testimonials = Testimonial.objects.filter(
        is_active=True
    )[:3]

    context = {
        'services': services,
        'projects': projects,
        'blogs': blogs,
        'testimonials': testimonials
    }

    return render(
        request,
        'core/home.html',
        context
    )

def about(request):
    return render(request, 'core/about.html')