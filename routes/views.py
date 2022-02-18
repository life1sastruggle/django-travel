from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from routes.models import Routes
from routes.serializers import RoutesSerializer
from rest_framework.response import Response


class RoutesViewSet(ModelViewSet):
    serializer_class = RoutesSerializer
    pagination_class = PageNumberPagination
    queryset = Routes.objects.all()

    def list(self, request, **kwargs):
        page_obj = MyPageNumber()
        queryset = page_obj.paginate_queryset(queryset=Routes.objects.all(), request=request, view=self)
        serializer = RoutesSerializer(queryset, many=True)
        response = {'code': 0, 'data': serializer.data, 'msg': '', 'total': page_obj.page.paginator.count}
        return Response(response)


class MyPageNumber(PageNumberPagination):
    page_size = 10  # 每页显示多少条
    page_size_query_param = 'size'  # URL中每页显示条数的参数
    page_query_param = 'page'  # URL中页码的参数
    max_page_size = None  # 最大页码数限制
