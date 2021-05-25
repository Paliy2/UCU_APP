from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from rest_framework.generics import CreateAPIView, ListAPIView

from organizations.models import Organization, Department
from organizations.serializers import OrganizationSerializer, DepartmentSerializer


class OrganizationListView(ListAPIView):
    model = Organization
    # queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self, **kwargs):
        # print(kwargs)
        # self.res = get_object_or_404(Organization, name=self.kwargs['id'])

        return Organization.objects.all()
        # return Organization.objects.all() # filter(id=kwargs.get('id'))[:1]

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

class OrganizationDetailView(DetailView):
    model = Organization



class DepartmentListView(ListAPIView):
    model = Department
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self, **kwargs):
        return Department.objects.all()

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

class DepartmentDetailView(DetailView):
    model = Department
