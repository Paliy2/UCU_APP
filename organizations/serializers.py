from organizations.models import Organization
from organizations.models import Department
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'organization_name', 'head', 'secretary', 'financier', 'members',
                  'media', 'status')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'department_name', 'web_site',)
