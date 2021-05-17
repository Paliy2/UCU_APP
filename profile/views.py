from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from user.serializers import UserRegistrationSerializer
from profile.models import UserProfile, PhoneNumber
from profile.serializers import PhoneNumberSerializer
from rest_framework import filters
from user.serializers import UserSerializer


class PhoneNumberListView(ListAPIView):
    paginate_by = 3
    model = PhoneNumber

    serializer_class = PhoneNumberSerializer
    permission_classes = (AllowAny,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['lastnameukr', 'firstnameukr', 'lastnameeng', 'firstnameeng', ]

    def get_queryset(self, **kwargs):
        return PhoneNumber.objects.all()

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


class ContactListView(ListAPIView):
    # todo add correct permissions
    permission_classes = (AllowAny,)

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ['lastnameukr', 'firstnameukr', 'lastnameeng', 'firstnameeng',]


class UserProfileView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': []
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)
