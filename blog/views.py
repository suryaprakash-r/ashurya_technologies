from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Blog, Comment


def blog_list(request):

    featured_blog = Blog.objects.filter(
        is_published=True,
        featured=True
    ).first()

    blogs = Blog.objects.filter(
        is_published=True
    ).order_by("-created_at")

    paginator = Paginator(blogs, 6)

    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)

    context = {
        "featured_blog": featured_blog,
        "blogs": blogs
    }

    return render(request, "blog/blog_list.html", context)

def blog_detail(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug,
        is_published=True
    )
    
    print("REQUEST METHOD:", request.method)

    if request.method == "POST":

        print("POST RECEIVED")  # 🔥 DEBUG
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        comment =Comment.objects.create(
            blog=blog,
            name=name,
            email=email,
            message=message,
            is_approved=False
        )

        # 🔥 AJAX RESPONSE
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            print("AJAX DETECTED")  # 🔥 DEBUG

            return JsonResponse({
                "status": "success",
                "name": comment.name,
                "message": comment.message,
                "created_at": comment.created_at.strftime("%B %d, %Y")
            })

        return redirect("blog_detail", slug=slug)
    
    

    comments = blog.comments.filter(is_approved=True).select_related("parent").order_by("created_at")

    print("TAGS:", blog.tags.all())
    related_blogs = Blog.objects.filter(
        is_published=True
    ).exclude(id=blog.id)

    if blog.tags.exists():
        related_blogs = related_blogs.filter(
            tags__in=blog.tags.all()
        ).distinct()

    related_blogs = related_blogs[:3]

    return render(request, "blog/blog_detail.html", {
        "blog": blog,
        "comments": comments,
        "related_blogs": related_blogs
    })