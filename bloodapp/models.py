from django.db import models
from django.contrib.auth.models import User

# Blood Group Choices
BLOOD_GROUP_CHOICES = [
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
]

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

class DonorRegistration(models.Model):
    # Personal Information
    aadhar = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    
    # Medical Information
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    weight = models.IntegerField()  # in kg
    height = models.IntegerField(null=True, blank=True)  # in cm
    last_donation = models.DateField(null=True, blank=True)
    
    # Health Status
    no_disease = models.BooleanField(default=False)
    no_medication = models.BooleanField(default=False)
    
    # Address Information
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=100, default='India')
    
    # Additional Information
    additional_info = models.TextField(null=True, blank=True)
    
    # Status and Timestamps
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    
    class Meta:
        ordering = ['-registration_date']
        verbose_name = 'Donor Registration'
        verbose_name_plural = 'Donor Registrations'
    
    def __str__(self):
        return f"{self.name} - {self.blood_group} ({self.status})"

class BloodRequest(models.Model):
    # Personal Information
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    
    # Blood Request Information
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    units_required = models.IntegerField()  # Number of units needed
    
    # Status and Timestamps
    request_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('fulfilled', 'Fulfilled'), ('cancelled', 'Cancelled')],
        default='pending'
    )
    
    class Meta:
        ordering = ['-request_date']
        verbose_name = 'Blood Request'
        verbose_name_plural = 'Blood Requests'
    
    def __str__(self):
        return f"{self.name} - {self.blood_group} ({self.units_required} units) - {self.status}"

class BloodDonationCenter(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    services = models.CharField(max_length=255)  # Comma-separated services
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['city', 'name']
        verbose_name = 'Blood Donation Center'
        verbose_name_plural = 'Blood Donation Centers'
    
    def __str__(self):
        return f"{self.name} - {self.city}"
    
    def get_services_list(self):
        return [s.strip() for s in self.services.split(',')]
