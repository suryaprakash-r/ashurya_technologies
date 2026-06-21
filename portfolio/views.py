from django.shortcuts import render, get_object_or_404

from .models import Project


def portfolio_list(request):

    featured_projects = Project.objects.filter(
        featured=True
    )

    projects = Project.objects.all()

    return render(
        request,
        'portfolio/portfolio.html',
        {
            'featured_projects': featured_projects,
            'projects': projects,
        }
    )


def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    related_projects = Project.objects.exclude(
        id=project.id
    )[:3]

    return render(
        request,
        'portfolio/project_detail.html',
        {
            'project': project,
            'related_projects': related_projects
        }
    )