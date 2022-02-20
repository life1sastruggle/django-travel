from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from route.models import Route
from route.serializers import RouteSerializer
from rest_framework.response import Response

from spot.serializers import SpotSerializer


class RouteViewSet(ModelViewSet):
    serializer_class = RouteSerializer
    pagination_class = PageNumberPagination
    queryset = Route.objects.all()

    def list(self, request, **kwargs):
        page_obj = MyPageNumber()
        queryset = page_obj.paginate_queryset(queryset=Route.objects.all(), request=request, view=self)
        serializer = RouteSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'total': page_obj.page.paginator.count}
        return Response(response)


class RouteSpotMappingView(APIView):
    def get(self, request, *args, **kwargs):
        route_id = self.request.data['route_id']
        serializer = SpotSerializer(Route.objects.get(id=route_id).spots.all(), many=True)
        print(serializer.data)
        response = {'code': 0, 'data': serializer.data}
        return Response(response)


class MyPageNumber(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = None
