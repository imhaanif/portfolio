from django.contrib import admin
from portfolio.models import (OwnerDetails,
                              Service,
                              FeaturedProjects,
                              CliantTestimonails,
                              TechnicalSkills,
                              ProfessonalSkills,
                              Education,
                              Expirence,
                              Pricing,
                              Services,
                              CliantMessage,
                              AboutSection,
                              ClientReview,
                              Teammates)

# Register your models here.

class CliantTestimonailsAdmin(admin.StackedInline):
    model = CliantTestimonails

class FeaturedProjectsAdmin(admin.ModelAdmin):
    inlines = [CliantTestimonailsAdmin]
    
class ServicesAdmin(admin.StackedInline):
    model = Services

class PricingAdmin(admin.ModelAdmin):
    inlines = [ServicesAdmin]

admin.site.register(OwnerDetails)
admin.site.register(Service)
admin.site.register(FeaturedProjects,FeaturedProjectsAdmin)
admin.site.register(TechnicalSkills)
admin.site.register(ProfessonalSkills)
admin.site.register(Education)
admin.site.register(Expirence)
admin.site.register(CliantMessage)
admin.site.register(ClientReview)
admin.site.register(AboutSection)
admin.site.register(Teammates)
admin.site.register(Pricing,PricingAdmin)
