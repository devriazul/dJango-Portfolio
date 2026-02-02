from django.contrib import admin
from .models import SiteSettings, ContactSubmission, HomePage


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_title', 'email', 'location', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['site_title', 'email', 'location']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_title', 'tagline', 'description', 'avatar')
        }),
        ('Statistics', {
            'fields': ('years_experience', 'projects_completed', 'clients_served')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'whatsapp', 'location')
        }),
        ('Documents', {
            'fields': ('resume_file',)
        }),
        ('SEO', {
            'fields': ('meta_keywords',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'is_active', 'updated_at']
    list_filter = ['is_active', 'updated_at']
    search_fields = ['hero_title', 'hero_subtitle']
    list_editable = ['is_active']
    
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_description', 'hero_cta_text', 'hero_cta_link')
        }),
        ('About Section', {
            'fields': ('about_title', 'about_content')
        }),
        ('Skills Section', {
            'fields': ('skills_title', 'skills_subtitle')
        }),
        ('Projects Section', {
            'fields': ('projects_title', 'projects_subtitle')
        }),
        ('Contact Section', {
            'fields': ('contact_title', 'contact_subtitle')
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
