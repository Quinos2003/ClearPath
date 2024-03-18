from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    installation_service = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.TextField()
    subscription_plan = models.CharField(max_length=50)
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Additional Fields
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    subscription_start_date = models.DateField()
    subscription_end_date = models.DateField()
    billing_address = models.TextField()
    payment_method = models.CharField(max_length=50)
    last_service_date = models.DateField()
    next_service_date = models.DateField()
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
    notes = models.TextField(blank=True)

    # Define any other fields as needed based on your requirements

    class Meta:
        db_table = 'organizations'
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ['-created_at']

    def __str__(self):
        return self.name
# Path: ClearPath/Administration_Backend/organizations/serializers.py