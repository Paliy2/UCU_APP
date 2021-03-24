from rest_framework import serializers
from UCU_buildings.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ("location", "name", "description")
