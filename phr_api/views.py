from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from phr.models import PHR
from .serializers import PHRSerializer, UserSerializer

# Create your views here.
class PHRList(generics.ListCreateAPIView):
    queryset = PHR.objects.all()
    serializer_class = PHRSerializer

    permission_classes = [permissions.DjangoModelPermissions]


class PHRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PHR.objects.all()
    serializer_class = PHRSerializer

    permission_classes = [permissions.DjangoModelPermissions]


class CreateUserView(CreateAPIView):
    model = get_user_model()
    queryset = model.objects.all()
    serializer_class = UserSerializer

    permission_classes = [permissions.DjangoModelPermissions]