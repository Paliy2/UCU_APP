from rest_framework import serializers
from trapezna.models import FoodItem


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ("building",
                  "item_name",
                  "item_type",
                  "portion_size",
                  "price",
                  "created_at",
                  "available"
                  )
