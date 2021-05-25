from events.models import Event
from events.models import EventFavorites
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id',  'image', 'name', 'description', 'created_by', 'lecturer',
                  'category', 'location', 'event_datetime', 'created_at',
                  'is_online', 'event_online_meeting_link',
                  )


class EventFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFavorites
        fields = ('event_id', 'user')
