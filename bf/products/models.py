from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('buah', 'Buah'),
        ('sayur', 'Sayur'),
        ('groceries', 'Groceries'),
        ('meat', 'Meat'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    review_count = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True, null=True)
    discount = models.PositiveIntegerField(default=0)
    is_new = models.BooleanField(default=False)
    sold = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'