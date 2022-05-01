from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from file.models import File
from file.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
