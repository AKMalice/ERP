from django.db import models
from django.utils import timezone

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mother_phone_no = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    father_phone_no = models.CharField(max_length=15, blank=True, null=True)  # Optional field
    dob = models.DateField(null=True, blank=True)  # Allow NULL and blank
    parent_email = models.EmailField(blank=True, null=True)  # Optional field
    enrollment_date = models.DateField(default=timezone.now)  # Default to current date

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
