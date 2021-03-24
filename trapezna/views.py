from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from trapezna.models import FoodItem
from trapezna.serializers import FoodItemSerializer
from rest_framework import status


class MenuItemView(ListCreateAPIView):
    model = FoodItem
    serializer_class = FoodItemSerializer
    queryset = model.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_200_OK
        response = {
            'success': 'True',
            'status code': status_code,
            'message': "new item was added successfully"
        }

        return Response(response, status=status_code)