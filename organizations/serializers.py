from organizations.models import Organization
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id',  'organization_name', 'head', 'secretary', 'financier', 'members',
                  'media', 'status')
