from django.contrib import admin
from .models import Education, Skill, Project, Experience, ContactMessage

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("qualification", "institution", "period", "sort_order")
    list_editable = ("sort_order",)
    search_fields = ("qualification", "institution")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "sort_order")
    list_filter = ("category",)
    search_fields = ("name", "category")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "sort_order")
    list_editable = ("featured", "sort_order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description", "technologies")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "kind", "period", "sort_order")
    list_filter = ("kind",)
    search_fields = ("title", "organization")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    list_editable = ("is_read",)
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("created_at",)
