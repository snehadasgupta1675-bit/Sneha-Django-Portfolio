from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Education, Skill, Project, Experience
from .forms import ContactForm

def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    return render(request, "portfolio/home.html", {"featured_projects": featured_projects})

def about(request):
    return render(request, "portfolio/about.html")

def education(request):
    return render(request, "portfolio/education.html", {"education_list": Education.objects.all()})

def skills(request):
    skills_list = Skill.objects.all()
    grouped = {}
    for skill in skills_list:
        grouped.setdefault(skill.category, []).append(skill)
    return render(request, "portfolio/skills.html", {"grouped_skills": grouped})

def projects(request):
    return render(request, "portfolio/projects.html", {"projects": Project.objects.all()})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/project_detail.html", {"project": project})

def experience(request):
    return render(request, "portfolio/experience.html", {"experiences": Experience.objects.all()})

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Thank you! Your message has been saved. I will get back to you.")
        return redirect("contact")
    return render(request, "portfolio/contact.html", {"form": form})
