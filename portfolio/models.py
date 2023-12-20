from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class OwnerDetails(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='owner', blank= True, null=True)
    profession = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=70)
    
    
    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    service_title = models.CharField(max_length=70)
    service_description = models.TextField()
    icon = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.service_title

        
class FeaturedProjects(models.Model):
    project_category = models.CharField(max_length=40)
    project_subCategory = models.CharField(max_length=40)
    company_name = models.CharField(max_length=40)
    details = models.TextField()
    project_image = models.ImageField(upload_to='featured_project')
    project_url = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.company_name

class CliantTestimonails(models.Model):
    project = models.ForeignKey(
        FeaturedProjects,
        on_delete= models.CASCADE
    )
    cliant_name = models.CharField(max_length=40)
    testimonials = models.TextField()

    
    def __str__(self) -> str:
        return self.cliant_name
    
    
class TechnicalSkills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()

    def __str__(self) -> str:
        return self.skill_name
    
    
class ProfessonalSkills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()

    def __str__(self) -> str:
        return self.skill_name

        
class Education(models.Model):
    degree_name = models.CharField(max_length=30)
    institute_name = models.CharField(max_length=50)
    course_start_year = models.IntegerField()
    course_ending_year = models.IntegerField()
    about_degree = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.degree_name
    
    
class Expirence(models.Model):
    job_title = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    job_joining_year = models.IntegerField()
    job_ending_year = models.IntegerField()
    role_ot_post = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.job_title
    
    
class Pricing(models.Model):
    work_type = models.CharField(max_length=50)
    quote = models.CharField(max_length=120)
    icon = models.CharField(max_length=20)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.work_type

class Services(models.Model):
    table = models.ForeignKey(
        Pricing,
        on_delete=models.CASCADE
    )
    service_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.service_name
    
class CliantMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

        
class AboutSection(models.Model):
    about_me = RichTextField()
    cv = models.FileField(upload_to='cv')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.created)

class ClientReview(models.Model):
    client_name = models.CharField(max_length=50)
    client_company = models.CharField(max_length=50)
    rewiew = RichTextField()
    image = models.ImageField(upload_to='clients')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.client_name

class Teammates(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=70)
    image = models.ImageField(upload_to='teammates')


