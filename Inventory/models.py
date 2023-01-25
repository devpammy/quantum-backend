from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

from django.db import models

class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Variant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_variants')
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    inventory = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
