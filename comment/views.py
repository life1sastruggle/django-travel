from rest_framework.response import Response
from rest_framework.views import APIView

from comment.models import Comment
from comment.serializers import CommentSerializer


class SpotCommentMappingView(APIView):
    def get(self, request, spot_id, *args, **kwargs):
        serializer = CommentSerializer(Comment.objects.filter(spot_id=spot_id).all(), many=True)
        print(serializer.data)
        response = {'code': 0, 'data': serializer.data}
        return Response(response)
