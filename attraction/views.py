from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from attraction.models import Attraction
from attraction.serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    serializer_class = AttractionSerializer
    pagination_class = PageNumberPagination
    queryset = Attraction.objects.all()

    def list(self, request, **kwargs):
        queryset = Attraction.objects.all().filter(expiration_time=None)
        serializer = AttractionSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'msg': '', 'total': len(serializer.data)}
        return Response(response)


