from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'total_price']

    def create(self, validated_data):
        name = validated_data['name']
        description = validated_data['description']
        price = validated_data['price']
        
        existing_product = Product.objects.filter(
            name=name, 
            description=description, 
            price=price
        ).first()
        
        if existing_product:
            existing_product.quantity += validated_data['quantity']
            existing_product.save()
            return existing_product
        
        return super().create(validated_data)