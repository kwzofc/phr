from rest_framework import generics, permissions
from phr.models import PHR
from .serializers import PHRSerializer

# Create your views here.
class PHRList(generics.ListCreateAPIView):
    queryset = PHR.objects.all()
    serializer_class = PHRSerializer
    permission_classes = [permissions.DjangoModelPermissions]

class PHRDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PHR.objects.all()
    serializer_class = PHRSerializer
    permission_classes = [permissions.DjangoModelPermissions]