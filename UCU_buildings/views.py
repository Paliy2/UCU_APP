from rest_framework.generics import ListCreateAPIView
from UCU_buildings.serializers import BuildingSerializer
from UCU_buildings.models import Building

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class BuildingsView(ListCreateAPIView):
    permission_classes = (AllowAny, )
    model = Building
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_200_OK
        response = {
            'success': 'True',
            'status code': status_code,
            'message': "new building was added successfully"
        }

        return Response(response, status=status_code)