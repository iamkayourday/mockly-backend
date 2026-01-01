from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model for future authentication and API key management
    For now, just a placeholder
    """
    api_key = models.CharField(max_length=100, blank=True, unique=True)
    rate_limit = models.IntegerField(default=100, help_text="Requests per hour")
    is_premium = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Account User'
        verbose_name_plural = 'Account Users'
    
    def generate_api_key(self):
        """Generate API key for the user"""
        import secrets
        self.api_key = secrets.token_urlsafe(32)
        self.save()
        return self.api_key