from rest_framework import serializers
from snippets.models import  Snippet
from django.contrib.auth import get_user_model


User = get_user_model()

class SnippetReadonlySerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    snippets = SnippetReadonlySerializer(many=True)

    class Meta:
        model = User 
        fields = ['id','username', 'snippets']



class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = '__all__'
        # fields = ['id', 'title','owner']

    def create(self , validated_data):
        print(validated_data)
        """create and return a new instance of snippet given the validated data..."""
        return Snippet.objects.create(**validated_data)

    def update(self , instance ,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.code = validated_data.get('code',instance.code)
        instance.linenos = validated_data.get('linenos',instance.linenos)
        instance.language = validated_data.get('language',instance.language)
        instance.style = validated_data.get('style',instance.style)
        instance.save()
        return instance