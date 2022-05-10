import json

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from route.models import Route
from route.serializers import RouteSerializer
from rest_framework.response import Response

from attraction.serializers import AttractionSerializer


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


class RouteAttractionMappingView(APIView):
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body)
        route_id = body["route_id"]
        serializer = AttractionSerializer(Route.objects.get(id=route_id).attraction.all(), many=True)
        print(serializer.data)
        response = {'code': 0, 'data': serializer.data}
        return Response(response)


class MyPageNumber(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = None
