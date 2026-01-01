from django.contrib import admin
from .models import RequestLog

# Register your models here.
@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'endpoint', 'method', 'response_status', 'response_time', 'timestamp')
    list_filter = ('method','response_status', 'timestamp')
    search_fields = ('ip_address', 'endpoint', 'user_agent')
    readonly_fields = ('ip_address', 'endpoint', 'method', 'user_agent', 'response_status', 'response_time', 'timestamp')
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False  # Prevent manual adding logs
    
    def has_change_permission(self, request, obj=None):
        return False  # Prevent editing logs