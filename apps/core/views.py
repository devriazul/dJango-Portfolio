from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import SiteSettings, ContactSubmission, HomePage


def get_site_settings():
    """Get site settings, create default if none exists"""
    settings, created = SiteSettings.objects.get_or_create(
        pk=1,
        defaults={
            'site_title': 'Riazul Islam',
            'tagline': 'Full Stack Developer',
            'description': 'Passionate full stack developer specializing in Django, React, and modern web technologies.',
            'email': 'contact@example.com',
            'phone': '+1 (555) 123-4567',
            'location': 'San Francisco, CA',
        }
    )
    return settings


class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = get_site_settings()
        
        # Get home page content or create default
        home_page, created = HomePage.objects.get_or_create(
            pk=1,
            defaults={
                'hero_title': "Hi, I'm Riazul Islam",
                'hero_subtitle': "Full Stack Developer",
                'hero_description': "I build exceptional and accessible digital experiences for the web.",
            }
        )
        context['home_page'] = home_page
        
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_settings'] = get_site_settings()
        return context


@require_http_methods(["GET", "POST"])
def contact_view(request):
    site_settings = get_site_settings()
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # Basic validation
        if not all([name, email, subject, message]):
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'error': 'All fields are required.'
                })
            messages.error(request, 'All fields are required.')
            return render(request, 'core/contact.html', {'site_settings': site_settings})
        
        # Create contact submission
        ContactSubmission.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': 'Thank you for your message! I\'ll get back to you soon.'
            })
        
        messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
        return redirect('core:contact_success')
    
    return render(request, 'core/contact.html', {'site_settings': site_settings})


def contact_success_view(request):
    return render(request, 'core/contact_success.html', {
        'site_settings': get_site_settings()
    })
