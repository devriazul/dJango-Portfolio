from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.core.models import SiteSettings, HomePage


class Command(BaseCommand):
    help = 'Initialize the site with default data'
    
    def handle(self, *args, **options):
        self.stdout.write('Initializing site with default data...')
        
        # Create site settings if they don't exist
        site_settings, created = SiteSettings.objects.get_or_create(
            pk=1,
            defaults={
                'site_title': 'Riazul Islam',
                'tagline': 'Full Stack Developer',
                'description': 'Passionate full stack developer specializing in Django, React, and modern web technologies. I build exceptional and accessible digital experiences for the web.',
                'email': 'contact@devriazul.com',
                'phone': '+1 (555) 123-4567',
                'location': 'San Francisco, CA',
                'years_experience': 5,
                'projects_completed': 50,
                'clients_served': 20,
                'github_url': 'https://github.com/riazul-islam',
                'linkedin_url': 'https://linkedin.com/in/riazul-islam',
                'twitter_url': 'https://twitter.com/riazul_islam',
                'meta_keywords': 'full stack developer, django, react, python, javascript, web development, portfolio',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Site settings created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Site settings already exist'))
        
        # Create home page content if it doesn't exist
        home_page, created = HomePage.objects.get_or_create(
            pk=1,
            defaults={
                'hero_title': "Hi, I'm Riazul Islam",
                'hero_subtitle': "Full Stack Developer",
                'hero_description': "I build exceptional and accessible digital experiences for the web. Specializing in Django, React, and modern web technologies.",
                'hero_cta_text': "Get In Touch",
                'hero_cta_link': "/contact/",
                'about_title': "About Me",
                'about_content': "I'm a passionate full stack developer with over 5 years of experience in creating web applications. My expertise spans across frontend and backend technologies, with a focus on creating scalable and maintainable solutions.",
                'skills_title': "My Skills",
                'skills_subtitle': "Technologies I work with",
                'projects_title': "Featured Projects",
                'projects_subtitle': "Some of my recent work",
                'contact_title': "Let's Work Together",
                'contact_subtitle': "Have a project in mind? Let's discuss how we can help bring your ideas to life.",
                'is_active': True,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('✓ Home page content created'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Home page content already exists'))
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@devriazul.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('✓ Superuser created (admin/admin123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠ Superuser already exists'))
        
        self.stdout.write(self.style.SUCCESS('Site initialization completed!'))
        self.stdout.write('')
        self.stdout.write('Next steps:')
        self.stdout.write('1. Run: python manage.py runserver')
        self.stdout.write('2. Visit: http://127.0.0.1:8000/admin')
        self.stdout.write('3. Login with: admin/admin123')
        self.stdout.write('4. Visit: http://127.0.0.1:8000 to see your portfolio site')