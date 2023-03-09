from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins , generics



class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self , request , *arg , **kwargs):
        return self.list(request , *arg , **kwargs)
    
    def post(self,request , *arg , **kwargs):
        return self.create(request , *arg , **kwargs)
    

class SnippetDetail(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self , request , *arg ,**kwargs):
        return self.retrieve(request , *arg ,**kwargs )
    
    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self , request , *args , **kwargs):
        return self.destroy(request , *args , **kwargs)
  
