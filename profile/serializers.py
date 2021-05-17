from profile.models import PhoneNumber
from rest_framework import serializers


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('id',  'emailucu', 'lastnameukr', 'firstnameukr', 'lastnameeng', 'firstnameeng',
                  'phone', 'department')
