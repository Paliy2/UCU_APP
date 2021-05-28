from datetime import date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from events.models import Event
from events.models import EventFavorites
from events.serializers import EventSerializer
from events.serializers import EventFavoritesSerializer

class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    # lookup_field = 'id'
    # filters = (filters.SearchFilter, )

    def get(self, request, id, *args, **kwargs):
        try:
            res = Event.objects.get(id=id)
        except Event.DoesNotExist:
            res = None

        if not res:
            return Response(
                {"res": "Object with given id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = EventSerializer(res)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        try:
            res = Event.objects.get(id=id)
        except Event.DoesNotExist:
            res = None
        if not res:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        res.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class EventListView(ListAPIView):
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['event_datetime    ', ]
    # print(date.today())

    # bigger than todat
    queryset = queryset.filter(created_at__gte=date.today())

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'Event POST success',
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class EventFavoritesView(ListCreateAPIView):
    model = EventFavorites
    queryset = EventFavorites.objects.all()
    serializer_class = EventFavoritesSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'Event POST success',
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)



