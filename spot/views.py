from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from spot.models import Spot
from spot.serializers import SpotSerializer


class SpotViewSet(ModelViewSet):
    serializer_class = SpotSerializer
    pagination_class = PageNumberPagination
    queryset = Spot.objects.all()

    def list(self, request, **kwargs):
        queryset = Spot.objects.all().filter(expirationTime=None)
        serializer = SpotSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'msg': '', 'total': len(serializer.data)}
        return Response(response)


