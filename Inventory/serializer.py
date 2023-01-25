from rest_framework import serializers
from .models import Product,Variant

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']

class VariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Variant
        exclude = ['created_at', 'updated_at']


