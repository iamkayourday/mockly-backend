import time
import json
from django.utils.deprecation import MiddlewareMixin
from .models import RequestLog

class RequestLoggingMiddleware(MiddlewareMixin):
    # Middleware to log each request and response details
    
    def process_request(self, request):
        request.start_time = time.time()
        return None
    
    def process_response(self, request, response):
        # Calculate response time
        if hasattr(request, 'start_time'):
            response_time = (time.time() - request.start_time) * 1000  # Convert to milliseconds
            
            # Only log API requests (not admin, static files, etc.)
            if request.path.startswith('/api/'):
                RequestLog.objects.create(
                    ip_address=self._get_client_ip(request),
                    endpoint=request.path,
                    method=request.method,
                    user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],  # Limit length
                    response_status=response.status_code,
                    response_time=round(response_time, 2)
                )
        
        return response
    
    def _get_client_ip(self, request):
        """Extract client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip