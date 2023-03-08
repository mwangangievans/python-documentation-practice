from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@api_view(['GET','POST'])
def snippet_list(request):
    """
    list all code snippets , or create a new snippet

    """

    if request.method == 'GET':
        snippet_ = Snippet.objects.all()
        serializer_ = SnippetSerializer(snippet_ , many=True)
        return Response(serializer_.data)
    
    elif request.method == 'POST':
        serializer_ = SnippetSerializer(data=request.data)
        if serializer_.is_valid():
            serializer_.save()
            return Response(serializer_.data , status=status.HTTP_201_CREATED)
        return Response(serializer_.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request , pk):
    """
    Retrieve , update or delete a code spippets
    
    """
    try:
        snippet_ = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer_ = SnippetSerializer(snippet_)
        return Response(serializer_.data)
    
    elif request.method == 'PUT':
        serializer_ = SnippetSerializer(snippet_ , data=request.data)
        if serializer_.is_valid():
            serializer_.save()
            return Response(serializer_.data)
        return Response(serializer_.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 