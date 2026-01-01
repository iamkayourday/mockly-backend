from django.contrib import admin
from .models import MockUser

@admin.register(MockUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'gender', 'city', 'country', 'job_title')
    list_filter = ('gender', 'country', 'state', 'city')
    search_fields = ('first_name', 'last_name', 'email', 'job_title', 'company')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'gender', 'phone', 'avatar')
        }),
        ('Address', {
            'fields': ('street', 'city', 'state', 'country', 'postal_code')
        }),
        ('Job Info', {
            'fields': ('job_title', 'company')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )