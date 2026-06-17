from django.urls import path

from .views import (
    dashboard_home,
    lead_list,
    lead_detail,
    project_list,
    project_detail,
)

urlpatterns = [

    path(
        '',
        dashboard_home,
        name='dashboard_home'
    ),

    path(
        'leads/',
        lead_list,
        name='lead_list'
    ),

    path(
        'leads/<int:pk>/',
        lead_detail,
        name='lead_detail'
    ),
    path(
        "projects/",
        project_list,
        name="project_list"
    ),

    path(
        "projects/<int:pk>/",
        project_detail,
        name="project_detail"
    ),

]