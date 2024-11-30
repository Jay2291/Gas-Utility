from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('install', 'Install'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)  
    details = models.TextField()  
    attachments = models.FileField(upload_to='attachments/', null=True, blank=True)  
    status = models.CharField(max_length=20, default='pending')  
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_service_type_display()} request by {self.customer.username}"
