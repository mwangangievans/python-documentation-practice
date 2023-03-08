from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(APIView):


    def get(self , request , format=None):
        Snippet_ = Snippet.objects.all()
        serializer_ = SnippetSerializer(Snippet_ , many=True)
        return Response(serializer_.data)

    def post(self,request,format=None):
        serializer_ = SnippetSerializer(data = request.data)
        if serializer_.is_valid():
            serializer_.save()
            return Response(serializer_.data,status=status.HTTP_201_CREATED)
        return Response(serializer_.errors,status=status.HTTP_400_BAD_REQUEST)



class SnippetDetails(APIView):
    """
    Retrieve , update or delete a snippet instance.

    """
    def get_object(self , pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
        
    def get(self , request , pk , format=None):
        Snippet_ =  self.get_object(pk)
        seriliazer_ = SnippetSerializer(Snippet_)
        return Response(seriliazer_.data)
    
    def put(self , request , pk , format=None):
        snippet_= self.get_object(pk)
        serializer_ = SnippetSerializer(snippet_ , request.data)
        if serializer_.is_valid():
            serializer_.save()
            return Response(serializer_.data,status=status.HTTP_201_CREATED)
        return Response(serializer_.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def  delete(self,pk , request , format=None):
        Snippet_ = self.get_object(pk)
        Snippet_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
