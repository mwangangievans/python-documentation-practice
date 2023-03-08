from rest_framework import serializers
from snippets.models import LANGUAGE_CHOICES,STYLE_CHOICES, Snippet
# from tutorial.snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Snippet
        fields = '__all__'

    


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