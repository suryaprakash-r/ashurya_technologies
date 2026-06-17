from django.shortcuts import render
from .models import Project


def portfolio(request):

    featured_projects = Project.objects.filter(
        featured=True
    ).order_by('-created_at')

    projects = Project.objects.all().order_by('-created_at')

    context = {
        'featured_projects': featured_projects,
        'projects': projects,
    }

    return render(
        request,
        'portfolio/portfolio.html',
        context
    )