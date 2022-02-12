from rest_framework.viewsets import ModelViewSet

from routes.models import Routes
from routes.serializers import RoutesSerializer


class RoutesViewSet(ModelViewSet):
    serializer_class = RoutesSerializer
    queryset = Routes.objects.all()
