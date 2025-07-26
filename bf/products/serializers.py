from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'original_price',
            'category',
            'stock',
            'rating',
            'review_count',
            'brand',
            'discount',
            'is_new',
            'sold',
            'image_url',
            'is_active',
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None