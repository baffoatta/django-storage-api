from rest_framework import serializers
from .models import Item, Location

class ItemSerializer(serializers.ModelSerializer):
    """Serializes the item object to json format."""
    class Meta:
        model = Item
        fields = ('__all__')
        
        
        
class LocationSerializer(serializers.ModelSerializer):
    """Serializes the item object to json format."""
    class Meta:
        model = Location
        fields = ('__all__')