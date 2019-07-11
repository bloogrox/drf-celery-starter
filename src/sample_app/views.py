from rest_framework import generics
from rest_framework import permissions
from .serializers import SampleSerializer
from .models import Sample


class SampleListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SampleSerializer
    queryset = Sample.objects
