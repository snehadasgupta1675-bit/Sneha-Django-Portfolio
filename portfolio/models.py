from django.db import models
from django.utils import timezone

class Education(models.Model):
    qualification = models.CharField(max_length=160)
    institution = models.CharField(max_length=200)
    period = models.CharField(max_length=100, blank=True)
    details = models.TextField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["sort_order", "-id"]
    def __str__(self):
        return f"{self.qualification} — {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="Technical")
    sort_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["category", "sort_order", "name"]
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=240)
    description = models.TextField()
    technologies = models.CharField(max_length=300, blank=True, help_text="Separate technologies with commas.")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["sort_order", "title"]
    def __str__(self):
        return self.title

class Experience(models.Model):
    KIND_CHOICES = [("Internship", "Internship"), ("Certificate", "Certificate"), ("Training", "Training")]
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default="Internship")
    title = models.CharField(max_length=180)
    organization = models.CharField(max_length=180)
    period = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    credential_url = models.URLField(blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["sort_order", "-id"]
        verbose_name_plural = "Internships and certificates"
    def __str__(self):
        return f"{self.title} — {self.organization}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return f"{self.name} — {self.created_at:%Y-%m-%d}"
