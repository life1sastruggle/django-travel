from decimal import Decimal

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
        if len(self.request.query_params) != 0:
            scenery = self.request.query_params.get("scenery")
            shopping = self.request.query_params.get("shopping")
            repast = self.request.query_params.get("repast")
            entertainment = self.request.query_params.get("entertainment")
            accommodation = self.request.query_params.get("accommodation")
            traffic = self.request.query_params.get("traffic")
            res_list = sorted(list(queryset), key=lambda x: -(
                    x.scenery_score * Decimal(scenery) +
                    x.shopping_score * Decimal(shopping) +
                    x.repast_score * Decimal(repast) +
                    x.entertainment_score * Decimal(entertainment) +
                    x.accommodation_score * Decimal(accommodation) +
                    x.traffic_score * Decimal(traffic)))
            serializer = AttractionSerializer(res_list, many=True)
        else:
            serializer = AttractionSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'msg': '', 'total': len(serializer.data)}
        return Response(response)
