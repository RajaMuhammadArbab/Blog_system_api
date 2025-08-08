from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post  
from .serializers import PostSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()      
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)  
    except Post.DoesNotExist:
        return Response({'error': 'Post Not Found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
