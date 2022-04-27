from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializers import CommentSerializer


class AttractionCommentMappingView(APIView):
    def get(self, request, attraction_id, *args, **kwargs):
        page_obj = MyPageNumber()
        queryset = page_obj.paginate_queryset(queryset=Comment.objects.filter(attraction_id=attraction_id).all(),
                                              request=request)
        serializer = CommentSerializer(queryset, many=True)
        print(serializer.data)
        response = {'code': 0, 'data': serializer.data, 'total': page_obj.page.paginator.count}
        return Response(response)


class MyPageNumber(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = None
