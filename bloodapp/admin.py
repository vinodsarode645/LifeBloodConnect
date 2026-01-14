from django.contrib import admin
from bloodapp.models import DonorRegistration, BloodRequest, BloodDonationCenter

@admin.register(DonorRegistration)
class DonorRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'aadhar', 'blood_group', 'phone', 'status', 'registration_date')
    list_filter = ('blood_group', 'status', 'registration_date', 'gender')
    search_fields = ('name', 'email', 'phone', 'aadhar', 'city')
    readonly_fields = ('registration_date', 'updated_date')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('aadhar', 'name', 'email', 'phone', 'gender', 'dob')
        }),
        ('Medical Information', {
            'fields': ('blood_group', 'weight', 'height', 'last_donation')
        }),
        ('Health Status', {
            'fields': ('no_disease', 'no_medication')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state', 'pincode', 'country')
        }),
        ('Additional Information', {
            'fields': ('additional_info',)
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'registration_date', 'updated_date')
        }),
    )


@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'units_required', 'contact_no', 'status', 'request_date')
    list_filter = ('blood_group', 'status', 'request_date')
    search_fields = ('name', 'contact_no', 'address')
    readonly_fields = ('request_date', 'updated_date')
    
    fieldsets = (
        ('Requester Information', {
            'fields': ('name', 'contact_no', 'address')
        }),
        ('Blood Request Details', {
            'fields': ('blood_group', 'units_required')
        }),
        ('Status & Timestamps', {
            'fields': ('status', 'request_date', 'updated_date')
        }),
    )


@admin.register(BloodDonationCenter)
class BloodDonationCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone', 'email')
    list_filter = ('city',)
    search_fields = ('name', 'city', 'phone', 'email')
    ordering = ('city', 'name')
