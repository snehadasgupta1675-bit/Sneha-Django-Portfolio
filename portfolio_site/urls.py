from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("education/", views.education, name="education"),
    path("skills/", views.skills, name="skills"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("experience/", views.experience, name="experience"),
    path("contact/", views.contact, name="contact"),
]
