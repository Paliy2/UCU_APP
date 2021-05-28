from events.models import Event
from events.models import EventFavorites
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    # category = StringArrayField()
    category = serializers.SerializerMethodField('get_category')

    def get_category(self, obj):
        if obj:
            print(obj.category)
            return obj.category.split(',')
        return ''

    class Meta:
        model = Event
        fields = '__all__'


class EventFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFavorites
        fields = ('event_id', 'user')
