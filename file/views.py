from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from file.models import AttractionImage, Banner
from file.serializers import AttractionImageSerializer, BannerSerializer


class AttractionImageViewSet(ModelViewSet):
    def list(self, request, *args, **kwargs):
        attraction_image_id = self.request.query_params.get('id')
        queryset = AttractionImage.objects.filter(attraction_id=attraction_image_id)
        serializer = AttractionImageSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'total': len(serializer.data)}
        return Response(response)


class BannerViewSet(ModelViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Banner.objects.all()
        serializer = BannerSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'total': len(serializer.data)}
        return Response(response)

