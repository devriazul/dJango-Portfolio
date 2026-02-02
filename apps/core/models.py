from django.db import models
from django.contrib.auth.models import User


class SiteSettings(models.Model):
    """Global site settings - singleton model"""
    site_title = models.CharField(max_length=100, default="Riazul Islam")
    tagline = models.CharField(max_length=200, default="Full Stack Developer")
    description = models.TextField(default="Passionate full stack developer specializing in Django, React, and modern web technologies.")
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='documents/', blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=5)
    projects_completed = models.PositiveIntegerField(default=50)
    clients_served = models.PositiveIntegerField(default=20)
  
    # Social Links
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    email = models.EmailField(default="contact@example.com")
    phone = models.CharField(max_length=20, default="+1 (555) 123-4567")
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, default="San Francisco, CA")
    
    # SEO
    meta_keywords = models.TextField(blank=True, help_text="Comma-separated keywords for SEO")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return f"{self.site_title} - Settings"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise SiteSettings.MultipleObjectsReturned("Only one SiteSettings instance is allowed")
        super().save(*args, **kwargs)


class ContactSubmission(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Contact Submission"
        verbose_name_plural = "Contact Submissions"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"


class HomePage(models.Model):
    """Home page content management"""
    hero_title = models.CharField(max_length=200, default="Hi, I'm Riazul Islam")
    hero_subtitle = models.CharField(max_length=300, default="Full Stack Developer")
    hero_description = models.TextField(default="I build exceptional and accessible digital experiences for the web.")
    hero_cta_text = models.CharField(max_length=50, default="Get In Touch")
    hero_cta_link = models.CharField(max_length=200, default="/contact/")
    
    # About section
    about_title = models.CharField(max_length=100, default="About Me")
    about_content = models.TextField(default="I'm a passionate full stack developer with expertise in modern web technologies.")
    
    # Skills section
    skills_title = models.CharField(max_length=100, default="My Skills")
    skills_subtitle = models.CharField(max_length=200, default="Technologies I work with")
    
    # Projects section
    projects_title = models.CharField(max_length=100, default="Featured Projects")
    projects_subtitle = models.CharField(max_length=200, default="Some of my recent work")
    
    # Contact section
    contact_title = models.CharField(max_length=100, default="Let's Work Together")
    contact_subtitle = models.CharField(max_length=200, default="Have a project in mind? Let's discuss how we can help.")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
    
    def __str__(self):
        return self.hero_title
