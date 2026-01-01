from django.db import models

# Create your models here.
class MockUser(models.Model):
    GENDER_CHOICES = [
        ('male', 'MAle'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=20, unique=True)
    avatar = models.URLField(blank=True, null=True)

    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Mock User'
        verbose_name_plural = 'Mock Users'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def full_address(self):
        parts = [self.street, self.city, self.state, self.country, self.postal_code]
        return ", ".join(filter(None, parts))