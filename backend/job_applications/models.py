from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('IN_PROGRESS', 'In Progress'),
        ('REJECTED', 'Rejected'),
        ('OFFER', 'Offer Received'),
        ('ACCEPTED', 'Offer Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='job_applications')
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    application_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='APPLIED')
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company.name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts')
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='contacts', blank=True, null=True)

    def __str__(self):
        return self.name

class Interview(models.Model):
    INTERVIEW_TYPE_CHOICES = [
        ('PHONE', 'Phone'),
        ('VIDEO', 'Video'),
        ('IN_PERSON', 'In-Person'),
        ('TECHNICAL', 'Technical'),
    ]

    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, related_name='interviews')
    date_time = models.DateTimeField()
    interview_type = models.CharField(max_length=20, choices=INTERVIEW_TYPE_CHOICES)
    interviewer = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_interview_type_display()} Interview for {self.job_application}"
    
class Subscription(models.Model):
    TIER_CHOICES = [
        ('FREE', 'Free'),
        ('PLUS', 'Plus'),
        ('PRO', 'Pro'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tier = models.CharField(max_length=10, choices=TIER_CHOICES, default='FREE')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    resume = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    about = models.TextField(blank=True)