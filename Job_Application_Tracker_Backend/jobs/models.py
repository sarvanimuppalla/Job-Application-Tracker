from django.db import models

# Create your models here.
class jobs(models.Model):
    job_title = models.CharField(max_length=100, blank=False)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_link = models.URLField(blank=True, null=True)
    job_alerts = models.BooleanField(default=False)
    # job_accepted = models.BooleanField(default=False)
    # job_rejected = models.BooleanField(default=False)
    # job_interviewed = models.BooleanField(default=False)
    # job_offer_received = models.BooleanField(default=False)

    company_name = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

