from django.db import models

# Create your models here.
class RequestLog(models.Model):
    ip_address = models.GenericIPAddressField()
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=20, default='GET')
    user_agent = models.TextField(blank=True, null=True)
    response_status = models.IntegerField()
    response_time = models.FloatField(help_text="Response time in milliseconds")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-timestamp']),
            models.Index(fields=['ip_address']),
            models.Index(fields=['endpoint']),
        ]
        ordering = ['-timestamp']
        verbose_name = 'Request Log'
        verbose_name_plural = 'Request Logs'
    
    def __str__(self):
        return f"{self.ip_address} - {self.endpoint} ({self.response_status})"
