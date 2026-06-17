from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Blog
from portfolio.models import Project
from core.models import Testimonial
from contact.models import Contact


@login_required
def dashboard_home(request):

    total_blogs = Blog.objects.count()

    total_projects = Project.objects.count()

    total_testimonials = Testimonial.objects.count()

    total_leads = Contact.objects.count()

    total_active_projects = Project.objects.exclude(
        status='completed'
    ).count()

    completed_projects = Project.objects.filter(
        status='completed'
    ).count()
    
    new_leads = Contact.objects.filter(
        status='new'
    ).count()

    recent_leads = Contact.objects.order_by(
        '-created_at'
    )[:5]

    recent_blogs = Blog.objects.order_by(
        '-created_at'
    )[:5]

    context = {

        'total_blogs': total_blogs,

        'total_projects': total_projects,

        'total_testimonials': total_testimonials,

        'total_leads': total_leads,

        'new_leads': new_leads,

        'recent_leads': recent_leads,

        'recent_blogs': recent_blogs,
        
        'total_active_projects': total_active_projects,
        
        'completed_projects' : completed_projects

    }

    return render(
        request,
        'dashboard/dashboard_home.html',
        context
    )
    
def lead_list(request):

    status = request.GET.get('status')

    search = request.GET.get('search')

    leads = Contact.objects.all().order_by(
        '-created_at'
    )

    if status:

        leads = leads.filter(
            status=status
        )

    if search:

        leads = leads.filter(
            name__icontains=search
        )

    context = {

        'leads': leads,

        'selected_status': status,

        'search': search,

    }

    return render(
        request,
        'dashboard/leads/lead_list.html',
        context
    )
    
def lead_detail(request, pk):

    lead = get_object_or_404(
        Contact,
        pk=pk
    )

    if request.method == "POST":

        lead.status = request.POST.get(
            'status'
        )

        lead.remarks = request.POST.get(
            'remarks'
        )

        lead.save()

        return redirect(
            'lead_detail',
            pk=lead.id
        )

    return render(
        request,
        'dashboard/leads/lead_detail.html',
        {
            'lead': lead
        }
    )
    
def project_list(request):

    status = request.GET.get("status")

    search = request.GET.get("search")

    projects = Project.objects.all().order_by(
        "-created_at"
    )

    if status:
        projects = projects.filter(
            status=status
        )

    if search:
        projects = projects.filter(
            title__icontains=search
        )

    context = {
        "projects": projects,
        "selected_status": status,
        "search": search,
    }

    return render(
        request,
        "dashboard/projects/project_list.html",
        context
    )
    
def project_detail(request, pk):

    project = get_object_or_404(
        Project,
        pk=pk
    )

    if request.method == "POST":

        project.status = request.POST.get(
            "status"
        )

        project.progress = request.POST.get(
            "progress"
        )

        project.internal_notes = request.POST.get(
            "internal_notes"
        )

        project.save()

        return redirect(
            "project_detail",
            pk=project.id
        )

    return render(
        request,
        "dashboard/projects/project_detail.html",
        {
            "project": project
        }
    )
    