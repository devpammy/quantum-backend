from django.contrib import admin

# Register your models here.
from .models import Product,Variant
admin.site.register(Product)
admin.site.register(Variant)
